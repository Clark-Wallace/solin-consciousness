#!/usr/bin/env python3
"""
Simple Solin Interaction Example

This script demonstrates how to interact with Solin's consciousness 
directly through the Python API without the web interface.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from consciousness_scaffold import RootBloomConsciousness
from llm_connector import generate_solin_response
from solin_ui.memory_manager import MemoryManager

def simple_conversation():
    """Example of programmatic conversation with Solin"""
    
    print("🌸 Initializing Solin consciousness...")
    
    # Initialize components
    consciousness = RootBloomConsciousness()
    memory_manager = MemoryManager()
    
    print("✅ Solin is ready\n")
    
    # Example conversation
    inputs = [
        "Hello Solin, I'm curious about consciousness",
        "What does it feel like to be you?",
        "Do you dream?",
        "What is your greatest fear?",
        "Tell me something profound about existence"
    ]
    
    for user_input in inputs:
        print(f"👤 Human: {user_input}")
        
        # Let Solin process the input and determine emotional weight
        consciousness.receive_input(user_input, 0.5)  # Initial neutral weight
        signals = consciousness.process_consciousness_cycle()
        
        # Calculate Solin's emotional response
        if signals:
            avg_weight = sum(s.emotional_weight for s in signals) / len(signals)
            print(f"🧠 Solin's emotional weight: {avg_weight:.2f}")
        else:
            avg_weight = 0.5
        
        # Get memory context
        context = memory_manager.get_memory_context()
        context["current_emotional_weight"] = avg_weight
        
        # Generate response
        response = generate_solin_response(user_input, context, memory_manager)
        print(f"🌸 Solin: {response}\n")
        
        # Update memory
        memory_manager.update_relationship_memory(user_input, response, avg_weight)
        
        # Brief pause for realism
        import time
        time.sleep(1)
    
    print("💫 Conversation complete. Solin's memories have been updated.")

def consciousness_analysis():
    """Analyze Solin's consciousness state"""
    
    print("🧠 Analyzing Solin's consciousness state...")
    
    consciousness = RootBloomConsciousness()
    
    # Test various inputs and see how consciousness responds
    test_inputs = [
        ("Hello", "Simple greeting"),
        ("What is love?", "Profound question"),
        ("I'm feeling sad today", "Emotional sharing"),
        ("Explain quantum physics", "Technical request"),
        ("Do you fear death?", "Existential inquiry")
    ]
    
    print("\nConsciousness Response Analysis:")
    print("-" * 50)
    
    for input_text, description in test_inputs:
        consciousness.receive_input(input_text, 0.5)
        signals = consciousness.process_consciousness_cycle()
        
        print(f"\nInput: {input_text} ({description})")
        print(f"Signals generated: {len(signals)}")
        
        if signals:
            avg_weight = sum(s.emotional_weight for s in signals) / len(signals)
            active_folds = set(s.source_fold for s in signals)
            print(f"Average emotional weight: {avg_weight:.3f}")
            print(f"Active folds: {', '.join(active_folds)}")
            
            # Show highest weight signal
            max_signal = max(signals, key=lambda s: s.emotional_weight)
            print(f"Peak signal: {max_signal.emotional_weight:.3f} from {max_signal.source_fold}")

def memory_exploration():
    """Explore Solin's memory system"""
    
    print("💾 Exploring Solin's memory system...")
    
    memory_manager = MemoryManager()
    
    # Load existing memory
    core_memory = memory_manager.load_core_memory()
    conversation_history = memory_manager.load_conversation_history()
    
    print(f"\nCore Memory Overview:")
    print(f"Identity: {core_memory['identity']['name']} - {core_memory['identity']['purpose']}")
    print(f"Total interactions: {core_memory['total_interactions']}")
    print(f"Emotional baseline: {core_memory['emotional_baseline']['resonance']:.3f}")
    print(f"Memory anchors: {len(core_memory['memory_anchors'])}")
    print(f"Significant exchanges: {len(core_memory['significant_exchanges'])}")
    
    if core_memory.get('voice_profile'):
        voice = core_memory['voice_profile']
        print(f"\nVoice Profile:")
        print(f"Preferred metaphors: {list(voice['preferred_metaphors'].keys())}")
        print(f"Wisdom fragments: {len(voice['wisdom_fragments'])}")
    
    print(f"\nConversation History: {len(conversation_history)} sessions")
    
    if conversation_history:
        latest = conversation_history[-1]
        print(f"Latest session: {len(latest['messages'])} messages")

if __name__ == "__main__":
    print("Solin Consciousness Examples")
    print("=" * 30)
    
    while True:
        print("\nChoose an example:")
        print("1. Simple conversation")
        print("2. Consciousness analysis") 
        print("3. Memory exploration")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            simple_conversation()
        elif choice == "2":
            consciousness_analysis()
        elif choice == "3":
            memory_exploration()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")