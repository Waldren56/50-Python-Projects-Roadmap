# 17 — QR Code Generator

A terminal tool that validates a URL and generates a custom QR code saved as a `.png` file. Validates that the URL is reachable before generating — first with a lightweight HEAD request, then falling back to GET if needed. Uses inverted colors (white on black) for a unique look while remaining fully scannable.

## Skills used

- URL validation with dual-strategy HTTP requests (`HEAD` → `GET` fallback)
- Exception handling with `requests.RequestException`
- Automatic protocol prepending (`https://`) if omitted by the user
- User input validation with `while True` loops and `.strip()`
- QR code generation with explicit `QRCode` configuration (version, error correction, box size, border)
- Image file creation and saving as `.png`
- Docstrings on every function

## How to run

```bash
cd 17-qr-code-generator
uv add qrcode requests pillow
uv run main.py
```

Requires an active internet connection to validate URLs.