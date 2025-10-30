import requests
import json

print("🧪 Testing AgriConnect AI on Port 8000 (Deta Space Compatible)")
print("=" * 65)

# Test API endpoint
url = "http://127.0.0.1:8000/analyze-sentiment"
test_feedback = "The new irrigation system increased our crop yield by 40%! Very satisfied with the results."

data = {"text": test_feedback}

try:
    response = requests.post(url, json=data, timeout=10)
    
    if response.status_code == 200:
        result = response.json()
        print("✅ API Test: SUCCESS")
        print(f"📝 Input: {test_feedback[:50]}...")
        print(f"😊 Sentiment: {result['sentiment'].upper()}")
        print(f"📊 Confidence: {result['confidence']:.2f}")
        print(f"🔑 Keywords: {', '.join(result['keywords'][:3])}")
        print(f"📈 Compound Score: {result['scores']['compound']:.3f}")
        print("\n✅ Ready for Deta Space deployment!")
    else:
        print(f"❌ API Test Failed: Status {response.status_code}")
        
except Exception as e:
    print(f"❌ Connection Error: {e}")

print("=" * 65)