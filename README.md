# TourExAgent
The TourExAIGC aims to provide a comprehensive and efficient solution for the teaching and assessment of tour guide explanations.

# TourEx-Eval Dataset
The TourEx-Eval (Tourism Explanation Evaluation) dataset is the first closed-loop assessment dataset of student feedback in tourism education. It can accurately and comprehensively evaluate students' performance in tour guide explanations, identify deficiencies, and provide improvement suggestions to enhance students' professional capabilities.

The TourGuide dataset follows a structured format designed to capture the complete evaluation cycle:
- Qid: Unique identifier for each tourism scenario
- Question: Description of the tourist attraction or scenario
- Reference Answer: Expert-crafted model explanation
- Student Answer: Learner's explanation attempt
- Output Label: Numerical score (1-3) assigned by the system
- Model Feedback: Initial evaluation and suggestions
- Student Feedback: Learner's response to evaluation
- Final Feedback: Refined recommendations based on interaction


  We present a representative example from the dataset featuring the Ruins of St. Paul's at night. The example demonstrates three distinct levels of student performance:
  Example from TourGuide Dataset - The Ruins of St. Paul's at Night.
  Reference Answer:  The Ruins of St. Paul's (1602-1637) represents a significant historical landmark in Macau, featuring Renaissance and Baroque architectural elements. Originally East Asia's largest Catholic church until the 1835 fire, its preserved facade showcases exquisite carvings and statues. Two classical street lamps illuminate the structure, creating an atmospheric evening view.
  Student#1 (Score: 3) :  Historical landmark from 16th century, preserved front wall showcases Renaissance and Baroque styles with detailed statues and carvings. Classical street lamps create warm illumination, offering unique historical ambiance.
 Model Feedback :  Strong historical context and architectural detail. Well-structured presentation with clear chronology. Effective description of nighttime atmosphere. Consider adding cultural significance details.
Student#2 (Score: 2) :  Built in 16th century, has beautiful statues and Renaissance style. Two classical street lamps present. Looks historical.
 Model Feedback :  Basic information provided but lacks depth. Add historical significance and architectural details. Improve description organization.
 Student#3 (Score: 1) : Front wall of old church, popular tourist spot.
 Model Feedback : Extremely limited content. Include historical background, architectural features, and cultural significance.



  
