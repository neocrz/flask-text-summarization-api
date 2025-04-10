from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from string import punctuation
from heapq import nlargest
from collections import defaultdict
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

app = Flask(__name__)
api = Api(app)

# classe auxiliar
class TextSummarizer:
    def __init__(self):
        # stopwords
        self.stopwords = set(stopwords.words('portuguese') + list(punctuation))
    
    def summarize(self, text, num_sentences=4):
        # tokenizando texto em sentenças e palavras (lower)
        sentences = sent_tokenize(text)
        words = word_tokenize(text.lower())
        
        # removendo stopwords
        words = [word for word in words if word not in self.stopwords and word.isalnum()]
        
        # frequencia
        freq = FreqDist(words)
        
        # score da sentença com base na frequencia de palavras
        sentence_scores = defaultdict(int)
        for i, sentence in enumerate(sentences):
            for word in word_tokenize(sentence.lower()):
                if word in freq:
                    sentence_scores[i] += freq[word]
        
        # índice das melhores sentenças
        top_sentence_indices = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
        
        # melhores sentenças
        summary = [sentences[i] for i in sorted(top_sentence_indices)]

        # retornando sumarização
        return ' '.join(summary)

# classe da API
class SummarizeAPI(Resource):
    def __init__(self):
        self.summarizer = TextSummarizer()
    
    def post(self):
        data = request.get_json()
        
        if not data or 'text' not in data:
            return {'error': 'Nenhum texto em \'text\' foi provido'}, 400
        
        text = data['text']
        num_sentences = data.get('num_sentences', 4)
        
        try:
            summary = self.summarizer.summarize(text, num_sentences)
            return {'summary': summary}, 200
        except Exception as e:
            return {'error': str(e)}, 500

api.add_resource(SummarizeAPI, '/summarize')

if __name__ == '__main__':
    app.run(debug=True)
