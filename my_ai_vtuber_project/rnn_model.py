import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class RNNLanguageModel:
    def __init__(self, max_vocab_size=2000, max_sequence_length=50):
        self.max_vocab_size = max_vocab_size
        self.max_sequence_length = max_sequence_length
        self.tokenizer = Tokenizer(num_words=max_vocab_size)
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Embedding(input_dim=self.max_vocab_size, output_dim=64, input_length=self.max_sequence_length))
        model.add(SimpleRNN(128, return_sequences=True))
        model.add(SimpleRNN(64))
        model.add(Dense(self.max_vocab_size, activation='softmax'))
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self, texts, epochs=10, batch_size=32):
        sequences = self.tokenizer.texts_to_sequences(texts)
        sequences = pad_sequences(sequences, maxlen=self.max_sequence_length)
        
        X = sequences[:, :-1]
        y = sequences[:, -1]
        
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size)

    def generate_text(self, seed_text, num_words=50):
        generated_text = seed_text
        for _ in range(num_words):
            token_list = self.tokenizer.texts_to_sequences([generated_text])[0]
            token_list = pad_sequences([token_list], maxlen=self.max_sequence_length - 1, padding='pre')
            
            predicted = np.argmax(self.model.predict(token_list), axis=-1)
            output_word = self.tokenizer.index_word.get(predicted[0], '')
            
            if output_word == '':
                break
            
            generated_text += ' ' + output_word
        
        return generated_text
