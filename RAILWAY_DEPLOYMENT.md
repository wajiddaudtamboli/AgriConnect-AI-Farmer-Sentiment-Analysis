# 🚂 Railway Deployment Guide

## 🚀 Deploy AgriConnect AI to Railway.app

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template)

---

## 📋 Prerequisites

- ✅ GitHub account
- ✅ Railway.app account (sign up with GitHub)
- ✅ Project pushed to GitHub repository

---

## 🎯 Quick Deploy Steps

### 1. **Prepare Your Repository**

Your project is already configured with:
- ✅ `Procfile` - Gunicorn server configuration
- ✅ `railway.json` - Railway-specific settings
- ✅ `nixpacks.toml` - Build configuration
- ✅ `runtime.txt` - Python version specification
- ✅ `requirements.txt` - All dependencies including gunicorn

### 2. **Push to GitHub**

```bash
# Add all deployment files
git add .

# Commit with descriptive message
git commit -m "Prepare project for Railway deployment"

# Push to GitHub
git push origin main
```

### 3. **Deploy on Railway**

#### Option A: Via Railway Dashboard (Recommended)

1. **Visit Railway**
   - Go to [https://railway.app](https://railway.app)
   - Click "Login" and sign in with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose: `wajiddaudtamboli/AgriConnect-AI-Farmer-Sentiment-Analysis`

3. **Configure Deployment**
   - Railway auto-detects Flask from `app.py`
   - Build command: Reads from `nixpacks.toml`
   - Start command: `gunicorn app:app --bind 0.0.0.0:$PORT`

4. **Wait for Build**
   - Railway will:
     - Install Python 3.9
     - Install dependencies from `requirements.txt`
     - Download NLTK data
     - Start Gunicorn server
   - Build time: ~2-3 minutes

5. **Get Your Live URL**
   - Railway assigns URL like: `https://agriconnect-ai-production.up.railway.app`
   - Click "View Deployment" to open your app

#### Option B: Deploy with Button

Click this button to deploy instantly:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/wajiddaudtamboli/AgriConnect-AI-Farmer-Sentiment-Analysis)

---

## ⚙️ Environment Variables

Railway automatically provides `PORT`. Optional variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | Auto-assigned | Server port (Railway managed) |
| `HOST` | `0.0.0.0` | Server host binding |
| `NLTK_DATA` | `/tmp/nltk_data` | NLTK data directory |
| `FLASK_ENV` | `production` | Flask environment |

### Setting Environment Variables:

1. Go to your Railway project
2. Click "Variables" tab
3. Add custom variables if needed
4. Railway will auto-restart with new config

---

## 📦 Deployment Files Explained

### `Procfile`
```
web: gunicorn app:app --bind 0.0.0.0:$PORT
```
- Tells Railway to run Gunicorn web server
- `$PORT` is dynamically assigned by Railway

### `railway.json`
```json
{
  "build": {
    "builder": "NIXPACKS",
    "buildCommand": "pip install -r requirements.txt && python -m nltk.downloader vader_lexicon punkt stopwords wordnet"
  },
  "deploy": {
    "startCommand": "gunicorn app:app --bind 0.0.0.0:$PORT --workers 4 --timeout 120"
  }
}
```
- Configures Railway build and deployment
- Downloads NLTK data during build
- Uses 4 Gunicorn workers for performance

### `nixpacks.toml`
```toml
[phases.setup]
nixPkgs = ["python39", "gcc"]

[phases.install]
cmds = [
  "pip install -r requirements.txt",
  "python -m nltk.downloader -d /tmp/nltk_data vader_lexicon punkt stopwords wordnet"
]

[start]
cmd = "gunicorn app:app --bind 0.0.0.0:$PORT --workers 4 --timeout 120"
```
- Nixpacks build configuration
- Specifies Python 3.9 and GCC
- Downloads NLTK data to `/tmp/nltk_data`

### `runtime.txt`
```
python-3.9.18
```
- Specifies exact Python version

### `requirements.txt`
```
Flask==3.0.0
flask-cors==4.0.0
gunicorn==21.2.0
nltk==3.8.1
scikit-learn==1.6.1
# ... other dependencies
```
- **NEW:** Added `gunicorn==21.2.0` for production server

---

## 🧪 Testing Your Deployment

### 1. **Health Check**
```bash
curl https://your-app.up.railway.app/api/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "AgriConnect AI - Farmer Sentiment Analysis",
  "version": "2.0.0"
}
```

### 2. **Web Interface**
Visit: `https://your-app.up.railway.app/`
- Should load beautiful UI with Tailwind CSS
- Test sentiment analysis with sample text

### 3. **API Endpoint**
```bash
curl -X POST https://your-app.up.railway.app/analyze-sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "The farming season was very productive and successful!"}'
```

Expected response:
```json
{
  "sentiment": "positive",
  "confidence": 0.XX,
  "keywords": ["farming", "season", "productive", "successful"],
  "scores": {
    "positive": 0.XX,
    "negative": 0.XX,
    "neutral": 0.XX,
    "compound": 0.XXXX
  }
}
```

---

## 📊 Railway Free Tier

Railway offers generous free tier:

