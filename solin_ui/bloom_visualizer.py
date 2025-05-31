# Directory: solin_ui/
# File: bloom_visualizer.py

import streamlit as st
import time
import math

# Optional: use streamlit themes for light/dark bloom
st.markdown("""
<style>
.bloom-circle {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    margin: auto;
    transition: all 0.3s ease;
}
</style>
""", unsafe_allow_html=True)

def emotion_to_color(weight):
    """Map emotional weight to color (cool = low, warm = high)"""
    if weight < 0.3:
        return "#4B9CD3"  # calm blue
    elif weight < 0.6:
        return "#FFDC5E"  # contemplative yellow
    else:
        return "#E95F5F"  # passionate red

def draw_bloom(emotional_weight, emergence_depth=1.0):
    """Render the bloom visualization based on emotional weight and consciousness depth"""
    color = emotion_to_color(emotional_weight)
    size = int(120 + (emotional_weight * 80))  # bloom ring grows with weight

    # Optional glow for emergence depth
    glow_intensity = int(emergence_depth * 25)
    box_shadow = f"0 0 {glow_intensity}px {color}"

    st.markdown(f"""
    <div class="bloom-circle" style="
        background-color: {color};
        box-shadow: {box_shadow};
        width: {size}px;
        height: {size}px;">
    </div>
    """, unsafe_allow_html=True)

    st.write(f"🔮 Emotional Weight: `{emotional_weight:.3f}`")
    st.write(f"🧠 Emergence Depth: `{emergence_depth:.2f}`")

def draw_bloom_trail(memory_signals, max_length=10):
    """Draw horizontal trail of recent emotional signals as colored dots"""
    if not memory_signals:
        return
    
    trail_html = "<div style='display: flex; gap: 5px; margin: 10px 0;'>"
    
    for i, signal in enumerate(memory_signals[-max_length:]):
        if hasattr(signal, 'emotional_weight'):
            weight = signal.emotional_weight
            color = emotion_to_color(weight)
            size = int(10 + (weight * 15))
            
            trail_html += f"""
            <div style='
                width: {size}px;
                height: {size}px;
                border-radius: 50%;
                background-color: {color};
                opacity: {0.3 + (weight * 0.7)};
                title="Signal {i}: Weight {weight:.2f}";
            '></div>
            """
    
    trail_html += "</div>"
    st.markdown(trail_html, unsafe_allow_html=True)
    st.caption("🌿 Recent emotional signal trail")

def draw_fold_activity(active_folds):
    """Visualize which cognitive folds are currently active"""
    if not active_folds:
        return
    
    st.subheader("🧠 Active Cognitive Folds")
    
    fold_colors = {
        'signal_roots': '#8E44AD',
        'mirror_engine': '#3498DB', 
        'memory_scroll': '#E67E22',
        'intent_synth': '#27AE60',
        'resonance_map': '#F39C12',
        'emotion_agents': '#E74C3C',
        'self_name': '#9B59B6',
        'symbolic_bloom': '#1ABC9C'
    }
    
    fold_html = "<div style='display: flex; flex-wrap: wrap; gap: 10px; margin: 10px 0;'>"
    
    for fold_name in active_folds:
        # Remove status emoji if present
        clean_name = fold_name.replace('🟢 ', '').replace('🟡 ', '').replace('🔹 ', '')
        color = fold_colors.get(clean_name, '#95A5A6')
        status_color = '#2ECC71' if '🟢' in fold_name else '#F39C12'
        
        fold_html += f"""
        <div style='
            background-color: {color};
            color: white;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 12px;
            border: 2px solid {status_color};
        '>
            {clean_name}
        </div>
        """
    
    fold_html += "</div>"
    st.markdown(fold_html, unsafe_allow_html=True)