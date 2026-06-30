# 14 — Unit Converter

A terminal-based unit converter supporting length (m, km, cm, mm) and weight (g, kg, lb). All conversions go through a base unit (metre for length, gram for weight), so adding new units requires only one new dictionary entry — no additional formulas.

## Skills used

- Nested dictionaries: one per category, each mapping unit names to conversion factors
- Dynamic validation: valid units read from dictionary keys, never hardcoded
- Modular design: data definition, conversion logic, and user interaction in separate functions
- `float` input for decimal measurements

## How to run

```bash
cd 14-unit-converter
python main.py
```

No external dependencies required.