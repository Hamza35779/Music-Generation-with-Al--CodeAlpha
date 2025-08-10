#!/usr/bin/env python3
"""
Install required dependencies for MP3 music generation
"""

import subprocess
import sys
import os

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def check_system_package(package):
    """Check if a system package is available"""
    try:
        subprocess.run([package, '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_system_package(package):
    """Install system package using apt-get"""
    try:
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', package], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("=== Installing Dependencies for MP3 Music Generation ===")
    
    # Python packages
    python_packages = [
        'pydub',
        'ffmpeg-python'
    ]
    
    print("\nInstalling Python packages...")
    for package in python_packages:
        print(f"Installing {package}...")
        if install_package(package):
            print(f"✓ {package} installed successfully")
        else:
            print(f"✗ Failed to install {package}")
    
    # System packages
    system_packages = ['timidity', 'fluidsynth']
    
    print("\nChecking system packages...")
    for package in system_packages:
        if check_system_package(package):
            print(f"✓ {package} is already installed")
        else:
            print(f"Installing {package}...")
            if install_system_package(package):
                print(f"✓ {package} installed successfully")
            else:
                print(f"✗ Failed to install {package}")
                print(f"Please install {package} manually: sudo apt-get install {package}")
    
    print("\n=== Installation Complete ===")
    print("You can now use the enhanced MP3 generator!")

if __name__ == "__main__":
    main()
