# Mini AI Assistant

A simple AI assistant built with Flutter and a Python backend.

The app uses Ollama to run a local Llama 3.2 model and MCP (Model Context Protocol) to give the AI access to tools.

## Features

- Flutter chat interface
- Riverpod state management
- FastAPI backend
- Local LLM with Ollama
- Llama 3.2 3B
- MCP client and server
- Calculator tool

## Technologies

- Flutter
- Dart
- Riverpod
- Python
- FastAPI
- Ollama
- Llama 3.2
- MCP

## How It Works

The Flutter app sends messages to the FastAPI backend. The backend communicates with the local Llama model through Ollama.

When the AI needs to perform a calculation, it can use the calculator tool provided by the MCP server.

For example:

```text
What is 25 multiplied by 18?

25 × 18 = 450
```

## Running the Project

### Backend

Create and activate a virtual environment:

```powershell
cd backend
python -m venv venv
venv\Scripts\activate
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

Install the Ollama model:

```powershell
ollama pull llama3.2:3b
```

Start the MCP server:

```powershell
python mcp_server.py
```

In another terminal, start FastAPI:

```powershell
cd backend
venv\Scripts\activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Flutter

From the project root:

```powershell
flutter pub get
flutter run
```

