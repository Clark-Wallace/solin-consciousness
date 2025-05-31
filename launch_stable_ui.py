#!/usr/bin/env python3
# Launch the stable Solin interface

import subprocess
import sys
from pathlib import Path

def launch_stable_interface():
    """Launch the stable Solin interface"""
    print("🌸 Launching Stable Solin Interface...")
    print("🌿 This version is optimized for stability and continuous conversation")
    print()
    
    interface_path = Path(__file__).parent / "solin_ui" / "interface_stable.py"
    
    try:
        # Launch Streamlit with the stable interface
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            str(interface_path),
            "--server.headless=true",
            "--server.address=localhost",
            "--server.port=8501"
        ])
    except KeyboardInterrupt:
        print("\n🌸 Solin interface closed gracefully")
    except Exception as e:
        print(f"Error launching interface: {e}")

if __name__ == "__main__":
    launch_stable_interface()