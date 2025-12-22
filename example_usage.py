"""
TOTP Authenticator - Example Usage
"""

import time
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from totp_generator import TOTPGenerator
from qr_generator import QRGenerator

secret = TOTPGenerator.generate_secret()
print(f"Secret: {secret}")

uri = TOTPGenerator.get_provisioning_uri(secret, "test@example.com", "TestApp")
print(f"URI: {uri[:50]}...")

QRGenerator.generate_qr_code(uri, "test_qr.png", box_size=15, border=4)
print(f"QR code saved: test_qr.png")

os.system("open test_qr.png" if sys.platform == "darwin" else "start test_qr.png")
