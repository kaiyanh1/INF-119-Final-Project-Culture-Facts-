# Author: Youssef Dessouky - Student ID: 92158941

import sys
import os
import json

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, render_template_string
from run_system import run_system

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Coder - Culture Facts Generator</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            border-bottom: 3px solid #3498db;
            padding-bottom: 15px;
        }
        h2 {
            color: #34495e;
            margin-top: 30px;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        textarea {
            width: 100%;
            height: 200px;
            padding: 15px;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 14px;
            font-family: monospace;
            resize: vertical;
        }
        textarea:focus {
            border-color: #3498db;
            outline: none;
        }
        button {
            background-color: #3498db;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 15px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #2980b9;
        }
        button:disabled {
            background-color: #95a5a6;
            cursor: not-allowed;
        }
        pre {
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 5px;
            overflow-x: auto;
            font-size: 13px;
            line-height: 1.5;
        }
        .success {
            background-color: #27ae60;
            color: white;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .error {
            background-color: #e74c3c;
            color: white;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .info-box {
            background-color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            border-left: 4px solid #3498db;
        }
        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #3498db;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌍 AI Coder - Culture Facts Generator</h1>
        
        <div class="info-box">
            <strong>How it works:</strong> This multi-agent system uses Google Gemini to automatically generate a Culture Facts application.
            <br><br>
            <strong>Agents:</strong>
            <ul>
                <li><strong>Architect Agent</strong> - Designs the application structure and generates code</li>
                <li><strong>Coder Agent</strong> - Writes files to disk using MCP tools</li>
                <li><strong>Tester Agent</strong> - Generates pytest test cases</li>
            </ul>
        </div>

        <form method="POST" onsubmit="showLoading()">
            <label for="req"><strong>Enter your requirements:</strong></label>
            <br><br>
            <textarea name="req" id="req" placeholder="Describe what you want the Culture Facts app to do...">{{ req }}</textarea>
            <br>
            <button type="submit" id="submitBtn">🚀 Generate Culture Facts App</button>
        </form>
        
        <div class="loading" id="loadingDiv">
            <div class="spinner"></div>
            <p>Generating application... This may take 30-60 seconds.</p>
        </div>

        {% if result %}
        <h2>✅ Build Result</h2>
        {% if result.error %}
        <div class="error">
            <strong>Error:</strong> {{ result.error }}
        </div>
        {% else %}
        <div class="success">
            Application generated successfully!
        </div>
        {% endif %}
        <pre>{{ result | tojson(indent=2) }}</pre>
        {% endif %}

        {% if usage %}
        <h2>📊 Usage Report</h2>
        <pre>{{ usage | tojson(indent=2) }}</pre>
        {% endif %}
        
        {% if result and not result.error %}
        <h2>📁 Next Steps</h2>
        <div class="info-box">
            <p><strong>To run the generated app:</strong></p>
            <pre style="background: #34495e;">cd generated_app
python main.py</pre>
            <p><strong>To run the tests:</strong></p>
            <pre style="background: #34495e;">python run_test.py
# OR
cd generated_app && pytest -v</pre>
        </div>
        {% endif %}
    </div>
    
    <script>
        function showLoading() {
            document.getElementById('loadingDiv').style.display = 'block';
            document.getElementById('submitBtn').disabled = true;
            document.getElementById('submitBtn').innerText = 'Generating...';
        }
    </script>
</body>
</html>
"""

DEFAULT_REQUIREMENTS = """Create a Culture Facts application with these features:
1. Show all cultures (list_cultures function)
2. Show detailed description of a specific culture (get_details function)
3. Search for a culture by name (search_culture function)
4. Randomly display a cultural trivia tidbit (get_random_fact function)
5. All data comes from cultures.json
6. Include at least 5 diverse cultures from around the world
7. Terminal-based UI with a menu system
8. Proper error handling for invalid inputs"""


@app.route("/", methods=["GET", "POST"])
def home():
    req = DEFAULT_REQUIREMENTS
    result = None
    usage = None

    if request.method == "POST":
        req = request.form.get("req", DEFAULT_REQUIREMENTS)
        
        try:
            out = run_system(req)
            result = out.get("result", {})
            usage = out.get("usage", {})
        except Exception as e:
            result = {"error": str(e)}
            usage = {}

    return render_template_string(HTML, req=req, result=result, usage=usage)


if __name__ == "__main__":
    print("=" * 50)
    print("Starting Culture Facts Generator GUI")
    print("Open http://127.0.0.1:5000 in your browser")
    print("=" * 50)
    app.run(debug=True, host="0.0.0.0", port=5000)
