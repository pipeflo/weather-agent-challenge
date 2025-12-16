# Weather Agent Challenge - Claude Code Workshop 🌤️

Welcome to the Claude Code Challenge! In this 30-45 minute workshop, you'll build and deploy a production-ready weather agent using **Amazon Bedrock AgentCore** while leveraging **Claude Code's unique agentic features**.

## What Makes This Workshop Special

This workshop is designed to showcase **Claude Code's specific capabilities**:

- **Plan Mode** - Safe code analysis and step-by-step planning
- **Auto Edit Mode** - Automated file modifications with approval
- **MCP Integration** - Model Context Protocol for external tool access
- **Subagents** - Specialized AI assistants for specific tasks
- **Slash Commands** - Custom workflows and shortcuts
- **Memory System** - Project and user context persistence
- **Hooks** - Automated reactions to development lifecycle events

## Workshop Architecture

You'll build a real production system using:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Claude Code   │───▶│  AgentCore       │───▶│  Weather Agent  │
│   (Terminal)    │    │  Runtime         │    │  (Container)    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
        │                       │
        ▼                       ▼
┌─────────────────┐    ┌──────────────────┐
│   Plan Mode     │    │  Session         │
│   Subagents     │    │  Management      │
│   MCP Tools     │    │  (8hr lifetime)  │
└─────────────────┘    └──────────────────┘
```

## Prerequisites

- **Claude Code installed** - `curl -fsSL https://claude.ai/install.sh | bash`
- AWS CLI configured with AgentCore permissions
- Python 3.10+ installed
- OpenWeather API key (provided during workshop)

## Challenge Overview

You'll complete an **incomplete weather agent** while learning to use:

1. **Claude Code's Plan Mode** - Analyze and plan implementation safely
2. **Subagents** - Create specialized assistants for different tasks
3. **Slash Commands** - Build custom workflows for deployment
4. **MCP Integration** - Connect to external APIs and tools
5. **Memory System** - Maintain project context and preferences
6. **AgentCore Runtime** - Deploy to real AWS infrastructure

## Getting Started

### Step 1: Initialize with Claude Code (5 minutes)

```bash
git clone https://github.com/pipeflo/weather-agent-challenge.git
cd weather-agent-challenge
claude
```

**🎯 Your Task**: Use Claude Code to explore the project and understand what needs to be built.

**Claude Code Features to Use**:
- **Plan Mode**: `Let's use plan mode to analyze this codebase and understand the AgentCore architecture`
- **Context Commands**: `/context` to see current project context
- **File Analysis**: Let Claude Code read and understand the project structure

### Step 2: Leverage Plan Mode for Architecture Understanding (10 minutes)

**🎯 Your Task**: Use Claude Code's Plan Mode to safely explore and understand the AgentCore implementation.

**Key Areas to Explore with Plan Mode**:
- How does the `BedrockAgentCoreApp` work?
- What's the HTTP protocol structure for AgentCore?
- How do sessions and containers work?
- What needs to be implemented in the weather agent?

**Claude Code Approach**:
- Ask Claude Code to enter Plan Mode for safe analysis
- Let it create a step-by-step implementation plan
- Review and refine the plan before any code changes

### Step 3: Create Specialized Subagents (10 minutes)

**🎯 Your Task**: Use Claude Code's subagent feature to create specialized assistants.

**Subagents to Create**:
- **Weather API Subagent** - Specialized in OpenWeather API integration
- **AgentCore Deployment Subagent** - Expert in AgentCore toolkit usage
- **Testing Subagent** - Focused on local and production testing

**Claude Code Features**:
- Create subagents with specific expertise
- Use subagents for parallel development tasks
- Leverage subagent memory for specialized knowledge

### Step 4: Implement with Auto Edit Mode (15 minutes)

**🎯 Your Task**: Use Claude Code's Auto Edit mode to implement the weather agent functionality.

**Implementation Areas**:
- **Message Parsing** - Extract cities from user input
- **API Integration** - OpenWeather API calls with error handling
- **Response Formatting** - User-friendly weather responses
- **AgentCore Protocol** - Proper HTTP request/response handling

**Claude Code Features to Use**:
- **Auto Edit Mode** - Let Claude Code modify files with your approval
- **Memory System** - Store coding preferences and patterns
- **Context Management** - Maintain awareness of the full project

### Step 5: Build Custom Slash Commands (10 minutes)

