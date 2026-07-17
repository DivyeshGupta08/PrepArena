from quizzes.models import Quiz, Question

quiz = Quiz.objects.get(title="HR Basic Quiz")

Question.objects.filter(quiz=quiz).delete()

questions = [
    
    {
        "question_text": "Why do you want to work for our company?",
        "option_a": "Only for salary",
        "option_b": "I like your company's reputation and growth opportunities",
        "option_c": "My friend works here",
        "option_d": "No specific reason",
        "correct_option": "B",
        "difficulty": "Medium",
        "explanation": "Interviewers expect a company-focused answer."
    },
    {
        "question_text": "How should you answer a question you don't know?",
        "option_a": "Guess randomly",
        "option_b": "Stay silent",
        "option_c": "Honestly admit you don't know and explain how you'd find the answer",
        "option_d": "Change the topic",
        "correct_option": "C",
        "difficulty": "Hard",
        "explanation": "Honesty and problem-solving are valued."
    },
    {
        "question_text": "What is considered a strength in an interview?",
        "option_a": "Laziness",
        "option_b": "Poor communication",
        "option_c": "Adaptability",
        "option_d": "Ignoring deadlines",
        "correct_option": "C",
        "difficulty": "Easy",
        "explanation": "Adaptability is a valuable workplace skill."
    },
    {
        "question_text": "How should you describe a weakness?",
        "option_a": "Mention a weakness and explain how you're improving it",
        "option_b": "Say you have no weaknesses",
        "option_c": "Avoid answering",
        "option_d": "Blame previous employers",
        "correct_option": "A",
        "difficulty": "Medium",
        "explanation": "Show self-awareness and improvement."
    },
    {
        "question_text": "What should you do before attending an interview?",
        "option_a": "Research the company",
        "option_b": "Arrive late",
        "option_c": "Ignore the job description",
        "option_d": "Memorize unrelated facts",
        "correct_option": "A",
        "difficulty": "Easy",
        "explanation": "Preparation shows interest."
    },
    {
        "question_text": "Which quality is most important in teamwork?",
        "option_a": "Communication",
        "option_b": "Ignoring teammates",
        "option_c": "Working alone always",
        "option_d": "Avoiding responsibility",
        "correct_option": "A",
        "difficulty": "Easy",
        "explanation": "Communication is essential for teamwork."
    },
    {
        "question_text": "If you disagree with your manager, what should you do?",
        "option_a": "Argue loudly",
        "option_b": "Respectfully discuss your viewpoint",
        "option_c": "Ignore instructions",
        "option_d": "Leave the job",
        "correct_option": "B",
        "difficulty": "Hard",
        "explanation": "Professional communication is important."
    },
    {
        "question_text": "What is the purpose of a resume?",
        "option_a": "To list hobbies only",
        "option_b": "To summarize qualifications and experience",
        "option_c": "To write stories",
        "option_d": "To advertise products",
        "correct_option": "B",
        "difficulty": "Easy",
        "explanation": "A resume highlights qualifications."
    },
    {
        "question_text": "Which behavior is professional during an interview?",
        "option_a": "Interrupting the interviewer",
        "option_b": "Maintaining eye contact and listening carefully",
        "option_c": "Using your phone",
        "option_d": "Speaking rudely",
        "correct_option": "B",
        "difficulty": "Medium",
        "explanation": "Professional body language creates a good impression."
    },
    {
        "question_text": "What should you do after an interview?",
        "option_a": "Forget about it",
        "option_b": "Send a thank-you email if appropriate",
        "option_c": "Call every hour",
        "option_d": "Post complaints online",
        "correct_option": "B",
        "difficulty": "Medium",
        "explanation": "A thank-you note shows professionalism."
    },
    
    {
        "question_text": "What does HR stand for?",
        "option_a": "Human Resource",
        "option_b": "Human Resources",
        "option_c": "Hiring Resource",
        "option_d": "Human Relation",
        "correct_option": "B",
        "difficulty": "Easy",
        "explanation": "HR stands for Human Resources."
    },
    {
        "question_text": "Which is the best way to introduce yourself in an interview?",
        "option_a": "Talk only about family",
        "option_b": "Talk only about hobbies",
        "option_c": "Give a brief summary of education, skills and experience",
        "option_d": "Ask the interviewer questions first",
        "correct_option": "C",
        "difficulty": "Easy",
        "explanation": "A professional introduction includes education, skills and experience."
    },
    {
        "question_text": "What is punctuality?",
        "option_a": "Completing work on time",
        "option_b": "Coming late every day",
        "option_c": "Ignoring deadlines",
        "option_d": "Leaving early without permission",
        "correct_option": "A",
        "difficulty": "Easy",
        "explanation": "Punctuality means being on time."
    },
    {
        "question_text": "Why do employers ask about your strengths?",
        "option_a": "To reject you",
        "option_b": "To understand your abilities",
        "option_c": "To test handwriting",
        "option_d": "To waste time",
        "correct_option": "B",
        "difficulty": "Medium",
        "explanation": "Employers want to know what value you can bring."
    },
    {
        "question_text": "What should you wear for a professional interview?",
        "option_a": "Casual shorts",
        "option_b": "Party clothes",
        "option_c": "Formal attire",
        "option_d": "Sportswear",
        "correct_option": "C",
        "difficulty": "Easy",
        "explanation": "Professional dress creates a good first impression."
    },
    {
        "question_text": "If you make a mistake at work, what should you do?",
        "option_a": "Hide it",
        "option_b": "Blame others",
        "option_c": "Accept it and fix it",
        "option_d": "Ignore it",
        "correct_option": "C",
        "difficulty": "Medium",
        "explanation": "Taking responsibility shows professionalism."
    },
    {
        "question_text": "What is a positive attitude?",
        "option_a": "Complaining constantly",
        "option_b": "Being willing to learn and improve",
        "option_c": "Ignoring feedback",
        "option_d": "Avoiding work",
        "correct_option": "B",
        "difficulty": "Medium",
        "explanation": "A positive attitude means being open to learning."
    },
    {
        "question_text": "Which skill is most valuable in customer service?",
        "option_a": "Communication",
        "option_b": "Sleeping",
        "option_c": "Arguing",
        "option_d": "Ignoring customers",
        "correct_option": "A",
        "difficulty": "Easy",
        "explanation": "Communication is essential in customer service."
    },
    {
        "question_text": "What should you do if you don't understand a task?",
        "option_a": "Guess",
        "option_b": "Ask for clarification",
        "option_c": "Ignore it",
        "option_d": "Leave the office",
        "correct_option": "B",
        "difficulty": "Medium",
        "explanation": "Clarifying instructions prevents mistakes."
    },
    {
        "question_text": "Which quality do employers value the most?",
        "option_a": "Honesty",
        "option_b": "Carelessness",
        "option_c": "Laziness",
        "option_d": "Disrespect",
        "correct_option": "A",
        "difficulty": "Easy",
        "explanation": "Honesty builds trust in the workplace."
    },

    {
        "question_text": "What is the main purpose of an interview?",
        "option_a": "Entertainment",
        "option_b": "Evaluate candidate suitability",
        "option_c": "Sell products",
        "option_d": "Sign contracts",
        "correct_option": "B",
        "difficulty": "Easy",
        "explanation": "Interviews assess whether a candidate is suitable for the role."
    },
    {
        "question_text": "Which skill helps resolve workplace conflicts?",
        "option_a": "Communication",
        "option_b": "Ignoring people",
        "option_c": "Anger",
        "option_d": "Avoidance",
        "correct_option": "A",
        "difficulty": "Medium",
        "explanation": "Good communication helps solve conflicts professionally."
    },
    {
        "question_text": "What should you do if you receive constructive criticism?",
        "option_a": "Get angry",
        "option_b": "Ignore it",
        "option_c": "Accept it and improve",
        "option_d": "Quit",
        "correct_option": "C",
        "difficulty": "Medium",
        "explanation": "Constructive criticism helps you grow."
    },
    {
        "question_text": "Which is an example of leadership?",
        "option_a": "Blaming teammates",
        "option_b": "Guiding the team toward goals",
        "option_c": "Avoiding responsibility",
        "option_d": "Working against the team",
        "correct_option": "B",
        "difficulty": "Hard",
        "explanation": "Leaders guide and motivate their teams."
    },
    {
        "question_text": "Why is teamwork important?",
        "option_a": "To increase conflicts",
        "option_b": "To achieve goals together",
        "option_c": "To avoid communication",
        "option_d": "To reduce productivity",
        "correct_option": "B",
        "difficulty": "Easy",
        "explanation": "Teamwork improves efficiency and productivity."
    },
    {
        "question_text": "What should you do if you finish your work early?",
        "option_a": "Leave the office",
        "option_b": "Browse social media",
        "option_c": "Ask for additional work",
        "option_d": "Sleep",
        "correct_option": "C",
        "difficulty": "Medium",
        "explanation": "Taking initiative creates a positive impression."
    },
    {
        "question_text": "Which quality builds trust with colleagues?",
        "option_a": "Dishonesty",
        "option_b": "Reliability",
        "option_c": "Excuses",
        "option_d": "Carelessness",
        "correct_option": "B",
        "difficulty": "Medium",
        "explanation": "Reliable employees earn trust."
    },
    {
        "question_text": "What should you do before answering an interview question?",
        "option_a": "Interrupt",
        "option_b": "Listen carefully",
        "option_c": "Guess",
        "option_d": "Avoid eye contact",
        "correct_option": "B",
        "difficulty": "Easy",
        "explanation": "Listening carefully ensures accurate answers."
    },
    {
        "question_text": "What is professionalism?",
        "option_a": "Being irresponsible",
        "option_b": "Displaying respectful and ethical behavior",
        "option_c": "Breaking rules",
        "option_d": "Ignoring deadlines",
        "correct_option": "B",
        "difficulty": "Hard",
        "explanation": "Professionalism means acting responsibly and ethically."
    },
    {
        "question_text": "What is the best way to end an interview?",
        "option_a": "Leave without speaking",
        "option_b": "Thank the interviewer politely",
        "option_c": "Demand immediate selection",
        "option_d": "Criticize the company",
        "correct_option": "B",
        "difficulty": "Easy",
        "explanation": "A polite thank-you leaves a positive final impression."
    },

]

for q in questions:
    Question.objects.create(
        quiz=quiz,
        question_text=q["question_text"],
        option_a=q["option_a"],
        option_b=q["option_b"],
        option_c=q["option_c"],
        option_d=q["option_d"],
        correct_option=q["correct_option"],
        explanation=q["explanation"],
        difficulty=q["difficulty"],
    )

print("10 HR questions imported successfully.")