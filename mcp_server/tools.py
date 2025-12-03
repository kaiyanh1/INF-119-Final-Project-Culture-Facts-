"""Starter Code"""
# Author: (Your Name) - Student ID: XXXXXXX

import os
from core.usage_tracker import usage_tracker

def write_file(path, content):
    full_path = os.path.join("generated_app", path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

    return {"status": "ok", "path": full_path}


def read_file(path):
    full_path = os.path.join("generated_app", path)
    if not os.path.exists(full_path):
        return {"error": "not found"}
    with open(full_path, "r", encoding="utf-8") as f:
        return {"content": f.read()}


def get_usage():
    return usage_tracker.get_usage_report()
