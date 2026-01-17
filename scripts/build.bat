@echo off
setlocal enabledelayedexpansion

REM 切换到项目根目录
cd /d "%~dp0.."

echo =========================================
echo PCL Installer Build Script
echo =========================================
echo.

REM Check if Python is installed
python --version >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python not found. Please install Python 3.14 or later.
    echo Download link: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python detected:
python --version
echo.

REM Install dependencies
echo Installing dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)
echo.

REM Build EXE
echo Building EXE file...
python -m PyInstaller --onefile --noconsole --add-data "assets/modpack.mrpack;assets" --name "PCL_Installer" src/main.py
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to build EXE
    pause
    exit /b 1
)
echo.

echo =========================================
echo Build completed successfully!
echo Output file: dist/PCL_Installer.exe
echo =========================================
echo.

REM Cleanup temporary files
echo Do you want to clean up temporary build files? (y/n)
set /p clean=""
if /i "%clean%"=="y" (
    echo Cleaning up temporary files...
    rmdir /s /q build >nul 2>nul
    del /q *.spec >nul 2>nul
    echo Cleanup completed
)

echo.
echo Press any key to exit...
pause >nul