# from fastapi import FastAPI
# from pydantic import BaseModel
# from openai import OpenAI
# import os

# app = FastAPI()

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )


# class ChatRequest(BaseModel):
#     message: str


# @app.post("/chat")
# def chat(request: ChatRequest):

#     response = client.responses.create(
#         model="gpt-5.4-mini",
#         input=request.message
#     )

#     return {
#         "response": response.output_text
#     }


###############################################################################################

# FastAPI + LLM + MCP client

from fastapi import FastAPI
from pydantic import BaseModel
from ollama import chat
from mcp import Client

app = FastAPI()

MCP_SERVER_URL = "http://127.0.0.1:8001/mcp"
OLLAMA_MODEL = "llama3.2:3b"


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat_endpoint(request: ChatRequest):

    async with Client(MCP_SERVER_URL) as mcp_client:

        # Get tools from MCP
        result = await mcp_client.list_tools()
        tools = result.tools

        # Convert MCP tools to Ollama format
        ollama_tools = []

        for tool in tools:
            ollama_tools.append({
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.input_schema,
                },
            })

        # Send user's message to Llama
        messages = [
            {
                "role": "user",
                "content": request.message,
            }
        ]

        response = chat(
            model=OLLAMA_MODEL,
            messages=messages,
            tools=ollama_tools,
        )

        message = response.message

        # Check if Llama wants to use an MCP tool
        if message.tool_calls:

            # Add Llama's tool request to the conversation
            messages.append(message)

            # Execute requested MCP tools
            for tool_call in message.tool_calls:

                tool_name = tool_call.function.name
                arguments = tool_call.function.arguments

                print(
                    f"LLM requested tool: "
                    f"{tool_name} {arguments}"
                )

                tool_result = await mcp_client.call_tool(
                    tool_name,
                    arguments,
                )

                # Extract MCP result
                result_text = ""

                for content in tool_result.content:
                    if hasattr(content, "text"):
                        result_text += content.text
                    else:
                        result_text += str(content)

                print(f"MCP result: {result_text}")

                # Send tool result back to Llama
                messages.append({
                    "role": "tool",
                    "content": result_text,
                })

            # Ask Llama for the final answer
            final_response = chat(
                model=OLLAMA_MODEL,
                messages=messages,
            )

            return {
                "response": final_response.message.content
            }

        # No tool was needed
        return {
            "response": message.content
        }