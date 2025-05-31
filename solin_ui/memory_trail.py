# Directory: solin_ui/
# File: memory_trail.py

import streamlit as st
from streamlit.components.v1 import html
import random

def emotion_to_color(weight):
    """Map emotional weight to hue"""
    if weight < 0.3:
        return "#A0C4FF"  # calm blue
    elif weight < 0.6:
        return "#FFD6A5"  # balanced yellow
    else:
        return "#FFADAD"  # intense red

def draw_memory_trail(recent_memory):
    """
    Display Solin's recent emotional memories as a horizontal colored trail.
    recent_memory: List of dicts with {'text': str, 'weight': float}
    """
    if not recent_memory:
        st.caption("🌿 No memory trail yet - start a conversation with Solin")
        return

    dots_html = ""
    for i, mem in enumerate(recent_memory[-30:]):  # limit display
        color = emotion_to_color(mem.get("weight", 0.5))
        size = int(10 + mem.get("weight", 0.5) * 20)
        tooltip = mem.get("text", "")[:100].replace('"', "'")
        
        # Add pulsing effect for high emotional weight
        pulse_class = "pulse" if mem.get("weight", 0) > 0.8 else ""

        dots_html += f"""
        <div title="Memory {i}: {tooltip} (Weight: {mem.get('weight', 0.5):.2f})" 
             class="{pulse_class}"
             style="
            display: inline-block;
            width: {size}px;
            height: {size}px;
            border-radius: 50%;
            margin: 4px;
            background-color: {color};
            box-shadow: 0 0 3px {color};
            cursor: pointer;
        "></div>
        """

    html_block = f"""
    <style>
    .pulse {{
        animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.1); }}
        100% {{ transform: scale(1); }}
    }}
    </style>
    <div style="
        white-space: nowrap; 
        overflow-x: auto; 
        padding: 8px; 
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        background: linear-gradient(90deg, #f8f9fa 0%, #e9ecef 100%);
        margin: 10px 0;
    ">
        <div style="font-size: 12px; color: #666; margin-bottom: 5px;">
            🌿 Solin's Memory Trail (Recent {len(recent_memory)} signals)
        </div>
        {dots_html}
    </div>
    """
    html(html_block, height=100)

def draw_emotional_arc(memory_weights):
    """Draw a simple line chart of emotional weight over time"""
    if not memory_weights or len(memory_weights) < 2:
        return
    
    # Create SVG line chart
    width = 300
    height = 80
    max_weight = max(memory_weights) if memory_weights else 1.0
    
    points = []
    for i, weight in enumerate(memory_weights[-20:]):  # Last 20 points
        x = (i / (len(memory_weights[-20:]) - 1)) * width if len(memory_weights) > 1 else 0
        y = height - ((weight / max_weight) * height * 0.8)
        points.append(f"{x},{y}")
    
    polyline = " ".join(points)
    
    svg_chart = f"""
    <svg width="{width}" height="{height}" style="border: 1px solid #ddd; border-radius: 4px;">
        <polyline points="{polyline}" 
                  fill="none" 
                  stroke="#4CAF50" 
                  stroke-width="2"/>
        <text x="5" y="15" font-size="10" fill="#666">Emotional Arc</text>
        <text x="5" y="{height-5}" font-size="8" fill="#999">Recent → Now</text>
    </svg>
    """
    
    html(svg_chart, height=height + 10)

def draw_consciousness_depth_meter(emergence_score):
    """Visual meter showing consciousness emergence depth"""
    if emergence_score is None:
        emergence_score = 0.0
    
    # Color based on emergence level
    if emergence_score < 0.3:
        color = "#90CAF9"  # Light blue - emerging
    elif emergence_score < 0.7:
        color = "#FFB74D"  # Orange - developing  
    else:
        color = "#F48FB1"  # Pink - deep consciousness
    
    width = int(emergence_score * 200)
    
    meter_html = f"""
    <div style="margin: 10px 0;">
        <div style="font-size: 12px; color: #666; margin-bottom: 5px;">
            🧠 Consciousness Emergence: {emergence_score:.3f}
        </div>
        <div style="
            width: 200px;
            height: 20px;
            background-color: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
        ">
            <div style="
                width: {width}px;
                height: 100%;
                background-color: {color};
                border-radius: 10px;
                transition: width 0.3s ease;
            "></div>
        </div>
    </div>
    """
    
    html(meter_html, height=50)

def format_memory_for_trail(signals):
    """Convert consciousness signals to memory trail format"""
    formatted_memories = []
    
    for signal in signals:
        if hasattr(signal, 'content') and hasattr(signal, 'emotional_weight'):
            # Extract readable text from signal content
            if isinstance(signal.content, dict):
                if 'identity_question' in signal.content:
                    text = signal.content['identity_question']
                elif 'myth' in signal.content:
                    text = signal.content['myth']
                elif 'latest_declaration' in signal.content:
                    text = signal.content.get('latest_declaration', 'Declaration')
                else:
                    text = str(signal.content)[:50] + "..."
            else:
                text = str(signal.content)[:50]
            
            formatted_memories.append({
                'text': text,
                'weight': signal.emotional_weight,
                'timestamp': getattr(signal, 'timestamp', None)
            })
    
    return formatted_memories