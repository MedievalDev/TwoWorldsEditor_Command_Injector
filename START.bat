@echo off
title TW Editor CMD Injector
echo Installiere Abhaengigkeiten...
pip install pyautogui pygetwindow >nul 2>&1
echo Starte Tool...
pythonw tw_editor_cmd_injector.py
if %errorlevel% neq 0 (
    echo.
    echo FEHLER beim Starten! Versuche mit python...
    echo.
    python tw_editor_cmd_injector.py
    echo.
    echo ---- Fenster bleibt offen zum Debuggen ----
    cmd /k
)
