from quizzes.models import Quiz, Question

quiz = Quiz.objects.get(title="Aptitude Basic Quiz")

Question.objects.filter(quiz=quiz).delete()

questions = [

{
"question_text":"What is 25% of 200?",
"option_a":"25",
"option_b":"40",
"option_c":"50",
"option_d":"75",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"25% of 200 = 50."
},

{
"question_text":"If the cost price is ₹500 and selling price is ₹600, what is the profit?",
"option_a":"₹50",
"option_b":"₹100",
"option_c":"₹150",
"option_d":"₹200",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"Profit = SP − CP = ₹100."
},

{
"question_text":"Average of 10, 20, 30 is?",
"option_a":"15",
"option_b":"20",
"option_c":"25",
"option_d":"30",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"(10+20+30)/3 = 20."
},

{
"question_text":"2 : 6 :: 5 : ?",
"option_a":"10",
"option_b":"12",
"option_c":"15",
"option_d":"20",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"2×3=6 therefore 5×3=15."
},

{
"question_text":"A train travels 120 km in 2 hours. Speed is?",
"option_a":"40 km/h",
"option_b":"50 km/h",
"option_c":"60 km/h",
"option_d":"70 km/h",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"Speed = Distance / Time = 60 km/h."
},

{
"question_text":"Simple Interest on ₹1000 at 10% for 2 years is?",
"option_a":"₹100",
"option_b":"₹150",
"option_c":"₹200",
"option_d":"₹250",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"SI = P×R×T/100 = ₹200."
},

{
"question_text":"If 5 workers finish a job in 10 days, total work equals?",
"option_a":"40 worker-days",
"option_b":"45 worker-days",
"option_c":"50 worker-days",
"option_d":"55 worker-days",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"5 × 10 = 50 worker-days."
},

{
"question_text":"Find the next number: 2, 4, 8, 16, ?",
"option_a":"20",
"option_b":"24",
"option_c":"30",
"option_d":"32",
"correct_option":"D",
"difficulty":"Easy",
"explanation":"Each number doubles."
},

{
"question_text":"If x = 5, then x² + 3 = ?",
"option_a":"25",
"option_b":"26",
"option_c":"28",
"option_d":"30",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"5² + 3 = 28."
},

{
"question_text":"Which number is divisible by both 2 and 5?",
"option_a":"15",
"option_b":"20",
"option_c":"25",
"option_d":"35",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"20 is divisible by both 2 and 5."
},

{
"question_text":"A shopkeeper buys an item for ₹800 and sells it for ₹920. What is the profit percentage?",
"option_a":"10%",
"option_b":"12%",
"option_c":"15%",
"option_d":"20%",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"Profit = 120. Profit% = (120/800)×100 = 15%."
},

{
"question_text":"The average of 12, 15, 18, 21 and 24 is?",
"option_a":"17",
"option_b":"18",
"option_c":"19",
"option_d":"20",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"(12+15+18+21+24)/5 = 18."
},

{
"question_text":"If 8 men complete a job in 15 days, how many man-days are required?",
"option_a":"100",
"option_b":"110",
"option_c":"120",
"option_d":"130",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"8 × 15 = 120 man-days."
},

{
"question_text":"A train travels 240 km in 4 hours. Its speed is?",
"option_a":"50 km/h",
"option_b":"55 km/h",
"option_c":"60 km/h",
"option_d":"65 km/h",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"240 ÷ 4 = 60 km/h."
},

{
"question_text":"Simple Interest on ₹5000 at 8% for 2 years is?",
"option_a":"₹600",
"option_b":"₹700",
"option_c":"₹800",
"option_d":"₹900",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"SI = (5000×8×2)/100 = ₹800."
},

{
"question_text":"Find the next number: 5, 10, 20, 40, ?",
"option_a":"60",
"option_b":"70",
"option_c":"80",
"option_d":"90",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"Each number doubles."
},

{
"question_text":"If x = 8, then x² is?",
"option_a":"48",
"option_b":"56",
"option_c":"64",
"option_d":"72",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"8 × 8 = 64."
},

{
"question_text":"3 : 9 :: 7 : ?",
"option_a":"18",
"option_b":"20",
"option_c":"21",
"option_d":"24",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"3 × 3 = 9, therefore 7 × 3 = 21."
},

{
"question_text":"If a car covers 150 km using 10 litres of fuel, mileage is?",
"option_a":"10 km/l",
"option_b":"12 km/l",
"option_c":"15 km/l",
"option_d":"20 km/l",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"150 ÷ 10 = 15 km/l."
},

{
"question_text":"Which number is a prime number?",
"option_a":"21",
"option_b":"29",
"option_c":"35",
"option_d":"39",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"29 has only two factors: 1 and 29."
},

{
"question_text":"A sum doubles itself in 10 years at simple interest. What is the annual rate?",
"option_a":"5%",
"option_b":"8%",
"option_c":"10%",
"option_d":"12%",
"correct_option":"C",
"difficulty":"Hard",
"explanation":"100% interest in 10 years means 10% per year."
},

{
"question_text":"If 12 workers complete a job in 15 days, how many days will 18 workers take?",
"option_a":"8",
"option_b":"10",
"option_c":"12",
"option_d":"15",
"correct_option":"B",
"difficulty":"Hard",
"explanation":"Work = 12×15 = 180 worker-days. 180÷18 = 10 days."
},

{
"question_text":"The ratio of boys to girls is 3:2. If there are 30 boys, how many girls are there?",
"option_a":"15",
"option_b":"18",
"option_c":"20",
"option_d":"25",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"3:2 = 30:x → x = 20."
},

{
"question_text":"Find the next number: 1, 4, 9, 16, ?",
"option_a":"20",
"option_b":"24",
"option_c":"25",
"option_d":"36",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"These are perfect squares."
},

{
"question_text":"If a discount of 20% is given on ₹500, what is the selling price?",
"option_a":"₹350",
"option_b":"₹380",
"option_c":"₹400",
"option_d":"₹450",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"20% of 500 = 100. Selling price = 400."
},

{
"question_text":"Compound Interest is calculated on?",
"option_a":"Principal only",
"option_b":"Interest only",
"option_c":"Principal + Previous Interest",
"option_d":"None",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"Compound Interest is calculated on the accumulated amount."
},

{
"question_text":"If 15% of a number is 45, what is the number?",
"option_a":"250",
"option_b":"275",
"option_c":"300",
"option_d":"325",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"45 ÷ 0.15 = 300."
},

{
"question_text":"Which is the smallest prime number?",
"option_a":"0",
"option_b":"1",
"option_c":"2",
"option_d":"3",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"2 is the smallest prime number."
},

{
"question_text":"A car travels 360 km in 6 hours. Its average speed is?",
"option_a":"50 km/h",
"option_b":"55 km/h",
"option_c":"60 km/h",
"option_d":"65 km/h",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"360 ÷ 6 = 60 km/h."
},

{
"question_text":"Find the missing number: 7, 14, 28, 56, ?",
"option_a":"98",
"option_b":"102",
"option_c":"112",
"option_d":"120",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"Each number doubles."
}

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

print("10 Aptitude questions imported successfully.")