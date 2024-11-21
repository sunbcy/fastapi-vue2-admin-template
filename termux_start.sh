#!/usr/bin/env bash
python init_project.py
cd api
tsu
source venv_termux/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
