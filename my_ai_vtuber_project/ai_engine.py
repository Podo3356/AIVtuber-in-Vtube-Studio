from rnn_model import RNNLanguageModel

class AIVTuberEngine:
    def __init__(self):
        self.language_model = RNNLanguageModel()
        self.previous_responses = []

    def learn_from_user(self, user_text):
        self.previous_responses.append(user_text)
        if len(self.previous_responses) >= 10:
            self.language_model.train(self.previous_responses)
            self.previous_responses = []

    def generate_response(self, user_input=None):
        if user_input:
            self.learn_from_user(user_input)
            response = self.language_model.generate_text(user_input)
        else:
            seed_text = self.previous_responses[-1] if self.previous_responses else "안녕하세요!"
            response = self.language_model.generate_text(seed_text)

        self.previous_responses.append(response)
        return response
