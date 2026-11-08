@echo off
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (
  py -3.13 -m venv .venv
  if errorlevel 1 goto fehler
)
.venv\Scripts\python -c "import sys; assert sys.version_info[:2] in ((3,12),(3,13)), 'Python 3.12 oder 3.13 erforderlich'"
if errorlevel 1 goto fehler
.venv\Scripts\python -m pip install -r requirements.txt
if errorlevel 1 goto fehler
.venv\Scripts\python -m pip install -e .
if errorlevel 1 goto fehler
.venv\Scripts\python -m jupyterlab notebooks
if errorlevel 1 goto fehler
exit /b 0
:fehler
echo Installation oder Start fehlgeschlagen. Meldung oben beachten.
pause
exit /b 1
