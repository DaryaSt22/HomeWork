# 16. Создайте класс EmailValidator с методом is_valid(email), который проверяет,
# содержит ли email символ '@' и точку '.'.

class EmailValidator:

    def __init__(self, email):
        self.email = email

    def is_valid_email(self):
        if "@" and "." in self.email :
            print("True")
        else:
            print("False")

p = EmailValidator("fhkevb@.com")
print(p.is_valid_email())