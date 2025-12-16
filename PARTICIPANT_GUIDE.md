# Weather Agent Workshop - Claude Code Mastery Guide 🌤️

**Duration**: 45-60 minutes  
**Goal**: Master Claude Code's agentic features while building a production weather agent

## What Makes This Workshop Unique

This workshop is specifically designed to showcase **Claude Code's advanced agentic capabilities**:

- **Plan Mode** - Safe code analysis and implementation planning
- **Subagents** - Specialized AI assistants for different tasks  
- **Slash Commands** - Custom workflow automation
- **MCP Integration** - Model Context Protocol for external tools
- **Memory System** - Persistent project and user context
- **Auto Edit Mode** - Automated file modifications with approval

## Workshop Philosophy

**Learn Claude Code's agentic approach** - Don't just code, orchestrate AI agents to handle complex development workflows.

## Getting Started

### Step 1: Initialize Claude Code Session (5 minutes)

```bash
git clone https://github.com/pipeflo/weather-agent-challenge.git
cd weather-agent-challenge
claude
```

**🎯 Task**: Start your Claude Code session and explore the project.

**Claude Code Features to Try**:
- Use `/context` to see current project awareness
- Let Claude Code read and understand the project structure
- Ask about the `.claude/` directory and project memory

**Key Questions**:
- What does Claude Code understand about this project?
- How does the memory system work?
- What AgentCore concepts does it recognize?

### Step 2: Master Plan Mode (10 minutes)

**🎯 Task**: Use Claude Code's Plan Mode to safely analyze and plan the implementation.

**Plan Mode Approach**:
- Ask Claude Code to enter Plan Mode for the weather agent
- Let it analyze the AgentCore architecture without making changes
- Review the step-by-step implementation plan it creates
- Refine the plan based on your understanding

**Key Learning**:
- How Plan Mode prevents accidental changes
- How Claude Code breaks down complex implementations
- How to review and approve plans before execution

**Example Interaction**:
> "Let's use plan mode to analyze this weather agent project and create a comprehensive implementation plan for AgentCore deployment"

### Step 3: Create Specialized Subagents (15 minutes)

**🎯 Task**: Use Claude Code's subagent feature to create specialized assistants.

**Subagents to Create**:
1. **Weather API Expert** - OpenWeather integration specialist
2. **AgentCore Deployment Expert** - AWS deployment specialist  
3. **Testing Specialist** - Local and production testing expert

**Subagent Approach**:
- Ask Claude Code to create subagents with specific expertise
- Configure each subagent's knowledge domain
- Use subagents for parallel development tasks
- Let subagents handle their specialized areas

**Key Learning**:
- How subagents provide specialized expertise
- How to configure subagent knowledge domains
- How to coordinate multiple subagents for complex tasks

**Example Interaction**:
> "Create a subagent specialized in OpenWeather API integration. It should be an expert in weather data parsing, error handling, and API best practices."

### Step 4: Implement with Auto Edit Mode (15 minutes)

**🎯 Task**: Use Claude Code's Auto Edit Mode to implement the weather agent functionality.

**Implementation Areas**:
- Message parsing and city extraction
- OpenWeather API integration with error handling
- Response formatting for user-friendly output
- AgentCore HTTP protocol compliance

**Auto Edit Approach**:
- Let Claude Code propose file modifications
- Review changes before approval
- Use the weather API subagent for API-specific code
- Use the deployment subagent for AgentCore-specific code

**Key Learning**:
- How Auto Edit Mode works with approval workflows
- How to coordinate subagents for implementation
- How to maintain code quality with AI assistance

**Example Interaction**:
> "Use auto edit mode with the weather API subagent to implement the OpenWeather integration in agent.py. Make sure to include proper error handling and response formatting."

### Step 5: Build Custom Slash Commands (10 minutes)

**🎯 Task**: Create custom slash commands for your development workflow.

**Slash Commands to Build**:
- `/weather-test` - Test weather API integration
- `/deploy-agent` - Deploy to AgentCore Runtime
- `/check-logs` - View CloudWatch logs
- `/session-test` - Test session management

**Slash Command Approach**:
- Ask Claude Code to create reusable workflow commands
- Configure commands for your specific project needs
- Test commands to ensure they work correctly
- Document command usage and parameters

