#!/usr/bin/env python3
"""
Generate detailed comparison file from before and after training results
"""

def load_results(filename):
    """Load results from file"""
    results = []
    current_q = ""
    current_a = ""
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('Q: '):
                current_q = line[3:]
            elif line.startswith('A: '):
                current_a = line[3:]
                if current_q and current_a:
                    results.append((current_q, current_a))
                    current_q = ""
                    current_a = ""
    
    return results

def analyze_relevance(question, answer):
    """Analyze if answer is relevant to Prolog question"""
    question_lower = question.lower()
    answer_lower = answer.lower()
    
    prolog_keywords = ['prolog', 'write', 'hello', 'list', 'parent', 'member', 'append', 'head', 'child', 'sibling']
    answer_words = answer_lower.split()
    
    # Count relevant keywords
    relevant_count = sum(1 for word in prolog_keywords if word in answer_lower)
    
    # Check if answer is empty or too short
    if len(answer.strip()) < 3:
        return "EMPTY", 0
    
    # Check if answer contains Prolog-specific content
    if any(keyword in answer_lower for keyword in prolog_keywords):
        if relevant_count >= 2:
            return "HIGHLY_RELEVANT", relevant_count
        else:
            return "RELEVANT", relevant_count
    else:
        return "NOT_RELEVANT", relevant_count

def generate_comparison():
    """Generate comparison report"""
    
    # Load results
    try:
        before_results = load_results('before_training_results.txt')
        after_results = load_results('after_training_results.txt')
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Make sure to run the complete test first!")
        return
    
    # Generate comparison report
    with open('training_comparison_report.md', 'w', encoding='utf-8') as f:
        f.write("# Prolog Model Training Comparison Report\n\n")
        f.write("## Overview\n")
        f.write("This report compares model responses before and after fine-tuning on Prolog examples.\n\n")
        
        # Summary table
        f.write("## Summary Table\n\n")
        f.write("| # | Question | Before Training | After Training | Improvement |\n")
        f.write("|---|----------|----------------|----------------|-------------|\n")
        
        improved_count = 0
        total_count = len(before_results)
        
        for i, ((before_q, before_a), (after_q, after_a)) in enumerate(zip(before_results, after_results), 1):
            # Analyze relevance
            before_status, before_relevance = analyze_relevance(before_q, before_a)
            after_status, after_relevance = analyze_relevance(after_q, after_a)
            
            # Determine improvement
            if after_relevance > before_relevance:
                improvement = "✅ YES"
                improved_count += 1
            elif after_relevance == before_relevance:
                improvement = "➡️ SAME"
            else:
                improvement = "❌ NO"
            
            # Truncate long answers for table
            before_short = before_a[:40] + "..." if len(before_a) > 40 else before_a
            after_short = after_a[:40] + "..." if len(after_a) > 40 else after_a
            
            f.write(f"| {i} | {before_q[:30]}... | {before_short} | {after_short} | {improvement} |\n")
        
        f.write("\n")
        
        # Statistics
        f.write("## Statistics\n\n")
        f.write(f"- **Total questions tested**: {total_count}\n")
        f.write(f"- **Improved responses**: {improved_count} ({improved_count/total_count*100:.1f}%)\n")
        f.write(f"- **Same or worse**: {total_count-improved_count} ({(total_count-improved_count)/total_count*100:.1f}%)\n\n")
        
        # Detailed comparison
        f.write("## Detailed Comparison\n\n")
        
        for i, ((before_q, before_a), (after_q, after_a)) in enumerate(zip(before_results, after_results), 1):
            f.write(f"### {i}. {before_q}\n\n")
            
            # Before analysis
            before_status, before_relevance = analyze_relevance(before_q, before_a)
            f.write("**Before Training:**\n")
            f.write(f"- Response: `{before_a}`\n")
            f.write(f"- Relevance: {before_status}\n")
            f.write(f"- Keywords found: {before_relevance}\n\n")
            
            # After analysis
            after_status, after_relevance = analyze_relevance(after_q, after_a)
            f.write("**After Training:**\n")
            f.write(f"- Response: `{after_a}`\n")
            f.write(f"- Relevance: {after_status}\n")
            f.write(f"- Keywords found: {after_relevance}\n\n")
            
            # Comparison
            if after_relevance > before_relevance:
                f.write("**🎉 IMPROVEMENT**: Model response became more relevant to Prolog concepts.\n\n")
            elif after_relevance == before_relevance:
                f.write("**➡️ NO CHANGE**: Model response relevance stayed the same.\n\n")
            else:
                f.write("**⚠️ REGRESSION**: Model response became less relevant.\n\n")
            
            f.write("---\n\n")
        
        # Conclusion
        f.write("## Conclusion\n\n")
        if improved_count >= total_count * 0.7:
            f.write("✅ **Training was SUCCESSFUL** - Model significantly improved on Prolog-related questions.\n")
        elif improved_count >= total_count * 0.4:
            f.write("⚠️ **Training was PARTIALLY SUCCESSFUL** - Model showed some improvement but could be better.\n")
        else:
            f.write("❌ **Training was NOT SUCCESSFUL** - Model did not improve significantly.\n")
        
        f.write(f"\n**Improvement Rate**: {improved_count/total_count*100:.1f}%\n")
        
        # Recommendations
        f.write("\n## Recommendations\n\n")
        if improved_count < total_count * 0.7:
            f.write("- Consider adding more training examples\n")
            f.write("- Increase training iterations\n")
            f.write("- Review training data quality\n")
            f.write("- Try different learning rates\n")
        else:
            f.write("- Training looks good!\n")
            f.write("- Consider testing with more diverse questions\n")
    
    print("✅ Comparison report generated: training_comparison_report.md")

if __name__ == "__main__":
    generate_comparison()
