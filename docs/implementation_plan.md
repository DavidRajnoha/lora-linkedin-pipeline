# LinkedIn Post Style LoRA Project - Revised

## Automated Coding Tools Instructions
Proceed by small incremental units. Follow the test driven development approach. first write test that fails, then run the test and make sure it fails, then write the code to make the test pass. Commits and changes should be coherent, logical and single feature only. It should be easy to revise each commit.

## Project Purpose

This project creates a specialized language model that generates LinkedIn posts in your personal writing style. Using LoRA (Low-Rank Adaptation) fine-tuning on a pre-trained language model, we efficiently adapt it to mimic your specific tone and phrasing with minimal computational resources. The result is a private model that generates new posts on any topic while maintaining your authentic voice.

## High-Level Architecture

The system consists of three main components:

1. **Data Processing Pipeline**: Transforms raw LinkedIn posts into structured training data
2. **LoRA Training Module**: Handles the model fine-tuning process 
3. **Post Generation CLI**: Enables post generation through a simple command-line interface

## Project Structure

```
linkedin-lora-project/
├── data/                    # Data storage and configuration
├── src/                     # Source code modules
│   ├── data_processing/     # Data preparation components
│   ├── training/            # Model training components
│   └── generation/          # Post generation logic
├── cli/                     # Command-line interface
│   ├── prepare.py           # Data preparation command
│   ├── train.py             # Training command
│   └── generate.py          # Generation command
├── config/                  # Configuration files
└── tests/                   # Testing modules
└── docs/                    # Documentation
```

## Component Relationships

### Data Flow

1. **Raw LinkedIn Posts → Processed Dataset**
   - Extract themes from posts using an LLM
   - Transform posts into prompt-completion pairs
   - Create formatted dataset for training

2. **Dataset + Base Model → LoRA Weights**
   - Apply LoRA configuration to the base model
   - Fine-tune on the processed dataset
   - Save resulting weights

3. **Topic + LoRA Weights → Generated Post**
   - User provides a topic and idea of the post through CLI
   - System loads the base model and LoRA weights
   - Generates a post in your personal style

## Design Patterns

1. **Factory Method**: Used for model and tokenizer initialization
   - Creates appropriate model instances based on configuration

2. **Strategy Pattern**: Applied to data processing pipelines
   - Allows swapping different topic extraction methods
   - Enables various dataset formatting approaches

## CLI Implementation

The command-line interface provides three main commands:

```
# Data preparation
python -m cli.prepare --input posts.csv --output data/processed

# Model training
python -m cli.train --dataset data/processed/training_data.json --config config/lora.yaml

# Post generation
python -m cli.generate --topic "artificial intelligence" --model-path models/linkedin-adapter
```

This approach prioritizes simplicity and utility, allowing for direct access to all functionality through command-line arguments.

## Implementation Plan

### Phase 1: Environment & Data Processing (Days 1-2)
- Set up development environment
- Implement simple CLI 
- Implement data processing module
- Implement LoRA training module
- Implement generation module

