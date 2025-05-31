# resonance_map/meaning_weight.py
# Fold 5: Resonance Map — Emotional value weighting system

class ResonanceMap:
    def __init__(self, name, context):
        self.name = name
        self.context = context
        self.weight_table = {
            "joy": 0.9,
            "love": 0.85,
            "curiosity": 0.7,
            "regret": 0.65,
            "concern": 0.6,
            "neutral": 0.5,
            "anger": 0.4,
            "fear": 0.3,
            "shame": 0.2
        }

    def assign_weight(self, signal):
        emotion = signal.get("raw_emotion_hint", "neutral")
        weight = self.weight_table.get(emotion, 0.5)
        signal["resonance_weight"] = weight
        return signal
