#!/bin/bash
#source /home/nbuser/anaconda3_420/bin/activate
#pip install -r requirements.txt
pelican content -s publishconf.py
ghp-import output -b master
git push origin master
git config --global user.email "wykeith@gmail.com"
git config --global user.name "wykeith"