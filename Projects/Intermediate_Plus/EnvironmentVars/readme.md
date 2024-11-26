# Environment Variables

## Required modules

1. [**python-dotenv**](https://pypi.org/project/python-dotenv/)

    Python-dotenv reads key-value pairs from a `.env` file and can set them as environment variables.

    ```py
    # Activate Development environment
    .venv\scripts\activate

    # Install dotenv
    python -m pip install python-dotenv

    # Deactivate Development environment
    deactivate
    ```

## Usage

1. **load_dotenv()**

    Load environment variables defined in .env file to os

    ```py
    load_dotenv()

    DOMAIN = os.getenv("DOMAIN")
    ```

2. **dotenv_values()**

    The function dotenv_values works more or less the same way as load_dotenv, except it doesn't touch the environment, it just returns a dict with the values parsed from the .env file.

    ```py
    config = {
        **dotenv_values(PATH_TO_PROJECT+".env"), # load environment vars
        **dotenv_values(PATH_TO_PROJECT+".env.shared"), # load shared dev vars
        **dotenv_values(PATH_TO_PROJECT+".env.secret"), # load secret dev vars
        **os.environ, # Load environment variables (will override shared, secret if existing)
    }

    DOMAIN = config["DOMAIN"]
    ```

## Sample

[Code Sample](./main.py)
