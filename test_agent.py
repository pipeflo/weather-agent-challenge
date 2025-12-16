#!/usr/bin/env python3
"""
Test script for the Weather Agent
Tests both local and deployed versions
"""

import requests
import json
import os
import boto3
from uuid import uuid4

def test_local_agent():
    """Test the agent running locally on port 8080"""
    print("🧪 Testing Local Agent")
    print("=" * 50)
    
    # Test data
    test_cases = [
        {"prompt": "What's the weather in London?"},
        {"prompt": "Tell me about the weather in Tokyo"},
        {"prompt": "How's the weather in New York today?"},
        {"prompt": "Hello, I need weather information"}
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test_case['prompt']}")
        
        try:
            response = requests.post(
                "http://localhost:8080/invocations",
                headers={"Content-Type": "application/json"},
                json=test_case,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Success: {result}")
            else:
                print(f"❌ Failed: {response.status_code} - {response.text}")
                
        except requests.exceptions.ConnectionError:
            print("❌ Connection failed - make sure agent is running locally")
            print("   Run: python agent.py")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def test_deployed_agent(agent_arn):
    """Test the agent deployed to AgentCore Runtime"""
    print("\n🚀 Testing Deployed Agent")
    print("=" * 50)
    
    if not agent_arn:
        print("❌ No agent ARN provided")
        return
    
    # Initialize AgentCore client
    try:
        client = boto3.client('bedrock-agentcore')
    except Exception as e:
        print(f"❌ Failed to create AgentCore client: {e}")
        return
    
    # Test cases
    test_cases = [
        {"prompt": "What's the weather in London?"},
        {"prompt": "Tell me about the weather in Paris"},
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test_case['prompt']}")
        session_id = str(uuid4())
        
        try:
            response = client.invoke_agent_runtime(
                agentRuntimeArn=agent_arn,
                runtimeSessionId=session_id,
                payload=json.dumps(test_case).encode(),
                qualifier="DEFAULT"
            )
            
            # Parse response
            content = []
            for chunk in response.get("response", []):
                content.append(chunk.decode('utf-8'))
            
            result = json.loads(''.join(content))
            print(f"✅ Success: {result}")
            
        except Exception as e:
            print(f"❌ Error: {e}")

def check_environment():
    """Check if environment is properly configured"""
    print("🔍 Environment Check")
    print("=" * 50)
    
    # Check API key
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    if api_key:
        print("✅ OPENWEATHER_API_KEY is set")
    else:
        print("❌ OPENWEATHER_API_KEY not found")
        print("   Set it with: export OPENWEATHER_API_KEY='your-key-here'")
    
    # Check AWS credentials
    try:
        boto3.client('sts').get_caller_identity()
        print("✅ AWS credentials are configured")
    except Exception as e:
        print(f"❌ AWS credentials issue: {e}")
    
    # Check dependencies
    try:
        import bedrock_agentcore
        print("✅ bedrock-agentcore package is installed")
    except ImportError:
        print("❌ bedrock-agentcore package not found")
        print("   Install with: pip install bedrock-agentcore")

def main():
    """Main test function"""
    print("🌤️ Weather Agent Test Suite")
    print("=" * 50)
    
    # Check environment first
    check_environment()
    
    # Test local agent
    test_local_agent()
    
    # Test deployed agent if ARN is provided
    agent_arn = os.environ.get('AGENT_ARN')
    if agent_arn:
        test_deployed_agent(agent_arn)
    else:
        print("\n💡 To test deployed agent, set AGENT_ARN environment variable")
        print("   export AGENT_ARN='your-agent-arn-here'")

if __name__ == "__main__":
    main()
