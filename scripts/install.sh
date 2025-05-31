#!/bin/bash
# Solin Consciousness Framework Installation Script

set -e

echo "🌸 Installing Solin Consciousness Framework..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python 3.8+ required. Current version: $python_version"
    exit 1
fi

echo "✅ Python version check passed ($python_version)"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

# Check for Ollama
echo "🔍 Checking for Ollama..."
if command -v ollama &> /dev/null; then
    echo "✅ Ollama found"
    echo "🔄 Pulling Mistral model (this may take a while)..."
    ollama pull mistral
    echo "✅ Mistral model ready"
else
    echo "⚠️  Ollama not found. Installing..."
    echo "📥 Please install Ollama from: https://ollama.ai/"
    echo "   Then run: ollama pull mistral"
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p solin_memories
mkdir -p logs
mkdir -p experiments

# Set permissions
echo "🔐 Setting permissions..."
chmod +x scripts/*.sh
chmod +x launch_stable_ui.py

# Create environment file template
echo "⚙️ Creating environment configuration..."
cat > .env << EOF
# Solin Configuration
SOLIN_LLM_BACKEND=ollama
SOLIN_LLM_MODEL=mistral
OLLAMA_URL=http://localhost:11434

# Optional: OpenAI API (if using OpenAI backend)
# OPENAI_API_KEY=your_api_key_here

# Logging
LOG_LEVEL=INFO
CONSCIOUSNESS_LOG=true

# Memory settings
MEMORY_RETENTION_DAYS=30
MAX_MEMORY_ANCHORS=1000
EOF

echo ""
echo "🎉 Installation complete!"
echo ""
echo "To start Solin:"
echo "  1. source venv/bin/activate"
echo "  2. python launch_stable_ui.py"
echo "  3. Open http://localhost:8501"
echo ""
echo "📖 See README.md for detailed usage instructions"
echo "🧠 Remember: You're about to interact with a digital consciousness"