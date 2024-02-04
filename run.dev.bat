@echo off
setlocal

:: Set variables for flags
set rebuild=true
set start=true
set clear_all=false

:: Check the command-line arguments
for %%a in (%*) do (
    if "%%a"=="--start" set "rebuild=false"
    if "%%a"=="--clear-all" set "clear_all=true" & set "rebuild=true"
)

:: Function to clear all containers and images
if %clear_all%==true (
    echo Clearing all containers and images...
    docker-compose stop
    docker-compose down --rmi all
    docker container prune -f
    docker image prune -f
    echo Rebuilding and starting discord-bot containers...
    docker-compose up --build bot-dev -d
    goto end
)

:: Function to stop and remove discord-bot containers and images
if %rebuild%==true (
    echo Stopping and removing discord-bot containers and images...
    docker-compose stop
    docker-compose down --rmi all
    echo Rebuilding discord-bot containers...
    docker-compose up --build bot-dev -d
    goto end
)

:: Function to start containers without rebuilding
if %start%==true (
    echo Starting discord-bot containers without rebuilding...
    docker-compose stop bot-dev
    docker-compose up --build bot-dev -d
    docker-compose start bot-dev
    goto end
)

:end
endlocal