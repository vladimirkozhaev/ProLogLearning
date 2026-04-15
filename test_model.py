#!/usr/bin/env python3
"""
Test the fine-tuned Prolog model with trained adapters
"""

import sys
from mlx_lm import generate, load

def test_model():
    """Test the trained model with Prolog-related questions"""
    
    # Load the model with adapters
    model, tokenizer = load(
        "mlx-community/Qwen1.5-0.5B-Chat-4bit",
        adapter_path="./prolog_adapters"
    )
    
    # Test questions based on training data
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
    
    print("Testing fine-tuned Prolog model...")
    print("=" * 50)
    
    for i, question in enumerate(test_questions, 1):
        print(f"\nTest {i}: {question}")
        print("-" * 30)
        
        # Generate response
        response = generate(
            model,
            tokenizer,
            prompt=question,
            temperature=0.1,
            max_tokens=100,
            verbose=False
        )
        
        print(f"Response: {response.strip()}")
        print()
    
    # Interactive mode
    print("\n" + "=" * 50)
    print("Interactive mode - type 'quit' to exit")
    print("=" * 50)
    
    while True:
        try:
            user_input = input("\nEnter your Prolog question: ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
                
            if user_input:
                response = generate(
                    model,
                    tokenizer,
                    prompt=user_input,
                    temperature=0.1,
                    max_tokens=150,
                    verbose=False
                )
                print(f"Response: {response.strip()}")
                
        except KeyboardInterrupt:
            break
    
    print("\nTesting completed!")

if __name__ == "__main__":
    test_model()
