"""Starter Code"""
# Author: (Your Name) - Student ID: XXXXXXX

import os
import json
import subprocess
from core.usage_tracker import usage_tracker

def write_file(path, content):
    """Writes content into a file inside generated_app/."""
    full_path = os.path.join("generated_app", path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    return {"status": "ok", "path": full_path}

def read_file(path):
    """Read a file from the generated_app directory."""
    full_path = os.path.join("generated_app", path)
    if not os.path.exists(full_path):
        return {"error": "File not found"}
    with open(full_path, "r", encoding="utf-8") as f:
        return {"content": f.read()}

def run_tests():
    """Run pytest in the generated_app folder."""
    result = subprocess.run(
        ["pytest", "generated_app"], capture_output=True, text=True
    )
    return {
        "stdout": result.stdout,
        "stderr": result.stderr
    }

def get_usage():
    """Return current model usage."""
    return usage_tracker.get_usage_report()

