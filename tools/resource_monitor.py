import psutil
import json
import time
from typing import Dict

class ResourceMonitor:
    """
    A standalone tool for monitoring local system resources.
    This tool is designed to be called by the Compute Local API.
    """
    
    @staticmethod
    def get_metrics() -> Dict:
        return {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory": {
                "total": psutil.virtual_memory().total,
                "available": psutil.virtual_memory().available,
                "percent": psutil.virtual_memory().percent
            },
            "disk": {
                "total": psutil.disk_usage('/').total,
                "free": psutil.disk_usage('/').free,
                "percent": psutil.disk_usage('/').percent
            },
            "timestamp": time.time()
        }

if __name__ == "__main__":
    # When run as a script, it outputs JSON metrics
    print(json.dumps(ResourceMonitor.get_metrics(), indent=4))
