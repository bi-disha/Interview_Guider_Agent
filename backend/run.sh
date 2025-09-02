#!/bin/bash
if [ "$1" == "cli" ]; then
  python backend/main.py
elif [ "$1" == "ui" ]; then
  streamlit run frontend/streamlit.py
else
  echo "Usage: ./run.sh [cli|ui]"
fi
