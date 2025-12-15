# Weather Agent Challenge - Solution Guide

This file contains the complete solution for instructors and reference.

## Complete Implementation

### Updated lambda_function.py

```python
import json
import os
import requests

def lambda_handler(event, context):
    """
    Weather Agent Lambda function for Bedrock Agent Core
    
    This agent helps users get weather information for any city.
    """
    
    # Parse the incoming event from Bedrock Agent
    agent = event.get('agent', {})
    action_group = event.get('actionGroup', '')
    function = event.get('function', '')
    parameters = event.get('parameters', [])
    
    # Extract city parameter
    city = None
    for param in parameters:
        if param.get('name') == 'city':
            city = param.get('value')
            break
    
    if not city:
        return create_error_response("City parameter is required")
    
    # Get weather data
    weather_data = get_weather(city)
    
    if weather_data:
        return create_success_response(weather_data)
    else:
        return create_error_response(f"Could not get weather data for {city}")

def get_weather(city):
    """
    Get weather data for a city using OpenWeather API
    """
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    
    if not api_key:
        return None
    
    try:
        # Make API call to OpenWeather
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Parse and format the weather data
        weather_info = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data.get('wind', {}).get('speed', 0)
        }
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return None
    except KeyError as e:
        print(f"Data parsing error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def create_success_response(weather_data):
    """Create a successful response for Bedrock Agent"""
    return {
        'response': {
            'actionGroup': 'weather-actions',
            'function': 'get_weather',
            'functionResponse': {
                'responseBody': {
                    'TEXT': {
                        'body': json.dumps(weather_data)
                    }
                }
            }
        }
    }

def create_error_response(error_message):
    """Create an error response for Bedrock Agent"""
    return {
        'response': {
            'actionGroup': 'weather-actions',
            'function': 'get_weather',
            'functionResponse': {
                'responseBody': {
                    'TEXT': {
                        'body': json.dumps({'error': error_message})
                    }
                }
            }
        }
    }
```

## Key Implementation Points

1. **Import requests**: Added `import requests` at the top
2. **Environment variable**: Get API key from `OPENWEATHER_API_KEY`
3. **API call**: Make GET request to OpenWeather API with proper parameters
4. **Error handling**: Handle various error scenarios gracefully
5. **Data parsing**: Extract relevant weather information from API response
6. **Response formatting**: Return data in the format expected by Bedrock Agent

## Testing Commands

Participants can test locally with:

```python
# test_weather.py
import os
from lambda_function import get_weather

# Set API key for testing
os.environ['OPENWEATHER_API_KEY'] = 'your-api-key-here'

# Test the function
result = get_weather('London')
print(result)
```

## Common Issues and Solutions

1. **Missing requests import**: Participants often forget to add the import
2. **Environment variable**: May not realize they need to get the API key from environment
3. **API response parsing**: Might struggle with extracting the right fields from the JSON response
4. **Error handling**: May not implement proper error handling for API failures

## Deployment Verification

After deployment, test in Bedrock console with prompts like:
- "What's the weather in London?"
- "Tell me about the weather in Tokyo"
- "How's the weather in New York today?"
