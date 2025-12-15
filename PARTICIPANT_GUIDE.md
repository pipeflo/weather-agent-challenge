# Weather Agent Challenge - Participant Guide 🌤️

**Time Limit**: 15-20 minutes  
**Goal**: Complete and deploy a weather agent using Claude Code

## 🚀 Quick Start

### Step 1: Setup (2 minutes)

```bash
# Clone the repository
git clone https://github.com/pipeflo/claude-weather-challenge.git
cd weather-agent-challenge

# Open in your preferred editor
code .  # or your preferred editor
```

**Your OpenWeather API Key**: `[PROVIDED_BY_INSTRUCTOR]`

### Step 2: Explore with Claude Code (3 minutes)

**Ask Claude Code**:
```
"Help me understand this weather agent codebase. What files are here and what needs to be implemented?"
```

**Expected Response**: Claude Code will explain the structure and identify the TODOs in `lambda_function.py`

### Step 3: Implement the Weather Function (8 minutes)

**Ask Claude Code**:
```
"Help me implement the get_weather function in lambda_function.py. I need to:
1. Import the requests library
2. Get the API key from environment variable OPENWEATHER_API_KEY  
3. Call the OpenWeather API with the city parameter
4. Parse and return the weather data

The API endpoint is: http://api.openweathermap.org/data/2.5/weather
Parameters: q={city}&appid={API_KEY}&units=metric"
```

**What Claude Code should help you add**:
- `import requests` at the top
- Complete `get_weather()` function implementation
- Proper error handling

### Step 4: Test Locally (2 minutes)

**Ask Claude Code**:
```
"Help me test the weather agent locally using the test_weather.py script"
```

**Run the test**:
```bash
python test_weather.py
# Enter your API key when prompted
```

### Step 5: Deploy to Bedrock (5 minutes)

**Ask Claude Code**:
```
"Help me deploy this weather agent to Amazon Bedrock using the deploy.py script"
```

**Run deployment**:
```bash
python deploy.py
# Enter your API key when prompted
```

**Expected output**:
```
🚀 Starting Weather Agent deployment...
Creating Lambda deployment package...
✅ Lambda deployment package created
Deploying Lambda function...
✅ Created new Lambda function: weather-agent-function
Creating Bedrock Agent...
✅ Created Bedrock Agent: [AGENT_ID]
Creating action group...
✅ Created action group

🎉 Deployment completed successfully!
Agent ID: [AGENT_ID]
You can now test your weather agent in the Bedrock console.
```

## ✅ Success Checklist

- [ ] Repository cloned and explored
- [ ] `get_weather()` function implemented
- [ ] Local testing passes
- [ ] Agent deployed to Bedrock
- [ ] Agent responds to weather queries

## 🧪 Test Your Agent

In the Bedrock console, try these prompts:
- "What's the weather in London?"
- "Tell me about the weather in Tokyo"
- "How's the weather in New York today?"

## 🆘 Troubleshooting

**Import Error**: Make sure you added `import requests`

**API Key Error**: Verify your OpenWeather API key is valid

**AWS Permissions**: Ensure your AWS credentials have necessary permissions

**Ask Claude Code**: "Help me troubleshoot [specific error message]"

## 🎯 Key Learning Points

1. **Code Exploration**: Using Claude Code to understand existing codebases
2. **API Integration**: Implementing external API calls with error handling
3. **Testing**: Local testing before deployment
4. **AWS Deployment**: Automated deployment to Bedrock Agent Core

## ⏱️ Time Management

- **0-2 min**: Setup and clone
- **2-5 min**: Explore with Claude Code
- **5-13 min**: Implement weather function
- **13-15 min**: Test locally
- **15-20 min**: Deploy to Bedrock

**Remember**: Use Claude Code for every step - it's your primary tool!
