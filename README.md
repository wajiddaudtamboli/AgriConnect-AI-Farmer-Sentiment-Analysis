# 🌾 AgriConnect AI - Farmer Sentiment Analysis

![AgriConnect AI](https://img.shields.io/badge/AgriConnect-AI-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-black)
![License](https://img.shields.io/badge/License-MIT-yellow)

> **Empowering agriculture with AI-driven insights to understand farmer feedback and sentiments**

An advanced sentiment analysis web application specifically designed for analyzing farmer feedback using Natural Language Processing (NLP) and AI-powered sentiment detection. Part of the **AgriConnect AI** ecosystem.

---

## ✨ Features

- 🤖 **AI-Powered Analysis** - Uses VADER sentiment analyzer for accurate sentiment detection
- 📊 **Comprehensive Metrics** - Provides positive, negative, neutral, and compound sentiment scores
- 🔑 **Keyword Extraction** - Automatically identifies key topics from feedback
- 🎨 **Modern UI** - Beautiful, responsive interface with purple/blue gradient theme
- ⚡ **Real-time Processing** - Instant sentiment analysis with animated results
- 📱 **Mobile Responsive** - Optimized for mobile, tablet, and desktop with Tailwind CSS
- 📱 **Cross-Device Support** - Perfect experience on phones, tablets, and computers
- 🔒 **Rate Limiting** - Built-in protection against abuse
- 📖 **API Documentation** - Complete REST API with detailed endpoints
- 🚀 **Production Ready** - Optimized for deployment on Deta Space, Railway, and Vercel
- ☁️ **Multiple Hosting Options** - Deploy on free platforms (Deta Space) or premium (Railway/Vercel)

---

## 📸 Screenshots

### Main Interface
Beautiful, intuitive interface with agriculture + AI fusion theme.

### Analysis Results
Real-time sentiment analysis with detailed scores and keyword extraction.

---

## 🏗️ Project Structure

```
AgriConnect-AI-Farmer-Sentiment-Analysis/
├── app.py                      # Main Flask application (port 8000 for Deta Space)
├── requirements.txt            # Python dependencies (optimized)
├── Spacefile                   # Deta Space deployment configuration  
├── Procfile                    # Railway deployment configuration
├── railway.json                # Railway build settings
├── nixpacks.toml              # Railway build configuration
├── runtime.txt                # Python version specification
├── vercel.json                # Vercel deployment configuration
├── .gitignore                 # Git ignore rules
├── README.md                  # Project documentation
├── DETA_DEPLOYMENT.md         # Detailed Deta Space deployment guide
├── RAILWAY_DEPLOYMENT.md      # Railway deployment guide
├── start_server.bat           # Windows server launcher
│
├── templates/
│   └── index.html            # Mobile-responsive web interface (Tailwind CSS)
│
├── static/                    # Static assets (if needed)
│
├── data/
│   ├── feedback.csv          # Training dataset
│   └── new_feedback.csv      # Additional feedback data
│
├── models/                    # Trained ML models (optional)
│
├── test_api.py               # API testing script
├── train_model.py            # Model training script
└── train.ipynb               # Jupyter notebook for training
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/wajiddaudtamboli/AgriConnect-AI-Farmer-Sentiment-Analysis.git
   cd AgriConnect-AI-Farmer-Sentiment-Analysis
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/Mac
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data** (automatic on first run)
   ```python
   python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('punkt'); nltk.download('stopwords')"
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser and navigate to: `http://127.0.0.1:5000`
   - API Documentation: `http://127.0.0.1:5000/api/info`

---

## 🌐 Deployment on Vercel

### Step 1: Prepare Your Repository

1. **Initialize Git** (if not already done)
   ```bash
   git init
   git add .
   git commit -m "Initial commit: AgriConnect AI Sentiment Analysis"
   ```

2. **Push to GitHub**
   ```bash
   git remote add origin https://github.com/wajiddaudtamboli/AgriConnect-AI-Farmer-Sentiment-Analysis.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy to Vercel

1. **Install Vercel CLI** (optional)
   ```bash
   npm install -g vercel
   ```

2. **Deploy via Vercel Dashboard**
   - Go to [vercel.com](https://vercel.com)
   - Click "Import Project"
   - Select your GitHub repository
   - Vercel will auto-detect the configuration from `vercel.json`
   - Click "Deploy"

3. **Or Deploy via CLI**
   ```bash
   vercel
   ```

### Step 3: Configure Environment Variables (Optional)

In Vercel Dashboard → Settings → Environment Variables:
- `FLASK_DEBUG=False`
- `FLASK_HOST=0.0.0.0`
- `FLASK_PORT=8000`

---

## ☁️ Deploy on Deta Space (FREE & Always-On)

[![Deploy to Deta Space](https://deta.space/buttons/deploy.svg)](https://deta.space)

### Why Deta Space?
- ✅ **100% FREE** hosting with no usage limits
- ✅ **Always-on** - no cold starts or sleep mode  
- ✅ **Instant HTTPS** with global CDN
- ✅ **Zero configuration** deployment

### Quick Deployment Steps:

1. **Install Deta CLI**
   ```bash
   curl -fsSL https://get.deta.dev/space-cli.sh | sh
   ```

2. **Login to Deta Space**
   ```bash
   space login
   ```

3. **Navigate to project & deploy**
   ```bash
   cd AgriConnect-AI-Farmer-Sentiment-Analysis
   space new
   space push
   ```

4. **Access your live app**
   - Your app will be available at: `https://agriconnect-ai-xyz.deta.app`
   - Fully functional with HTTPS, global CDN, and unlimited usage!

### 📖 Detailed Deployment Guide
For complete step-by-step instructions, see: **[DETA_DEPLOYMENT.md](./DETA_DEPLOYMENT.md)**

**Key Benefits:**
- 🌐 **Free HTTPS domain** automatically provisioned
- 📱 **Mobile responsive** design works perfectly
- 🚀 **Instant global deployment** with edge caching
- 💾 **No server management** required
- 📊 **Built-in monitoring** and logs

---

## 📡 API Documentation

### Endpoints

#### 1. Home Page
```http
GET /
```
Returns the main web interface.

#### 2. Analyze Sentiment
```http
POST /analyze-sentiment
Content-Type: application/json

{
  "text": "The new irrigation system is working wonderfully!"
}
```

**Response:**
```json
{
  "sentiment": "positive",
  "confidence": 0.27,
  "keywords": ["irrigation", "system", "working", "wonderfully"],
  "scores": {
    "positive": 0.27,
    "negative": 0.0,
    "neutral": 0.73,
    "compound": 0.7424
  }
}
```

#### 3. Health Check
```http
GET /api/health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "AgriConnect AI - Farmer Sentiment Analysis",
  "version": "2.0.0"
}
```

#### 4. API Information
```http
GET /api/info
```
Returns complete API documentation.

### Rate Limits

- **30 requests per minute** per IP address for `/analyze-sentiment`
- No limits on other endpoints

### Error Responses

```json
{
  "error": "Error type",
  "message": "Detailed error message"
}
```

**Status Codes:**
- `200` - Success
- `400` - Bad Request (invalid input)
- `429` - Rate Limit Exceeded
- `500` - Internal Server Error

---

## 🧪 Testing

### Run API Tests
```bash
python test_api.py
```

### Manual Testing with cURL

**Positive Sentiment:**
```bash
curl -X POST http://localhost:5000/analyze-sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "The harvest was excellent this year!"}'
```

**Negative Sentiment:**
```bash
curl -X POST http://localhost:5000/analyze-sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "The pest problem is terrible this season."}'
```

---

## 🛠️ Technology Stack

| Category | Technology |
|----------|-----------|
| **Backend** | Python 3.9+, Flask 3.0.0 |
| **Frontend** | HTML5, Tailwind CSS, Vanilla JavaScript |
| **NLP** | NLTK, VADER Sentiment Analyzer |
| **ML** | Scikit-learn (for future enhancements) |
| **Deployment** | Vercel, Docker (optional) |
| **Version Control** | Git, GitHub |

---

## 📊 How It Works

1. **User Input** - Farmer enters feedback through the web interface
2. **Preprocessing** - Text is tokenized and cleaned (stopwords removal)
3. **Sentiment Analysis** - VADER analyzer calculates sentiment scores
4. **Keyword Extraction** - Frequency distribution identifies key topics
5. **Results Display** - Beautiful visualization with sentiment classification

### Sentiment Classification Logic

- **Positive**: Compound score ≥ 0.05
- **Negative**: Compound score ≤ -0.05
- **Neutral**: -0.05 < Compound score < 0.05

---

## 🎨 UI Features

- ✨ Animated background particles
- 🎭 Color-coded sentiment cards (Green/Red/Gray)
- 📊 Interactive progress bars
- 🏷️ Keyword tags with gradients
- 📱 Fully responsive design
- ⌨️ Keyboard shortcuts (Ctrl+Enter to analyze)
- 🔄 Smooth animations and transitions

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Add comments for complex logic
- Update documentation for new features
- Test thoroughly before submitting PR

---

## 📝 Future Enhancements

- [ ] Multi-language support
- [ ] Custom ML model training interface
- [ ] Historical data analytics dashboard
- [ ] Export results as PDF/CSV
- [ ] Batch processing for multiple feedbacks
- [ ] Integration with farmer management systems
- [ ] Real-time feedback monitoring
- [ ] Email notifications for negative sentiments

---

## 🐛 Troubleshooting

### Common Issues

**Issue: NLTK data not found**
```bash
python -c "import nltk; nltk.download('all')"
```

**Issue: Port already in use**
```bash
# Change port in environment variable
export FLASK_PORT=8080
python app.py
```

**Issue: Module not found**
```bash
pip install -r requirements.txt --force-reinstall
```

---

## � Deploy on Railway

Deploy this Flask app instantly on [Railway.app](https://railway.app):

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/wajiddaudtamboli/AgriConnect-AI-Farmer-Sentiment-Analysis)

### Quick Deploy Steps

1. **Push to GitHub** (if not already done)
   ```bash
   git add .
   git commit -m "Prepare project for Railway deployment"
   git push origin main
   ```

2. **Deploy to Railway**
   - Go to [Railway.app](https://railway.app)
   - Click "New Project" → "Deploy from GitHub Repository"
   - Select: `wajiddaudtamboli/AgriConnect-AI-Farmer-Sentiment-Analysis`
   - Railway auto-detects Flask and deploys automatically

3. **Get Your Live URL**
   - Railway assigns a URL (e.g., `https://agriconnect-ai-production.up.railway.app`)
   - Visit the URL to see your live app!

### Environment Variables (Auto-configured)

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | Auto-assigned by Railway |
| `NLTK_DATA` | Path to NLTK resources | `/tmp/nltk_data` |
| `FLASK_ENV` | Run mode | `production` |

### Deployment Files

- ✅ `Procfile` - Gunicorn server configuration
- ✅ `railway.json` - Railway-specific settings
- ✅ `nixpacks.toml` - Build configuration  
- ✅ `runtime.txt` - Python 3.9 specification
- ✅ `requirements.txt` - Includes gunicorn for production

**📖 For detailed deployment guide, see:** [RAILWAY_DEPLOYMENT.md](./RAILWAY_DEPLOYMENT.md)

---

## 🌐 Alternative: Deploy on Vercel

For serverless deployment, see [VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md)

---

## �👥 Team

**Developed by Team AgriConnect AI**

---

<div align="center">

**Made with ❤️ by Team AgriConnect AI**
© 2025 AgriConnect AI. All rights reserved.

</div>
