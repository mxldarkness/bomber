#!/bin/bash
apt update
apt install git -y
apt install tor -y
apt install iptables -y
git clone https://github.com/ruped24/toriptables2
cd toriptables2
apt install python2
echo "Устоновка прошла успешно :D"
fi
python2 toriptables2.py -l
cd ..
python3 bomber.py 