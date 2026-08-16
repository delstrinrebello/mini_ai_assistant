from mcp.server import MCPServer

mcp = MCPServer("Mini AI Tools")


@mcp.tool()
def calculate(a: float, b: float, operation: str) -> float:
    """Perform a basic calculation using two numbers."""

    operation = operation.lower().strip()

    if operation in ("add", "+"):
        return a + b

    if operation in ("subtract", "-"):
        return a - b

    if operation in ("multiply", "*", "x"):
        return a * b

    if operation in ("divide", "/"):
        if b == 0:
            raise ValueError("Cannot divide by zero")

        return a / b

    raise ValueError(f"Unknown operation: {operation}")

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8001,
    )