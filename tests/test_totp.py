"""
Unit tests for TOTP Generator
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from totp_generator import TOTPGenerator
import pyotp
import pytest
import time

def test_generate_secret():
    """Test secret generation"""
    secret = TOTPGenerator.generate_secret()
    # Base32 secrets are 16+ characters
    assert len(secret) >= 16  
    assert isinstance(secret, str)


def tests_generate_secret_unique():
    """Test that generated secrets are unique"""
    secret1 = TOTPGenerator.generate_secret()
    secret2= TOTPGenerator.generate_secret()
    assert secret1 != secret2

def test_generate_totp():
    """Test TOTP generation"""
    test_secret = "JBSWY3DPEHPK3PXP" 
    
    # Generate with our library
    our_code = TOTPGenerator.generate_totp(test_secret)
    
    # Generate with pyotp directly to verify
    expected_code = pyotp.TOTP(test_secret).now()
    
    assert our_code == expected_code
    assert len(our_code) == 6
    assert our_code.isdigit()

def test_generate_totp_invalid_secret():
    """Test TOTP generation with invalid secret"""
    # Test with non-base 32 characters
    with pytest.raises(Exception):
        TOTPGenerator.generate_totp("INVALID!@#$")

def test_verify_code_correct():
    """Test code verification with correct code"""
    test_secret = "JBSWY3DPEHPK3PXP"
    current_code = pyotp.TOTP(test_secret).now()
    assert TOTPGenerator.verify_code(test_secret, current_code) == True
 
def test_verify_code_wrong():
    """Test code verification with wrong code"""
    test_secret = "JBSWY3DPEHPK3PXP"
    
    # Wrong code should fail
    assert TOTPGenerator.verify_code(test_secret, "000000") == False

    # Code with wrong length should fail
    assert TOTPGenerator.verify_code(test_secret, "12345") == False
    assert TOTPGenerator.verify_code(test_secret, "1234567") == False

    # Non-numeric code should fail
    assert TOTPGenerator.verify_code(test_secret, "abcdef") == False

def test_time_remaining():
    """Test time remaining calculation"""
    remaining = TOTPGenerator.time_remaining()
    assert 1 <= remaining <= 30
    assert isinstance(remaining, int)

def test_get_provisioning_uri_basic():
    """Test basic QR code URI generation"""
    secret = "JBSWY3DPEHPK3PXP"
    account = "2.max.leo.watson@gmail.com"
    uri = TOTPGenerator.get_provisioning_uri(secret, account)
    assert uri.startswith("otpauth://totp/")
    assert f"secret={secret}" in uri

    # Account email will be URL-encoded
    # @ becomes %40
    encoded_account = account.replace("@", "%40")
    assert encoded_account in uri

    # Issuer will be URL-encoded 
    # Space becomes %20 or +
    assert "issuer=TOTP%20Generator" in uri or "issuer=TOTP+Generator" in uri

    assert "?" in uri  # Has query parameters
    assert "&" in uri  # Has multiple parameters