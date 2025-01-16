from rouge_score import rouge_scorer
import numpy as np
from typing import Dict, List, Tuple

class TourismFeedbackEvaluator:
    def __init__(self):
        # Initialize rouge scorer with different ROUGE variants
        self.scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
        
    def evaluate_feedback_quality(self, 
                                student_answer: str,
                                model_feedback: str,
                                reference_answer: str) -> Dict[str, float]:
        """
        Evaluate the quality of model feedback for tourism explanations
        """
        try:
            # Calculate ROUGE scores
            scores = self.scorer.score(reference_answer, model_feedback)
            
            # Extract F1 scores for each ROUGE metric
            rouge_scores = {
                'rouge-1': scores['rouge1'].fmeasure,
                'rouge-2': scores['rouge2'].fmeasure,
                'rouge-l': scores['rougeL'].fmeasure
            }
            
            # Add content coverage score
            rouge_scores['content_coverage'] = self._calculate_content_coverage(
                student_answer, reference_answer)
            
            return rouge_scores
            
        except Exception as e:
            print(f"Error calculating ROUGE scores: {e}")
            return None

    def _calculate_content_coverage(self, 
                                  student_text: str, 
                                  reference_text: str) -> float:
        """
        Calculate how well student answer covers key points from reference
        """
        # Define key elements to look for in tourism explanations
        key_elements = [
            'historical', 'architectural', 'cultural',
            'Renaissance', 'Baroque', 'church',
            'carvings', 'statues', 'structure'
        ]
        
        # Count matching elements
        student_words = set(student_text.lower().split())
        ref_words = set(reference_text.lower().split())
        
        matches = sum(1 for elem in key_elements 
                     if elem.lower() in student_words 
                     or elem.lower() in ref_words)
        
        return matches / len(key_elements)

def main():
    # Example usage with provided data
    student_answer = "The Ruins of St. Paul's is like a monument of history, witnessing the vicissitudes and brilliance of Macau. It was originally built in the 16th century, but after suffering from several fires, only the front wall of the church remains. The Renaissance and Baroque architectural facade, exquisite statues and carvings, make one feel as if they have traveled back in time. Also, the two classical-style street lamps in the foreground, emitting a warm light, add a touch of warmth to this historical tapestry."
    
    model_feedback = """Your description of The Ruins of St. Paul's at night is quite evocative, but there's room for enhancement to make it more detailed and engaging. Here's a revised version incorporating the suggested improvements:
Nestled in the heart of Macau, The Ruins of St. Paul's stand as a poignant monument to the region's rich history. Originally constructed in the 16th century as part of the Jesuit College of St. Paul, the first Western university in Asia, this church bore witness to the vibrant cultural exchange between East and West. Despite being ravaged by several fires, the front wall remains, a testament to its resilience. The architectural facade is a harmonious blend of Renaissance and Baroque styles, with its ornate portal featuring exquisite carvings and statues of saints like St. Paul and St. Francis Xavier. The use of pilasters and the symmetry of the facade reflect Renaissance principles, while the lavish decorations are quintessentially Baroque. The grand staircase leading up to the facade adds to the imposing nature of the ruins, its stone texture highlighted by the moonlight. At night, the scene is further enhanced by the warm glow of two classical-style street lamps in the foreground, casting soft shadows that accentuate the intricate details of the carvings. This interplay of light and shadow creates a serene, contemplative atmosphere, inviting visitors to pause and reflect on the centuries of history encapsulated within these ruins. By adding these specific details, your description will not only inform but also immerse your audience in the historical, architectural, and cultural significance of The Ruins of St. Paul's at night."""
    
    reference_answer = """The Ruins of St. Paul's (1602-1637) represents 
    a significant historical landmark in Macau, featuring Renaissance and 
    Baroque architectural elements. Originally East Asia's largest Catholic 
    church until the 1835 fire, its preserved facade showcases exquisite 
    carvings and statues. Two classical street lamps illuminate the 
    structure, creating an atmospheric evening view."""

    # Initialize evaluator
    evaluator = TourismFeedbackEvaluator()
    
    # Calculate scores
    scores = evaluator.evaluate_feedback_quality(
        student_answer, model_feedback, reference_answer)
    
    # Print results
    if scores:
        print("\nEvaluation Results:")
        print("------------------")
        print(f"ROUGE-1 F1 Score: {scores['rouge-1']:.3f}")
        print(f"ROUGE-2 F1 Score: {scores['rouge-2']:.3f}")
        print(f"ROUGE-L F1 Score: {scores['rouge-l']:.3f}")
        print(f"Content Coverage Score: {scores['content_coverage']:.3f}")

if __name__ == "__main__":
    main()

# Additional evaluation functions for batch processing
def evaluate_feedback_batch(model_outputs: List[str], 
                          reference_feedbacks: List[str]) -> Dict[str, float]:
    """
    Evaluate a batch of feedback samples
    """
    evaluator = TourismFeedbackEvaluator()
    rouge_scores = []
    
    for model_out, ref in zip(model_outputs, reference_feedbacks):
        scores = evaluator.evaluate_feedback_quality(
            "", model_out, ref)  # Empty student answer for batch processing
        if scores:
            rouge_scores.append(scores)
    
    # Calculate average scores
    if rouge_scores:
        avg_scores = {
            'rouge-1': np.mean([s['rouge-1'] for s in rouge_scores]),
            'rouge-2': np.mean([s['rouge-2'] for s in rouge_scores]),
            'rouge-l': np.mean([s['rouge-l'] for s in rouge_scores]),
            'content_coverage': np.mean([s['content_coverage'] for s in rouge_scores])
        }
        return avg_scores
    return None
