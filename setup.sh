#!/data/data/com.termux/files/usr/bin/bash

pkg update && pkg upgrade -y
pkg install python git wget -y
pip install requests gpt4all
mkdir -p ~/reimagry/models
