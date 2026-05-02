### About Me MCP

[![Build Pipeline](https://github.com/sandofvega/about-me-mcp/actions/workflows/build.yml/badge.svg)](https://github.com/sandofvega/about-me-mcp/actions/workflows/build.yml)

#### Run in development
```bash
uv run fastmcp run main.py:mcp --reload --transport http --port 8080 --path /
```

#### Open Inspector
```bash
uv run fastmcp dev inspector main.py
```

#### Run in production
```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8080
```