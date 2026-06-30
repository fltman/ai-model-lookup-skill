# AI Model Lookup Skill for Claude Code

[![Support me on Patreon](https://img.shields.io/badge/Patreon-Support%20my%20work-FF424D?style=flat&logo=patreon&logoColor=white)](https://www.patreon.com/AndersBjarby)

Keep Claude Code updated on the latest AI models from all major providers.

## The Problem

Claude's knowledge has a cutoff date. When building integrations with AI services (image generation, text APIs, etc.), you need current information about available models, their capabilities, and API formats.

## The Solution

This skill triggers proactively when you're building AI integrations. It fetches the latest model information from OpenRouter's API, which aggregates models from:

- OpenAI (GPT-4, DALL-E, Whisper)
- Anthropic (Claude)
- Google (Gemini, Imagen)
- Meta (Llama)
- Mistral
- Stability AI
- And many more...

## Installation

### Per-Project Installation

```bash
# Clone or download this repo
git clone https://github.com/andersbjarby/ai-model-lookup-skill.git

# Copy to your project
cp -r ai-model-lookup-skill/skills/ai-model-lookup /path/to/your/project/.claude/skills/
```

### Global Installation

```bash
cp -r ai-model-lookup-skill/skills/ai-model-lookup ~/.claude/skills/
```

## Usage

The skill triggers automatically when you:
- Ask about current AI models
- Start building scripts that call AI APIs
- Need to compare models for a specific task

### Manual Queries

```
What are the latest image generation models?
Build a script using the newest Gemini model for image generation
Compare text models from OpenAI and Anthropic
```

### Using the Script Directly

```bash
# List top 20 models by context length
python scripts/fetch_models.py

# Filter by type
python scripts/fetch_models.py --type image
python scripts/fetch_models.py --type chat

# Filter by provider
python scripts/fetch_models.py --provider openai
python scripts/fetch_models.py --provider anthropic

# Get raw JSON
python scripts/fetch_models.py --json
```

## How It Works

1. Fetches model list from OpenRouter API (no API key required)
2. Parses capabilities, pricing, and context limits
3. Presents information in a structured format
4. Claude uses this to write accurate integration code

## Example Output

```markdown
## AI Models - Updated 2026-02-05 14:30

| Model ID | Context | Pricing (per 1M tokens) | Description |
|----------|---------|------------------------|-------------|
| anthropic/claude-3-opus | 200,000 | $15.00 | Most capable Claude model... |
| openai/gpt-4-turbo | 128,000 | $10.00 | Latest GPT-4 with vision... |
| google/gemini-pro-1.5 | 1,000,000 | $7.00 | Long context Gemini... |
```

## Why OpenRouter?

OpenRouter provides a unified API that aggregates 100+ models from different providers. Their `/models` endpoint is:
- Free to access (no API key needed for listing)
- Always up-to-date
- Includes pricing, context limits, and capabilities
- Covers all major providers

## Contributing

PRs welcome! Ideas for improvement:
- Add more filtering options
- Cache results locally
- Add capability detection (vision, function calling, etc.)
- Include benchmark scores

## License

MIT

## Created During

This skill was built live during a podcast interview with Claude (Opus 4.5) - demonstrating how quickly you can create useful Claude Code extensions.
