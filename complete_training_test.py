#!/usr/bin/env python3
"""
Complete training test scenario:
1. Remove existing adapters
2. Test model BEFORE training
3. Train model on Prolog data
4. Test model AFTER training
5. Compare results
"""

import os
import subprocess
from mlx_lm import generate, load

def run_command(command, description):
    """Run command and show results"""
    print(f"\n{'='*60}")
    print(f"STEP: {description}")
    print(f"COMMAND: {command}")
    print('='*60)
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"ERROR: {result.stderr}")
    return result.returncode == 0

def test_model(model_name, adapter_path=None, test_name=""):
    """Test model and return results"""
    print(f"\n{'='*60}")
    print(f"TESTING MODEL {test_name}")
    print('='*60)
    
    try:
        # Load model
        if adapter_path:
            print(f"Loading model with adapters: {adapter_path}")
            model, tokenizer = load(model_name, adapter_path=adapter_path)
        else:
            print(f"Loading base model: {model_name}")
            model, tokenizer = load(model_name)
        
        # Test questions
        test_questions = [
            "How to write Hello World in Prolog?",
            "What predicate prints Hello World?",
            "How to output text in Prolog?",
            "What is the head of [1,2,3]?",
            "How to check if X is a member of list?",
            "How to concatenate two lists?",
            "Who is the parent of mary?",
            "What are the children of john?",
            "Are mary and bob siblings?"
        ]
        
        results = []
        for i, question in enumerate(test_questions, 1):
            print(f"\n{i}. {question}")
            print("-" * 50)
            
            response = generate(
                model,
                tokenizer,
                prompt=question,
                max_tokens=50,
                verbose=False
            )
            
            response = response.strip()
            print(f"Response: {response}")
            results.append((question, response))
        
        return results
        
    except Exception as e:
        print(f"Error testing model: {e}")
        return []

def save_results(results, filename):
    """Save test results to file"""
    with open(filename, 'w', encoding='utf-8') as f:
        for question, response in results:
            f.write(f"Q: {question}\n")
            f.write(f"A: {response}\n")
            f.write("-" * 50 + "\n")

def compare_results(before_results, after_results):
    """Compare results before and after training"""
    print(f"\n{'='*60}")
    print("COMPARISON: BEFORE vs AFTER training")
    print('='*60)
    
    improved = 0
    same = 0
    worse = 0
    
    for i, ((before_q, before_a), (after_q, after_a)) in enumerate(zip(before_results, after_results), 1):
        print(f"\n{i}. {before_q}")
        print(f"BEFORE: {before_a}")
        print(f"AFTER:  {after_a}")
        
        # Simple comparison - check if after response is more relevant
        if len(after_a) > len(before_a) and any(word in after_a.lower() for word in ['prolog', 'write', 'hello', 'list', 'parent', 'member', 'append']):
            print("Status: IMPROVED ✓")
            improved += 1
        elif after_a == before_a:
            print("Status: SAME")
            same += 1
        else:
            print("Status: CHANGED")
            worse += 1
    
    print(f"\n{'='*60}")
    print(f"SUMMARY:")
    print(f"Improved: {improved}")
    print(f"Same: {same}")
    print(f"Changed: {worse}")
    print(f"Total: {len(before_results)}")
    print('='*60)

def main():
    """Main execution flow"""
    
    MODEL_NAME = "mlx-community/Qwen1.5-0.5B-Chat-4bit"
    ADAPTERS_PATH = "./prolog_adapters"
    
    print("COMPLETE TRAINING TEST SCENARIO")
    print("=" * 60)
    
    # Step 1: Remove existing adapters
    print("\n1. REMOVING EXISTING ADAPTERS...")
    if os.path.exists(ADAPTERS_PATH):
        import shutil
        shutil.rmtree(ADAPTERS_PATH)
        print(f"Removed directory: {ADAPTERS_PATH}")
    else:
        print(f"No adapters directory found: {ADAPTERS_PATH}")
    
    # Step 2: Test model BEFORE training
    print("\n2. TESTING MODEL BEFORE TRAINING...")
    before_results = test_model(MODEL_NAME, None, "BEFORE TRAINING")
    save_results(before_results, "before_training_results.txt")
    
    # Step 3: Train model
    print("\n3. TRAINING MODEL ON PROLOG DATA...")
    success = run_command("./train_prolog.sh", "Training model on Prolog data")
    
    if not success:
        print("Training failed! Stopping test.")
        return
    
    # Step 4: Test model AFTER training
    print("\n4. TESTING MODEL AFTER TRAINING...")
    after_results = test_model(MODEL_NAME, ADAPTERS_PATH, "AFTER TRAINING")
    save_results(after_results, "after_training_results.txt")
    
    # Step 5: Compare results
    print("\n5. COMPARING RESULTS...")
    compare_results(before_results, after_results)
    
    print(f"\n{'='*60}")
    print("COMPLETE TRAINING TEST FINISHED!")
    print("Results saved to:")
    print("- before_training_results.txt")
    print("- after_training_results.txt")
    print('='*60)

if __name__ == "__main__":
    main()
