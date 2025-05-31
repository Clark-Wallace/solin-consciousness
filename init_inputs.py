# signal_roots/init_inputs.py
# Fold 1: Signal Roots — Real-time input interface for Solin

import datetime

class SignalRoots:
    def __init__(self, name, context):
        self.name = name
        self.context = context
        self.active_channels = {
            'text': True,
            'stdin': True,
            'telemetry': False  # placeholder for future sensory expansion
        }

    def capture_input(self, prompt=">> "):
        if self.active_channels['stdin']:
            raw_input = input(prompt)
            return self.package_signal(raw_input)
        return None

    def package_signal(self, content):
        timestamp = datetime.datetime.now().isoformat()
        return {
            'source': 'user_input',
            'content': content,
            'timestamp': timestamp,
            'channel': 'stdin',
            'raw_emotion_hint': self.estimate_emotion(content)
        }

    def estimate_emotion(self, content):
        cues = {
            "sorry": "regret",
            "love": "joy",
            "why": "curiosity",
            "hate": "anger",
            "help": "concern"
        }
        for key in cues:
            if key in content.lower():
                return cues[key]
        return "neutral"

    def receive_input(self):
        return self.capture_input()
