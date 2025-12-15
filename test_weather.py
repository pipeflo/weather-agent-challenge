#!/usr/bin/env python3
"""
Test script for the weather agent
"""

import os
import json
from lambda_function import lambda_handler, get_weather

def test_get_weather_function():
    """Test the get_weather function directly"""
    print("Testing get_weather function...")
    
    # You need to set your API key here for testing
    api_key = input("Enter your OpenWeather API key for testing: ")
    os.environ['OPENWEATHER_API_KEY'] = api_key
    
    test_cities = ['London', 'New York', 'Tokyo', 'InvalidCity123']
    
    for city in test_cities:
        print(f"\n--- Testing city: {city} ---")
        result = get_weather(city)
        if result:
            print(f"✅ Success: {json.dumps(result, indent=2)}")
        else:
            print(f"❌ Failed to get weather for {city}")

def test_lambda_handler():
    """Test the complete Lambda handler"""
    print("\n" + "="*50)
    print("Testing Lambda handler...")
    
    # Mock Bedrock Agent event
    test_event = {
        'agent': {'agentId': 'test-agent'},
        'actionGroup': 'weather-actions',
        'function': 'get_weather',
        'parameters': [
            {
                'name': 'city',
                'value': 'London'
            }
        ]
    }
    
    print(f"Test event: {json.dumps(test_event, indent=2)}")
    
    result = lambda_handler(test_event, {})
    print(f"Lambda response: {json.dumps(result, indent=2)}")

if __name__ == "__main__":
    print("🧪 Weather Agent Test Suite")
    print("="*50)
    
    try:
        test_get_weather_function()
        test_lambda_handler()
        print("\n🎉 All tests completed!")
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
