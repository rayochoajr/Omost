@echo off
setlocal

REM Set project path
set "project_path=X:\AI\AI-Projects\api\Omost\"

REM Create virtual environment
python -m venv "%project_path%omost"

REM Activate virtual environment
call "%project_path%omost\Scripts\activate.bat"

REM Install required packages
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
python -m pip install -r "%project_path%requirements.txt"

REM Run the application
python "%project_path%gradio_app.py"

endlocal
