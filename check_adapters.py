#!/usr/bin/env python3
"""
Check if adapters are loaded correctly
"""

from mlx_lm import load
import os

def check_adapters():
    """Check if adapters exist and can be loaded"""
    
    adapter_path = "./prolog_adapters"
    
    # Check if adapter files exist
    if os.path.exists(adapter_path):
        print(f"Adapter directory exists: {adapter_path}")
        files = os.listdir(adapter_path)
        print(f"Files in adapter directory: {files}")
    else:
        print(f"Adapter directory does not exist: {adapter_path}")
        return
    
    try:
        # Try to load model with adapters
        print("Loading model with adapters...")
        model, tokenizer = load(
            "mlx-community/Qwen1.5-0.5B-Chat-4bit",
            adapter_path=adapter_path
        )
        print("Model with adapters loaded successfully!")
        
        # Try without adapters for comparison
        print("\nLoading model without adapters...")
        model_base, tokenizer_base = load("mlx-community/Qwen1.5-0.5B-Chat-4bit")
        print("Base model loaded successfully!")
        
        # Test simple generation
        from mlx_lm import generate
        
        print("\nTesting base model:")
        response = generate(model_base, tokenizer_base, prompt="Hello", max_tokens=10, verbose=False)
        print(f"Base model response: {response}")
        
        print("\nTesting model with adapters:")
        response = generate(model, tokenizer, prompt="Hello", max_tokens=10, verbose=False)
        print(f"Adapter model response: {response}")
        
    except Exception as e:
        print(f"Error loading adapters: {e}")

if __name__ == "__main__":
    check_adapters()
