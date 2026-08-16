import asyncio

from ollama import chat
from mcp import Client


MCP_SERVER_URL = "http://127.0.0.1:8001/mcp"


async def main():

    async with Client(MCP_SERVER_URL) as client:

        print("Connected to MCP server!")

        # Get MCP tools
        result = await client.list_tools()
        tools = result.tools

        print("\nAvailable MCP tools:")

        for tool in tools:
            print(f"- {tool.name}")

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

        # User message
        user_message = "What is 25 multiplied by 18?"

        print(f"\nUser: {user_message}")

        messages = [
            {
                "role": "user",
                "content": user_message,
            }
        ]

        # First LLM call
        response = chat(
            model="llama3.2:3b",
            messages=messages,
            tools=ollama_tools,
        )

        message = response.message

        # Check for tool calls
        if message.tool_calls:

            print("\nLLM requested a tool:")

            # Add the assistant's tool-call message
            messages.append(message)

            for tool_call in message.tool_calls:

                tool_name = tool_call.function.name
                arguments = tool_call.function.arguments

                print(f"Tool: {tool_name}")
                print(f"Arguments: {arguments}")

                # Call MCP
                tool_result = await client.call_tool(
                    tool_name,
                    arguments,
                )

                # Extract result
                result_text = ""

                for content in tool_result.content:
                    if hasattr(content, "text"):
                        result_text += content.text
                    else:
                        result_text += str(content)

                print(f"\nMCP result: {result_text}")

                # Give MCP result back to LLM
                messages.append({
                    "role": "tool",
                    "content": result_text,
                })

            # Second LLM call
            final_response = chat(
                model="llama3.2:3b",
                messages=messages,
            )

            print("\nFinal LLM response:")
            print(final_response.message.content)

        else:

            print("\nLLM answered directly:")
            print(message.content)


if __name__ == "__main__":
    asyncio.run(main())