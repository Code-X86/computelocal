from fastapi import FastAPI, Depends, HTTPException
from typing import List, Dict

app = FastAPI(title="Compute Local API")

# Mock database for tools
tools_registry: Dict[str, Dict] = {
    "resource_monitor": {"status": "active", "description": "Monitors CPU and RAM usage"},
    "task_scheduler": {"status": "active", "description": "Manages background compute tasks"},
}

@app.get("/")
async def root():
    return {"message": "Welcome to Compute Local API", "version": "0.1.0"}

@app.get("/tools")
async def list_tools():
    """List all registered tools available to the compute node."""
    return tools_registry

@app.get("/tools/{tool_name}")
async def get_tool(tool_name: str):
    """Get details for a specific tool."""
    if tool_name not in tools_registry:
        raise HTTPException(status_code=404, detail="Tool not found")
    return tools_registry[tool_name]

@app.post("/compute")
async def execute_compute(tool_name: str, params: Dict):
    """
    Generic endpoint to trigger compute tasks using specific tools.
    This follows the user's preference for tools being separate from the core program.
    """
    if tool_name not in tools_registry:
        raise HTTPException(status_code=404, detail="Tool not found")
    
    # In a real implementation, this would call the external tool process or service
    return {"status": "success", "tool": tool_name, "result": "Task accepted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
