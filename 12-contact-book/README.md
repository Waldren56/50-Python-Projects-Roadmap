# 12 — Contact Book (Terminal CRUD)

A terminal-based contact book with full CRUD operations (create, read, update, delete). Contacts are stored in a JSON file and persist between sessions. Each contact has a name, surname, and phone number.

## Skills used

- JSON persistence with `json.load()` and `json.dump()`
- Dictionaries as records (one dict per contact)
- List of dictionaries as the main data structure
- Input validation with `try/except` and `while True` loops
- Modular design: separate functions for each CRUD operation

## How to run

```bash
cd 12-contact-book
python main.py
```

No external dependencies required. A `Contacts.json` file is created automatically on first run.