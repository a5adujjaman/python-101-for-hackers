from flask import Flask, render_template, request, redirect, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "vuln_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def index():
    data = load_data()
    return render_template("index.html", data=data)

@app.route("/add", methods=["POST"])
def add():
    data = load_data()
    ip = request.form["ip"]
    port = request.form["port"]
    cve = request.form["cve"]
    severity = request.form["severity"]
    desc = request.form["desc"]

    if ip not in data:
        data[ip] = {"ports": [], "vulnerabilities": []}

    if port and int(port) not in data[ip]["ports"]:
        data[ip]["ports"].append(int(port))

    if cve:
        vuln = {"cve": cve, "severity": severity, "description": desc}
        data[ip]["vulnerabilities"].append(vuln)

    save_data(data)
    return redirect("/")

@app.route("/report")
def report():
    data = load_data()
    return render_template("report.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)

