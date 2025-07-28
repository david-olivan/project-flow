# Backend Development Setup

This backend uses a standard Python virtual environment with pip instead of pipenv.

## Quick Start (Git Bash)

1. **Navigate to the project root**:
   ```bash
   cd /c/dev/project-flow
   ```

2. **Activate the virtual environment**:
   ```bash
   source backend/activate.sh
   ```
   Or manually:
   ```bash
   source backend/.venv/Scripts/activate
   ```

3. **Install dependencies** (if not already done):
   ```bash
   pip install -r backend/requirements.txt
   pip install -r backend/requirements-dev.txt
   ```

4. **Run the FastAPI development server**:
   ```bash
   fastapi dev app/main.py
   ```

## Commands Reference

- **Activate virtual environment**: `source backend/.venv/Scripts/activate`
- **Deactivate virtual environment**: `deactivate`
- **Install new package**: `pip install package_name`
- **Update requirements**: `pip freeze > backend/requirements.txt`
- **Run FastAPI dev server**: `fastapi dev app/main.py`

## VS Code Integration

When using VS Code with Git Bash as your integrated terminal:

1. Open VS Code in the project root
2. Open the integrated terminal (Ctrl+`)
3. Make sure Git Bash is selected as your terminal
4. Run `source backend/activate.sh` to activate the virtual environment
5. The virtual environment will be indicated by `(.venv)` in your terminal prompt

## File Structure

```
backend/
├── .venv/              # Virtual environment (git ignored)
├── app/main.py         # FastAPI application
├── requirements.txt    # Python dependencies
├── activate.sh         # Convenience script to activate venv
└── DEV_SETUP.md        # This file
```
