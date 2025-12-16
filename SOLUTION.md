# Weather Agent Workshop - Solution Guide

This file contains the complete solution for instructors and reference.

## Complete Implementation

### Updated agent.py

```python
from bedrock_agentcore import BedrockAgentCoreApp
import requests
import os
import json
import re

# Initialize the AgentCore application
app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload):
    """
    Main entry point for the weather agent.
    
    This function is called by AgentCore Runtime for each request.
    """
    
    # Extract user message from payload
    user_message = payload.get("prompt", "")
    
    if not user_message:
        return {
            "result": "Hello! I'm a weather agent. Ask me about the weather in any city!"
        }
    
    # Parse the user's weather request
    city = extract_city_from_message(user_message)
    
    if not city:
        return {
            "result": "I'd be happy to help you with weather information! Please tell me which city you'd like to know about."
        }
    
    # Get weather data for the city
    weather_data = get_weather_data(city)
    
    if weather_data:
        # Format the weather response for the user
        response = format_weather_response(weather_data)
        return {"result": response}
    else:
        return {
            "result": f"I'm sorry, I couldn't get weather information for {city}. Please check the city name and try again."
        }

def extract_city_from_message(message):
    """
    Extract city name from user message using simple pattern matching.
    """
    # Convert to lowercase for easier matching
    message_lower = message.lower()
    
    # Common patterns for weather requests
    patterns = [
        r'weather in ([a-zA-Z\s]+)',
        r'weather for ([a-zA-Z\s]+)',
        r'weather at ([a-zA-Z\s]+)',
        r'how.*weather.*in ([a-zA-Z\s]+)',
        r'what.*weather.*in ([a-zA-Z\s]+)',
        r'tell me.*weather.*in ([a-zA-Z\s]+)',
        r'weather.*([a-zA-Z\s]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, message_lower)
        if match:
            city = match.group(1).strip()
            # Clean up common words that might be captured
            city = re.sub(r'\b(the|today|now|currently)\b', '', city).strip()
            if city and len(city) > 1:
                return city.title()  # Capitalize properly
    
    # If no pattern matches, try to find city names in common locations
    # This is a simplified approach - in production, you might use NLP
    words = message.split()
    for i, word in enumerate(words):
        if word.lower() in ['in', 'for', 'at'] and i + 1 < len(words):
            potential_city = words[i + 1]
            if len(potential_city) > 2:
                return potential_city.title()
    
    return None

def get_weather_data(city):
    """
    Fetch weather data from OpenWeather API.
    """
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    
    if not api_key:
        print("Warning: OPENWEATHER_API_KEY not found in environment variables")
        return None
    
    try:
        # OpenWeather API endpoint
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'  # Use Celsius
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def format_weather_response(weather_data):
    """
    Format weather data into a user-friendly response.
    """
    try:
        city = weather_data['name']
        country = weather_data['sys']['country']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        
        # Optional fields that might not always be present
        wind_speed = weather_data.get('wind', {}).get('speed', 'N/A')
        
        response = f"🌤️ Weather in {city}, {country}:\n"
        response += f"🌡️ Temperature: {temp}°C (feels like {feels_like}°C)\n"
        response += f"☁️ Conditions: {description.title()}\n"
        response += f"💧 Humidity: {humidity}%\n"
        
        if wind_speed != 'N/A':
            response += f"💨 Wind Speed: {wind_speed} m/s"
        
        return response
        
    except KeyError as e:
        print(f"Error parsing weather data: {e}")
        return "I received weather data but couldn't parse it properly. Please try again."

# Session management (optional - for advanced implementations)
class SessionManager:
    """
    Simple session management for conversation context.
    Note: In AgentCore, sessions are automatically managed by the runtime.
    This is just for application-level context if needed.
    """
    
    def __init__(self):
        self.sessions = {}
    
    def get_session_data(self, session_id):
        return self.sessions.get(session_id, {})
    
    def update_session_data(self, session_id, data):
        if session_id not in self.sessions:
            self.sessions[session_id] = {}
        self.sessions[session_id].update(data)

# Initialize session manager (optional)
session_manager = SessionManager()

if __name__ == "__main__":
    # Run the agent locally for testing
    print("🌤️ Starting Weather Agent locally on port 8080...")
    print("Test with: curl -X POST http://localhost:8080/invocations -H 'Content-Type: application/json' -d '{\"prompt\": \"weather in London\"}'")
    app.run()
```

## Key Implementation Points

### 1. Message Parsing
- Uses regex patterns to extract city names
- Handles common weather request phrasings
- Cleans up captured text to remove common words
- Falls back to simple word-based extraction

### 2. API Integration
- Proper error handling with try/catch
- Timeout configuration for reliability
- Environment variable for API key
- HTTP status code checking

### 3. Response Formatting
- User-friendly formatting with emojis
- Handles optional fields gracefully
- Proper error messages for parsing failures
- Temperature in Celsius with "feels like"

### 4. AgentCore Integration
- Uses `@app.entrypoint` decorator correctly
- Handles payload structure properly
- Returns dict in expected format
- Supports local testing with `app.run()`

## Testing Commands

### Local Testing
```bash
# Start the agent
python agent.py

# Test in another terminal
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What'\''s the weather in London?"}'
```

### Production Testing
```bash
# Deploy first
agentcore configure -e agent.py
agentcore launch

# Test deployed agent
agentcore invoke '{"prompt": "weather in Tokyo"}'
```

## Common Issues and Solutions

### 1. City Name Extraction
**Issue**: Agent can't find city names in user messages
**Solution**: Improve regex patterns or use NLP libraries

### 2. API Key Configuration
**Issue**: OpenWeather API returns 401 Unauthorized
**Solution**: Ensure `OPENWEATHER_API_KEY` is set in environment

### 3. Response Format
**Issue**: AgentCore returns errors about response structure
**Solution**: Ensure return value is a dict with expected keys

### 4. Local Testing
**Issue**: Port 8080 already in use
**Solution**: `lsof -ti:8080 | xargs kill -9`

### 5. Deployment Issues
**Issue**: Container build failures
**Solution**: Check requirements.txt and Python version compatibility

## Advanced Extensions

### 1. Multi-City Support
```python
def extract_cities_from_message(message):
    # Extract multiple cities from one request
    # "Compare weather in London and Paris"
```

### 2. Weather Forecasts
```python
def get_weather_forecast(city, days=5):
    # Use OpenWeather forecast API
    url = "http://api.openweathermap.org/data/2.5/forecast"
```

### 3. Session Context
```python
@app.entrypoint
def invoke(payload):
    session_id = payload.get('session_id')
    # Use session_manager to maintain conversation history
```

### 4. Enhanced NLP
```python
import spacy
# Use spaCy for better entity extraction
```

## Deployment Verification

After successful deployment, verify:
1. ✅ Agent ARN is generated
2. ✅ CloudWatch logs are created
3. ✅ Test invocations return weather data
4. ✅ Error handling works for invalid cities
5. ✅ Sessions maintain context (if implemented)

## Architecture Benefits

This implementation demonstrates:
- **Production-ready deployment** using real AWS infrastructure
- **Container-based scaling** with AgentCore Runtime
- **Session management** for stateful conversations
- **Proper error handling** for external API integration
- **Observability** through CloudWatch integration
