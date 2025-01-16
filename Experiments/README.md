# Experiments Directory

This directory contains various experiments and Python scripts related to the TourExAgent project.

#rouge_evaluation.py
Results Explanation:

-ROUGE-1 F1 Score: Measures unigram overlap between model feedback and reference
-ROUGE-2 F1 Score: Measures bigram overlap (zero because no 2-word phrases match exactly)
-ROUGE-L F1 Score: Measures longest common subsequence
-Content Coverage Score: Our custom metric for tourism-specific content elements

-ROUGE-L in Table 2: This is the system's overall performance in generating feedback that matches expert reference feedback
-Content Coverage Score : This is a custom metric specifically measuring how many key tourism elements are covered
-Understanding the Results:
-model_feedback = "Extremely limited content. Include historical background, architectural features, and cultural significance."
key_elements = [
    'historical', 'architectural', 'cultural',
    'Renaissance', 'Baroque', 'church',
    'carvings', 'statues', 'structure'
]
