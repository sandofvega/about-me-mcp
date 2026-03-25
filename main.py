from fastmcp import FastMCP

mcp = FastMCP(
    name="About Yasin",
    instructions="""
        This MCP provides information about Yasin Arafat.
    """
)

@mcp.tool
def get_yasin_profile() -> str:
    """Get information about Yasin"""
    with open("data/me.md") as f:
        return f.read()

if __name__ == "__main__":
    mcp.run(transport="http")