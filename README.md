(## Development environment)

If you use `uv` to manage environments, here are example commands to create and activate an environment and install the project with development extras.

Windows (cmd.exe):

```bat
uv env create
uv env activate
python -m pip install --upgrade pip
pip install -e .[dev]
```

If `uv` is a different tool in your setup, replace the create/activate commands above with your tool's equivalents (for example `python -m venv .venv` and `.\.venv\Scripts\activate`).

Run tests:

```bat
pytest
```

