import json
import os
# TODO: Add requests import for API calls

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
    
    # TODO: Implement get_weather function
    weather_data = get_weather(city)
    
    if weather_data:
        return create_success_response(weather_data)
    else:
        return create_error_response(f"Could not get weather data for {city}")

def get_weather(city):
    """
    Get weather data for a city using OpenWeather API
    
    TODO: Implement this function to:
    1. Get API key from environment variable OPENWEATHER_API_KEY
    2. Make API call to OpenWeather API
    3. Parse and return weather data
    """
    # TODO: Add your implementation here
    pass

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
