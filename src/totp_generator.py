"""
TOTP Generator - Core functionality
Generates time-based one-time passwords
"""
import pyotp
import time


class TOTPGenerator:
    """Simple TOTP generator class"""
    
    @staticmethod
    def generate_secret():
        """Generate a new base32 secret key"""
        return pyotp.random_base32()
    
    @staticmethod
    def generate_totp(secret_key):
        """Generate current TOTP code for given secret"""
        totp = pyotp.TOTP(secret_key)
        return totp.now()
    
    @staticmethod
    def verify_code(secret_key, user_code):
        """Verify if user's code is correct"""
        totp = pyotp.TOTP(secret_key)
        return totp.verify(user_code)
    
    @staticmethod
    def time_remaining():
        """Get seconds until next code change"""
        return 30 - (int(time.time()) % 30)
    
    @staticmethod
    def get_provisioning_uri(secret_key, account_name, issuer_name="TOTP Generator"):
        """Get otpauth:// URI for QR code generation"""
        return pyotp.totp.TOTP(secret_key).provisioning_uri(
            account_name,
            issuer_name=issuer_name
        )