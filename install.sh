#!/bin/bash
pkg update && pkg upgrade
pkg install python
pkg install python-pip
pip install colorama
pip install fake-useragent
echo("Устоновка прошла успешно :D")
fi
python3 bomber.py 