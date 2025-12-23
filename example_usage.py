"""
TOTP Authenticator - Example Usage
Demonstrates how to use the totp_authenticator package
"""

import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from totp_generator import TOTPGenerator
from qr_generator import QRGenerator

def main():
    print("TOTP Authenticator Demo")
    print("=" * 40)

    # 1. Generate a secret key
    print("\n1. Generating a secret key...")
    secret = TOTPGenerator.generate_secret()
    print(f"    Secret: {secret}")

    # 2. Create a TOTP URI for QR code
    print("\n2. Creating TOTP setup URI...")
    uri = TOTPGenerator.get_provisioning_uri(
        secret_key = secret,
        account_name = "example@example.com",
        issuer_name = "TestApp"
    )
    print(f"    URI: {uri[:60]}...")

    # 3. Generate QR code
    print("\n3. Generating QR code...")
    qr_filename = "totp_setup.png"
    QRGenerator.generate_qr_code(uri, qr_filename)
    print(f"    Saved: {qr_filename}")
    print(f"    (Scan with Google Authenticator)")

    # 4. Show TOTP codes
    print("\n4. Generated TOTP codes:")
    print("    Time       | Code   | Valid for")
    print("   " + "-" * 30)
    
    for i in range(3):
        code = TOTPGenerator.generate_totp(secret)
        remaining = TOTPGenerator.time_remaining()
        print(f"    {time.strftime('%H:%M:%S')}   | {code} | {remaining}s")
        
        if i < 2:
            time.sleep(5)  
    
    # 5. Verify a code
    print("\n5. Verifying codes...")
    valid_code = TOTPGenerator.generate_totp(secret)
    if TOTPGenerator.verify_code(secret, valid_code):
        print(f"   ✅ Code '{valid_code}' is valid")
    else:
        print(f"   ❌ Code '{valid_code}' is invalid")

    if not TOTPGenerator.verify_code(secret, "000000"):
        print("   ✅ Code '000000' correctly rejected")
    else:
        print("   ❌ Code '000000' should have been rejected")

    print("\n" + "=" * 40)
    print("Demo over!")
    print(f"Scan {qr_filename} with your authenticator app.")
    print("The codes should match")

if __name__ == "__main__":
    main()