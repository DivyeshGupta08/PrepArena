from quizzes.models import Quiz, Question

quiz = Quiz.objects.get(title="SQL Basic Quiz")

Question.objects.filter(quiz=quiz).delete()

questions = [

{
"question_text":"What does SQL stand for?",
"option_a":"Structured Query Language",
"option_b":"Simple Query Language",
"option_c":"Sequential Query Language",
"option_d":"Standard Question Language",
"correct_option":"A",
"difficulty":"Easy",
"explanation":"SQL stands for Structured Query Language."
},

{
"question_text":"Which SQL statement retrieves data from a table?",
"option_a":"GET",
"option_b":"SELECT",
"option_c":"SHOW",
"option_d":"FETCH",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"SELECT is used to retrieve records."
},

{
"question_text":"Which SQL statement inserts new data?",
"option_a":"ADD",
"option_b":"INSERT INTO",
"option_c":"NEW",
"option_d":"CREATE",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"INSERT INTO adds new rows."
},

{
"question_text":"Which SQL statement updates existing records?",
"option_a":"UPDATE",
"option_b":"MODIFY",
"option_c":"ALTER",
"option_d":"CHANGE",
"correct_option":"A",
"difficulty":"Easy",
"explanation":"UPDATE modifies existing data."
},

{
"question_text":"Which SQL statement deletes records?",
"option_a":"REMOVE",
"option_b":"DELETE",
"option_c":"DROP",
"option_d":"CLEAR",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"DELETE removes rows from a table."
},

{
"question_text":"Which clause filters records?",
"option_a":"GROUP BY",
"option_b":"WHERE",
"option_c":"ORDER BY",
"option_d":"HAVING",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"WHERE filters rows."
},

{
"question_text":"Which keyword sorts query results?",
"option_a":"SORT BY",
"option_b":"ORDER BY",
"option_c":"ARRANGE",
"option_d":"GROUP",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"ORDER BY sorts records."
},

{
"question_text":"Which SQL function counts rows?",
"option_a":"SUM()",
"option_b":"COUNT()",
"option_c":"TOTAL()",
"option_d":"NUMBER()",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"COUNT() returns the number of rows."
},

{
"question_text":"Which SQL keyword removes duplicate records?",
"option_a":"UNIQUE",
"option_b":"DISTINCT",
"option_c":"DIFFERENT",
"option_d":"FILTER",
"correct_option":"B",
"difficulty":"Medium",
"explanation":"DISTINCT returns unique values."
},

{
"question_text":"Which SQL operator matches a pattern?",
"option_a":"MATCH",
"option_b":"LIKE",
"option_c":"SIMILAR",
"option_d":"PATTERN",
"correct_option":"B",
"difficulty":"Medium",
"explanation":"LIKE is used with wildcard searches."
},

{
"question_text":"Which SQL clause groups rows with the same values?",
"option_a":"ORDER BY",
"option_b":"GROUP BY",
"option_c":"WHERE",
"option_d":"HAVING",
"correct_option":"B",
"difficulty":"Medium",
"explanation":"GROUP BY groups rows having the same values."
},

{
"question_text":"Which clause filters grouped records?",
"option_a":"WHERE",
"option_b":"HAVING",
"option_c":"ORDER BY",
"option_d":"LIMIT",
"correct_option":"B",
"difficulty":"Medium",
"explanation":"HAVING filters groups after GROUP BY."
},

{
"question_text":"Which SQL function returns the highest value?",
"option_a":"TOP()",
"option_b":"MAX()",
"option_c":"HIGH()",
"option_d":"UPPER()",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"MAX() returns the largest value."
},

{
"question_text":"Which SQL function returns the lowest value?",
"option_a":"LOW()",
"option_b":"MIN()",
"option_c":"BOTTOM()",
"option_d":"FIRST()",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"MIN() returns the smallest value."
},

{
"question_text":"Which SQL function returns the average value?",
"option_a":"AVG()",
"option_b":"MEAN()",
"option_c":"AVERAGE()",
"option_d":"MID()",
"correct_option":"A",
"difficulty":"Easy",
"explanation":"AVG() calculates the average."
},

{
"question_text":"Which SQL function returns the total sum?",
"option_a":"COUNT()",
"option_b":"ADD()",
"option_c":"SUM()",
"option_d":"TOTAL()",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"SUM() adds numeric values."
},

{
"question_text":"Which JOIN returns matching rows from both tables?",
"option_a":"LEFT JOIN",
"option_b":"RIGHT JOIN",
"option_c":"INNER JOIN",
"option_d":"FULL JOIN",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"INNER JOIN returns only matching records."
},

{
"question_text":"Which JOIN returns all rows from the left table?",
"option_a":"LEFT JOIN",
"option_b":"RIGHT JOIN",
"option_c":"INNER JOIN",
"option_d":"CROSS JOIN",
"correct_option":"A",
"difficulty":"Medium",
"explanation":"LEFT JOIN returns all rows from the left table."
},

{
"question_text":"Which command creates a new table?",
"option_a":"NEW TABLE",
"option_b":"MAKE TABLE",
"option_c":"CREATE TABLE",
"option_d":"ADD TABLE",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"CREATE TABLE creates a new table."
},

{
"question_text":"Which command permanently removes a table?",
"option_a":"DELETE TABLE",
"option_b":"REMOVE TABLE",
"option_c":"DROP TABLE",
"option_d":"CLEAR TABLE",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"DROP TABLE permanently deletes the table."
},

{
"question_text":"Which command modifies an existing table structure?",
"option_a":"UPDATE TABLE",
"option_b":"ALTER TABLE",
"option_c":"CHANGE TABLE",
"option_d":"MODIFY TABLE",
"correct_option":"B",
"difficulty":"Medium",
"explanation":"ALTER TABLE changes the structure of an existing table."
},

{
"question_text":"Which constraint uniquely identifies each row?",
"option_a":"UNIQUE",
"option_b":"PRIMARY KEY",
"option_c":"FOREIGN KEY",
"option_d":"NOT NULL",
"correct_option":"B",
"difficulty":"Medium",
"explanation":"PRIMARY KEY uniquely identifies every record."
},

{
"question_text":"Which constraint creates a relationship between two tables?",
"option_a":"PRIMARY KEY",
"option_b":"UNIQUE",
"option_c":"FOREIGN KEY",
"option_d":"CHECK",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"FOREIGN KEY links two tables."
},

{
"question_text":"Which constraint prevents NULL values?",
"option_a":"CHECK",
"option_b":"NOT NULL",
"option_c":"PRIMARY KEY",
"option_d":"DEFAULT",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"NOT NULL ensures a value is always provided."
},

{
"question_text":"Which SQL statement removes all rows but keeps the table?",
"option_a":"DELETE",
"option_b":"DROP",
"option_c":"TRUNCATE",
"option_d":"REMOVE",
"correct_option":"C",
"difficulty":"Hard",
"explanation":"TRUNCATE removes all records but preserves the table."
},

{
"question_text":"Which wildcard represents multiple characters in LIKE?",
"option_a":"_",
"option_b":"%",
"option_c":"*",
"option_d":"#",
"correct_option":"B",
"difficulty":"Medium",
"explanation":"% matches zero or more characters."
},

{
"question_text":"Which wildcard represents exactly one character?",
"option_a":"%",
"option_b":"_",
"option_c":"*",
"option_d":"?",
"correct_option":"B",
"difficulty":"Medium",
"explanation":"_ matches exactly one character."
},

{
"question_text":"Which SQL clause limits the number of returned rows?",
"option_a":"TOP",
"option_b":"LIMIT",
"option_c":"FETCH",
"option_d":"Both TOP and LIMIT depending on SQL database",
"correct_option":"D",
"difficulty":"Hard",
"explanation":"LIMIT is used in MySQL/PostgreSQL while TOP is used in SQL Server."
},

{
"question_text":"Which command saves the current transaction permanently?",
"option_a":"SAVE",
"option_b":"COMMIT",
"option_c":"CONFIRM",
"option_d":"FINISH",
"correct_option":"B",
"difficulty":"Hard",
"explanation":"COMMIT permanently saves the transaction."
},

{
"question_text":"Which command undoes changes before COMMIT?",
"option_a":"UNDO",
"option_b":"ROLLBACK",
"option_c":"REVERT",
"option_d":"CANCEL",
"correct_option":"B",
"difficulty":"Hard",
"explanation":"ROLLBACK reverts uncommitted changes."
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

print("10 SQL questions imported successfully.")