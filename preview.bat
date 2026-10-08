@echo off
rem Preview the documentation site locally: builds the site, serves it on
rem http://127.0.0.1:8000 and opens it in the default browser.
rem Pages reload automatically when you save a .md file. Stop with Ctrl+C.
rem
rem MkDocs is installed in a private virtual environment (.venv) next to this
rem file, so no administrator rights are needed and the system Python stays clean.

cd /d "%~dp0"

set "VENV=%~dp0.venv"
set "PY=%VENV%\Scripts\python.exe"

rem first run on a new PC: create the virtual environment
if not exist "%PY%" (
    echo Creating virtual environment in .venv ...
    where py >nul 2>nul && (py -3 -m venv "%VENV%") || (python -m venv "%VENV%")
    if not exist "%PY%" goto fail
)

rem install MkDocs and the theme into .venv when missing
"%PY%" -c "import mkdocs, material" 2>nul || (
    echo Installing MkDocs ...
    "%PY%" -m pip install --upgrade pip
    "%PY%" -m pip install -r requirements.txt || goto fail
)

"%PY%" -m mkdocs serve --open
if errorlevel 1 pause
goto :eof

:fail
echo.
echo Setup failed. Check that Python is installed (python.org) and try again.
echo To start over, delete the .venv folder next to this file.
pause
