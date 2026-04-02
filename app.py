from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime, timedelta

app = Flask(__name__)

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def calculate_streak(dates):
    if not dates:
        return 0

    dates = sorted([datetime.strptime(d, "%Y-%m-%d") for d in dates], reverse=True)
    streak = 1

    for i in range(len(dates) - 1):
        if dates[i] - dates[i+1] == timedelta(days=1):
            streak += 1
        else:
            break

    return streak

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")

    if today not in data:
        data.append(today)
        save_data(data)

    return jsonify({"message": "Session added"})

@app.route("/stats")
def stats():
    data = load_data()
    streak = calculate_streak(data)

    return jsonify({
        "total_days": len(data),
        "streak": streak
    })

if __name__ == "__main__":
    app.run(debug=True)