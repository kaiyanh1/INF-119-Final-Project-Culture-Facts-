# Author: Your Name - Student ID: XXXXXXX

import os
import subprocess
from core.usage_tracker import usage_tracker

BASE_DIR = "generated_app"


def write_file(path: str, content: str):
    """
    Write content into generated_app/path.
    Creates parent directories if needed.
    """
    full_path = os.path.join(BASE_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

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
    result = subprocess.run(
        ["pytest", "."],
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
    return usage_tracker.get_usage_report()
