# Project file structure

- [`src`](../src/)
    Source code directory
    - [`data`](../src/data/)
        Useful classes and constants for bot  
        - [`buttons`](../src/data/buttons/)
            Interaction button classes that bot has
        - [`commands`](../src/data/commands/)
            Constants for command names
        - [`forms`](../src/data/forms/)
            Interaction forms that bot has
    - [`data`](../src/handlers/)
        Handlers for bot commands
    - [`services`](../src/services/)
        Services and data providers for bot application
        -  [`database`](../src/services/database/)
            Database-related services of bot
    - [`start.py`](../src/start.py)
        Main entry point of application