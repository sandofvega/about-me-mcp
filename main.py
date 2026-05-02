from fastmcp import FastMCP
from starlette.responses import JSONResponse

mcp = FastMCP(
    name="About Yasin",
    instructions="This MCP provides information about Yasin Arafat."
)

@mcp.tool
def get_yasin_profile() -> str:
    """Get information about Yasin"""
    with open("data/me.md") as f:
        return f.read()
    
@mcp.custom_route("/health", methods=["GET"])
async def health_check(request):
    return JSONResponse({
        "status": "healthy"
    })

app = mcp.http_app(path="/")