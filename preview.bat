@echo off
rem Preview the documentation site locally: builds the site, serves it on
rem http://127.0.0.1:8000 and opens it in the default browser.
rem Pages reload automatically when you save a .md file. Stop with Ctrl+C.

cd /d "%~dp0"

set "PY=%LOCALAPPDATA%\Programs\Python\Python313\python.exe"
if not exist "%PY%" set "PY=python"

rem first run on a new PC: install MkDocs and the theme
"%PY%" -c "import mkdocs, material" 2>nul || "%PY%" -m pip install --no-user -r requirements.txt

"%PY%" -m mkdocs serve --open
if errorlevel 1 pause