# 17 — QR Code Generator

A terminal tool that validates a URL and generates a custom QR code image. Uses inverted colors (white QR on a black background) to give the code a unique look while remaining scannable.

## Skills used

- HTTP requests with `requests.head()` and `requests.get()`
- URL validation with `response.ok`
- Exception handling with `RequestException`
- User input validation with loops
- QR code generation using the `qrcode` library
- File creation and image saving as `.png`

## How to run

```bash
cd 17-qr-code-generator
uv add qrcode requests pillow
uv run main.py
```

Requires an active internet connection to validate URLs.