**Key Learning**:
- How to create custom workflow automation
- How to build project-specific shortcuts
- How to make development tasks repeatable

**Example Interaction**:
> "Create a slash command called /weather-test that tests our weather API integration locally. It should check the API key, test different cities, and validate response formats."

### Step 6: Deploy with MCP Integration (10 minutes)

**🎯 Task**: Use Claude Code's MCP (Model Context Protocol) to integrate with AWS services.

**MCP Integration Areas**:
- AWS CLI for service interaction
- CloudWatch for log monitoring  
- AgentCore toolkit for deployment
- Environment management for configuration

**MCP Approach**:
- Let Claude Code connect to external AWS tools
- Use MCP for real-time deployment monitoring
- Integrate with CloudWatch for log analysis
- Automate AWS resource management

**Key Learning**:
- How MCP connects Claude Code to external tools
- How to monitor deployments in real-time
- How to automate AWS service interactions

**Example Interaction**:
> "Use MCP to connect to AWS services and deploy our weather agent to AgentCore Runtime. Monitor the deployment progress and check CloudWatch logs automatically."

## Success Criteria

Demonstrate mastery of Claude Code's agentic features:

✅ **Plan Mode Mastery** - Safe analysis and implementation planning  
✅ **Subagent Creation** - Specialized assistants for different domains  
✅ **Slash Command Automation** - Custom workflow commands  
✅ **MCP Integration** - External tool connectivity  
✅ **Memory System Usage** - Persistent context management  
✅ **Auto Edit Coordination** - AI-assisted implementation  
✅ **Production Deployment** - Real AgentCore Runtime deployment  

## Key Learning Objectives

1. **Agentic Development** - Orchestrate AI agents instead of manual coding
2. **Plan-First Approach** - Use Plan Mode for safe exploration
3. **Specialization** - Create expert subagents for complex domains
4. **Workflow Automation** - Build custom slash commands
5. **External Integration** - Use MCP for tool connectivity
6. **Context Persistence** - Leverage memory systems effectively

## Claude Code Feature Deep Dive

### Plan Mode Benefits
- **Risk-free exploration** of complex codebases
- **Step-by-step planning** before implementation
- **Safe analysis** without accidental modifications
- **Collaborative planning** with review and refinement

### Subagent Advantages  
- **Specialized expertise** for different domains
- **Parallel task execution** with isolated contexts
- **Consistent knowledge** across development sessions
- **Expert-level assistance** for complex topics

### Slash Command Power
- **Workflow automation** for repetitive tasks
- **Project-specific shortcuts** for common operations
- **Consistent execution** of complex procedures
- **Team knowledge sharing** through reusable commands

### MCP Integration Benefits
- **External tool connectivity** beyond code editing
- **Real-time monitoring** of deployments and services
- **Automated resource management** for cloud services
- **Seamless workflow integration** with existing tools

## Time Management

- **0-5 min**: Initialize Claude Code and explore project
- **5-15 min**: Master Plan Mode for safe analysis
- **15-30 min**: Create and configure specialized subagents
- **30-45 min**: Implement with Auto Edit Mode coordination
- **45-55 min**: Build custom slash commands for workflow
- **55-65 min**: Deploy with MCP integration and monitoring

## Workshop Success Indicators

**Beginner Level**:
- Successfully used Plan Mode for project analysis
- Created at least one specialized subagent
- Built a basic slash command for testing

**Intermediate Level**:
- Coordinated multiple subagents for implementation
- Created comprehensive slash commands for workflow
- Used MCP for basic AWS integration

**Advanced Level**:
- Mastered all Claude Code agentic features
- Built a complete automated workflow
- Successfully deployed to production with monitoring

## Important Notes

- This workshop focuses on **Claude Code's unique capabilities**
- **Plan Mode** ensures safe exploration and learning
- **Subagents** provide expert-level assistance
- **MCP integration** connects to real AWS services
- **Memory systems** persist knowledge across sessions

## Getting Help

Use Claude Code's full agentic capabilities! Try interactions like:

- "Enter plan mode and analyze this AgentCore implementation"
- "Create a subagent specialized in weather API integration"  
- "Build a slash command for automated deployment"
- "Use MCP to monitor our CloudWatch logs in real-time"
- "Store our project preferences in the memory system"

Remember: This workshop is about mastering Claude Code's agentic features while building a real production system! 🚀