**🎯 Your Task**: Create custom slash commands for your development workflow.

**Slash Commands to Build**:
- `/weather-test` - Test the weather API integration
- `/deploy-agent` - Deploy to AgentCore Runtime
- `/check-logs` - View CloudWatch logs
- `/session-test` - Test session management

**Claude Code Capabilities**:
- Create reusable workflow commands
- Automate repetitive development tasks
- Build project-specific shortcuts

### Step 6: Deploy with MCP Integration (10 minutes)

**🎯 Your Task**: Use Claude Code's MCP (Model Context Protocol) to integrate with AWS services.

**MCP Integration Areas**:
- **AWS CLI Integration** - Direct AWS service interaction
- **CloudWatch Access** - Real-time log monitoring
- **AgentCore Toolkit** - Seamless deployment workflow
- **Environment Management** - API key and configuration handling

**Claude Code MCP Features**:
- Connect to external tools and APIs
- Automate AWS resource management
- Monitor deployment status in real-time

## Success Criteria

Your weather agent should demonstrate:

✅ **Plan Mode Usage** - Safe analysis and implementation planning  
✅ **Subagent Creation** - Specialized assistants for different tasks  
✅ **Slash Commands** - Custom workflow automation  
✅ **MCP Integration** - External tool and API connectivity  
✅ **Memory System** - Persistent project context  
✅ **AgentCore Deployment** - Production-ready container deployment  
✅ **Session Management** - Stateful conversation handling  

## Key Learning Objectives

1. **Claude Code Mastery** - Plan Mode, subagents, slash commands, MCP
2. **Agentic Development** - Let Claude Code handle complex workflows
3. **AgentCore Architecture** - Container-based AI agent deployment
4. **Production Deployment** - Real AWS infrastructure usage
5. **Context Management** - Memory systems and project persistence

## Workshop Philosophy

This workshop emphasizes **Claude Code's unique agentic capabilities**:

- **Plan First** - Use Plan Mode to understand before implementing
- **Specialize** - Create subagents for different aspects of development
- **Automate** - Build slash commands for repetitive tasks
- **Connect** - Use MCP to integrate with external tools
- **Remember** - Leverage memory systems for context persistence
- **Deploy** - Use real AWS infrastructure for production deployment

## Files in This Repository

- `agent.py` - Main AgentCore application (needs completion)
- `requirements.txt` - Python dependencies for AgentCore
- `.claude/` - Claude Code configuration and memory files
- `slash-commands/` - Custom workflow commands
- `subagents/` - Specialized assistant configurations
- `test_agent.py` - Testing utilities with MCP integration

## Time Management

- **0-5 min**: Initialize with Claude Code and explore
- **5-15 min**: Use Plan Mode for architecture understanding
- **15-25 min**: Create subagents for specialized tasks
- **25-40 min**: Implement with Auto Edit Mode
- **40-50 min**: Build custom slash commands
- **50-60 min**: Deploy with MCP integration

## Claude Code Specific Features to Master

### Plan Mode
- Safe code analysis without modifications
- Step-by-step implementation planning
- Risk-free exploration of complex codebases

### Subagents
- Specialized AI assistants for specific domains
- Parallel task execution with isolated contexts
- Expert knowledge for different aspects of development

### Slash Commands
- Custom workflow automation
- Repeatable development tasks
- Project-specific shortcuts and utilities

### MCP (Model Context Protocol)
- External tool and API integration
- Real-time system monitoring
- Automated resource management

### Memory System
- Project-wide context persistence
- User preference storage
- Team knowledge sharing

## Important Notes

- This uses **real Claude Code features** - not simulations
- Your agent deploys to **real AWS AgentCore Runtime**
- **Plan Mode** ensures safe exploration and implementation
- **Subagents** provide specialized expertise for complex tasks
- **MCP integration** connects to real AWS services
- **Memory systems** persist knowledge across sessions

## Getting Help

Use Claude Code's full feature set! Try commands like:

- `Let's use plan mode to understand this AgentCore implementation`
- `Create a subagent specialized in OpenWeather API integration`
- `Build a slash command for deploying to AgentCore Runtime`
- `Use MCP to connect to AWS CloudWatch for log monitoring`
- `Store our coding preferences in the project memory`

Remember: This workshop showcases Claude Code's unique agentic capabilities - use them to build a production-ready weather agent! 🚀
