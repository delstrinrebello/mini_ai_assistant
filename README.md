# Mini AI Assistant

A simple AI assistant built with Flutter, FastAPI, Ollama, and Model Context Protocol (MCP).

## Architecture

Flutter
   ↓
FastAPI
   ↓
Ollama / Llama 3.2
   ↓
MCP Client
   ↓
MCP Server
   ↓
Tools

## Technologies

- Flutter
- Dart
- Riverpod
- Python
- FastAPI
- Ollama
- Llama 3.2
- Model Context Protocol (MCP)

## Features

- Chat interface built with Flutter
- Local LLM using Ollama
- MCP tool discovery
- MCP calculator tool
- Automatic LLM tool calling
- FastAPI backend

## Current MCP Tools

### Calculator

The assistant can use the MCP calculator tool for operations such as:

- Addition
- Subtraction
- Multiplication
- Division

Example:

User:
"What is 5 multiplied by 7?"

Assistant:
"The result of multiplying 5 and 7 is 35."

## Running the Project

### Backend

Create a virtual environment:

```bash
python -m venv venv

ollama pull llama3.2:3b

python mcp_server.py

uvicorn main:app --reload --host 0.0.0.0 --port 8000