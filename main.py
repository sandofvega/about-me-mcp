from fastmcp import FastMCP
from starlette.responses import JSONResponse
from lib.qdrant import search_similar

mcp = FastMCP(
    name="About Yasin",
    instructions="This MCP provides information about Yasin Arafat."
)

@mcp.tool
def query(q: str) -> str:
    """Get 10 sentences about Yasin depending on your query."""

    similar_data = search_similar('hi')

    return "\n".join(f"- {item}" for item in similar_data)
    
@mcp.custom_route("/health", methods=["GET"])
async def health_check(request):
    return JSONResponse({
        "status": "healthy"
    })

app = mcp.http_app(path="/")