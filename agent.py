from bedrock_agentcore import BedrockAgentCoreApp
import requests
import os
import json

# Initialize the AgentCore application
app = BedrockAgentCoreApp()

# TODO: Complete the weather agent implementation
# This agent should:
# 1. Handle HTTP requests through the AgentCore protocol
# 2. Manage session state across multiple interactions
# 3. Call the OpenWeather API to get weather data
# 4. Return properly formatted responses

@app.entrypoint
def invoke(payload):
    """
    Main entry point for the weather agent.
    
    This function is called by AgentCore Runtime for each request.
    It should handle the weather query and return appropriate responses.
    
    Args:
        payload (dict): The request payload from AgentCore Runtime
        
    Returns:
        dict: Response in AgentCore format
    """
    
    # TODO: Extract user message from payload
    # The payload structure depends on how the agent is invoked
    user_message = payload.get("prompt", "")
    
    # TODO: Parse the user's weather request
    # Extract city name from the user's message
    city = extract_city_from_message(user_message)
    
    if not city:
        return {
            "result": "I'd be happy to help you with weather information! Please tell me which city you'd like to know about."
        }
    
    # TODO: Get weather data for the city
    weather_data = get_weather_data(city)
    
    if weather_data:
        # TODO: Format the weather response for the user
        response = format_weather_response(weather_data)
        return {"result": response}
    else:
        return {
            "result": f"I'm sorry, I couldn't get weather information for {city}. Please check the city name and try again."
        }

def extract_city_from_message(message):
    """
    Extract city name from user message.
    
    TODO: Implement logic to parse city names from natural language.
    This could be simple keyword extraction or more sophisticated NLP.
    
    Args:
        message (str): User's message
        
    Returns:
        str: Extracted city name or None
    """
    # TODO: Implement city extraction logic
    # For now, this is a placeholder - you should implement proper parsing
    pass

def get_weather_data(city):
    """
    Fetch weather data from OpenWeather API.
    
    TODO: Implement the OpenWeather API integration.
    
    Args:
        city (str): City name to get weather for
        
    Returns:
        dict: Weather data from API or None if failed
    """
    # TODO: Get API key from environment variable
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    
    if not api_key:
        print("Warning: OPENWEATHER_API_KEY not found in environment variables")
        return None
    
    # TODO: Make API request to OpenWeather
    # API endpoint: http://api.openweathermap.org/data/2.5/weather
    # Parameters: q={city}&appid={api_key}&units=metric
    
    try:
        # TODO: Implement the API call
        pass
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def format_weather_response(weather_data):
    """
    Format weather data into a user-friendly response.
    
    TODO: Create a natural language response from the weather data.
    
    Args:
        weather_data (dict): Raw weather data from API
        
    Returns:
        str: Formatted response for the user
    """
    # TODO: Extract relevant information and format it nicely
    # Include temperature, description, humidity, etc.
    pass

# Session management helpers
class SessionManager:
    """
    Helper class for managing conversation context.
    
    TODO: Implement session state management.
    AgentCore provides session isolation, but you may want to track
    conversation history or user preferences within a session.
    """
    
    def __init__(self):
        # TODO: Initialize session storage
        pass
    
    def get_session_data(self, session_id):
        """Get data for a specific session."""
        # TODO: Implement session data retrieval
        pass
    
    def update_session_data(self, session_id, data):
        """Update data for a specific session."""
        # TODO: Implement session data storage
        pass

# Initialize session manager
session_manager = SessionManager()

if __name__ == "__main__":
    # Run the agent locally for testing
    # This will start the HTTP server on port 8080
    app.run()
