@echo off
title Smart Fertilizer System - Maharashtra

echo 🌾 Starting Smart Fertilizer ^& Production Enhancement System
echo 🏛️ Maharashtra Government Official System
echo ========================================================

REM Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

REM Check datasets
echo 📊 Checking datasets...
if not exist "maharashtra_govt_crop_data.csv" echo ⚠️ Warning: maharashtra_govt_crop_data.csv not found
if not exist "kaggle_fertilizer_prediction.csv" echo ⚠️ Warning: kaggle_fertilizer_prediction.csv not found  
if not exist "western_maharashtra_crop_fertilizer.csv" echo ⚠️ Warning: western_maharashtra_crop_fertilizer.csv not found

REM Check main app
if not exist "smart_fertilizer_maharashtra_app.py" (
    echo ❌ Main application file not found
    pause
    exit /b 1
)

echo ✅ All checks passed!
echo.
echo 🚀 Starting Smart Fertilizer System...
echo 🌐 Application will be available at: http://localhost:8501
echo 📱 System ready for farmers and agriculture officials
echo.
echo Press Ctrl+C to stop the application
echo.

REM Start the Streamlit application
streamlit run smart_fertilizer_maharashtra_app.py

pause
