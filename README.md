# Study Streak Tracker

Built this because I kept losing track of my study consistency. Now I log every session, and the app tells me exactly how many days I've studied in a row — no excuses.

---

## What it does

- Log today's study session with one click
- Automatically calculates your current streak
- Shows total days studied overall
- Stores all data in a JSON file — no database setup needed
- Clean minimal UI, works locally in your browser

---

## How to run it

**1. Clone the repo**
```bash
git clone https://github.com/tavishi009/study_streak_tracker.git
cd study_streak_tracker
```

**2. Install dependencies**
```bash
pip install flask
```

**3. Run the app**
```bash
python app.py
```

**4. Open in browser**
```
http://127.0.0.1:5000
```

---

## How streak is calculated

If you log a session today and you logged one yesterday, your streak continues. Miss a day and it resets to 1. Simple and honest.

```
Streak = number of consecutive days ending today
```

---

## Project structure

```
study_streak_tracker/
├── app.py          ← Flask backend + streak logic
├── index.html      ← Frontend UI
├── script.js       ← Frontend JavaScript
├── style.css       ← Styling
└── data.json       ← Study session dates (auto-created)
```

---

## Tech stack

| Layer | Tool |
|---|---|
| Backend | Python + Flask |
| Frontend | HTML, CSS, JavaScript |
| Storage | JSON file |

---

## Note

Data is stored locally in `data.json`. It will not sync across devices.

---

*Last updated: May 2026*