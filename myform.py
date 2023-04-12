import re
from datetime import datetime
from bottle import post, request

@post('/home', method='post')

def my_form():
    name = request.forms.get('NAME')
    mail = request.forms.get('ADRESS')
    # проверяем, заполнены ли оба поля формы
    if not name or not mail:
        return "Please fill in all fields"
    else: # проверяем формат адреса электронной почты с помощью регулярного выражения
        if not re.match(r"[^@]+@[^@]+\.[^@]+", mail):
            return "Invalid email format" # если формат некорректный, возвращаем сообщение об ошибке
        else:
            date = datetime.today().strftime('%Y-%m-%d') # получаем текущую дату
            return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (name, mail, date) 
        # если все данные заполнены корректно, формируем и возвращаем сообщение с указанием имени, email и даты