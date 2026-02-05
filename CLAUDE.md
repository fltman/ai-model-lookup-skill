# AI Model Lookup Skill

A Claude Code skill that keeps you updated on the latest AI models from major providers.

## Problem

Claude's knowledge has a cutoff date, which means information about the latest AI models, APIs, and capabilities may be outdated. When building integrations with AI services, you need current information.

## Solution

This skill triggers proactively when you're building AI integrations, automatically fetching the latest model information from official sources.

## Installation

Copy the `skills/ai-model-lookup` folder to your project's `.claude/skills/` directory:

```bash
cp -r skills/ai-model-lookup /path/to/your/project/.claude/skills/
```

Or add it globally to `~/.claude/skills/`.

## Usage

The skill triggers automatically when you:
- Ask about current AI models
- Start building scripts that call AI APIs
- Need to compare models for a specific task

You can also trigger it manually:
```
What are the latest image generation models available?
```

## Supported Providers

- OpenAI (GPT, DALL-E, Whisper)
- Anthropic (Claude)
- Google (Gemini, Imagen, Veo)
- Meta (Llama)
- Mistral
- Stability AI (Stable Diffusion)

## Contributing

Feel free to add more providers or update the documentation links as APIs evolve.

## License

MIT - Use freely in your projects.
