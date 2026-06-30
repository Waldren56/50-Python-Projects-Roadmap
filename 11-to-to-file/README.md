# 11 — To-Do List with File Persistence

A terminal-based to-do list that saves tasks to a `.txt` file so they persist between sessions. Supports adding, editing, removing, and clearing tasks, with input validation throughout.

## Skills used

- File I/O with `open()` in read, write, and append modes
- `os.path.exists()` to handle missing files gracefully
- Input validation with `try/except` and `while True` loops
- Separation of concerns: each operation has its own function

## How to run

```bash
cd 11-todo-file
python main.py
```

No external dependencies required.