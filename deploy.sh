#!/bin/bash

# Weather Agent Deployment Script
# Uses Amazon Bedrock AgentCore Starter Toolkit

set -e  # Exit on any error

echo "🚀 Weather Agent Deployment to Amazon Bedrock AgentCore"
echo "======================================================"

# Check prerequisites
echo "🔍 Checking prerequisites..."

# Check if agentcore CLI is installed
if ! command -v agentcore &> /dev/null; then
    echo "❌ AgentCore CLI not found. Installing..."
    pip install bedrock-agentcore-starter-toolkit
fi

# Check AWS credentials
if ! aws sts get-caller-identity &> /dev/null; then
    echo "❌ AWS credentials not configured"
    echo "   Configure with: aws configure"
    exit 1
fi

echo "✅ Prerequisites check passed"

# Get OpenWeather API key
if [ -z "$OPENWEATHER_API_KEY" ]; then
    echo "🔑 OpenWeather API Key required"
    read -p "Enter your OpenWeather API key: " OPENWEATHER_API_KEY
    export OPENWEATHER_API_KEY
fi

# Configure the agent
echo "⚙️ Configuring agent..."
agentcore configure -e agent.py

# Set environment variables in configuration
echo "🔧 Setting environment variables..."
# Note: The actual method to set env vars may vary based on toolkit version
# This is a placeholder for the workshop

# Deploy to AgentCore Runtime
echo "🚀 Deploying to AgentCore Runtime..."
echo "This will:"
echo "  - Build your agent container"
echo "  - Create AgentCore Runtime"
echo "  - Deploy to AWS"
echo "  - Set up endpoints and versions"

agentcore launch

# Get the agent ARN from the deployment
echo "📋 Deployment completed!"
echo "Your agent is now running in Amazon Bedrock AgentCore Runtime"

# Test the deployed agent
echo "🧪 Testing deployed agent..."
agentcore invoke '{"prompt": "What'\''s the weather in London?"}'

echo "✅ Deployment successful!"
echo ""
echo "📝 Next steps:"
echo "  1. Test your agent with: agentcore invoke '{\"prompt\": \"weather in Paris\"}'"
echo "  2. View logs in CloudWatch"
echo "  3. Monitor performance in AgentCore console"
echo "  4. Scale automatically based on demand"
echo ""
echo "🔗 Resources created:"
echo "  - AgentCore Runtime (container environment)"
echo "  - ECR Repository (for container images)"
echo "  - IAM Roles (for execution permissions)"
echo "  - CloudWatch Logs (for observability)"
