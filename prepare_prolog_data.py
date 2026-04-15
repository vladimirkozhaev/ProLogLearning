#!/usr/bin/env python3
"""
Convert Prolog files to training data for MLX LM
Reads .pl files and extracts training instructions from comments
"""

import json
import os
import re
from pathlib import Path

def extract_training_data_from_pl(pl_file_path):
    """Extract training examples from a Prolog file"""
    examples = []
    
    with open(pl_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find TRAIN comment at the beginning
    train_match = re.search(r'%\s*TRAIN:\s*(.+)', content, re.IGNORECASE)
    if train_match:
        topic = train_match.group(1).strip()
    else:
        topic = "Prolog programming"
    
    # Extract examples from comments
    example_pattern = r'%\s*["\']?(.+?)["\']?\s*->\s*["\']?(.+?)["\']?\s*$'
    
    for match in re.finditer(example_pattern, content, re.MULTILINE):
        question = match.group(1).strip()
        answer = match.group(2).strip()
        
        # Create training example
        example = {
            "text": question,
            "response": answer
        }
        examples.append(example)
    
    # If no explicit examples found, create from facts and rules
    if not examples:
        # Extract facts
        fact_pattern = r'(\w+)\([^)]+\)\.'
        facts = re.findall(fact_pattern, content)
        
        # Extract rules
        rule_pattern = r'(\w+)\([^)]+\)\s*:-'
        rules = re.findall(rule_pattern, content)
        
        if facts:
            examples.append({
                "text": f"What facts are defined in this Prolog code about {topic}?",
                "response": f"The code defines facts: {', '.join(set(facts))}"
            })
        
        if rules:
            examples.append({
                "text": f"What rules are defined in this Prolog code about {topic}?",
                "response": f"The code defines rules: {', '.join(set(rules))}"
            })
    
    return examples

def prepare_training_data_from_directory(data_dir):
    """Prepare training data from all .pl files in a directory"""
    all_examples = []
    
    # Find all .pl files
    pl_files = list(Path(data_dir).rglob("*.pl"))
    
    for pl_file in pl_files:
        print(f"Processing {pl_file}...")
        examples = extract_training_data_from_pl(pl_file)
        all_examples.extend(examples)
        print(f"  Found {len(examples)} examples")
    
    return all_examples

if __name__ == "__main__":
    # Search in both examples/ and data/ directories
    data_dirs = ["./examples", "./data"]
    output_file = "./data/train.jsonl"
    
    # Create data directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    all_examples = []
    
    for data_dir in data_dirs:
        if os.path.exists(data_dir):
            print(f"Searching in {data_dir}...")
            examples = prepare_training_data_from_directory(data_dir)
            all_examples.extend(examples)
    
    # Write to JSONL file
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in all_examples:
            f.write(json.dumps(example) + '\n')
    
    print(f"Total examples: {len(all_examples)}")
    print(f"Training data saved to: {output_file}")
