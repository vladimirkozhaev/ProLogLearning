#!/bin/bash

echo "🚀 Starting complete training and comparison workflow..."
echo ""

# Activate virtual environment
source mlx_venv/bin/activate

echo "📁 Step 1: Clean up and prepare..."
rm -rf prolog_adapters/
rm -f before_training_results.txt after_training_results.txt training_comparison_report.md

echo "✅ Cleaned up old files"
echo ""

echo "🧪 Step 2: Test model BEFORE training..."
python -c "
from mlx_lm import generate, load
import sys

model, tokenizer = load('mlx-community/Qwen1.5-0.5B-Chat-4bit')

questions = [
    'How to write Hello World in Prolog?',
    'What predicate prints Hello World?',
    'How to output text in Prolog?',
    'What is the head of [1,2,3]?',
    'How to check if X is a member of list?',
    'How to concatenate two lists?',
    'Who is the parent of mary?',
    'What are the children of john?',
    'Are mary and bob siblings?'
]

print('Testing model BEFORE training...')
with open('before_training_results.txt', 'w') as f:
    for i, q in enumerate(questions, 1):
        print(f'Test {i}: {q}')
        response = generate(model, tokenizer, prompt=q, max_tokens=50, verbose=False)
        print(f'Response: {response.strip()}')
        f.write(f'Q: {q}\n')
        f.write(f'A: {response.strip()}\n')
        f.write('-' * 50 + '\n')
        print()

print('✅ Before training test completed!')
"

echo ""
echo "🎓 Step 3: Train model on Prolog data..."
./train_prolog.sh

echo ""
echo "🧪 Step 4: Test model AFTER training..."
python -c "
from mlx_lm import generate, load

model, tokenizer = load('mlx-community/Qwen1.5-0.5B-Chat-4bit', adapter_path='./prolog_adapters')

questions = [
    'How to write Hello World in Prolog?',
    'What predicate prints Hello World?',
    'How to output text in Prolog?',
    'What is the head of [1,2,3]?',
    'How to check if X is a member of list?',
    'How to concatenate two lists?',
    'Who is the parent of mary?',
    'What are the children of john?',
    'Are mary and bob siblings?'
]

print('Testing model AFTER training...')
with open('after_training_results.txt', 'w') as f:
    for i, q in enumerate(questions, 1):
        print(f'Test {i}: {q}')
        response = generate(model, tokenizer, prompt=q, max_tokens=50, verbose=False)
        print(f'Response: {response.strip()}')
        f.write(f'Q: {q}\n')
        f.write(f'A: {response.strip()}\n')
        f.write('-' * 50 + '\n')
        print()

print('✅ After training test completed!')
"

echo ""
echo "📊 Step 5: Generate comparison report..."
python generate_comparison.py

echo ""
echo "🎉 COMPLETE WORKFLOW FINISHED!"
echo ""
echo "📄 Generated files:"
echo "  - before_training_results.txt (model behavior before training)"
echo "  - after_training_results.txt (model behavior after training)"
echo "  - training_comparison_report.md (detailed comparison analysis)"
echo ""
echo "📖 View the comparison report: training_comparison_report.md"
