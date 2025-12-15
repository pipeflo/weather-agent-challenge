#!/usr/bin/env python3
"""
Deployment script for Weather Agent to Bedrock Agent Core
"""

import boto3
import json
import zipfile
import os
import time

def create_lambda_deployment_package():
    """Create a deployment package for Lambda"""
    print("Creating Lambda deployment package...")
    
    with zipfile.ZipFile('weather-agent.zip', 'w') as zip_file:
        zip_file.write('lambda_function.py')
    
    print("✅ Lambda deployment package created")

def deploy_lambda_function(api_key):
    """Deploy the Lambda function"""
    print("Deploying Lambda function...")
    
    lambda_client = boto3.client('lambda')
    
    # Read the deployment package
    with open('weather-agent.zip', 'rb') as zip_file:
        zip_content = zip_file.read()
    
    function_name = 'weather-agent-function'
    
    try:
        # Try to update existing function
        response = lambda_client.update_function_code(
            FunctionName=function_name,
            ZipFile=zip_content
        )
        print(f"✅ Updated existing Lambda function: {function_name}")
    except lambda_client.exceptions.ResourceNotFoundException:
        # Create new function
        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.9',
            Role=get_lambda_role_arn(),
            Handler='lambda_function.lambda_handler',
            Code={'ZipFile': zip_content},
            Environment={
                'Variables': {
                    'OPENWEATHER_API_KEY': api_key
                }
            },
            Timeout=30
        )
        print(f"✅ Created new Lambda function: {function_name}")
    
    return response['FunctionArn']

def get_lambda_role_arn():
    """Get or create Lambda execution role"""
    iam = boto3.client('iam')
    role_name = 'weather-agent-lambda-role'
    
    try:
        response = iam.get_role(RoleName=role_name)
        return response['Role']['Arn']
    except iam.exceptions.NoSuchEntityException:
        # Create the role
        trust_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "lambda.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
        
        response = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy)
        )
        
        # Attach basic execution policy
        iam.attach_role_policy(
            RoleName=role_name,
            PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
        )
        
        print(f"✅ Created Lambda execution role: {role_name}")
        return response['Role']['Arn']

def create_bedrock_agent(lambda_arn):
    """Create Bedrock Agent"""
    print("Creating Bedrock Agent...")
    
    bedrock = boto3.client('bedrock-agent')
    
    agent_name = 'weather-agent'
    
    try:
        response = bedrock.create_agent(
            agentName=agent_name,
            description='Weather information agent',
            foundationModel='anthropic.claude-3-haiku-20240307-v1:0',
            instruction='You are a helpful weather assistant. Use the get_weather function to provide current weather information for any city the user asks about.',
            agentResourceRoleArn=get_bedrock_agent_role_arn()
        )
        
        agent_id = response['agent']['agentId']
        print(f"✅ Created Bedrock Agent: {agent_id}")
        
        # Create action group
        create_action_group(agent_id, lambda_arn)
        
        return agent_id
        
    except Exception as e:
        print(f"❌ Error creating Bedrock Agent: {e}")
        return None

def create_action_group(agent_id, lambda_arn):
    """Create action group for the agent"""
    print("Creating action group...")
    
    bedrock = boto3.client('bedrock-agent')
    
    with open('agent-schema.json', 'r') as f:
        api_schema = json.load(f)
    
    response = bedrock.create_agent_action_group(
        agentId=agent_id,
        agentVersion='DRAFT',
        actionGroupName='weather-actions',
        description='Actions for getting weather information',
        actionGroupExecutor={
            'lambda': lambda_arn
        },
        apiSchema={
            'payload': json.dumps(api_schema)
        }
    )
    
    print("✅ Created action group")

def get_bedrock_agent_role_arn():
    """Get or create Bedrock Agent service role"""
    iam = boto3.client('iam')
    role_name = 'AmazonBedrockExecutionRoleForAgents_weather'
    
    try:
        response = iam.get_role(RoleName=role_name)
        return response['Role']['Arn']
    except iam.exceptions.NoSuchEntityException:
        # Create the role
        trust_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "bedrock.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
        
        response = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy)
        )
        
        # Attach Bedrock agent policy
        policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "bedrock:InvokeModel"
                    ],
                    "Resource": "*"
                },
                {
                    "Effect": "Allow",
                    "Action": [
                        "lambda:InvokeFunction"
                    ],
                    "Resource": "*"
                }
            ]
        }
        
        iam.put_role_policy(
            RoleName=role_name,
            PolicyName='BedrockAgentPolicy',
            PolicyDocument=json.dumps(policy_document)
        )
        
        print(f"✅ Created Bedrock Agent service role: {role_name}")
        return response['Role']['Arn']

def main():
    """Main deployment function"""
    print("🚀 Starting Weather Agent deployment...")
    
    # Get API key from user
    api_key = input("Enter your OpenWeather API key: ")
    
    if not api_key:
        print("❌ API key is required")
        return
    
    try:
        # Step 1: Create deployment package
        create_lambda_deployment_package()
        
        # Step 2: Deploy Lambda function
        lambda_arn = deploy_lambda_function(api_key)
        
        # Step 3: Create Bedrock Agent
        agent_id = create_bedrock_agent(lambda_arn)
        
        if agent_id:
            print(f"\n🎉 Deployment completed successfully!")
            print(f"Agent ID: {agent_id}")
            print(f"You can now test your weather agent in the Bedrock console.")
        else:
            print("❌ Deployment failed")
            
    except Exception as e:
        print(f"❌ Deployment error: {e}")

if __name__ == "__main__":
    main()
