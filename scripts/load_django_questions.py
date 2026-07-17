from quizzes.models import Quiz, Question

quiz = Quiz.objects.get(title="Django Basic Quiz")

Question.objects.filter(quiz=quiz).delete()

questions = [

{
"question_text":"What is Django?",
"option_a":"Java Framework",
"option_b":"Python Web Framework",
"option_c":"Database",
"option_d":"IDE",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"Django is a high-level Python web framework."
},

{
"question_text":"Which command creates a new Django project?",
"option_a":"django-admin startproject",
"option_b":"django start",
"option_c":"python newproject",
"option_d":"django create",
"correct_option":"A",
"difficulty":"Easy",
"explanation":"django-admin startproject creates a project."
},

{
"question_text":"Which command starts the development server?",
"option_a":"python manage.py server",
"option_b":"python manage.py run",
"option_c":"python manage.py runserver",
"option_d":"django runserver",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"runserver starts Django's development server."
},

{
"question_text":"Which file contains installed apps?",
"option_a":"urls.py",
"option_b":"views.py",
"option_c":"models.py",
"option_d":"settings.py",
"correct_option":"D",
"difficulty":"Easy",
"explanation":"INSTALLED_APPS is inside settings.py."
},

{
"question_text":"Which ORM does Django use?",
"option_a":"SQLAlchemy",
"option_b":"Hibernate",
"option_c":"Django ORM",
"option_d":"Entity Framework",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"Django has its own built-in ORM."
},

{
"question_text":"Which file maps URLs to views?",
"option_a":"models.py",
"option_b":"urls.py",
"option_c":"admin.py",
"option_d":"forms.py",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"urls.py contains URL patterns."
},

{
"question_text":"Which command creates migrations?",
"option_a":"python manage.py makemigrations",
"option_b":"python manage.py migrate",
"option_c":"python manage.py collectstatic",
"option_d":"python manage.py shell",
"correct_option":"A",
"difficulty":"Medium",
"explanation":"makemigrations generates migration files."
},

{
"question_text":"Which command applies migrations?",
"option_a":"makemigrations",
"option_b":"migrate",
"option_c":"syncdb",
"option_d":"dbupdate",
"correct_option":"B",
"difficulty":"Medium",
"explanation":"migrate applies changes to the database."
},

{
"question_text":"Which file defines database models?",
"option_a":"views.py",
"option_b":"admin.py",
"option_c":"models.py",
"option_d":"urls.py",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"Database tables are defined in models.py."
},

{
"question_text":"Which Django component handles business logic?",
"option_a":"Template",
"option_b":"View",
"option_c":"Static",
"option_d":"Migration",
"correct_option":"B",
"difficulty":"Medium",
"explanation":"Views process requests and return responses."
},

{
"question_text":"Which command creates a new Django app?",
"option_a":"python manage.py newapp",
"option_b":"python manage.py startapp",
"option_c":"django-admin app",
"option_d":"python app.py",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"startapp creates a new Django application."
},

{
"question_text":"Which file is used to register models in Django Admin?",
"option_a":"views.py",
"option_b":"settings.py",
"option_c":"admin.py",
"option_d":"apps.py",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"Models are registered in admin.py."
},

{
"question_text":"Which decorator restricts a view to logged-in users?",
"option_a":"@admin_required",
"option_b":"@login_required",
"option_c":"@authenticated",
"option_d":"@user_required",
"correct_option":"B",
"difficulty":"Medium",
"explanation":"@login_required protects views."
},

{
"question_text":"Which template syntax prints a variable?",
"option_a":"{{ variable }}",
"option_b":"{% variable %}",
"option_c":"<%= variable %>",
"option_d":"${variable}",
"correct_option":"A",
"difficulty":"Easy",
"explanation":"Variables are displayed using double curly braces."
},

{
"question_text":"Which template tag is used for loops?",
"option_a":"{% while %}",
"option_b":"{% repeat %}",
"option_c":"{% for %}",
"option_d":"{% loop %}",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"{% for %} iterates over objects."
},

{
"question_text":"Which shortcut returns a 404 if an object does not exist?",
"option_a":"get()",
"option_b":"find_object()",
"option_c":"object_or_404()",
"option_d":"get_object_or_404()",
"correct_option":"D",
"difficulty":"Medium",
"explanation":"get_object_or_404() raises Http404."
},

{
"question_text":"Which model field stores long text?",
"option_a":"CharField",
"option_b":"IntegerField",
"option_c":"TextField",
"option_d":"FloatField",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"TextField stores long text."
},

{
"question_text":"Which model field stores True or False?",
"option_a":"BooleanField",
"option_b":"CharField",
"option_c":"BinaryField",
"option_d":"IntegerField",
"correct_option":"A",
"difficulty":"Easy",
"explanation":"BooleanField stores boolean values."
},

{
"question_text":"Which command opens the Django shell?",
"option_a":"python manage.py console",
"option_b":"python manage.py shell",
"option_c":"python manage.py terminal",
"option_d":"python shell.py",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"shell opens the interactive Django shell."
},

{
"question_text":"Which setting file contains DATABASES configuration?",
"option_a":"urls.py",
"option_b":"settings.py",
"option_c":"admin.py",
"option_d":"models.py",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"DATABASES is configured in settings.py."
},

{
"question_text":"Which model field creates a relationship to another model?",
"option_a":"RelationField",
"option_b":"ForeignKey",
"option_c":"ConnectField",
"option_d":"LinkField",
"correct_option":"B",
"difficulty":"Medium",
"explanation":"ForeignKey creates a many-to-one relationship."
},

{
"question_text":"Which relationship represents many-to-many?",
"option_a":"ForeignKey",
"option_b":"OneToOneField",
"option_c":"ManyToManyField",
"option_d":"RelationField",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"ManyToManyField creates many-to-many relationships."
},

{
"question_text":"Which relationship allows exactly one related object?",
"option_a":"ForeignKey",
"option_b":"ManyToManyField",
"option_c":"OneToOneField",
"option_d":"UniqueField",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"OneToOneField creates a one-to-one relationship."
},

{
"question_text":"Which function renders an HTML template?",
"option_a":"render()",
"option_b":"display()",
"option_c":"response()",
"option_d":"show()",
"correct_option":"A",
"difficulty":"Easy",
"explanation":"render() returns an HTML response."
},

{
"question_text":"Which HTTP method is generally used to create data?",
"option_a":"GET",
"option_b":"POST",
"option_c":"DELETE",
"option_d":"HEAD",
"correct_option":"B",
"difficulty":"Easy",
"explanation":"POST is used to submit new data."
},

{
"question_text":"Which HTTP method updates existing data?",
"option_a":"POST",
"option_b":"PUT",
"option_c":"GET",
"option_d":"OPTIONS",
"correct_option":"B",
"difficulty":"Medium",
"explanation":"PUT updates existing resources."
},

{
"question_text":"Which package is commonly used to build REST APIs in Django?",
"option_a":"FastAPI",
"option_b":"Flask",
"option_c":"Django REST Framework",
"option_d":"Bottle",
"correct_option":"C",
"difficulty":"Medium",
"explanation":"DRF is the standard API framework for Django."
},

{
"question_text":"Which serializer converts model objects into JSON?",
"option_a":"ModelSerializer",
"option_b":"JsonField",
"option_c":"APIView",
"option_d":"JsonResponse",
"correct_option":"A",
"difficulty":"Hard",
"explanation":"ModelSerializer automatically serializes model fields."
},

{
"question_text":"Which authentication method did you use in PrepArena APIs?",
"option_a":"JWT",
"option_b":"Session",
"option_c":"OAuth",
"option_d":"Token Authentication",
"correct_option":"D",
"difficulty":"Hard",
"explanation":"PrepArena uses DRF Token Authentication."
},

{
"question_text":"Which file contains URL patterns for an app?",
"option_a":"models.py",
"option_b":"admin.py",
"option_c":"urls.py",
"option_d":"apps.py",
"correct_option":"C",
"difficulty":"Easy",
"explanation":"App routes are defined in urls.py."
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

print("10 Django questions imported successfully.")