# Weather Agent Scenario - Complete Solution

This file contains the complete implementation for the inherited weather agent project.

## Completed agent.py

```python
from bedrock_agentcore import BedrockAgentCoreApp
import requests
import os
import json
import re

app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload):
    """Main entry point for weather agent"""
    user_message = payload.get("prompt", "")
    
    if not user_message:
        return {"result": "Hello! Ask me about the weather in any city."}
    
    # Extract city from message
    city = extract_city(user_message)
    
    if not city:
        return {"result": "Please tell me which city you'd like weather for."}
    
    # Get weather data
    weather = get_weather(city)
    
    if weather:
        response = format_response(weather)
        return {"result": response}
    else:
        return {"result": f"Sorry, couldn't get weather for {city}."}

def extract_city(message):
    """Parse city from user message"""
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
    ]
    
    for pattern in patterns:
        match = re.search(pattern, message_lower)
        if match:
            city = match.group(1).strip()
            # Clean up common words
            city = re.sub(r'\b(the|today|now|currently)\b', '', city).strip()
            if city and len(city) > 1:
                return city.title()
    
    # Fallback: look for city after common words
    words = message.split()
    for i, word in enumerate(words):
        if word.lower() in ['in', 'for', 'at'] and i + 1 < len(words):
            potential_city = words[i + 1]
            if len(potential_city) > 2:
                return potential_city.title()
    
    return None

def get_weather(city):
    """Call OpenWeather API"""
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    
    if not api_key:
        print("Warning: OPENWEATHER_API_KEY not found")
        return None
    
    try:
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def format_response(weather_data):
    """Format weather into user-friendly message"""
    try:
        city = weather_data['name']
        country = weather_data['sys']['country']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        
        response = f"🌤️ Weather in {city}, {country}:\n"
        response += f"🌡️ Temperature: {temp}°C (feels like {feels_like}°C)\n"
        response += f"☁️ Conditions: {description.title()}\n"
        response += f"💧 Humidity: {humidity}%"
        
        return response
        
    except KeyError as e:
        print(f"Error parsing weather data: {e}")
        return "I received weather data but couldn't parse it properly."

if __name__ == "__main__":
    app.run()
```

## Key Implementation Details

### City Extraction
- Uses regex patterns to match common weather request phrasings
- Handles variations like "weather in London", "how's Paris weather"
- Cleans up captured text to remove common words
- Falls back to simple word-based extraction
- Returns properly capitalized city names

### Weather API Integration
- Gets API key from `OPENWEATHER_API_KEY` environment variable
- Makes HTTP request to OpenWeather API with proper parameters
- Includes timeout for reliability
- Handles various error scenarios (network, API, parsing)
- Returns parsed JSON response or None on failure

### Response Formatting
- Extracts key weather information (temperature, description, humidity)
- Formats with emojis for visual appeal
- Includes both actual and "feels like" temperature
- Handles missing data gracefully
- Returns user-friendly formatted string

## Testing Commands

### Local Testing
```bash
# Set API key
export OPENWEATHER_API_KEY="your-api-key-here"

# Start agent
python agent.py

# Test in another terminal
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What'\''s the weather in London?"}'
```

### Production Deployment
```bash
# Configure AgentCore toolkit
agentcore configure -e agent.py

# Deploy to AgentCore Runtime
agentcore launch

# Test deployed agent
agentcore invoke '{"prompt": "weather in Tokyo"}'
```

## Common Issues and Solutions

### Issue: City not extracted from message
**Cause**: User phrasing doesn't match regex patterns
**Solution**: Add more patterns or improve fallback logic

### Issue: API returns 401 Unauthorized
**Cause**: Invalid or missing API key
**Solution**: Verify `OPENWEATHER_API_KEY` environment variable

### Issue: API returns 404 Not Found
**Cause**: Invalid city name
**Solution**: Improve city name validation or suggest alternatives

### Issue: Deployment fails
**Cause**: Missing AWS credentials or permissions
**Solution**: Check `aws sts get-caller-identity` and IAM permissions

### Issue: Agent doesn't respond in production
**Cause**: Environment variable not set in deployment
**Solution**: Configure API key in AgentCore deployment settings

## Realistic Development Notes

This solution represents what a developer would create when inheriting the incomplete codebase:

1. **Followed existing patterns** - Maintained the structure and style
2. **Implemented pragmatic solutions** - Used simple regex instead of complex NLP
3. **Added proper error handling** - Handled API failures gracefully
4. **Included user-friendly formatting** - Made responses engaging with emojis
5. **Tested incrementally** - Each function can be tested independently

The implementation balances functionality with simplicity, which is typical when completing inherited projects under time constraints.
