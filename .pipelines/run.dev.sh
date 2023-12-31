#!/bin/bash

# File to store the PID of the running application
PID_FILE="app.pid"

# Function to start the app
start_app() {
    # Start your application here & write its PID to a file
    py -m pip install pipenv
    py -m pipenv install
    py -m pipenv run py -m pylint --recursive=y ./src

    py -m pipenv run py ./src/start.py dev &
    echo $! > "$PID_FILE"
}

# Function to stop the app
stop_app() {
    if [ -f "$PID_FILE" ]; then
        kill $(cat "$PID_FILE") && rm "$PID_FILE"
    fi
}

# Stop the currently running app if exists
stop_app

# Start the app
start_app