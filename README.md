# The Warden V2 🛡️

> AI-Powered Security Monitoring & Threat Intelligence Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

## 🚧 Status: Under Development

The Warden V2 is a complete architectural redesign focused on:
- **Persistent Memory**: Redis-backed investigation context
- **Multi-Agent Architecture**: Specialized agents for different security tasks
- **Modular Design**: Easy to extend with new threat intel sources
- **100% Open Source**: No vendor lock-in

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Orchestrator                         │
├─────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐ │
│  │ Threat   │  │   Log    │  │ Incident │  │ Report  │ │
│  │ Analyzer │  │Investig. │  │Responder │  │Generator│ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬────┘ │
├───────┴──────────────┴─────────────┴──────────────┴─────┤
│              Memory Manager (Redis)                     │
├─────────────────────────────────────────────────────────┤
│  MCP Servers: AbuseIP | ThreatFox | Elastic | Custom   │
└─────────────────────────────────────────────────────────┘
```

## 📋 Roadmap

### Phase 1: Foundation ✅ (In Progress)
- [x] Directory structure setup
- [ ] Base classes implementation
- [ ] Redis memory store
- [ ] LangGraph/LangChain integration
- [ ] First MCP server migration

### Phase 2: Core Features (Week 3-4)
- [ ] Investigation memory manager
- [ ] Threat analyzer agent
- [ ] Report builder with templates
- [ ] Migrate all legacy MCP servers

### Phase 3: Enhancement (Week 5-6)
- [ ] Additional specialized agents
- [ ] Workflow orchestration
- [ ] REST API (FastAPI)
- [ ] New threat intel integrations

### Phase 4: Production (Week 7-8)
- [ ] Docker containerization
- [ ] Observability (LangFuse)
- [ ] Performance optimization
- [ ] Comprehensive documentation

## 🚀 Quick Start (Coming Soon)

```bash
# Clone the repository
git clone https://github.com/yourusername/the-warden-v2.git
cd the-warden-v2

# Install dependencies
pip install -r requirements.txt

# Set up Redis
docker-compose up -d redis

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Run The Warden
python main.py
```

## 🛠️ Technology Stack

**Framework & Orchestration:**
- [LangChain](https://github.com/langchain-ai/langchain) - LLM framework
- [LangGraph](https://github.com/langchain-ai/langgraph) - Stateful agent orchestration
- [FastAPI](https://fastapi.tiangolo.com/) - REST API

**LLM & Intelligence:**
- [Ollama](https://ollama.ai/) - Local LLM inference
- Multiple threat intel sources via MCP

**Data & Memory:**
- [Redis](https://redis.io/) - Memory store
- [Elasticsearch](https://www.elastic.co/) - Log storage
- [Pydantic](https://docs.pydantic.dev/) - Data validation

**Observability:**
- [LangFuse](https://langfuse.com/) - Open source LLM monitoring

## 📚 Documentation

- [Architecture Overview](docs/architecture.md)
- [API Reference](docs/api_reference.md)
- [Workflow Guide](docs/workflows.md)
- [Deployment Guide](docs/deployment.md)

## 🤝 Contributing

Contributions are welcome! This project is in active development.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- [Legacy Version (V1)](https://github.com/yourusername/the-warden-v1)
- [Documentation](https://warden-docs.example.com)
- [Issue Tracker](https://github.com/yourusername/the-warden-v2/issues)

## ⚠️ Disclaimer

The Warden is a security tool intended for authorized security monitoring only. 
Users are responsible for compliance with applicable laws and regulations.

---

**Note:** This is V2 - a complete rewrite. For the legacy version, see [the-warden-v1](https://github.com/Dannychz7/the_warden).
