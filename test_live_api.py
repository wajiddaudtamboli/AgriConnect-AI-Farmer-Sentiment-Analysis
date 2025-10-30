import requests
import json

print("🧪 Testing AgriConnect AI Sentiment Analysis API...")
print("=" * 60)

# Test 1: Health Check
try:
    health_response = requests.get("http://127.0.0.1:5000/api/health", timeout=5)
    if health_response.status_code == 200:
        print("✅ Health Check: PASSED")
        print(f"   Response: {health_response.json()}")
    else:
        print(f"❌ Health Check: FAILED (Status: {health_response.status_code})")
except Exception as e:
    print(f"❌ Health Check: ERROR - {e}")

print("-" * 60)

# Test 2: Sentiment Analysis
test_texts = [
    "The crop yield was excellent this year! Very happy with the results.",
    "The weather destroyed my entire harvest. Very disappointed.",
    "The farming season was okay, nothing special to report."
]

for i, text in enumerate(test_texts, 1):
    print(f"Test {i}: '{text[:50]}...'")
    try:
        response = requests.post(
            "http://127.0.0.1:5000/analyze-sentiment",
            json={"text": text},
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"   ✅ Sentiment: {result['sentiment'].upper()}")
            print(f"   📊 Confidence: {result['confidence']:.2f}")
            print(f"   🔑 Keywords: {', '.join(result['keywords'][:3])}")
            print(f"   📈 Compound Score: {result['scores']['compound']:.3f}")
        else:
            print(f"   ❌ FAILED (Status: {response.status_code})")
            
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
    
    print("-" * 40)

print("🎯 API Testing Complete!")