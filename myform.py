import re
from datetime import datetime
from bottle import post, request

@post('/home', method='post')

def my_form():
    name = request.forms.get('NAME')
    mail = request.forms.get('ADRESS')
    # ���������, ��������� �� ��� ���� �����
    if not name or not mail:
        return "Please fill in all fields"
    else: # ��������� ������ ������ ����������� ����� � ������� ����������� ���������
        if not re.match(r"[^@]+@[^@]+\.[^@]+", mail):
            return "Invalid email format" # ���� ������ ������������, ���������� ��������� �� ������
        else:
            date = datetime.today().strftime('%Y-%m-%d') # �������� ������� ����
            return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (name, mail, date) 
        # ���� ��� ������ ��������� ���������, ��������� � ���������� ��������� � ��������� �����, email � ����