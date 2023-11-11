{
    "editor.formatOnSave": true,
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.linting.lintOnSave": true,
    "python.formatting.blackPath": "venv/Scripts/black.exe",
    // Adjust the path accordingly
    "python.formatting.blackArgs": [
        "--line-length",
        "88",
    ],
    "python.linting.flake8Args": [
        "--max-line-length",
        "88",
    ],
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    }
}