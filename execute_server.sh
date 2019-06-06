#!/bin/bash

cd ~/Documents/cedecur
source cedecur_env/bin/activate
DEBUG=True ./manage.py runserver
