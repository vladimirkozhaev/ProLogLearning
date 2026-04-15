#!/usr/bin/env python3
"""
Interactive test to see what the model actually generates
"""

from mlx_lm import generate, load

def interactive_test():
    """Test the model interactively"""
    
    # Load the model with adapters
    model, tokenizer = load(
        "mlx-community/Qwen1.5-0.5B-Chat-4bit",
        adapter_path="./prolog_adapters"
    )
    
    print("Interactive test of fine-tuned model")
    print("Type 'quit' to exit")
    print("=" * 40)
    
    while True:
        try:
            user_input = input("\nPrompt: ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
                
            if user_input:
                print("Generating...")
                response = generate(
                    model,
                    tokenizer,
                    prompt=user_input,
                    max_tokens=100,
                    verbose=True  # Show generation process
                )
                print(f"Response: {response.strip()}")
                
        except KeyboardInterrupt:
            break
    
    print("\nTest completed!")

if __name__ == "__main__":
    interactive_test()
