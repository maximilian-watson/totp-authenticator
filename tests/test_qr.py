"""
Tests for QR code generator
"""
import os
import tempfile
import pytest

from PIL import Image
from qr_generator import QRGenerator

def test_generate_qr_code_basic():
    """Test basic QR code generation"""

    # Create a temporary file
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
        temp_path = tmp.name

    try:
        # Test data
        test_data = "https://example.com"

        # Generate QR code
        result_path = QRGenerator.generate_qr_code(test_data, temp_path)

        # Check file was created
        assert os.path.exists(result_path)
        assert result_path == temp_path

        # Check it is a valid image
        with Image.open(result_path) as img:
            assert img.format == 'PNG'
            assert img.size[0] > 0
            assert img.size[1] > 0

    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)

def test_generate_qr_code_empty_data():
    """Test that empty data raises ValueError"""
    with tempfile.TemporaryDirectory() as temp_dir:
        filename = os.path.join(temp_dir, "test.png")

        # Test empty string
        with pytest.raises(ValueError) as exc_info:
            QRGenerator.generate_qr_code("", filename)

        error_msg = str(exc_info.value) 
        assert "Data must be a non empty string" == error_msg
        
        # Test None
        with pytest.raises(ValueError) as exc_info:
            QRGenerator.generate_qr_code(None, filename)
        
        error_msg = str(exc_info.value)
        assert "Data must be a non empty string" == error_msg
        