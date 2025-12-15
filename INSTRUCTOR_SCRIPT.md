# Weather Agent Challenge - Instructor Script 👨‍🏫

**Duration**: 20 minutes  
**Prerequisites**: Participants completed Claude Code workshop labs

## 🎯 Workshop Objectives

By the end of this challenge, participants will:
- Use Claude Code to explore and understand existing codebases
- Implement API integrations with proper error handling
- Deploy agents to Amazon Bedrock Agent Core
- Apply Claude Code skills in a real-world scenario

## 📋 Pre-Workshop Setup

### Materials Needed
- [ ] OpenWeather API keys (one per participant)
- [ ] AWS accounts with Bedrock permissions
- [ ] Repository URL: `https://github.com/pipeflo/weather-agent-challenge.git`

### AWS Permissions Required
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lambda:*",
                "iam:CreateRole",
                "iam:AttachRolePolicy",
                "iam:PutRolePolicy",
                "bedrock-agent:*"
            ],
            "Resource": "*"
        }
    ]
}
```

## 🎬 Workshop Script

### Opening (2 minutes)

**Say**: 
> "Welcome to the Claude Code Challenge! You've learned how to use Claude Code in the previous labs. Now it's time to apply those skills to complete and deploy a real weather agent to Amazon Bedrock.
> 
> You have 20 minutes to:
> 1. Explore the codebase using Claude Code
> 2. Complete the weather agent implementation
> 3. Deploy it to Bedrock Agent Core
> 
> Your OpenWeather API key is: `[DISTRIBUTE_KEYS]`
> Repository: `https://github.com/pipeflo/weather-agent-challenge.git`"

### Challenge Phase (15 minutes)

**Circulate and help participants**. Common issues:

**5-minute mark**: Check that everyone has cloned and is exploring
- **If stuck**: "Ask Claude Code to explain the repository structure"

**10-minute mark**: Most should be implementing the weather function
- **If stuck**: "Ask Claude Code to help implement the get_weather function with the OpenWeather API"

**15-minute mark**: Should be testing or deploying
- **If behind**: "Focus on getting the basic implementation working first"

### Wrap-up (3 minutes)

**Ask for show of hands**:
- "Who successfully implemented the weather function?"
- "Who got it deployed to Bedrock?"
- "Who tested it in the Bedrock console?"

## 🔧 Common Issues & Solutions

### Issue: Import Error
**Symptom**: `ModuleNotFoundError: No module named 'requests'`
**Solution**: Guide them to add `import requests` at the top of `lambda_function.py`

### Issue: API Key Not Working
**Symptom**: 401 Unauthorized from OpenWeather API
**Solution**: Verify they're using the correct API key and it's set in environment variable

### Issue: AWS Permissions
**Symptom**: Access denied errors during deployment
**Solution**: Check AWS credentials and permissions

### Issue: Bedrock Agent Not Responding
**Symptom**: Agent created but not responding to queries
**Solution**: Check that action group was created and Lambda permissions are correct

## 📊 Success Metrics

**Excellent** (80%+ participants):
- Complete implementation
- Successful deployment
- Working agent in Bedrock console

**Good** (60%+ participants):
- Complete implementation
- Local testing works
- Deployment attempted

**Needs Improvement** (<60%):
- Review Claude Code usage patterns
- Provide additional guided practice

## 🎤 Key Teaching Points

1. **Claude Code as Primary Tool**: Emphasize using Claude Code for every step
2. **Iterative Development**: Test locally before deploying
3. **Error Handling**: Proper API error handling is crucial
4. **Real-world Application**: This mirrors actual development workflows

## 📝 Debrief Questions

1. "How did Claude Code help you understand the existing codebase?"
2. "What was the most challenging part of the implementation?"
3. "How would you extend this agent with additional features?"
4. "What did you learn about deploying to Bedrock Agent Core?"

## 🔄 Follow-up Activities

- Extend the agent with additional weather features
- Add support for multiple cities
- Implement weather alerts or forecasts
- Create a web interface for the agent

## 📞 Support Contacts

**Technical Issues**: [Your contact info]
**AWS Account Issues**: [AWS support contact]
**API Key Issues**: [OpenWeather support or backup keys]
