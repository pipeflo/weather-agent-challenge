# Weather Agent Scenario Workshop - Instructor Guide 👨‍🏫

**Workshop Type**: Realistic Development Scenario  
**Duration**: 60 minutes  
**Scenario**: Inheriting incomplete code from departed developer

## Workshop Concept

Participants take on the role of a **new developer** who has inherited an incomplete weather agent project. This mirrors real-world scenarios where developers must:

- Understand existing codebases
- Complete partial implementations
- Work with minimal documentation
- Deploy inherited projects to production

## Pre-Workshop Setup

### Required Materials
- [ ] OpenWeather API keys (one per participant)
- [ ] AWS accounts with AgentCore permissions
- [ ] Repository URL: `https://github.com/pipeflo/weather-agent-scenario.git`
- [ ] Working directory: `weather-agent-scenario/weather-agent/`

### Scenario Setup
The repository contains:
- **Minimal README** - As if left by previous developer
- **Incomplete agent.py** - Basic structure with TODO functions
- **Basic requirements.txt** - Just the essentials
- **No deployment config** - Participants must figure this out

## Workshop Flow

### Opening (5 minutes)

**Set the Scene**:
> "You've just joined a new team and inherited a weather agent project from a developer who left the company. They left behind some basic code but it's incomplete. Your job is to finish it and get it deployed to production.
> 
> You have minimal documentation and need to figure out what's missing. Claude Code will be your development partner to help you understand, complete, and deploy this inherited codebase.
> 
> This is a realistic scenario - you're not building from scratch, you're completing someone else's work."

### Phase 1: Code Archaeology (10 minutes)

**Participant Goal**: Understand the inherited codebase

**What They Should Discover**:
- Basic AgentCore structure is in place
- Three functions need implementation
- Uses Amazon Strands framework
- Needs OpenWeather API integration
- No deployment configuration exists

**Instructor Guidance**:
- Let them explore and ask questions
- Guide them to use Claude Code for analysis
- Help them understand the existing patterns
- Don't give away the solutions

**Common Questions**:
- "What is Amazon Strands?" → Guide them to ask Claude Code
- "How does this AgentCore thing work?" → Let Claude Code explain
- "What exactly needs to be implemented?" → Help them analyze the TODOs

### Phase 2: Requirements Analysis (10 minutes)

**Participant Goal**: Reverse-engineer what needs to be built

**Key Realizations**:
- `extract_city()` needs natural language parsing
- `get_weather()` needs OpenWeather API integration
- `format_response()` needs user-friendly formatting
- Deployment needs AgentCore toolkit configuration

**Instructor Guidance**:
- Help them think like detectives
- Guide them to research the OpenWeather API
- Let Claude Code explain the technical requirements
- Encourage systematic analysis

### Phase 3: Implementation (25 minutes)

**Participant Goal**: Complete the three TODO functions

**Implementation Order**:
1. **City Extraction** (8 minutes)
2. **Weather API Integration** (10 minutes)
3. **Response Formatting** (7 minutes)

**Instructor Monitoring**:
- **City Extraction**: Should use regex or simple string parsing
- **API Integration**: Must handle errors and environment variables
- **Response Formatting**: Should be user-friendly with emojis/formatting

**Common Issues**:
- **Regex complexity**: Guide them to simple patterns first
- **API key setup**: Help with environment variable configuration
- **Error handling**: Ensure they handle API failures gracefully

### Phase 4: Testing (10 minutes)

**Participant Goal**: Test locally before deployment

**Testing Process**:
- Run agent locally on port 8080
- Test with curl commands
- Try various city names and edge cases
- Debug any issues found

**Instructor Support**:
- Help with local testing setup
- Guide debugging of common issues
- Ensure they test edge cases

### Phase 5: Deployment (10 minutes)

**Participant Goal**: Deploy to AgentCore Runtime

**Deployment Steps**:
- Configure AgentCore toolkit
- Set environment variables
- Deploy to AWS
- Test production deployment

**Instructor Assistance**:
- Help with AgentCore toolkit configuration
- Support AWS deployment issues
- Verify successful production testing

## Success Indicators

### Beginner Success (60%):
- Understood the inherited codebase structure
- Implemented basic functionality for all three functions
- Successfully tested locally
- Attempted deployment

### Intermediate Success (80%):
- Completed all functions with proper error handling
- Successfully deployed to AgentCore Runtime
- Tested production deployment
- Understood the full development workflow

### Advanced Success (100%):
- Implemented robust, production-ready code
- Added comprehensive error handling
- Successfully deployed with monitoring
- Demonstrated understanding of inherited code patterns

## Key Teaching Points

### Code Inheritance Reality
- **Real-world scenario**: Developers often inherit incomplete projects
- **Documentation gaps**: Minimal docs are common in real projects
- **Pattern recognition**: Understanding existing code style and architecture
- **Incremental completion**: Building on existing foundations

### Claude Code as Development Partner
- **Code analysis**: Using AI to understand existing codebases
- **Implementation guidance**: Getting help with specific technical challenges
- **Best practices**: Learning proper patterns and error handling
- **Deployment support**: Understanding infrastructure and deployment

### Professional Development Skills
- **Problem solving**: Figuring out requirements from incomplete code
- **Research skills**: Understanding new frameworks and APIs
- **Testing discipline**: Verifying code works before deployment
- **Production mindset**: Deploying real code to real infrastructure

## Troubleshooting Guide

### "I don't understand what Amazon Strands is"
**Response**: "That's exactly what a real developer would face! Ask Claude Code to explain Amazon Strands and how it relates to AgentCore."

### "The previous developer's code doesn't make sense"
**Response**: "Welcome to real development! Use Claude Code to analyze the existing patterns and understand the intended architecture."

### "I don't know what the functions should do"
**Response**: "Look at how they're called in the main function and the TODO comments. Ask Claude Code to help you understand the expected behavior."

### "The API integration is too complex"
**Response**: "Break it down into steps: get the API key, make the request, handle errors, parse the response. Claude Code can guide you through each step."

### "Deployment isn't working"
**Response**: "This is common with inherited projects. Check AWS credentials, verify the AgentCore toolkit is configured, and ensure environment variables are set."

## Assessment Criteria

**Technical Implementation**:
- Correct function implementations
- Proper error handling
- Working API integration
- Successful deployment

**Problem-Solving Approach**:
- Systematic analysis of inherited code
- Effective use of Claude Code for guidance
- Logical implementation sequence
- Proper testing before deployment

**Professional Skills**:
- Understanding of real-world development scenarios
- Ability to work with incomplete documentation
- Effective collaboration with AI development tools
- Production deployment capabilities

## Debrief Questions

1. "How did this scenario compare to starting from scratch?"
2. "What was most challenging about inheriting someone else's code?"
3. "How did Claude Code help you understand the existing codebase?"
4. "What would you do differently if you were the original developer?"
5. "How does this experience prepare you for real development work?"

This scenario-based workshop provides a realistic development experience while teaching Claude Code usage in practical, professional contexts.
