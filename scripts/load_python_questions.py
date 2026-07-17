from quizzes.models import Quiz, Question

quiz = Quiz.objects.get(title="Python Basics Quiz")

Question.objects.filter(quiz=quiz).delete()

questions = [

{
"question_text":"What is the correct extension of Python files?",
"option_a":".pt",
"option_b":".python",
"option_c":".py",
"option_d":".p",
"correct_option":"C",
"explanation":"Python source files use the .py extension.",
"difficulty":"Easy"
},

{
"question_text":"Which keyword is used to define a function?",
"option_a":"func",
"option_b":"function",
"option_c":"define",
"option_d":"def",
"correct_option":"D",
"explanation":"Functions are defined using def.",
"difficulty":"Easy"
},

{
"question_text":"Which function is used to display output?",
"option_a":"echo()",
"option_b":"printf()",
"option_c":"display()",
"option_d":"print()",
"correct_option":"D",
"explanation":"print() displays output.",
"difficulty":"Easy"
},

{
"question_text":"Which symbol starts a comment in Python?",
"option_a":"//",
"option_b":"#",
"option_c":"/*",
"option_d":"--",
"correct_option":"B",
"explanation":"Python uses # for comments.",
"difficulty":"Easy"
},

{
"question_text":"Which data type is returned by input()?",
"option_a":"int",
"option_b":"float",
"option_c":"str",
"option_d":"bool",
"correct_option":"C",
"explanation":"input() always returns a string.",
"difficulty":"Easy"
},

{
"question_text":"Which bracket creates a list?",
"option_a":"{}",
"option_b":"()",
"option_c":"[]",
"option_d":"<>",
"correct_option":"C",
"explanation":"Lists are created with square brackets.",
"difficulty":"Easy"
},

{
"question_text":"What is len('Python')?",
"option_a":"5",
"option_b":"6",
"option_c":"7",
"option_d":"8",
"correct_option":"B",
"explanation":"Python has six letters.",
"difficulty":"Easy"
},

{
"question_text":"Which operator is used for exponentiation?",
"option_a":"^",
"option_b":"**",
"option_c":"//",
"option_d":"%",
"correct_option":"B",
"explanation":"** calculates powers.",
"difficulty":"Medium"
},

{
"question_text":"Which keyword creates a class?",
"option_a":"object",
"option_b":"class",
"option_c":"struct",
"option_d":"new",
"correct_option":"B",
"explanation":"Classes are declared using class.",
"difficulty":"Medium"
},

{
"question_text":"Which of these is immutable?",
"option_a":"List",
"option_b":"Dictionary",
"option_c":"Tuple",
"option_d":"Set",
"correct_option":"C",
"explanation":"Tuples cannot be modified.",
"difficulty":"Medium"
},

{
"question_text":"Which keyword is used to handle exceptions?",
"option_a":"try",
"option_b":"catch",
"option_c":"except",
"option_d":"error",
"correct_option":"A",
"explanation":"Exception handling starts with try.",
"difficulty":"Medium"
},

{
"question_text":"Which block always executes whether an exception occurs or not?",
"option_a":"catch",
"option_b":"final",
"option_c":"finally",
"option_d":"last",
"correct_option":"C",
"explanation":"finally always executes.",
"difficulty":"Medium"
},

{
"question_text":"Which function converts a string into an integer?",
"option_a":"str()",
"option_b":"float()",
"option_c":"int()",
"option_d":"bool()",
"correct_option":"C",
"explanation":"int() converts numeric strings to integers.",
"difficulty":"Easy"
},

{
"question_text":"Which loop is preferred when the number of iterations is known?",
"option_a":"while",
"option_b":"repeat",
"option_c":"loop",
"option_d":"for",
"correct_option":"D",
"explanation":"for loops are used when the iteration count is known.",
"difficulty":"Medium"
},

{
"question_text":"Which keyword skips the current iteration of a loop?",
"option_a":"break",
"option_b":"continue",
"option_c":"pass",
"option_d":"skip",
"correct_option":"B",
"explanation":"continue skips only the current iteration.",
"difficulty":"Medium"
},

{
"question_text":"Which keyword exits a loop immediately?",
"option_a":"exit",
"option_b":"stop",
"option_c":"break",
"option_d":"return",
"correct_option":"C",
"explanation":"break terminates the loop.",
"difficulty":"Easy"
},

{
"question_text":"Which module provides sqrt() and factorial()?",
"option_a":"math",
"option_b":"random",
"option_c":"os",
"option_d":"sys",
"correct_option":"A",
"explanation":"The math module provides mathematical functions.",
"difficulty":"Medium"
},

{
"question_text":"Which built-in function returns the largest value?",
"option_a":"largest()",
"option_b":"top()",
"option_c":"high()",
"option_d":"max()",
"correct_option":"D",
"explanation":"max() returns the largest value.",
"difficulty":"Easy"
},

{
"question_text":"What is the result of 10 // 3 ?",
"option_a":"3.33",
"option_b":"3",
"option_c":"4",
"option_d":"1",
"correct_option":"B",
"explanation":"// performs floor division.",
"difficulty":"Medium"
},

{
"question_text":"Which of these is a Python dictionary?",
"option_a":"[1,2,3]",
"option_b":"(1,2,3)",
"option_c":"{'a':1,'b':2}",
"option_d":"{1,2,3}",
"correct_option":"C",
"explanation":"Key-value pairs represent dictionaries.",
"difficulty":"Medium"
},

{
"question_text":"Which keyword is used to import a module?",
"option_a":"include",
"option_b":"using",
"option_c":"import",
"option_d":"require",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"Modules are imported using the import keyword."
},

{
"question_text":"Which function returns the type of an object?",
"option_a":"typeof()",
"option_b":"type()",
"option_c":"class()",
"option_d":"object()",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"type() returns the object's type."
},

{
"question_text":"Which statement is used to define an anonymous function?",
"option_a":"lambda",
"option_b":"anonymous",
"option_c":"func",
"option_d":"def",
"correct_option":"A",
"difficulty":"Hard",
"explanation":"lambda creates anonymous functions."
},

{
"question_text":"Which keyword is used to inherit a class?",
"option_a":"extends",
"option_b":"inherits",
"option_c":"super",
"option_d":"Use parent class inside parentheses",
"correct_option":"D",
"difficulty":"Intermediate",
"explanation":"Inheritance is done by passing the parent class inside parentheses."
},

{
"question_text":"Which collection stores unique values?",
"option_a":"List",
"option_b":"Tuple",
"option_c":"Dictionary",
"option_d":"Set",
"correct_option":"D",
"difficulty":"Medium",
"explanation":"Sets contain unique elements."
},

{
"question_text":"Which keyword creates a generator?",
"option_a":"yield",
"option_b":"return",
"option_c":"generate",
"option_d":"next",
"correct_option":"A",
"difficulty":"Hard",
"explanation":"yield is used in generator functions."
},

{
"question_text":"Which function opens a file?",
"option_a":"read()",
"option_b":"open()",
"option_c":"file()",
"option_d":"load()",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"open() is used for file handling."
},

{
"question_text":"Which mode opens a file for appending?",
"option_a":"r",
"option_b":"w",
"option_c":"a",
"option_d":"x",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"a opens a file in append mode."
},

{
"question_text":"Which keyword is used to remove an object?",
"option_a":"remove",
"option_b":"delete",
"option_c":"del",
"option_d":"clear",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"del removes variables or objects."
},

{
"question_text":"Which function returns the number of items in a list?",
"option_a":"count()",
"option_b":"length()",
"option_c":"size()",
"option_d":"len()",
"correct_option":"D",
"difficulty":"Easy",
"explanation":"len() returns the number of elements."
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

print("10 Python questions imported successfully.")