import requests
import json
import time

# API endpoint
base_url = "http://127.0.0.1:5000"

print("\n" + "="*70)
print("🧪 Testing Farmer Sentiment Analysis API")
print("="*70 + "\n")

# Test 1: Check if server is running
print("Test 1: Checking API Documentation (GET /)...")
try:
    response = requests.get(base_url, timeout=5)
    if response.status_code == 200:
        print("✅ Server is running!")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"⚠️  Unexpected status: {response.status_code}")
except Exception as e:
    print(f"❌ Server is not responding: {str(e)}")
    print("Please make sure app.py is running!")
    exit(1)

print("\n" + "-"*70 + "\n")

# Test 2: Positive sentiment
print("Test 2: Analyzing POSITIVE feedback...")
test_positive = {
    "text": "The new irrigation system is working wonderfully! Our crops are healthier than ever and the yield has increased significantly."
}

try:
    response = requests.post(f"{base_url}/analyze-sentiment", json=test_positive, timeout=5)
    if response.status_code == 200:
        result = response.json()
        print("✅ Analysis complete!")
        print(f"📊 Sentiment: {result['sentiment'].upper()}")
        print(f"🎯 Confidence: {result['confidence']:.2%}")
        print(f"🔑 Keywords: {', '.join(result['keywords'])}")
        print(f"📈 Scores: {json.dumps(result['scores'], indent=2)}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"❌ Error: {str(e)}")

print("\n" + "-"*70 + "\n")

# Test 3: Negative sentiment
print("Test 3: Analyzing NEGATIVE feedback...")
test_negative = {
    "text": "The pest problem is terrible this season. My crops are dying and I'm very disappointed with the results."
}

try:
    response = requests.post(f"{base_url}/analyze-sentiment", json=test_negative, timeout=5)
    if response.status_code == 200:
        result = response.json()
        print("✅ Analysis complete!")
        print(f"📊 Sentiment: {result['sentiment'].upper()}")
        print(f"🎯 Confidence: {result['confidence']:.2%}")
        print(f"🔑 Keywords: {', '.join(result['keywords'])}")
        print(f"📈 Scores: {json.dumps(result['scores'], indent=2)}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"❌ Error: {str(e)}")

print("\n" + "-"*70 + "\n")

# Test 4: Neutral sentiment
print("Test 4: Analyzing NEUTRAL feedback...")
test_neutral = {
    "text": "The weather this season has been average. Some crops did okay."
}

try:
    response = requests.post(f"{base_url}/analyze-sentiment", json=test_neutral, timeout=5)
    if response.status_code == 200:
        result = response.json()
        print("✅ Analysis complete!")
        print(f"📊 Sentiment: {result['sentiment'].upper()}")
        print(f"🎯 Confidence: {result['confidence']:.2%}")
        print(f"🔑 Keywords: {', '.join(result['keywords'])}")
        print(f"📈 Scores: {json.dumps(result['scores'], indent=2)}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"❌ Error: {str(e)}")

print("\n" + "="*70)
print("✅ All tests completed!")
print("="*70 + "\n")
