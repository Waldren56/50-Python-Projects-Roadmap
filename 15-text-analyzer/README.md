# 15 — Text File Analyzer

A terminal tool that reads a `.txt` file and prints the 10 most frequently occurring words. Text is normalized before counting — lowercased and stripped of punctuation — so "Driver", "driver", and "driver," are all counted as the same word. If the target file doesn't exist, it is created automatically with an empty content notice.

## Skills used

- File I/O with `open()` and `os.path.exists()`
- Text normalization: `.lower()` and `str.translate()` with `string.punctuation`
- `collections.Counter` for word frequency counting
- `.most_common(N)` to retrieve top N results already sorted
- Graceful handling of missing files without crashing

## How to run

```bash
cd 15-text-analyzer
python main.py
```

No external dependencies required. Place your text in `text.txt` in the same folder before running.