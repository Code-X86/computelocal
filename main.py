from fastapi import FastAPI, Depends, HTTPException
from typing import List, Dict
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from tools.resource_monitor import ResourceMonitor
from tools.file_manager import FileManager

app = FastAPI(title="Compute Local API")

# Mock database for tools
tools_registry: Dict[str, Dict] = {
    "resource_monitor": {"status": "active", "description": "Monitors CPU and RAM usage", "class": "ResourceMonitor"},
    "file_manager": {"status": "active", "description": "Handles local file operations", "class": "FileManager"},
}

fm = FileManager()

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

@app.get("/tools/resource_monitor/metrics")
async def get_metrics():
    """Specific endpoint for the resource monitor tool."""
    return ResourceMonitor.get_metrics()

@app.get("/tools/file_manager/list")
async def list_files():
    """Specific endpoint for the file manager tool."""
    return fm.list_files()

@app.post("/compute")
async def execute_compute(tool_name: str, params: Dict = None):
    """
    Generic endpoint to trigger compute tasks using specific tools.
    This follows the user's preference for tools being separate from the core program.
    """
    if tool_name not in tools_registry:
        raise HTTPException(status_code=404, detail="Tool not found")
    
    if tool_name == "resource_monitor":
        return ResourceMonitor.get_metrics()
    elif tool_name == "file_manager":
        return fm.list_files()
        
    return {"status": "success", "tool": tool_name, "result": "Task executed"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
