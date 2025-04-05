# LinkedIn Post Style LoRA Project

A tool for generating LinkedIn posts in your personal writing style using LoRA fine-tuning.

## Project Purpose

This project creates a specialized language model that generates LinkedIn posts in your personal writing style. Using LoRA (Low-Rank Adaptation) fine-tuning on a pre-trained language model, we efficiently adapt it to mimic your specific tone and phrasing with minimal computational resources. The result is a private model that generates new posts on any topic while maintaining your authentic voice.

## Features

- Data processing pipeline to transform raw LinkedIn posts into structured training data
- LoRA training module for efficient fine-tuning of language models
- Post generation CLI for creating new content in your style

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/lora-linkedin-pipeline.git
cd lora-linkedin-pipeline

# Install with Poetry
poetry install
```

## Usage

```bash
# Data preparation
poetry run linkedin-lora prepare --input posts.csv --output data/processed

# Model training
poetry run linkedin-lora train --dataset data/processed/training_data.json --config config/lora.yaml

# Post generation
poetry run linkedin-lora generate --topic "artificial intelligence" --model-path models/linkedin-adapter
```

## Development

This project follows test-driven development practices:

```bash
# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=linkedin_lora
```

## License

MIT
