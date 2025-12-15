# Weather Agent Challenge 🌤️

Welcome to the Claude Code Challenge! In this 10-20 minute challenge, you'll complete a weather agent and deploy it to Amazon Bedrock Agent Core using Claude Code.

## Challenge Overview

You have been provided with an incomplete weather agent that needs to be finished. Your task is to:

1. **Explore the codebase** using Claude Code
2. **Complete the weather agent** by implementing the OpenWeather API integration
3. **Deploy the agent** to Amazon Bedrock Agent Core

## Prerequisites

- AWS CLI configured with appropriate permissions
- Python 3.9+ installed
- OpenWeather API key (will be provided during the lab)

## Getting Started

### Step 1: Clone and Explore

```bash
git clone <repository-url>
cd weather-agent-challenge
```

**🎯 Challenge Task**: Use Claude Code to explore the repository structure and understand what needs to be completed.

**Ask Claude Code**: "Help me understand this weather agent codebase and what needs to be implemented"

### Step 2: Complete the Weather Agent

The main file `lambda_function.py` has a `get_weather()` function that needs to be implemented.

**🎯 Challenge Task**: Use Claude Code to implement the missing functionality.

**What you need to implement**:
- Import the `requests` library
- Implement the `get_weather()` function to call the OpenWeather API
- Parse the API response and return formatted weather data

**OpenWeather API Details**:
- Base URL: `http://api.openweathermap.org/data/2.5/weather`
- Parameters: `q={city}&appid={API_KEY}&units=metric`
- API Key: Use environment variable `OPENWEATHER_API_KEY`

**Ask Claude Code**: "Help me implement the get_weather function to call the OpenWeather API"

### Step 3: Test Your Implementation

**🎯 Challenge Task**: Use Claude Code to help you test the implementation locally.

**Ask Claude Code**: "Help me create a test script to verify my weather agent works correctly"

### Step 4: Deploy to Bedrock Agent Core

**🎯 Challenge Task**: Use the provided deployment script to deploy your agent.

```bash
python deploy.py
```

When prompted, enter your OpenWeather API key.

**Ask Claude Code**: "Help me understand the deployment process and troubleshoot any issues"

## Expected Outcome

After completing the challenge, you should have:

1. ✅ A working weather agent that can fetch weather data
2. ✅ The agent deployed to Amazon Bedrock Agent Core
3. ✅ Ability to test the agent through the Bedrock console

## Files in This Repository

- `lambda_function.py` - Main Lambda function (needs completion)
- `requirements.txt` - Python dependencies
- `agent-schema.json` - OpenAPI schema for Bedrock Agent
- `deploy.py` - Deployment script for AWS resources
- `README.md` - This file

## Success Criteria

Your weather agent should be able to:
- Accept a city name as input
- Return current weather information including:
  - Temperature
  - Weather description
  - Humidity
- Handle errors gracefully

## Tips for Success

1. **Use Claude Code extensively** - It's your primary tool for this challenge
2. **Read the TODO comments** - They guide you to what needs implementation
3. **Test incrementally** - Verify each step before moving to the next
4. **Ask specific questions** - Claude Code works best with clear, specific requests

## Troubleshooting

If you encounter issues:

1. **API Key Issues**: Ensure your OpenWeather API key is valid and active
2. **AWS Permissions**: Verify your AWS credentials have the necessary permissions
3. **Import Errors**: Make sure all required packages are installed

**Ask Claude Code**: "Help me troubleshoot [specific error message]"

## Time Management

- **5 minutes**: Explore and understand the codebase
- **10 minutes**: Implement the weather API integration
- **5 minutes**: Deploy and test the agent

Good luck with your challenge! 🚀
