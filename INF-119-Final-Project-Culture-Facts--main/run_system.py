# Author: Youssef Dessouky - Student ID: 92158941

import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.orchestrator import Orchestrator


def run_system(requirements):
    """
    Main entry point to run the multi-agent system.
    
    Args:
        requirements: String describing what the Culture Facts app should do
        
    Returns:
        Dictionary with build result and usage statistics
    """
    orch = Orchestrator(model_name="gemini-2.0-flash")
    result = orch.build_app(requirements)
    usage = orch.server.call_tool("get_usage")

    return {"result": result, "usage": usage}


if __name__ == "__main__":
    # Default requirements if run directly
    default_requirements = """
    Create a Culture Facts application with these features:
    1. Show all cultures (list_cultures)
    2. Show detailed description of a specific culture (get_details)
    3. Search for a culture by name (search_culture)
    4. Randomly display a cultural trivia tidbit (get_random_fact)
    5. All data comes from cultures.json
    6. Include at least 5 diverse cultures from around the world
    """
    
    print("Running Culture Facts Generator...")
    print("-" * 50)
    
    output = run_system(default_requirements)
    
    print("\n" + "=" * 50)
    print("FINAL OUTPUT")
    print("=" * 50)
    print(f"\nResult: {output['result']}")
    print(f"\nUsage: {output['usage']}")
