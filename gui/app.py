# Author: Your Name - Student ID: XXXXXXX

from flask import Flask, request, render_template_string
from run_system import run_system

app = Flask(__name__)

HTML = """
<h1>AI Coder - Culture Facts (Gemini Version)</h1>

<form method="POST">
<textarea name="req" style="width:600px;height:200px;">{{ req }}</textarea><br>
<button type="submit">Generate Culture Facts App</button>
</form>

{% if result %}
<h2>Build Result</h2>
<pre>{{ result }}</pre>
{% endif %}

{% if usage %}
<h2>Usage Report</h2>
<pre>{{ usage }}</pre>
{% endif %}
"""

@app.route("/", methods=["GET","POST"])
def home():
    req = ""
    result = None
    usage = None

    if request.method == "POST":
        req = request.form["req"]
        out = run_system(req)
        result = out["result"]
        usage = out["usage"]

    return render_template_string(HTML, req=req, result=result, usage=usage)

if __name__ == "__main__":
    app.run(debug=True)

