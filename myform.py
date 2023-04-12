import re
from bottle import post, request

@post('/home')
def my_form():
    email = request.forms.get('ADRESS')
    # Проверяем, соответствует ли email шаблону регулярного выражения
    pattern = r"[^@]+@[^@]+\.[^@]+"
    if re.match(pattern, email):
        return "Thanks! The answer will be sent to the email %s" % email
    else:
        return "Invalid email address. Please enter a valid email address."
