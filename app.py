from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime, timedelta, date

app = Flask(__name__)

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
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

def calculate_longest_streak(dates):
    if not dates:
        return 0
    dates = sorted([datetime.strptime(d, "%Y-%m-%d") for d in dates])
    longest = 1
    current = 1
    for i in range(1, len(dates)):
        if dates[i] - dates[i-1] == timedelta(days=1):
            current += 1
            longest = max(longest, current)
        else:
            current = 1
    return longest

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
        return jsonify({"message": "Session added", "date": today})
    return jsonify({"message": "Already logged today", "date": today})

@app.route("/delete", methods=["POST"])
def delete():
    data = load_data()
    date = request.json.get("date")
    if date in data:
        data.remove(date)
        save_data(data)
        return jsonify({"message": f"Removed {date}"})
    return jsonify({"message": "Date not found"}), 404

@app.route("/history")
def history():
    data = load_data()
    data_sorted = sorted(data, reverse=True)
    return jsonify({"history": data_sorted, "count": len(data_sorted)})

@app.route("/weekly")
def weekly():
    data = load_data()
    today = date.today()
    week = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(6, -1, -1)]
    result = [{"date": d, "studied": d in data} for d in week]
    return jsonify({"week": result})

if __name__ == "__main__":
    app.run(debug=True)