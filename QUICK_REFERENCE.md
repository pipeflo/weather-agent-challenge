# Quick Reference Card 📋

## 🔗 Essential Links
- **Repository**: `https://github.com/pipeflo/claude-weather-challenge.git`
- **Your API Key**: `[PROVIDED_BY_INSTRUCTOR]`

## ⚡ Quick Commands

```bash
# Setup
git clone https://github.com/pipeflo/claude-weather-challenge.git
cd weather-agent-challenge

# Test locally
python test_weather.py

# Deploy to Bedrock
python deploy.py
```

## 🤖 Claude Code Prompts

### Explore Codebase
```
"Help me understand this weather agent codebase. What files are here and what needs to be implemented?"
```

### Implement Weather Function
```
"Help me implement the get_weather function in lambda_function.py. I need to call the OpenWeather API with endpoint: http://api.openweathermap.org/data/2.5/weather"
```

### Test Implementation
```
"Help me test the weather agent locally using the test_weather.py script"
```

### Deploy Agent
```
"Help me deploy this weather agent to Amazon Bedrock using the deploy.py script"
```

### Troubleshoot
```
"Help me troubleshoot this error: [paste error message]"
```

## 🎯 Implementation Checklist

- [ ] Add `import requests`
- [ ] Get API key from `os.environ.get('OPENWEATHER_API_KEY')`
- [ ] Make GET request to OpenWeather API
- [ ] Parse JSON response
- [ ] Return formatted weather data
- [ ] Handle errors gracefully

## 🧪 Test Prompts for Bedrock

- "What's the weather in London?"
- "Tell me about the weather in Tokyo"
- "How's the weather in New York today?"

## 🆘 Common Fixes

**Import Error**: Add `import requests` at top of file
**API Error**: Check your API key is correct
**Deploy Error**: Verify AWS credentials and permissions

## ⏱️ Time Targets

- **5 min**: Explore and understand
- **10 min**: Implement weather function  
- **15 min**: Test locally
- **20 min**: Deploy to Bedrock