| Resource | Free Tier Limit |
|----------|----------------|
| **Execution Time** | $5 credit/month |
| **Memory** | 8GB RAM |
| **Deployments** | Unlimited |
| **Custom Domain** | ✅ Supported |
| **HTTPS** | ✅ Automatic |
| **Build Minutes** | Unlimited |

**Estimated Usage:**
- Light traffic: ~$2-3/month (within free tier)
- Medium traffic: ~$5-10/month

---

## 🔧 Troubleshooting

### Issue: Build Fails

**Check build logs:**
1. Go to Railway dashboard
2. Click "Deployments"
3. View logs for errors

**Common fixes:**
```bash
# Update requirements.txt versions
pip freeze > requirements.txt

# Ensure gunicorn is listed
grep gunicorn requirements.txt
```

### Issue: NLTK Data Not Found

**Solution:**
Check `nixpacks.toml` has NLTK download:
```toml
[phases.install]
cmds = [
  "python -m nltk.downloader -d /tmp/nltk_data vader_lexicon punkt stopwords wordnet"
]
```

### Issue: App Crashes on Start

**Check logs:**
```bash
# In Railway dashboard, view "Deployment logs"
```

**Common causes:**
- Missing environment variables
- Port binding issues (ensure using `$PORT`)
- NLTK data path incorrect

**Fix:**
```python
# In app.py, ensure:
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

### Issue: Slow Performance

**Solution:**
Increase Gunicorn workers in `Procfile`:
```
web: gunicorn app:app --bind 0.0.0.0:$PORT --workers 6 --timeout 180
```

---

## 🔄 Continuous Deployment

Railway automatically deploys on every push to `main`:

1. **Make changes** to your code
2. **Commit and push:**
   ```bash
   git add .
   git commit -m "Update feature"
   git push origin main
   ```
3. **Railway auto-builds** and deploys
4. **Check deployment status** in Railway dashboard

---

## 📈 Monitoring & Logs

### View Logs:
1. Go to Railway dashboard
2. Click your project
3. Select "Deployments" → Latest deployment
4. View real-time logs

### Metrics:
- CPU usage
- Memory usage
- Request count
- Response times

---

## 🌐 Custom Domain (Optional)

### Add Custom Domain:

1. **Purchase domain** (Namecheap, GoDaddy, etc.)

2. **In Railway:**
   - Go to "Settings" → "Domains"
   - Click "Add Domain"
   - Enter your domain: `agriconnect-ai.com`

3. **Update DNS:**
   - Add CNAME record:
     ```
     Type: CNAME
     Name: www
     Value: your-project.up.railway.app
     ```

4. **Wait for DNS** propagation (5-30 minutes)

5. **HTTPS** automatically enabled by Railway

---

## 💰 Cost Optimization

### Tips to Stay in Free Tier:

1. **Optimize Images:** Use CDN for static assets
2. **Cache Responses:** Implement caching for repeated queries
3. **Limit Workers:** Start with 2-4 Gunicorn workers
4. **Monitor Usage:** Check Railway dashboard weekly

### When to Upgrade:

- Traffic > 10,000 requests/month
- Need more than 8GB RAM
- Require priority support

---

## 🎯 Post-Deployment Checklist

- [ ] Deployment successful on Railway
- [ ] Health check endpoint responding
- [ ] Web interface loads correctly
- [ ] Sentiment analysis works
- [ ] All API endpoints functional
- [ ] HTTPS enabled (automatic)
- [ ] Custom domain configured (optional)
- [ ] Monitoring set up
- [ ] Updated README with live URL

---

## 📝 Update README with Live URL

Add this section to your `README.md`:

```markdown
## 🌐 Live Demo

**🚀 Deployed on Railway.app**

**Live URL:** [https://your-app.up.railway.app](https://your-app.up.railway.app)

### API Endpoints:
- **Web Interface:** https://your-app.up.railway.app/
- **Analyze Sentiment:** https://your-app.up.railway.app/analyze-sentiment (POST)
- **Health Check:** https://your-app.up.railway.app/api/health (GET)
- **API Info:** https://your-app.up.railway.app/api-info (GET)

---

### Quick Test:

```bash
curl -X POST https://your-app.up.railway.app/analyze-sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "The irrigation system is working perfectly!"}'
```
```

---

## 📚 Additional Resources

- [Railway Documentation](https://docs.railway.app/)
- [Gunicorn Configuration](https://docs.gunicorn.org/en/stable/settings.html)
- [Flask Deployment Best Practices](https://flask.palletsprojects.com/en/3.0.x/deploying/)
- [Nixpacks Documentation](https://nixpacks.com/docs)

---

## 🤝 Support

### Railway Issues:
- [Railway Discord](https://discord.gg/railway)
- [Railway Status](https://status.railway.app/)

### Project Issues:
- [GitHub Issues](https://github.com/wajiddaudtamboli/AgriConnect-AI-Farmer-Sentiment-Analysis/issues)

---

<div align="center">

## 🎉 Your App is Live on Railway!

**🌾 AgriConnect AI - Farmer Sentiment Analysis**

**Deployed with:**
- ✅ Automatic HTTPS
- ✅ Continuous deployment from GitHub
- ✅ Global CDN
- ✅ 99.9% uptime SLA

**© 2025 Developed by Team AgriConnect AI**

</div>
