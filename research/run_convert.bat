@echo off
echo Starting PDF to Markdown conversion...

set PYTHON_EXE=C:\ProgramData\miniconda3\envs\markitdown\python.exe
set SCRIPT_PATH=%~dp0convert_pdfs.py

"%PYTHON_EXE%" "%SCRIPT_PATH%"

echo.
pause