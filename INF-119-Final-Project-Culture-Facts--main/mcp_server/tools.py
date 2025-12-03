# Author: Youssef Dessouky - Student ID: 92158941

import os
import subprocess
import sys

# Get the base directory relative to where the project runs from
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "generated_app")


def write_file(path: str, content: str):
    """
    Write content into generated_app/path.
    Creates parent directories if needed.
    """
    full_path = os.path.join(BASE_DIR, path)
    os.makedirs(os.path.dirname(full_path) if os.path.dirname(full_path) else BASE_DIR, exist_ok=True)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

    return {"status": "ok", "path": full_path}


def read_file(path: str):
    """
    Read content from generated_app/path.
    """
    full_path = os.path.join(BASE_DIR, path)
    if not os.path.exists(full_path):
        return {"error": "File not found"}

    with open(full_path, "r", encoding="utf-8") as f:
        return {"content": f.read()}


def run_pytest():
    """
    Run pytest inside generated_app folder.
    Returns stdout/stderr.
    """
    # Ensure generated_app exists
    if not os.path.exists(BASE_DIR):
        return {
            "returncode": 1,
            "stdout": "",
            "stderr": f"Directory {BASE_DIR} does not exist"
        }
    
    result = subprocess.run(
        [sys.executable, "-m", "pytest", ".", "-v"],
        cwd=BASE_DIR,
        capture_output=True,
        text=True
    )
    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def get_usage():
    """
    Return current model usage report as dict.
    """
    from core.usage_tracker import usage_tracker
    return usage_tracker.get_usage_report()
