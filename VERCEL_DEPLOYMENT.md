# 🚀 Vercel Deployment Guide

## Quick Deploy to Vercel

### Method 1: Deploy via Vercel Dashboard (Recommended)

1. **Visit Vercel Dashboard**
   - Go to [vercel.com](https://vercel.com)
   - Sign in with your GitHub account

2. **Import Repository**
   - Click "Add New Project"
   - Select "Import Git Repository"
   - Choose `AgriConnect-AI-Farmer-Sentiment-Analysis`

3. **Configure Project**
   ```
   Framework Preset: Other
   Root Directory: ./
   Build Command: (leave empty)
   Output Directory: (leave empty)
   Install Command: pip install -r requirements.txt
   ```

4. **Environment Variables**
   ```
   FLASK_HOST=0.0.0.0
   FLASK_PORT=8000
   PYTHONUNBUFFERED=1
   ```

5. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete
   - Your app will be live at `https://your-project.vercel.app`

---

### Method 2: Deploy via Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```

4. **Follow Prompts**
   - Set up and deploy: Yes
   - Which scope: Your account
   - Link to existing project: No
   - Project name: agriconnect-ai-farmer-sentiment
   - Directory: ./
   - Override settings: No

5. **Production Deployment**
   ```bash
   vercel --prod
   ```

---

### Method 3: GitHub Integration (Auto-Deploy)

1. **Connect Repository**
   - Go to Vercel Dashboard
   - Click "Import Project"
   - Select your GitHub repository

2. **Enable Auto-Deploy**
   - Vercel will automatically deploy on every push to `main` branch
   - Preview deployments for pull requests

3. **Configure Settings**
   - Set environment variables in Vercel Dashboard
   - Configure build settings if needed

---

## 📋 Pre-Deployment Checklist

- [x] `vercel.json` configuration file present
- [x] `requirements.txt` with all dependencies
- [x] Flask app properly configured
- [x] NLTK data downloads handled in code
- [x] Environment variables documented
- [x] CORS enabled for API calls
- [x] Error handling implemented
- [x] Health check endpoint available

---

## 🔧 Vercel Configuration (`vercel.json`)

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python",
      "config": {
        "maxLambdaSize": "50mb",
        "runtime": "python3.9"
      }
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
  "env": {
    "FLASK_HOST": "0.0.0.0",
    "FLASK_PORT": "8000"
  }
}
```

---

## 🌐 Environment Variables

Set these in Vercel Dashboard under Project Settings → Environment Variables:

| Variable | Value | Description |
|----------|-------|-------------|
| `FLASK_HOST` | `0.0.0.0` | Flask host binding |
| `FLASK_PORT` | `8000` | Flask port number |
| `PYTHONUNBUFFERED` | `1` | Python output buffering |

---

## 🧪 Testing Deployment

### 1. Check Health Endpoint
```bash
curl https://your-project.vercel.app/api/health
```

Expected Response:
```json
{
  "status": "healthy",
  "service": "AgriConnect AI - Farmer Sentiment Analysis",
  "version": "2.0.0"
}
```

### 2. Test Sentiment Analysis
```bash
curl -X POST https://your-project.vercel.app/analyze-sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "The farming season was very productive!"}'
```

### 3. Access Web Interface
Visit: `https://your-project.vercel.app/`

---

## 🐛 Troubleshooting

### Issue: Build Fails

**Solution:**
- Check `requirements.txt` has all dependencies
- Ensure Python version compatibility (3.9+)
- Verify `vercel.json` configuration

### Issue: NLTK Data Not Found

**Solution:**
- NLTK data is downloaded in `app.py` on startup
- Check logs for download errors
- Increase `maxLambdaSize` if needed

### Issue: Module Import Errors

**Solution:**
```bash
# Update requirements.txt with exact versions
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push
```

### Issue: Function Timeout

**Solution:**
- Optimize NLTK data loading
- Cache sentiment analyzer instance
- Reduce processing complexity

