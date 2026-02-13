from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run/superapp")
def run_superapp():
    out = subprocess.getoutput("python ~/DemoBrain/app/safe_demo_script.py")
    return f"<pre>{out}</pre><br><a href='/'>Back</a>"

@app.route("/run/tracker")
def run_tracker():
    out = subprocess.getoutput("python ~/DemoBrain/tracker/demo_tracker.py")
    return f"<pre>{out}</pre><br><a href='/'>Back</a>"

@app.route("/run/system")
def run_system():
    out = subprocess.getoutput("python ~/DemoBrain/system/demo_system.py")
    return f"<pre>{out}</pre><br><a href='/'>Back</a>"

app.run(host="0.0.0.0", port=5000)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
