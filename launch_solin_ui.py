# File: launch_solin_ui.py
# Launch Solin's interface using Streamlit

import subprocess
import os
import sys
from pathlib import Path

def launch_streamlit_ui():
    project_root = Path(__file__).resolve().parent
    ui_file = project_root / "solin_ui" / "interface.py"
    
    if not ui_file.exists():
        print("🌸 Error: Solin interface not found.")
        return

    print("🌿 Launching Solin Bloom Interface...")
    command = [
        "streamlit",
        "run",
        str(ui_file)
    ]
    
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Streamlit failed to launch: {e}")

if __name__ == "__main__":
    launch_streamlit_ui()