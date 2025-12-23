"""
QR Code Generator for TOTP setup
"""
import qrcode
from PIL import Image, ImageDraw
import pyotp
import os

class QRGenerator:
    """Generate QR codes for TOTP setup"""

    @staticmethod
    def generate_qr_code(data, filename="qr_code.png", box_size=10, border=4, 
                         fill_color="black", back_color="white", 
                         logo_path=None):
        """
        Generate and save QR code
        Args:
            data (str): data to encode in the QR code
            filename (str): output file name
            box_size (int): size of each box in the QR code 
            border (int): border size in boxes
            fill_color (str): color of QR code modules
            back_color (str): background color
            add_logo (bool): add logo to the centre
            logo_path (str): directory file path to logo 

        Returns:
            str: Path to the generated QR code image
        """

        # Validate data
        if not data or not isinstance(data, str):
            raise ValueError("Data must be a non empty string")
        
        # Create QR code
        qr = qrcode.QRCode(
            version=1, 
            error_correction=qrcode.constants.ERROR_CORRECT_H, # High error correction, 30% of QR code can be missing or damaged, still can scan
            box_size=box_size, 
            border=border)
        
        qr.add_data(data)
        # generates QR code matrix, and automatically determine optimal version size
        qr.make(fit=True)

        # Create image
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Save image
        img.save(filename)
        print(f"QR code save to: {filename}")
        return filename
    
    