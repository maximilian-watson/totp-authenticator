from setuptools import setup, find_packages

setup(
    name="totp_authenticator",
    version="0.1.0",
    description="A simple TOTP generator like Google Authenticator",
    author="Max Watson",
    author_email="2.max.leo.watson@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pyotp>=2.9.0",
        "qrcode[pil]>=7.4.2",
        "Pillow>=10.1.0",
    ],
    python_requires=">=3.8",
)