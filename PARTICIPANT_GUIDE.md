# Weather Agent Completion Challenge 🌤️

**Scenario**: You've just joined the team and inherited a partially completed weather agent from a developer who left the company. Your task is to finish the implementation and deploy it to production using Claude Code as your development partner.

**Duration**: 45-60 minutes  
**Your Role**: New developer taking over an incomplete project

## The Situation

The previous developer left behind:
- ✅ Basic project structure with AgentCore setup
- ✅ Main entry point and flow logic
- ❌ Incomplete API integration
- ❌ Missing city parsing logic  
- ❌ No response formatting
- ❌ No deployment configuration
- ❌ Minimal documentation

**Your Mission**: Complete the weather agent and get it deployed to production.

## Getting Started

### Step 1: Assess the Inherited Codebase (10 minutes)

```bash
git clone https://github.com/pipeflo/weather-agent-challenge.git
cd weather-agent-challenge/weather-agent
claude
```

**Your First Task**: Use Claude Code to understand what you've inherited.

**Approach**:
- Ask Claude Code to analyze the existing codebase
- Understand what's implemented vs what's missing
- Identify the architecture and framework being used
- Plan your completion strategy

**Key Questions to Explore**:
- What is this Amazon Strands framework?
- How does AgentCore deployment work?
- What exactly needs to be implemented?
- What's the overall architecture and flow?

### Step 2: Understand the Requirements (10 minutes)

**Your Task**: Use Claude Code to help you reverse-engineer the requirements from the incomplete code.

**Investigation Areas**:
- What should the `extract_city()` function do?
- How should the OpenWeather API integration work?
- What format should the weather response have?
- How does AgentCore deployment work?

**Claude Code Approach**:
- Ask about Amazon Strands and AgentCore
- Research the OpenWeather API structure
- Understand the expected user interaction flow
- Plan the implementation approach

### Step 3: Implement Missing Functionality (20 minutes)

**Your Task**: Complete the three TODO functions using Claude Code's assistance.

**Implementation Priority**:
1. **City Extraction** - Parse city names from user messages
2. **Weather API** - Integrate with OpenWeather API
3. **Response Formatting** - Create user-friendly responses

**Development Approach**:
- Use Claude Code to implement each function
- Test each piece as you build it
- Handle edge cases and errors
- Follow the existing code patterns

**Key Implementation Areas**:
- Natural language processing for city extraction
- HTTP API calls with proper error handling
- User-friendly response formatting with weather data

### Step 4: Local Testing and Debugging (10 minutes)

**Your Task**: Test your implementation locally before deployment.

**Testing Strategy**:
- Run the agent locally on port 8080
- Test with various user inputs
- Verify API integration works
- Debug any issues found

**Testing Commands**:
```bash
# Start agent locally
python agent.py

# Test with curl (in another terminal)
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What'\''s the weather in London?"}'
```

### Step 5: Deploy to Production (10 minutes)

**Your Task**: Deploy the completed agent to AgentCore Runtime.

**Deployment Process**:
- Configure the AgentCore toolkit
- Set up environment variables (API key)
- Deploy to AWS infrastructure
- Test the production deployment

**Deployment Commands**:
```bash
# Configure deployment
agentcore configure -e agent.py

# Deploy to AgentCore Runtime
agentcore launch

# Test deployed agent
agentcore invoke '{"prompt": "weather in Paris"}'
```

## Success Criteria

Your completed weather agent should:

✅ **Parse user requests** - Extract city names from natural language  
✅ **Call weather API** - Successfully fetch data from OpenWeather  
✅ **Format responses** - Provide user-friendly weather information  
✅ **Handle errors** - Gracefully manage API failures and invalid inputs  
✅ **Deploy successfully** - Run in AgentCore Runtime on AWS  
✅ **Work in production** - Respond to real user queries  

## Development Philosophy

**You're not starting from scratch** - you're completing someone else's work:

- **Understand first** - Figure out what the previous developer intended
- **Follow patterns** - Maintain consistency with existing code style
- **Complete systematically** - Implement one function at a time
- **Test incrementally** - Verify each piece works before moving on
- **Use Claude Code extensively** - It's your primary development partner

## Key Learning Objectives

1. **Code Archaeology** - Understanding and completing inherited codebases
2. **Claude Code Partnership** - Using AI as your development companion
3. **API Integration** - Working with external weather services
4. **Production Deployment** - Getting code running on real AWS infrastructure
5. **Problem Solving** - Figuring out requirements from incomplete implementations

## Common Challenges

**Challenge**: Understanding the existing architecture
**Approach**: Ask Claude Code to explain Amazon Strands and AgentCore concepts

**Challenge**: Implementing natural language parsing
**Approach**: Use Claude Code to suggest regex patterns or simple parsing logic

**Challenge**: API integration complexity
**Approach**: Let Claude Code guide you through the OpenWeather API structure

**Challenge**: Deployment configuration
**Approach**: Use Claude Code to understand AgentCore toolkit usage

## Time Management

- **0-10 min**: Analyze inherited codebase with Claude Code
- **10-20 min**: Understand requirements and plan implementation
- **20-40 min**: Complete the three TODO functions
- **40-50 min**: Test locally and debug issues
- **50-60 min**: Deploy to production and verify

## Getting Help

Use Claude Code as your development partner throughout:

- "Help me understand this inherited codebase and what needs to be completed"
- "What is Amazon Strands and how does it work with AgentCore?"
- "How should I implement the city extraction from user messages?"
- "Guide me through integrating with the OpenWeather API"
- "Help me format the weather response in a user-friendly way"
- "How do I deploy this to AgentCore Runtime?"

## Important Notes

- This is a **realistic development scenario** - you're completing real work
- The previous developer's code **follows good patterns** - maintain consistency
- **Claude Code is your pair programming partner** - use it extensively
- **Test locally first** - don't deploy broken code to production
- **Production deployment** uses real AWS infrastructure

Remember: You're stepping into a real developer's shoes - use Claude Code to help you understand, complete, and deploy professional-quality code! 🚀
