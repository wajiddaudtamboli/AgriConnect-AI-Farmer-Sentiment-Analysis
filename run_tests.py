"""
Test script that starts the Flask server and runs API tests
"""
import subprocess
import time
import requests
import json
import sys
import os

def start_server():
    """Start Flask server as a subprocess"""
    python_path = os.path.join('.venv-1', 'Scripts', 'python.exe')
    process = subprocess.Popen(
        [python_path, 'app.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print("⏳ Starting Flask server...")
    time.sleep(5)  # Wait for server to start
    return process

def test_endpoints(base_url="http://127.0.0.1:5000"):
    """Test all API endpoints"""
    print("\n" + "="*70)
    print("🧪 Testing AgriConnect AI - Farmer Sentiment Analysis API")
    print("="*70 + "\n")
    
    # Test 1: Health check
    print("Test 1: Health Check (GET /api/health)...")
    try:
        response = requests.get(f"{base_url}/api/health", timeout=5)
        if response.status_code == 200:
            print("✅ Health check passed!")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    print("\n" + "-"*70 + "\n")
    
    # Test 2: API Info
    print("Test 2: API Documentation (GET /api-info)...")
    try:
        response = requests.get(f"{base_url}/api-info", timeout=5)
        if response.status_code == 200:
            print("✅ API info retrieved!")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"❌ Failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    print("\n" + "-"*70 + "\n")
    
    # Test 3: Positive sentiment
    print("Test 3: Analyzing POSITIVE feedback...")
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
            print(f"🔑 Keywords: {', '.join(result['keywords'][:5])}")
            print(f"📈 Positive Score: {result['scores']['positive']:.3f}")
        else:
            print(f"❌ Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    print("\n" + "-"*70 + "\n")
    
    # Test 4: Negative sentiment
    print("Test 4: Analyzing NEGATIVE feedback...")
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
            print(f"🔑 Keywords: {', '.join(result['keywords'][:5])}")
            print(f"📈 Negative Score: {result['scores']['negative']:.3f}")
        else:
            print(f"❌ Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    print("\n" + "="*70)
    print("✅ All tests completed!")
    print("="*70 + "\n")

if __name__ == "__main__":
    server_process = None
    try:
        server_process = start_server()
        test_endpoints()
        
        print("\n🌐 Server is still running at http://127.0.0.1:5000")
        print("📱 Open the web interface to test the UI!")
        print("Press Ctrl+C to stop the server...\n")
        
        # Keep the script running
        server_process.wait()
        
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down server...")
    finally:
        if server_process:
            server_process.terminate()
            server_process.wait()
        print("✅ Server stopped\n")
