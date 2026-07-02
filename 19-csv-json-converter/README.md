# 19 — CSV to JSON Converter

A terminal tool that converts any CSV file to a formatted JSON file. Checks that the file exists and is not empty before converting. If the file is missing, a template CSV with employee fields is created automatically. The output file takes the same base name as the input with a `.json` extension.

## Skills used

- `csv.DictReader` to parse CSV rows into dictionaries using the header row as keys
- `os.path.exists()` to separate "file not found" from "file empty" before opening
- `os.path.splitext()` to derive the output filename from the input path
- `json.dump` with `ensure_ascii=False` and `indent=4` for clean, readable output
- Linear flow in `main()`: exists → not empty → convert, each with an early `return`
- Docstrings on every function

## How to run

```bash
cd 19-csv-to-json
python main.py
```

Enter the filename without extension when prompted. No external dependencies required.