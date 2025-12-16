# Deploy Agent Slash Command

## Command: /deploy-agent

### Description
Automated deployment of the weather agent to Amazon Bedrock AgentCore Runtime.

### Usage
```
/deploy-agent [--region us-west-2] [--env-file .env]
```

### Parameters
- `--region` (optional): AWS region for deployment. Defaults to "us-west-2"
- `--env-file` (optional): Environment file with API keys. Defaults to ".env"

### Functionality
1. Validate prerequisites (AWS credentials, API keys, dependencies)
2. Configure AgentCore toolkit with project settings
3. Set environment variables for deployment
4. Launch deployment to AgentCore Runtime
5. Monitor deployment progress and status
6. Test deployed agent with sample invocation
7. Display deployment summary and next steps

### Example Output
```
🚀 Deploying Weather Agent to AgentCore Runtime
==============================================

✅ Prerequisites: All checks passed
⚙️ Configuring: AgentCore toolkit setup
🔧 Environment: API keys configured
📦 Building: Container image creation
🚀 Deploying: AgentCore Runtime deployment
🧪 Testing: Sample invocation successful

🎉 Deployment completed successfully!

Agent ARN: arn:aws:bedrock-agentcore:us-west-2:123456789012:agent-runtime/weather-agent-abc123
Endpoint: DEFAULT
Region: us-west-2

Next steps:
- Test with: agentcore invoke '{"prompt": "weather in Paris"}'
- View logs: CloudWatch → /aws/bedrock-agentcore/runtimes/weather-agent-abc123-DEFAULT
- Monitor: AgentCore console
```

### Error Handling
- AWS credentials: Guide to configuration
- Missing dependencies: Installation instructions
- Deployment failures: Troubleshooting steps
- Permission issues: IAM policy requirements

### Implementation
This command should:
- Run prerequisite checks before deployment
- Execute AgentCore toolkit commands in sequence
- Handle errors gracefully with helpful messages
- Provide clear status updates during deployment
- Test the deployed agent automatically
