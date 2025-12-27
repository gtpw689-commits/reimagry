#!/data/data/com.termux/files/usr/bin/bash
# Update Termux packages
pkg update && pkg upgrade -y

# Install essential packages
pkg install python git wget -y

# Install Python packages
pip install --upgrade pip
pip install gpt4all requests

# Create models folder
mkdir -p ~/reimagry/models
