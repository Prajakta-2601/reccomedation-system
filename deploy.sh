#!/bin/bash

# Smart Fertilizer System - Deployment Script
# Maharashtra Agriculture Department

echo "🌾 Starting Smart Fertilizer & Production Enhancement System"
echo "🏛️ Maharashtra Government Official System"
echo "========================================================"

# Check Python version
python_version=$(python --version 2>&1)
echo "🐍 Python Version: $python_version"

if ! command -v python &> /dev/null; then
    echo "❌ Python not found. Please install Python 3.8+"
    exit 1
fi

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Check if datasets exist
echo "📊 Checking datasets..."
datasets=("maharashtra_govt_crop_data.csv" "kaggle_fertilizer_prediction.csv" "western_maharashtra_crop_fertilizer.csv")

for dataset in "${datasets[@]}"; do
    if [ ! -f "$dataset" ]; then
        echo "⚠️ Warning: Dataset $dataset not found"
    else
        echo "✅ Found: $dataset"
    fi
done

# Check if main app exists
if [ ! -f "smart_fertilizer_maharashtra_app.py" ]; then
    echo "❌ Main application file not found"
    exit 1
fi

echo "✅ All checks passed!"
echo ""
echo "🚀 Starting Smart Fertilizer System..."
echo "🌐 Application will be available at: http://localhost:8501"
echo "📱 System ready for farmers and agriculture officials"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

# Start the Streamlit application
streamlit run smart_fertilizer_maharashtra_app.py
