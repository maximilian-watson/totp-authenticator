"""
Unit tests for TOTP Generator
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from totp_generator import TOTPGenerator
import pyotp
import time

def test_generate_secret():
    """Test secret generation"""
    secret = TOTPGenerator.generate_secret()
    assert len(secret) >= 16  
    assert isinstance(secret, str)

def test_generate_totp():
    """Test TOTP generation"""
    test_secret = "JBSWY3DPEHPK3PXP" 
    
    our_code = TOTPGenerator.generate_totp(test_secret)
    
    expected_code = pyotp.TOTP(test_secret).now()
    
    assert our_code == expected_code
    assert len(our_code) == 6
    assert our_code.isdigit()
