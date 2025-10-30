from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Download NLTK data quietly
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon', quiet=True)

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

app = Flask(__name__)
CORS(app)

sia = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))

def extract_keywords(text, top_n=5):
    # Tokenize and clean the text
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalpha()]  # remove punctuation
    tokens = [word for word in tokens if word not in stop_words]  # remove stopwords
    
    # Get most frequent words
    freq_dist = FreqDist(tokens)
    keywords = [word for word, freq in freq_dist.most_common(top_n)]
    
    return keywords

@app.route('/analyze-sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Perform sentiment analysis
    sentiment_scores = sia.polarity_scores(text)
    
    # Determine sentiment label
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'positive'
        confidence = sentiment_scores['pos']
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'negative'
        confidence = sentiment_scores['neg']
    else:
        sentiment = 'neutral'
        confidence = sentiment_scores['neu']
    
    # Extract keywords
    keywords = extract_keywords(text)
    
    response = {
        'sentiment': sentiment,
        'confidence': confidence,
        'keywords': keywords,
        'scores': {
            'positive': sentiment_scores['pos'],
            'negative': sentiment_scores['neg'],
            'neutral': sentiment_scores['neu'],
            'compound': sentiment_scores['compound']
        }
    }
    
    return jsonify(response)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api-info', methods=['GET'])
def api_info():
    return jsonify({
        'name': 'AgriConnect AI - Farmer Sentiment Analysis',
        'version': '2.0.0',
        'message': 'AI-powered sentiment analysis for farmer feedback',
        'endpoints': {
            '/analyze-sentiment': {
                'method': 'POST',
                'description': 'Analyze sentiment of farmer feedback',
                'example': {
                    'text': 'The crop yield was excellent this year!'
                }
            }
        },
        'developed_by': 'Team AgriConnect AI'
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'AgriConnect AI - Farmer Sentiment Analysis',
        'version': '2.0.0'
    }), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Not Found',
        'message': 'The requested resource was not found',
        'status': 404
    }), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        'error': 'Internal Server Error',
        'message': 'An unexpected error occurred',
        'status': 500
    }), 500

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🌾 AgriConnect AI - Farmer Sentiment Analysis")
    print("="*70)
    print("📍 Server running at: http://127.0.0.1:5000")
    print("🌐 Web Interface: http://127.0.0.1:5000/")
    print("📊 API Endpoint: http://127.0.0.1:5000/analyze-sentiment")
    print("📖 API Documentation: http://127.0.0.1:5000/api-info")
    print("🏥 Health Check: http://127.0.0.1:5000/api/health")
    print("="*70)
    print("✨ Developed by Team AgriConnect AI")
    print("="*70 + "\n")
    app.run(debug=False, use_reloader=False, host='127.0.0.1', port=5000, threaded=True)