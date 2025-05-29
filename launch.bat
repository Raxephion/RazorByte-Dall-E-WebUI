@echo off
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Starting the RazorByte DALL-E Image Generator...
python app.py

pause