### Issue: CORS Errors

**Solution:**
- Verify Flask-CORS is installed
- Check CORS configuration in `app.py`
- Add allowed origins if needed

---

## 📊 Monitoring & Logs

### View Deployment Logs
1. Go to Vercel Dashboard
2. Select your project
3. Click on a deployment
4. View "Build Logs" and "Function Logs"

### Real-time Logs
```bash
vercel logs
```

### Monitor Function Performance
- Check execution time in Vercel Dashboard
- Monitor function invocations
- Track error rates

---

## 🔄 Update Deployment

### Automatic Updates (Recommended)
1. Make changes to your code
2. Commit and push to GitHub
```bash
git add .
git commit -m "Update feature"
git push
```
3. Vercel automatically redeploys

### Manual Updates
```bash
vercel --prod
```

---

## 🎯 Custom Domain Setup

1. **Purchase Domain** (optional)
   - Use Vercel Domains or external provider

2. **Add Domain in Vercel**
   - Go to Project Settings
   - Click "Domains"
   - Add your custom domain

3. **Configure DNS**
   - Add CNAME record pointing to Vercel
   - Wait for DNS propagation (up to 24 hours)

4. **Enable HTTPS**
   - Vercel automatically provisions SSL certificate
   - Your site will be available at `https://yourdomain.com`

---

## 📈 Performance Optimization

### 1. Enable Caching
```python
# Add to app.py
@app.after_request
def add_header(response):
    response.cache_control.max_age = 300  # 5 minutes
    return response
```

### 2. Optimize NLTK Loading
```python
# Cache sentiment analyzer
_sia = None

def get_sentiment_analyzer():
    global _sia
    if _sia is None:
        _sia = SentimentIntensityAnalyzer()
    return _sia
```

### 3. Use CDN for Static Assets
- Tailwind CSS is already loaded from CDN
- Consider using Vercel's Edge Network

---

## 🔐 Security Best Practices

1. **Environment Variables**
   - Never commit secrets to Git
   - Use Vercel Environment Variables

2. **API Rate Limiting**
   - Implement rate limiting for production
   - Use Vercel's rate limiting features

3. **Input Validation**
   - Validate all user inputs
   - Sanitize text before processing

4. **HTTPS Only**
   - Vercel automatically enforces HTTPS
   - Redirect HTTP to HTTPS

---

## 💰 Pricing Considerations

### Vercel Free Tier Includes:
- ✅ Unlimited deployments
- ✅ 100GB bandwidth/month
- ✅ 100 hours function execution/month
- ✅ Automatic HTTPS
- ✅ Global CDN

### When to Upgrade:
- High traffic (>100GB bandwidth)
- Long function execution times
- Need for team collaboration
- Custom domains and advanced features

---

## 📱 Mobile Access

Your deployed app will be automatically mobile-responsive:
- Share URL: `https://your-project.vercel.app`
- Create QR code for easy mobile access
- Test on multiple devices

---

## 🎉 Post-Deployment

### Share Your Project
- Add deployment URL to README.md
- Update GitHub repository description
- Share on social media

### Monitor Usage
- Check Vercel Analytics
- Monitor function invocations
- Track error rates

### Gather Feedback
- Test with real users
- Collect feedback
- Iterate and improve

---

## 📞 Support

### Vercel Documentation
- [Vercel Python Guide](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Vercel Configuration](https://vercel.com/docs/project-configuration)

### Project Support
- GitHub Issues: [Report Issues](https://github.com/wajiddaudtamboli/AgriConnect-AI-Farmer-Sentiment-Analysis/issues)
- Documentation: See README.md

---

<div align="center">

## 🌾 Ready to Deploy!

Your AgriConnect AI application is fully configured for Vercel deployment.

**Choose your deployment method above and go live in minutes!**

---

**© 2025 Developed by Team AgriConnect AI**

</div>
