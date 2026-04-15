#!/bin/bash

echo "🚀 Starting complete training test scenario..."
echo "This will:"
echo "1. Remove existing adapters"
echo "2. Test model before training"
echo "3. Train model on Prolog data"
echo "4. Test model after training"
echo "5. Compare results"
echo ""

# Activate virtual environment
source mlx_venv/bin/activate

# Run the complete test
python complete_training_test.py

echo ""
echo "✅ Complete test finished!"
echo "Check the following files:"
echo "- before_training_results.txt (model behavior before training)"
echo "- after_training_results.txt (model behavior after training)"
echo "- Comparison output in terminal"
