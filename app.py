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

# Set NLTK data path for cloud deployment (Railway, Deta Space, etc.)
nltk_data_path = os.environ.get('NLTK_DATA', '/tmp/nltk_data')
if nltk_data_path not in nltk.data.path:
    nltk.data.path.append(nltk_data_path)

# Download NLTK data quietly with error handling
def download_nltk_data():
    required_datasets = [
        ('vader_lexicon', 'vader_lexicon'),
        ('tokenizers/punkt', 'punkt'),
        ('corpora/stopwords', 'stopwords')
    ]
    
    for data_name, download_name in required_datasets:
        try:
            nltk.data.find(data_name)
            logger.info(f"✅ NLTK {download_name} already available")
        except LookupError:
            logger.info(f"📥 Downloading NLTK {download_name}...")
            nltk.download(download_name, quiet=True)
            logger.info(f"✅ NLTK {download_name} downloaded successfully")

# Initialize NLTK data
download_nltk_data()

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
    # Get port from environment variable or default to 8000 for Deta Space compatibility
    port = int(os.environ.get('PORT', 8000))
    host = os.environ.get('HOST', '0.0.0.0')
    
    print("\n" + "="*70)
    print("🌾 AgriConnect AI - Farmer Sentiment Analysis")
    print("="*70)
    print(f"📍 Server running at: http://{host}:{port}")
    print(f"🌐 Web Interface: http://{host}:{port}/")
    print(f"📊 API Endpoint: http://{host}:{port}/analyze-sentiment")
    print(f"📖 API Documentation: http://{host}:{port}/api-info")
    print(f"🏥 Health Check: http://{host}:{port}/api/health")
    print("="*70)
    print("✨ Developed with ❤️ by Team AgriConnect AI")
    print("="*70 + "\n")
    app.run(debug=False, use_reloader=False, host=host, port=port, threaded=True)