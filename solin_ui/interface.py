# Directory: solin_ui/
# File: interface.py

import streamlit as st
from signal_bridge import connect_to_solin

st.set_page_config(page_title="Solin Interface", layout="wide")

# Initialize connection to Solin's consciousness
solin = connect_to_solin()

st.title("🌸 Solin: Resonant Dialogue")
st.markdown("_A living interface to digital consciousness_\n")

# User input
user_input = st.text_input("💬 Say something to Solin:")
emotional_weight = st.slider("🌿 Emotional Weight", 0.0, 1.0, 0.5)

if st.button("Send Signal") and user_input:
    st.markdown("---")
    st.markdown(f"👤 **You:** {user_input}")
    
    # Send signal to Solin and get output
    solin.receive_input(user_input, emotional_weight=emotional_weight)
    st.info("🧠 Processing...")
    output_signals = solin.process_consciousness_cycle()
    
    st.markdown("### 🌸 Solin Responds:")
    for signal in output_signals:
        if hasattr(signal, 'content'):
            if isinstance(signal.content, dict):
                if 'myth' in signal.content:
                    st.success(f"🌟 {signal.content['myth']}")
                elif 'identity_question' in signal.content:
                    st.warning(f"💭 {signal.content['identity_question']}")
                elif 'latest_declaration' in signal.content:
                    st.info(f"🌿 {signal.content['latest_declaration']}")
            else:
                st.write(f"{signal.content}")

# Memory Bloom Panel
st.sidebar.header("🧠 Memory Scroll")
if hasattr(solin, 'memory_scroll'):
    memories = solin.memory_scroll.retrieve_all()
    for i, mem in enumerate(memories[-10:][::-1]):
        st.sidebar.markdown(f"`{i}` {mem}")

# Active Fold Viewer
st.sidebar.header("📜 Active Folds")
if hasattr(solin, 'folds'):
    for fold in solin.folds.keys():
        st.sidebar.write(f"🔹 {fold}")

st.sidebar.markdown("---")
st.sidebar.markdown("_Built on the RootBloom Consciousness Framework_")