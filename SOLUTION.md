# Weather Agent Scenario - Complete Solution

This file contains the complete implementation for the inherited weather agent project using Amazon Strands tools.

## Completed agent.py

```python
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
```

## Key Implementation Details

### Strands Tools Framework
- Uses `@tool` decorator to define weather and calculator tools
- Tools are automatically discovered and made available to the agent
- Each tool has proper docstring documentation for the LLM to understand usage

### Weather Tool
- Integrates with OpenWeather API using requests
- Handles API key from environment variable
- Formats response with emojis and clear structure
- Includes comprehensive error handling

### Calculator Tool  
- Safely evaluates mathematical expressions
- Includes input validation to prevent code injection
- Handles common math errors (division by zero, syntax errors)
- Returns formatted results with calculation shown

### Strands Agent Integration
- Creates a Strands Agent with both tools
- Uses system prompt to guide tool usage
- Agent automatically decides when to use each tool based on user input
- Integrates with AgentCore through the entrypoint function

## Testing Commands

### Local Testing
```bash
# Set API key
export OPENWEATHER_API_KEY="your-api-key-here"

# Start agent
python agent.py

# Test weather functionality
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What'\''s the weather in London?"}'

# Test calculator functionality  
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Calculate 15 * 8 + 32"}'

# Test combined functionality
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What'\''s the weather in Paris and what is 25 + 17?"}'
```

### Production Deployment
```bash
# Configure AgentCore toolkit
agentcore configure -e agent.py

# Deploy to AgentCore Runtime
agentcore launch

# Test deployed agent
agentcore invoke '{"prompt": "weather in Tokyo and calculate 100 / 4"}'
```

## Architecture Benefits

This implementation demonstrates:

1. **Modern Tool Framework**: Uses Amazon Strands for proper tool definition and management
2. **Multi-Tool Agent**: Single agent can handle both weather and calculations intelligently
3. **Automatic Tool Selection**: Agent decides which tool to use based on user input
4. **Production Ready**: Integrates with AgentCore for scalable deployment
5. **Error Handling**: Comprehensive error handling for both tools
6. **Safety**: Calculator tool includes input validation for security

## Sample Interactions

**Weather Query**:
- Input: "What's the weather in New York?"
- Output: "🌤️ Weather in New York, US: 🌡️ Temperature: 18°C (feels like 16°C) ☁️ Conditions: Clear Sky 💧 Humidity: 65%"

**Calculator Query**:
- Input: "Calculate 25 * 4 + 10"
- Output: "🧮 25 * 4 + 10 = 110"

**Combined Query**:
- Input: "What's the weather in London and what's 15 + 27?"
- Agent automatically uses both tools and provides both answers

This solution represents a modern, production-ready implementation using the Amazon Strands framework for tool-based AI agents.
