from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent, tool
import requests
import os
import json
import re

app = BedrockAgentCoreApp()

# Weather tool using Strands @tool decorator
@tool
def get_weather(city: str) -> str:
    """Get current weather information for a city.
    
    Args:
        city: The name of the city to get weather for
    """
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    
    if not api_key:
        return "Error: OPENWEATHER_API_KEY not found in environment variables"
    
    try:
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Format weather information
        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        
        weather_info = f"🌤️ Weather in {city_name}, {country}:\n"
        weather_info += f"🌡️ Temperature: {temp}°C (feels like {feels_like}°C)\n"
        weather_info += f"☁️ Conditions: {description.title()}\n"
        weather_info += f"💧 Humidity: {humidity}%"
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
    except KeyError as e:
        return f"Error parsing weather data: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

# Calculator tool using Strands @tool decorator
@tool
def calculate(expression: str) -> str:
    """Perform mathematical calculations safely.
    
    Args:
        expression: Mathematical expression to evaluate (e.g., "2 + 3 * 4")
    """
    try:
        # Basic safety check - only allow numbers, operators, parentheses, and spaces
        allowed_chars = set('0123456789+-*/()., ')
        if not all(c in allowed_chars for c in expression):
            return "Error: Invalid characters in expression. Only numbers and basic operators (+, -, *, /, parentheses) are allowed."
        
        # Evaluate the expression safely
        result = eval(expression)
        return f"🧮 {expression} = {result}"
        
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except SyntaxError:
        return "Error: Invalid mathematical expression."
    except Exception as e:
        return f"Error calculating expression: {e}"

# Create Strands agent with tools
strands_agent = Agent(
    system_prompt="""You are a helpful assistant that can provide weather information and perform calculations.

For weather queries:
- Use the get_weather tool to fetch current weather data for any city
- Provide clear, formatted weather information

For calculations:
- Use the calculate tool to perform mathematical operations
- Support basic arithmetic operations (+, -, *, /, parentheses)
- Show the calculation and result clearly

Always be helpful and provide clear, accurate information.""",
    tools=[get_weather, calculate]
)

@app.entrypoint
def invoke(payload):
    """Main entry point for AgentCore"""
    user_message = payload.get("prompt", "")
    
    if not user_message:
        return {"result": "Hello! I can help you with weather information and calculations. What would you like to know?"}
    
    try:
        # Use Strands agent to process the request
        response = strands_agent(user_message)
        return {"result": response}
        
    except Exception as e:
        return {"result": f"Sorry, I encountered an error: {e}"}

if __name__ == "__main__":
    app.run()
