# Author: Your Name - Student ID: XXXXXXX

from flask import Flask, request, render_template_string
from run_system import run_system

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Coder - Culture Facts</title>
</head>
<body>
    <h1>AI Coder - Culture Facts</h1>
    <form method="post">
        <p>Paste your Culture Facts requirements:</p>
        <textarea name="req" style="width:600px;height:200px;">{{ req }}</textarea><br>
        <button type="submit">Generate App</button>
    </form>

    {% if result %}
    <h2>Build Result</h2>
    <pre>{{ result }}</pre>
    {% endif %}

    {% if usage %}
    <h2>Model Usage Report</h2>
    <pre>{{ usage }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    req_text = ""
    result = None
    usage = None

    if request.method == "POST":
        req_text = request.form.get("req", "")
        output = run_system(req_text)
        result = output.get("build")
        usage = output.get("usage")

    return render_template_string(
        HTML,
        req=req_text,
        result=result,
        usage=usage
    )

if __name__ == "__main__":
    # Default for local debugging
    app.run(debug=True)
