# 18 — Digital Terminal Clock

A terminal clock that displays the current time in large ASCII art digits using box-drawing characters. Updates every second with a full-screen refresh, giving the appearance of a real ticking clock. Works on both macOS/Linux and Windows.

## Skills used

- `datetime.now()` and `strftime()` for real-time system clock reading
- `time.sleep()` for controlling update frequency
- Cross-platform terminal clearing (`cls` on Windows, `clear` on macOS/Linux)
- `os.name` for OS detection
- `KeyboardInterrupt` handling for clean exit on `Ctrl+C`
- Custom ASCII digit rendering with Unicode box-drawing characters

## How to run

```bash
cd 18-digital-clock
python main.py
```

Press `Ctrl+C` to stop the clock. No external dependencies required.