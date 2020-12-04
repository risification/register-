def register(username, password, check_password):
    if password == check_password and 8 < len(username) < 40 and 8 < len(password) < 14:
        print('регистрация успешна')
        with open('dstabase.txt', 'w') as bd1:
            bd1.write(username + '\n' + password)
        code = 1234
        return code
    else:
        print('неправильная длина или пароль не совпадают')


answer = register('username.com', '12345678a', '12345678a')


def check_code(guess, answer):
    if answer == guess:
        print('Все успешно можете заходить')
    else:
        print('неверный код')


check_code(1234, answer)


#def auth():
#    pass


#def sort():
#    pass
