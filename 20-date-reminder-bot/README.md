# 20 — Event Reminder

A terminal tool to track upcoming events with date-based reminders. For each saved event, shows how many days are left, flags it as TODAY, or marks it as passed. Supports full CRUD: add, view, update, and delete events. Data persists across sessions in a JSON file.

## Skills used

- `datetime.strptime()` to parse date strings into `date` objects
- `date.today()` for real-time date comparison
- `timedelta.days` arithmetic to calculate days remaining
- Three-state reminder logic: today / N days left / passed
- JSON persistence with `read_json()` / `write_json()` pattern
- Input validation for both event name and date format (DD/MM/YYYY)
- Past-date rejection at input time

## How to run

```bash
cd 20-event-reminder
python main.py
```

No external dependencies required. Events are saved to `data.json` in the same folder.