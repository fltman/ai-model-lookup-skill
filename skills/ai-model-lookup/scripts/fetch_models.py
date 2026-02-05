#!/usr/bin/env python3
"""
Fetch latest AI models from OpenRouter API.
No API key required for listing models.
"""

import json
import sys
import urllib.request
from datetime import datetime

OPENROUTER_API = "https://openrouter.ai/api/v1/models"

def fetch_models():
    """Fetch all models from OpenRouter."""
    try:
        req = urllib.request.Request(
            OPENROUTER_API,
            headers={"User-Agent": "AI-Model-Lookup-Skill/1.0"}
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode())
            return data.get("data", [])
    except Exception as e:
        print(f"Error fetching models: {e}", file=sys.stderr)
        return []

def format_models(models, filter_type=None, filter_provider=None, limit=20):
    """Format models into a readable markdown table."""

    # Sort by context length (descending) as a proxy for capability
    models = sorted(models, key=lambda x: x.get("context_length", 0), reverse=True)

    # Filter by type if specified
    if filter_type:
        filter_type = filter_type.lower()
        if filter_type == "image":
            models = [m for m in models if any(kw in m.get("id", "").lower()
                     for kw in ["dalle", "imagen", "stable", "flux", "midjourney", "sdxl"])]
        elif filter_type == "chat" or filter_type == "text":
            models = [m for m in models if not any(kw in m.get("id", "").lower()
                     for kw in ["dalle", "imagen", "stable-diffusion", "whisper", "tts"])]

    # Filter by provider if specified
    if filter_provider:
        filter_provider = filter_provider.lower()
        models = [m for m in models if filter_provider in m.get("id", "").lower()]

    # Limit results
    models = models[:limit]

    if not models:
        return "No models found matching criteria."

    output = [f"## AI Models - Updated {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"]
    output.append("| Model ID | Context | Pricing (per 1M tokens) | Description |")
    output.append("|----------|---------|------------------------|-------------|")

    for model in models:
        model_id = model.get("id", "unknown")
        context = model.get("context_length", "N/A")
        if isinstance(context, int):
            context = f"{context:,}"

        pricing = model.get("pricing", {})
        prompt_price = pricing.get("prompt", "N/A")
        if prompt_price != "N/A":
            try:
                prompt_price = f"${float(prompt_price) * 1000000:.2f}"
            except:
                pass

        desc = model.get("description", "")[:50]
        if len(model.get("description", "")) > 50:
            desc += "..."

        output.append(f"| {model_id} | {context} | {prompt_price} | {desc} |")

    return "\n".join(output)

def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Fetch AI models from OpenRouter")
    parser.add_argument("--type", choices=["chat", "text", "image"],
                       help="Filter by model type")
    parser.add_argument("--provider", help="Filter by provider (e.g., openai, anthropic, google)")
    parser.add_argument("--limit", type=int, default=20, help="Max models to show")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    models = fetch_models()

    if not models:
        print("Failed to fetch models. Check your internet connection.")
        sys.exit(1)

    if args.json:
        print(json.dumps(models, indent=2))
    else:
        print(format_models(models, args.type, args.provider, args.limit))
        print(f"\nTotal models available: {len(fetch_models())}")

if __name__ == "__main__":
    main()
