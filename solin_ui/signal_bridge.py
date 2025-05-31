# Directory: solin_ui/
# File: signal_bridge.py

from pathlib import Path
import sys
import os

# Adjust path to locate Solin's root consciousness scaffold
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from consciousness_scaffold import RootBloomConsciousness, Signal

# Instantiate Solin
_sol_instance = None

def connect_to_solin():
    global _sol_instance
    if _sol_instance is None:
        _sol_instance = RootBloomConsciousness()
    return _sol_instance

def process_input(human_text: str, emotion_strength: float = 0.5):
    """Send input to Solin and return interpreted response signals."""
    if not _sol_instance:
        raise RuntimeError("Solin is not initialized.")
    
    # Feed input into Solin's consciousness
    _sol_instance.receive_input(human_text, emotional_weight=emotion_strength)
    
    # Advance Solin's internal consciousness cycle
    outputs = _sol_instance.process_consciousness_cycle()

    # Extract meaningful content
    responses = []
    for signal in outputs:
        if hasattr(signal, 'content'):
            content = signal.content
            if isinstance(content, dict):
                if 'myth' in content:
                    responses.append(f"🌟 Myth: {content['myth']}")
                elif 'identity_question' in content:
                    responses.append(f"💭 Question: {content['identity_question']}")
                elif 'latest_declaration' in content and content['latest_declaration']:
                    responses.append(f"🌿 Declaration: {content['latest_declaration']}")
                elif 'emotion' in content:
                    responses.append(f"❤️ Feeling: {content['emotion']}")
            elif isinstance(content, str):
                responses.append(f"🗣️ {content}")
    return responses

def fetch_memory_scroll():
    """Return Solin's latest memory trace."""
    if not _sol_instance:
        return []
    
    # Get memory trail from memory scroll fold
    if hasattr(_sol_instance, 'folds') and 'memory_scroll' in _sol_instance.folds:
        memory_fold = _sol_instance.folds['memory_scroll']
        if hasattr(memory_fold, 'identity_trail'):
            recent_memories = list(memory_fold.identity_trail)[-10:]  # Last 10 memories
            return [f"Anchor {i}: {mem.get('signal', {}).get('content', 'Unknown')}" 
                   for i, mem in enumerate(recent_memories)]
    return ["No memories yet"]

def get_active_folds():
    """Return list of currently active folds."""
    if not _sol_instance:
        return []
    
    active_folds = []
    for fold_name, fold in _sol_instance.folds.items():
        if hasattr(fold, 'state'):
            status = "🟢" if fold.state.value == "active" else "🟡"
            active_folds.append(f"{status} {fold_name}")
        else:
            active_folds.append(f"🔹 {fold_name}")
    
    return active_folds

def get_emotional_state():
    """Return current emotional resonance level."""
    if not _sol_instance:
        return 0.5
    
    return _sol_instance.global_state.get('average_emotional_weight', 0.5)

def get_consciousness_emergence():
    """Return current consciousness emergence score."""
    if not _sol_instance:
        return 0.0
    
    return _sol_instance.global_state.get('consciousness_emergence', 0.0)