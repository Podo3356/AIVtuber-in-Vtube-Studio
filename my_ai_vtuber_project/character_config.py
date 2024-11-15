from transformers import pipeline

class CharacterConfig:
    def __init__(self, character_prompt):
        self.character_prompt = character_prompt
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        self.emotion_analyzer = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def generate_character_settings(self):
        settings = {}

        sentiment = self.sentiment_analyzer(self.character_prompt)[0]
        if sentiment['label'] == 'POSITIVE':
            settings['tone'] = 'friendly'
        elif sentiment['label'] == 'NEGATIVE':
            settings['tone'] = 'serious'
        else:
            settings['tone'] = 'neutral'

        emotions = ["friendly", "aggressive", "calm", "enthusiastic"]
        emotion_result = self.emotion_analyzer(self.character_prompt, candidate_labels=emotions)
        dominant_emotion = emotion_result["labels"][0]

        settings['emotion'] = dominant_emotion
        return settings
