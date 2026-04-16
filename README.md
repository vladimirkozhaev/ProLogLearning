# Prolog Learning Extension - LLM Training for Prolog

# Prolog Learning Extension - LLM Training for Prolog

## Overview / Overview (English)

Prolog Learning Extension is a VSCode/Windsurf extension that provides a convenient interface for testing and training LLM models on Prolog code.

## Overview / Overview (Russian)

Prolog Learning Extension - this is a VSCode/Windsurf extension that provides a convenient interface for testing and training LLM models on Prolog code.

## Features

- **Complete Workflow**: Full training and testing cycle
- **VSCode/Windsurf Integration**: Native editor support
- **Automated Testing**: Before/after training comparison
- **Detailed Reports**: Comprehensive analysis and metrics
- **Multi-language Support**: Russian and English documentation

## Quick Start

### Installation

```bash
# Install to both VSCode and Windsurf
./install_universal.sh

# Or install to specific editor
./install_vsix.sh          # VSCode only
./install_to_windsurf.sh   # Windsurf only
```

### Usage

1. Open VSCode or Windsurf
2. Press `Ctrl+Shift+P`
3. Type: `Show Prolog Testing Panel`
4. Click **Run Complete Test**

## Project Structure

```
ProLogLearning/
|
|-- vscode_extension/           # Extension files
|   |-- extension.js           # Main extension code
|   |-- package.json           # Extension manifest
|   |-- README.md              # Extension documentation
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
| `install_universal.sh` | Install extension to both editors |
| `check_installation.sh` | Verify extension installation |
| `launch_windsurf_debug.sh` | Launch Windsurf with debug mode |

## Troubleshooting

### Extension Not Working
```bash
# Check installation
./check_installation.sh

# Reinstall extension
./uninstall_extension.sh
./install_universal.sh

# Launch with debug
./launch_windsurf_debug.sh
```

### Training Issues
```bash
# Check virtual environment
source mlx_venv/bin/activate

# Verify training data
python prepare_prolog_data.py

# Run training manually
./train_prolog.sh
```

## Requirements

- **VSCode**: 1.74.0+ or **Windsurf**
- **Python**: 3.8+
- **MLX LM**: For model training
- **Virtual Environment**: mlx_venv

## Extension Commands

| Command | Description |
|---------|-------------|
| `Show Prolog Testing Panel` | Open testing interface |
| `Run Complete Test` | Full training cycle |
| `Quick Test` | Quick model check |
| `View Report` | Show comparison report |

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
