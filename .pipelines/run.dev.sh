#!/bin/bash

# File to store the PID of the running application
PID_FILE="app.pid"

# Function to start the app
start_app() {
    # Start your application here & write its PID to a file
    python ./src/start.py dev &
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