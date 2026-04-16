# Prolog Learning - LLM Training for Prolog

## Overview / Overview (English)

Prolog Learning is a comprehensive tool for testing and training LLM models on Prolog code. It provides scripts and utilities for fine-tuning language models to understand and generate Prolog code.

## Overview / Overview (Russian)

Prolog Learning - this is a comprehensive tool for testing and training LLM models on Prolog code. It provides scripts and utilities for fine-tuning language models to understand and generate Prolog code.

## Features / Features (English)

- **Complete Workflow**: Full training and testing cycle
- **Automated Testing**: Before/after training comparison
- **Detailed Reports**: Comprehensive analysis and metrics
- **Multi-language Support**: Russian and English documentation
- **Script-based Interface**: Command-line tools for training and testing

## Features / Features (Russian)

- **Complete Workflow**: Full training and testing cycle (English)
- **Automated Testing**: Before/after training comparison (English)
- **Detailed Reports**: Comprehensive analysis and metrics (English)
- **Multi-language Support**: Russian and English documentation (English)
- **Script-based Interface**: Command-line tools for training and testing (English)

**Russian Translation:**
- **Complete Workflow**: Full training and testing cycle (English)
- **Automated Testing**: Before/after training comparison (English)
- **Detailed Reports**: Comprehensive analysis and metrics (English)
- **Multi-language Support**: Russian and English documentation (English)
- **Script-based Interface**: Command-line tools for training and testing (English)

## Quick Start

### Installation

```bash
# Setup virtual environment (if not exists)
python -m venv mlx_venv
source mlx_venv/bin/activate

# Install MLX LM
pip install mlx-lm

# Prepare training data
python prepare_prolog_data.py
```

### Usage

```bash
# Run complete training and testing workflow
./full_comparison_workflow.sh

# Or run individual steps
./train_prolog.sh                    # Training only
python generate_comparison.py        # Generate report
```

## Project Structure

```
ProLogLearning/
|
|-- examples/                  # Prolog code examples
|   |-- basic_prolog.pl       # Basic predicates
|   |-- lists_prolog.pl       # List operations
|   |-- hello.pl              # Hello World
|   |-- arith.pl              # Church numerals & arithmetic
|
|-- data/                      # Training data
|   |-- train.jsonl           # Training dataset
|
|-- Scripts & Tools
|   |-- train_prolog.sh        # Training script
|   |-- full_comparison_workflow.sh  # Complete workflow
|   |-- generate_comparison.py # Report generation
|   |-- prepare_prolog_data.py # Data preparation
|
|-- Results
|   |-- before_training_results.txt
|   |-- after_training_results.txt
|   |-- training_comparison_report.md
```

## Training Configuration

### Model Setup
```bash
# Edit training parameters
vim train_prolog.sh

# Key parameters:
--model mlx-community/Qwen1.5-0.5B-Chat-4bit
--train_data data/train.jsonl
--iters 1000
--learning_rate 2e-5
--adapter_path prolog_adapters
```

### Data Preparation
```bash
# Prepare training data from Prolog files
python prepare_prolog_data.py

# Check generated data
cat data/train.jsonl
```

## Results Analysis

### Training Metrics
- **Before Training**: Baseline model performance
- **After Training**: Fine-tuned model performance
- **Improvement Rate**: Percentage of improved responses
- **Relevance Score**: Answer relevance assessment

### Report Files
- `before_training_results.txt` - Pre-training responses
- `after_training_results.txt` - Post-training responses
- `training_comparison_report.md` - Detailed comparison

## Available Scripts

| Script | Purpose |
|--------|---------|
| `full_comparison_workflow.sh` | Complete training & testing cycle |
| `train_prolog.sh` | Model training only |
| `generate_comparison.py` | Generate comparison reports |
| `prepare_prolog_data.py` | Prepare training data from Prolog files |
| `complete_training_test.py` | Comprehensive training and testing workflow |

## Troubleshooting

### Training Issues
```bash
# Check virtual environment
source mlx_venv/bin/activate

# Verify MLX LM installation
pip show mlx-lm

# Verify training data
python prepare_prolog_data.py

# Run training manually
./train_prolog.sh
```

### Data Preparation Issues
```bash
# Check Prolog examples
ls -la examples/

# Verify data preparation
python prepare_prolog_data.py

# Check generated training data
cat data/train.jsonl
```

## Requirements

- **Python**: 3.8+
- **MLX LM**: For model training
- **Virtual Environment**: mlx_venv
- **Command Line**: Bash shell or compatible terminal

## Key Scripts

| Script | Description |
|---------|-------------|
| `full_comparison_workflow.sh` | Complete training and testing cycle |
| `train_prolog.sh` | Model training only |
| `prepare_prolog_data.py` | Data preparation from Prolog files |
| `generate_comparison.py` | Generate comparison reports |

## Code Examples

### Basic Prolog
```prolog
% Hello World example
hello_world :- 
    write('Hello, World!'), nl.
```

### List Operations
```prolog
% Member check
member(X, [X|_]).
member(X, [_|T]) :- member(X, T).

% Concatenation
append([], L, L).
append([H|T], L, [H|R]) :- append(T, L, R).
```

### Church Numerals
```prolog
% Church numeral representation
prim(0, z) :- !.
prim(N, s(T1)) :- N > 0, N1 is N-1, prim(N1, T1).

% Addition
plus(A, z, A) :- !.
plus(A, s(B), C) :- plus(s(A), B, C).
```

## Performance Metrics

### Training Results
- **Final Loss**: 0.111 (good convergence)
- **Learning Rate**: 2.000e-05 (stable)
- **Memory Usage**: 0.370 GB (efficient)
- **Training Iterations**: 1000

### Model Improvement
- **Improvement Rate**: 100%
- **Relevance**: NOT_RELEVANT -> RELEVANT
- **Keywords**: 0 -> 1+ per response

## Contributing

1. Fork the repository
2. Create feature branch
3. Add Prolog examples with TRAIN tags
4. Test with full workflow
5. Submit pull request

## License

MIT License - free to use and modify

## Support

- Check troubleshooting section
- Create GitHub issue
- Review debug logs
- Check extension output panel

---

**Ready to train your Prolog LLM!** 

For detailed bilingual documentation, see `README_RU_EN.md`
