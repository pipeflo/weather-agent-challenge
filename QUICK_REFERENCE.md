# AgentCore Weather Workshop - Quick Reference 📋

## 🔗 Essential Links
- **Repository**: `https://github.com/pipeflo/weather-agent-challenge.git`
- **Your API Key**: `[PROVIDED_BY_INSTRUCTOR]`
- **AgentCore Docs**: https://docs.aws.amazon.com/bedrock-agentcore/

## ⚡ Quick Commands

```bash
# Setup
git clone https://github.com/pipeflo/weather-agent-challenge.git
cd weather-agent-challenge
pip install -r requirements.txt

# Local testing
python agent.py
curl -X POST http://localhost:8080/invocations -H "Content-Type: application/json" -d '{"prompt": "weather in London"}'

# Deploy to AgentCore
agentcore configure -e agent.py
agentcore launch

# Test deployed agent
agentcore invoke '{"prompt": "weather in Paris"}'
```

## 🏗️ AgentCore Architecture

```
Client → AgentCore Runtime → Your Agent (Container)
                ↓
         Session Management (8hr microVMs)
                ↓
         Observability (CloudWatch)
```

## 🤖 Key Concepts to Explore with Claude Code

### AgentCore Fundamentals
- "How does AgentCore Runtime work?"
- "What's the difference between AgentCore and Lambda?"
- "How do sessions work in AgentCore?"
- "What's the HTTP protocol structure?"

### Implementation Guidance
- "How do I implement the BedrockAgentCoreApp entrypoint?"
- "What's the best way to parse user messages for city names?"
- "How should I structure the OpenWeather API call?"
- "What's the proper response format for AgentCore?"

### Deployment & Testing
- "How does the AgentCore toolkit deployment work?"
- "What AWS resources are created during deployment?"
- "How do I debug deployment issues?"
- "How do I test the agent locally vs in production?"

## 🎯 Implementation Checklist

### Core Functions to Complete
- [ ] `extract_city_from_message()` - Parse user input
- [ ] `get_weather_data()` - Call OpenWeather API  
- [ ] `format_weather_response()` - Format user response
- [ ] Error handling for API failures
- [ ] Proper AgentCore response structure

### Key Implementation Details
- [ ] Import `bedrock_agentcore` and `requests`
- [ ] Use `@app.entrypoint` decorator
- [ ] Handle payload structure correctly
- [ ] Set `OPENWEATHER_API_KEY` environment variable
- [ ] Return dict with proper structure

## 🧪 Testing Scenarios

### Local Testing
```bash
# Basic weather query
{"prompt": "What's the weather in London?"}

# Different phrasing
{"prompt": "Tell me about Tokyo weather"}

# Error cases
{"prompt": "Hello there"}  # No city specified
```

### Production Testing
```bash
# Via CLI
agentcore invoke '{"prompt": "weather in Berlin"}'

# Via Python script
python test_agent.py
```

## 🚀 Deployment Process

1. **Configure**: `agentcore configure -e agent.py`
2. **Deploy**: `agentcore launch` 
3. **Test**: `agentcore invoke '{"prompt": "test"}'`
4. **Monitor**: Check CloudWatch logs

## 🔧 Common Issues & Solutions

### Local Development
- **Port 8080 in use**: `lsof -ti:8080` then `kill -9 PID`
- **Missing dependencies**: `pip install bedrock-agentcore requests`
- **API key not set**: `export OPENWEATHER_API_KEY='your-key'`

### Deployment Issues
- **AWS credentials**: `aws sts get-caller-identity`
- **Permissions**: Check IAM policies for AgentCore
- **Toolkit not found**: `pip install bedrock-agentcore-starter-toolkit`

### Runtime Issues
- **Agent not responding**: Check CloudWatch logs
- **API errors**: Verify OpenWeather API key
- **Session issues**: Understand 8-hour session lifecycle

## 📊 Success Indicators

✅ **Local agent runs** on port 8080  
✅ **Weather API calls** return data  
✅ **Deployment succeeds** with agent ARN  
✅ **Production testing** works via CLI  
✅ **Sessions maintain** conversation context  
✅ **Observability** shows in CloudWatch  

## ⏱️ Time Targets

- **0-5 min**: Setup and exploration
- **5-15 min**: Understand AgentCore architecture  
- **15-30 min**: Implement weather functions
- **30-35 min**: Local testing and debugging
- **35-45 min**: Deploy and test in production

## 🎓 Key Learning Goals

1. **AgentCore vs Serverless**: Container-based vs function-based
2. **Session Management**: 8-hour persistent environments
3. **HTTP Protocol**: AgentCore's communication contract
4. **Production Deployment**: Real AWS infrastructure
5. **Observability**: Built-in monitoring and logging

## 💡 Workshop Philosophy

- **Explore** with Claude Code rather than follow exact steps
- **Understand** architecture before implementing
- **Debug** issues using Claude Code's expertise
- **Deploy** to real AWS infrastructure
- **Learn** production-ready agent development

Remember: Use Claude Code as your development partner throughout the workshop!
