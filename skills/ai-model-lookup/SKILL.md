---
name: ai-model-lookup
description: Looks up the latest AI models from major providers (OpenAI, Anthropic, Google, Meta, Mistral, etc.) including capabilities, API endpoints, and documentation links. Use PROACTIVELY when building scripts that integrate with AI APIs or when user asks about current AI models.
---

# AI Model Lookup Skill

This skill fetches current information about AI models from major providers to ensure you have up-to-date knowledge when building integrations.

## When to Use

- Before writing scripts that call AI APIs (image generation, text, video, audio)
- When user asks "what's the latest model from X?"
- When building integrations and you need current API documentation
- When comparing models for a specific use case

## How to Use

### Option 1: OpenRouter API (Recommended)

OpenRouter aggregates models from all major providers. Use their API to get a current list:

```bash
curl https://openrouter.ai/api/v1/models
```

This returns JSON with all available models, their capabilities, pricing, and context limits.

**Parse the response for:**
- `id`: Model identifier for API calls
- `context_length`: Max tokens
- `pricing`: Cost per token
- `top_provider`: Original provider
- `description`: Capabilities

### Option 2: Web Search

Search for latest models using WebSearch with queries like:
   - `"[provider] latest AI model 2026 API"`
   - `"[provider] image generation API documentation"`
   - `"[provider] model comparison capabilities"`

### Option 3: Official Documentation

Fetch official documentation using WebFetch from:
   - OpenAI: https://platform.openai.com/docs/models
   - Anthropic: https://docs.anthropic.com/en/docs/models-overview
   - Google AI: https://ai.google.dev/models
   - Mistral: https://docs.mistral.ai/getting-started/models/

3. **Compile a summary** with:
   - Model name and version
   - Release date (if available)
   - Key capabilities (text, image, video, audio, code)
   - API endpoint format
   - Pricing tier (if available)
   - Context window / limits

## Provider Quick Reference

### OpenAI
- **Text**: GPT-4, GPT-4 Turbo, GPT-4o
- **Images**: DALL-E 3
- **Audio**: Whisper, TTS
- **Embeddings**: text-embedding-3-large
- Docs: https://platform.openai.com/docs

### Anthropic
- **Text**: Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku
- Docs: https://docs.anthropic.com

### Google
- **Text**: Gemini 1.5 Pro, Gemini 1.5 Flash
- **Images**: Imagen 3
- **Video**: Veo
- Docs: https://ai.google.dev

### Meta
- **Text**: Llama 3
- **Images**: Various open models
- Docs: https://llama.meta.com

### Mistral
- **Text**: Mistral Large, Mistral Medium, Mistral Small
- Docs: https://docs.mistral.ai

### Stability AI
- **Images**: Stable Diffusion 3, SDXL
- **Video**: Stable Video Diffusion
- Docs: https://platform.stability.ai/docs

## Output Format

When reporting findings, use this format:

```markdown
## AI Model Update - [Date]

### [Provider Name]

**Latest Models:**
| Model | Type | Released | Key Features |
|-------|------|----------|--------------|
| model-name | text/image/etc | date | features |

**API Example:**
\`\`\`python
# Quick usage example
\`\`\`

**Documentation:** [link]
```

## Important Notes

- Always verify information is current by checking release dates
- API formats change frequently - always fetch latest docs before writing code
- Some models may be in preview/beta - note this in your summary
- Pricing and availability vary by region
