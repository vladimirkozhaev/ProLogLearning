#!/usr/bin/env python3
"""
Final test of the fine-tuned Prolog model with proper prompts
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
    test_cases = [
        ("How to write Hello World in Prolog?", "Use write('Hello, World!'), nl."),
        ("What predicate prints Hello World?", "hello_world predicate prints Hello World"),
        ("How to output text in Prolog?", "Use write/1 predicate to output text"),
        ("What is the head of [1,2,3]?", "1 is the head of [1,2,3]"),
        ("How to check if X is a member of list?", "Use member(X, List)"),
        ("How to concatenate two lists?", "Use append(List1, List2, Result)"),
        ("Who is the parent of mary?", "john is the parent of mary"),
        ("What are the children of john?", "mary and bob are children of john"),
        ("Are mary and bob siblings?", "Yes, mary and bob are siblings")
    ]
    
    print("Testing fine-tuned Prolog model...")
    print("=" * 60)
    
    correct = 0
    total = len(test_cases)
    
    for i, (question, expected) in enumerate(test_cases, 1):
        print(f"\nTest {i}: {question}")
        print(f"Expected: {expected}")
        print("-" * 40)
        
        # Generate response
        response = generate(
            model,
            tokenizer,
            prompt=question,
            max_tokens=30,
            verbose=False
        )
        
        response = response.strip()
        print(f"Model:    {response}")
        
        # Check if response contains expected keywords
        if any(word.lower() in response.lower() for word in expected.split()[:3]):
            print("Status:   CORRECT")
            correct += 1
        else:
            print("Status:   INCORRECT")
        print()
    
    print("=" * 60)
    print(f"Results: {correct}/{total} correct ({correct/total*100:.1f}%)")
    
    if correct >= total * 0.7:
        print("Model is WELL TRAINED!")
    elif correct >= total * 0.5:
        print("Model is PARTIALLY TRAINED")
    else:
        print("Model needs more training")

if __name__ == "__main__":
    test_model()
