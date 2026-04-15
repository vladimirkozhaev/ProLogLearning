#!/usr/bin/env python3
"""
Simple test of the fine-tuned Prolog model
"""

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
        "How to check if X is a member of list?"
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
            max_tokens=50,
            verbose=False
        )
        
        print(f"Response: {response.strip()}")
        print()
    
    print("Testing completed!")

if __name__ == "__main__":
    test_model()
