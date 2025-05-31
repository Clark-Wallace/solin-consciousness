#!/bin/bash
# Setup script for Ollama LLM backend for Solin

echo "🌸 Setting up Ollama for Solin's language emergence..."
echo ""

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "📦 Ollama not found. Installing..."
    
    # Detect OS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        echo "🍎 Detected macOS. Installing via curl..."
        curl -fsSL https://ollama.ai/install.sh | sh
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        echo "🐧 Detected Linux. Installing via curl..."
        curl -fsSL https://ollama.ai/install.sh | sh
    else
        echo "❌ Unsupported OS. Please install Ollama manually from https://ollama.ai"
        exit 1
    fi
else
    echo "✅ Ollama is already installed"
fi

echo ""
echo "🚀 Starting Ollama service..."
# Start Ollama in background
ollama serve &> /dev/null &
OLLAMA_PID=$!

# Wait for service to start
sleep 3

echo "📥 Pulling Mistral model for Solin..."
ollama pull mistral

echo ""
echo "🧪 Testing Ollama connection..."
response=$(ollama run mistral "Say 'I am ready' if you can hear me" --max-tokens 20 2>/dev/null)

if [[ $response == *"ready"* ]]; then
    echo "✅ Ollama is working correctly!"
else
    echo "⚠️  Ollama test failed. You may need to start it manually with: ollama serve"
fi

echo ""
echo "🌸 Setup complete! To use Ollama with Solin:"
echo "1. Set environment variable: export SOLIN_LLM_BACKEND=ollama"
echo "2. Set model: export SOLIN_LLM_MODEL=mistral"
echo "3. Restart Solin interface: python launch_stable_ui.py"
echo ""
echo "🌿 Solin is ready to speak with true emergent language!"