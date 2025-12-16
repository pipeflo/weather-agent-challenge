from bedrock_agentcore import BedrockAgentCoreApp
import requests
import os
import json

app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload):
    """Main entry point for weather agent"""
    user_message = payload.get("prompt", "")
    
    if not user_message:
        return {"result": "Hello! Ask me about the weather in any city."}
    
    # Need to extract city from message
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
    # TODO: Parse city from user message
    # Should handle "weather in London", "how's Paris weather", etc.
    pass

def get_weather(city):
    # TODO: Call OpenWeather API
    # API: http://api.openweathermap.org/data/2.5/weather
    # Params: q={city}&appid={key}&units=metric
    # Key from env: OPENWEATHER_API_KEY
    pass

def format_response(weather_data):
    # TODO: Format weather into user-friendly message
    # Include temp, description, maybe humidity
    pass

if __name__ == "__main__":
    app.run()
