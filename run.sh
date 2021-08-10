#!/bin/bash

flask db upgrade
sleep 5

python insert_data.py
sleep 5

flask run --host 0.0.0.0
