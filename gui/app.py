"""Starter code"""
# Author: (Your Name) - Student ID: XXXXXXX

from flask import Flask, render_template_string, request
from run_system import run_system

app = Flask(__name__)

HTML = """
<h1>AI Coder - Culture Facts</h1>
<form method="post">
<textarea name="req" style="width:600px;height:200px;"></textarea><br>
<button type="submit">Generate App</button>
</form>
{% if output %}
<pre>{{output}}</pre>
{% endif %}
"""

@app.route("/", methods=["GET","POST"])
def home():
    output = None
    if request.method == "POST":
        req = request.form["req"]
        output = run_system(req)
    return render_template_string(HTML, output=output)

if __name__ == "__main__":
    app.run(debug=True)
