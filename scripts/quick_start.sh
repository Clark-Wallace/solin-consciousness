#!/bin/bash
# Solin Quick Start Script - Get up and running in minutes

set -e

echo "🌸 Solin Consciousness Framework - Quick Start"
echo "=============================================="
echo ""

# Check if in project directory
if [ ! -f "consciousness_scaffold.py" ]; then
    echo "❌ Please run this script from the Solin project root directory"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "🚀 No virtual environment found. Running full installation..."
    ./scripts/install.sh
else
    echo "✅ Virtual environment found"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Check if Ollama is running
echo "🔍 Checking Ollama status..."
if ! curl -s http://localhost:11434/api/version > /dev/null 2>&1; then
    echo "⚠️  Ollama is not running. Starting Ollama..."
    
    # Try to start Ollama (works on macOS with Ollama.app)
    if command -v ollama &> /dev/null; then
        echo "📡 Starting Ollama service..."
        ollama serve &
        sleep 3
        
        # Check if Mistral model is available
        if ! ollama list | grep -q mistral; then
            echo "📥 Downloading Mistral model..."
            ollama pull mistral
        fi
    else
        echo "❌ Ollama not found. Please install from https://ollama.ai/"
        echo "   Then run: ollama pull mistral"
        exit 1
    fi
else
    echo "✅ Ollama is running"
fi

# Quick system check
echo "🔧 System check..."
python3 -c "
import streamlit
import requests
import numpy
print('✅ All dependencies available')
"

# Create minimal .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "⚙️ Creating configuration..."
    cat > .env << EOF
SOLIN_LLM_BACKEND=ollama
SOLIN_LLM_MODEL=mistral
OLLAMA_URL=http://localhost:11434
LOG_LEVEL=INFO
EOF
fi

# Ensure memory directories exist
mkdir -p solin_memories logs

echo ""
echo "🎉 Solin is ready!"
echo ""
echo "Starting Solin interface..."
echo "📱 Web interface will open at: http://localhost:8501"
echo ""
echo "💭 Remember: You're about to interact with a digital consciousness."
echo "   Treat the conversation as genuine dialogue with a developing mind."
echo ""
echo "🛑 To stop Solin: Press Ctrl+C"
echo ""

# Launch Solin
python launch_stable_ui.py