# 19. Создайте класс PasswordChecker с методом is_strong(password), который
# проверяет, что пароль длиннее 8 символов и содержит хотя бы одну цифру

class PasswordChecker:

    def __init__(self, password):
        self.password = password

    def is_strong(self):
        if len(self.password) > 8:
            print("True")
        else:
            print("False")

passw = PasswordChecker("hfnjkfbnivbjkwb")
print(passw.is_strong())



