#!/bin/bash

while [ "$input" != finish ]; do
  echo "Re-starting Django runserver"
  python3 manage.py runserver
  sleep 0.5
done