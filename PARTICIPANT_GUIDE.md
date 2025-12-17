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

### Step 1: Initialize Claude Code Project (5 minutes)

```bash
git clone https://github.com/pipeflo/weather-agent-scenario.git
cd weather-agent-scenario/weather-agent
claude
```

**Initialize Project Memory**:
```
/init
```

This creates a `CLAUDE.md` file that helps Claude Code understand your project context and maintain memory across sessions.

### Step 2: Configure MCP Servers (10 minutes)

**Configure the recommended MCP servers** to enhance Claude Code's capabilities:

**AgentCore MCP Server**:
- Repository: https://github.com/awslabs/mcp/tree/main/src/amazon-bedrock-agentcore-mcp-server
- Provides AgentCore deployment and management capabilities

**Strands MCP Server**:
- Repository: https://github.com/strands-agents/mcp-server  
- Provides Strands agents framework integration

**Your Task**: Ask Claude Code to help you configure these MCP servers for enhanced development capabilities.

### Step 3: Code Review and Analysis (10 minutes)

**Ask Claude Code to review the existing codebase**:

**Your Approach**:
- Have Claude Code analyze the current implementation
- Understand what's already built vs what's missing
- Identify the architecture and framework being used
- Get recommendations for completion strategy

**Key Areas to Review**:
- Current Strands and AgentCore integration
- Tool definitions and structure
- Missing functionality in weather and calculator tools
- Deployment configuration needs

### Step 4: Complete the Implementation (15 minutes)

**Ask Claude Code to finish the incomplete code**:

**Your Task**: Work with Claude Code to complete all missing functionality:
- Weather API integration with proper error handling
- Calculator tool implementation with safety checks
- Strands agent configuration and tool integration
- AgentCore entrypoint optimization

**Implementation Focus**:
- Follow existing code patterns and style
- Ensure proper tool integration with Strands framework
- Add comprehensive error handling
- Maintain production-ready code quality

### Step 5: Create Local AgentCore Environment (10 minutes)

**Ask Claude Code to set up local testing environment**:

**Your Task**: Have Claude Code help you create a local AgentCore environment for testing:
- Set up the necessary dependencies
- Configure environment variables (API keys)
- Prepare local testing infrastructure
- Ensure proper AgentCore simulation

### Step 6: Local Testing and Validation (10 minutes)

**Test your completed agent locally**:

**Testing Strategy**:
- Test weather functionality with various cities
- Test calculator functionality with different expressions
- Test combined requests (weather + calculations)
- Verify error handling for edge cases

**Testing Commands**:
```bash
# Start agent locally
python agent.py

# Test weather functionality
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What'\''s the weather in London?"}'

# Test calculator functionality  
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Calculate 25 * 4 + 10"}'
```

## Success Criteria

Your completed weather agent should:

✅ **Initialize properly** - CLAUDE.md file created and MCP servers configured  
✅ **Code review complete** - Understanding of existing architecture and gaps  
✅ **Implementation finished** - All tools working with proper Strands integration  
✅ **Local environment ready** - AgentCore testing environment configured  
✅ **Testing successful** - Both weather and calculator tools working locally  
✅ **Production ready** - Code ready for AgentCore Runtime deployment  

## Development Philosophy

**You're working with Claude Code as your development partner**:

- **Initialize first** - Set up project memory and MCP servers for enhanced capabilities
- **Review before coding** - Understand the existing architecture thoroughly
- **Collaborate on implementation** - Let Claude Code guide the completion process
- **Test systematically** - Verify each component works before moving forward
- **Use MCP capabilities** - Leverage the configured servers for better development experience

## Key Learning Objectives

1. **Claude Code Project Setup** - Using /init and MCP server configuration
2. **Code Archaeology with AI** - Understanding inherited codebases with Claude Code
3. **Collaborative Development** - Working with Claude Code to complete implementations
4. **Strands Framework Mastery** - Understanding modern AWS agent development
5. **Local Testing Strategies** - Setting up and using local AgentCore environments

## Time Management

- **0-5 min**: Initialize Claude Code project with /init
- **5-15 min**: Configure MCP servers for enhanced capabilities
- **15-25 min**: Code review and architecture analysis
- **25-40 min**: Complete implementation with Claude Code
- **40-50 min**: Set up local AgentCore testing environment
- **50-60 min**: Test and validate completed agent

## Getting Help

Use Claude Code as your primary development partner:

- "Help me configure the AgentCore and Strands MCP servers"
- "Review this inherited codebase and explain what needs to be completed"
- "Complete the missing weather and calculator tool implementations"
- "Set up a local AgentCore environment for testing"
- "Help me test the agent functionality locally"

## Important Notes

- This uses **real Claude Code features** with MCP server integration
- **Project memory** persists through the CLAUDE.md file
- **MCP servers** provide enhanced development capabilities
- **Local testing** simulates the AgentCore Runtime environment
- **Collaborative approach** leverages Claude Code's full potential

Remember: You're not just completing code - you're learning to work effectively with Claude Code as your development partner in realistic scenarios! 🚀
