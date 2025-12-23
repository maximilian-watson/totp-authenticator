# totp-authenticator

A Python implementation of Time based On Time Password (TOTP) generation, similar to the Google Authenticator. This project demonstrates Two Factor Authentication (2FA) in the real world, with 100% test coverage and CI automation.

## Features

- Generate TOTP codes
- Create QR codes for easy setup with authenticator apps
- Verifying TOTP codes with time drift tolerance
- Command-line interface
- Comprehensive testing, 100% coverage
- CI/CD pipeline with GitHub Actions

## How TOTP Works
TOTP generates a 6 digit code that changes every 30 secondes. It combines:

- A secret key, known only to the user and the server
- The current time, each 30 seconds

### Step by Step Process

- Secret Key is generated, this is shared securely through the QR code
- Time Caluclation
  - Time is divided into 30 second chunks
- HMAC-SHA1
  - Creates a unique 6 digit code using the Secret Key and time chunk
  - The 6 digit code
    - Changes every 30 seconds
    - Can't be reversed to find the secret
    - Is always the same for the same time chunk
  - Extracting the 6 digit code
    - Current Unix timestamp is divided by 30 seconds
    - HMAC-SHA1 generates a hash of the time counter using the secret key
    - Extract 4 bytes based on the hash result
    - Converted to a 31-bit integer
    - Take modulo 1,000,000 for the final 6 digit code
    - This process is repeated every 30 seconds, generating new codes in sync with the authenticator app

# Quick Start

```bash
# Clone the repository
git clone https://github.com/maximilian-watson/totp-authenticator.git
cd totp-authenticator

# Install dependencies
pip install -r requirements.txt

# Run the example
python example_usage.py
```

## Testing

```bash
# Install dependencies
pip install -r requirements-dev.txt

# Run tests with coverage
pytest tests/ -v --cov=src --cov-report=html

# Open coverage report
open htmlcov/index.html
```

# Acknowledgments

- Built with PyOTP for TOTP implementation
- QR code generation with qrcode
