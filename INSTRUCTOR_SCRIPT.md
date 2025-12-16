# Weather Agent Workshop - Instructor Guide 👨‍🏫

**Duration**: 45 minutes  
**Prerequisites**: Participants completed Claude Code workshop labs

## Workshop Objectives

By the end of this workshop, participants will:
- Understand **Amazon Bedrock AgentCore** architecture and concepts
- Build agents using the **AgentCore Runtime** environment
- Implement **HTTP protocol contracts** for AgentCore
- Deploy agents to **real AWS infrastructure** using containers
- Use **Claude Code effectively** for exploration and implementation

## Pre-Workshop Setup

### Required Materials
- [ ] OpenWeather API keys (one per participant)
- [ ] AWS accounts with AgentCore permissions
- [ ] Repository URL: `https://github.com/pipeflo/weather-agent-challenge.git`

### AWS Permissions Required
Participants need permissions for:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:*",
                "ecr:*",
                "codebuild:*",
                "iam:CreateRole",
                "iam:AttachRolePolicy",
                "iam:PutRolePolicy",
                "logs:*"
            ],
            "Resource": "*"
        }
    ]
}
```

### Environment Verification
- [ ] AgentCore Starter Toolkit access
- [ ] Python 3.10+ available
- [ ] AWS CLI configured
- [ ] Model access: Anthropic Claude enabled in Bedrock

## Workshop Flow

### Opening (5 minutes)

**Key Messages**:
> "Today you'll build a production-ready weather agent using Amazon Bedrock AgentCore - AWS's new platform for deploying AI agents at scale.
> 
> This isn't a simulation - you'll deploy to real AWS infrastructure using containers, sessions, and automatic scaling.
> 
> You'll use Claude Code as your development partner to explore, implement, and deploy. The workshop provides guidance, not exact steps - you'll learn by doing."

**Distribute**:
- OpenWeather API keys
- Repository URL
- AWS account details

### Phase 1: Environment & Architecture (10 minutes)

**Circulate and observe**:
- Are participants cloning and exploring the repository?
- Are they asking Claude Code about AgentCore concepts?
- Do they understand the difference from Lambda/traditional deployment?

**Common questions to guide them toward**:
- "What is AgentCore Runtime?"
- "How do sessions work?"
- "What's the HTTP protocol structure?"
- "How does containerized deployment work?"

**If participants are stuck**: Guide them to ask Claude Code conceptual questions about AgentCore architecture.

### Phase 2: Implementation (20 minutes)

**Key implementation areas to monitor**:
1. **Message parsing** - extracting cities from user input
2. **API integration** - calling OpenWeather with error handling
3. **Response formatting** - creating user-friendly responses
4. **HTTP protocol** - proper AgentCore request/response format

**Circulate and help with**:
- Understanding the `BedrockAgentCoreApp` structure
- Implementing the missing functions in `agent.py`
- Debugging local testing issues
- Understanding session management concepts

**Common issues**:
- **Port 8080 conflicts**: Help them find and kill conflicting processes
- **API key setup**: Ensure environment variables are set correctly
- **HTTP format confusion**: Guide them to understand AgentCore's protocol
- **Missing dependencies**: Help with pip install issues

### Phase 3: Deployment (10 minutes)

**Monitor deployment process**:
- AgentCore toolkit installation
- Container build process
- AWS resource creation
- Endpoint configuration

**Common deployment issues**:
- **AWS permissions**: Verify IAM policies
- **Toolkit configuration**: Help with `agentcore configure`
- **Container build failures**: Check CodeBuild logs
- **Environment variables**: Ensure API keys are set in deployment

**Success indicators**:
- Agent ARN is generated
- CloudWatch logs are created
- Test invocations work

## Teaching Philosophy

### Guided Discovery Approach
- **Don't give exact answers** - guide participants to ask Claude Code
- **Focus on concepts** - help them understand AgentCore architecture
- **Encourage exploration** - let them discover implementation details
- **Support debugging** - help them troubleshoot with Claude Code

### Key Concepts to Reinforce

1. **AgentCore vs Lambda**:
   - Containers vs functions
   - Session persistence vs stateless
   - 8-hour runtime vs 15-minute limit

2. **Production Architecture**:
   - Real AWS infrastructure
   - Automatic scaling
   - Built-in observability

3. **Development Workflow**:
   - Local testing first
   - Container deployment
   - Version management

## Assessment Checkpoints

### 15-minute mark:
- [ ] Environment set up
- [ ] AgentCore concepts understood
- [ ] Local agent running

### 30-minute mark:
- [ ] Weather functions implemented
- [ ] Local testing successful
- [ ] Ready for deployment

### 45-minute mark:
- [ ] Agent deployed to AgentCore
- [ ] Production testing successful
- [ ] Understanding of full workflow

## Success Metrics

**Excellent** (80%+ participants):
- Complete implementation and deployment
- Understanding of AgentCore architecture
- Successful production testing

**Good** (60%+ participants):
- Working local implementation
- Attempted deployment
- Basic understanding of concepts

**Needs Improvement** (<60%):
- Review Claude Code usage patterns
- Additional AgentCore concept explanation

## Debrief Questions (5 minutes)

1. "How does AgentCore Runtime differ from what you've used before?"
2. "What advantages does the session model provide?"
3. "How would you extend this agent for production use?"
4. "What did you learn about containerized agent deployment?"
5. "How did Claude Code help you understand the architecture?"

## Follow-up Activities

**Immediate extensions**:
- Add weather forecasts (not just current weather)
- Implement conversation memory across sessions
- Add support for multiple cities in one request

**Advanced projects**:
- Multi-agent weather system
- Integration with other AWS services
- Custom observability dashboards

## Troubleshooting Guide

### Environment Issues
- **Python version**: Ensure 3.10+
- **AWS credentials**: Verify with `aws sts get-caller-identity`
- **Toolkit installation**: `pip install bedrock-agentcore-starter-toolkit`

### Implementation Issues
- **HTTP protocol**: Guide to AgentCore documentation
- **API integration**: Help with requests and error handling
- **Local testing**: Port conflicts and curl commands

### Deployment Issues
- **Permissions**: Check IAM policies
- **Container builds**: Review CodeBuild logs
- **Resource creation**: Verify in AWS console

## Key Takeaways

Participants should leave understanding:
- **AgentCore architecture** and how it differs from serverless functions
- **Container-based deployment** for AI agents
- **Session management** in production environments
- **Real AWS infrastructure** usage for agent hosting
- **Claude Code as a development partner** for complex implementations

The workshop emphasizes **learning by doing** with **real infrastructure** rather than simulations or toy examples.
