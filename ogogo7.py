def register(username, password, check_password):
    if password == check_password:
        if 8 < len(username) < 40 and 8 <= len(password) < 14:
            print('регистрация успешна')
            with open('database.txt', 'w') as db1:
                db1.write(username + '\n' + password)
                code = 1234
                return code
        else:
            print('не правильная длина логина или пароля!')
    else:
        print('не правильный пароль')


username = input('введите ваш логин: ')
password = input('введите ваш пароль: ')
check_password = input('введите ваш пароль еще раз: ')
answer = register(username, password, check_password)


def check_code(guess, answer):
    if answer == guess:
        print('успешно можете заходить')
    else:
        print('не правильный пароль!')


check_code(1234, answer)

check_nameuser_auth = username
check_password_auth = password


def auth(tries: int):
    count = 0
    while count < tries:
        username1 = input('введите пожалуйста логин: ')
        password1 = input('введите пожалуйста пароль: ')
        username1 = username1.strip()
        password1 = password1.strip()
        if username1 == check_nameuser_auth and password1 == check_password:
            print('вы успешно вошли!!!')
            break
        else:
            print('вы ввели не правильно пароль или логин')
        count += 1


auth(3)

products = ['Acer', 'ASUS razer', 'HP', 'hp zenbook', 'acer aspire', 'ihpone x', 'Iphone PRO MAX', 'samsung galaxy',
            'samsung TAB515',
            'Sony Ericson', 'nokia 3310', 'Nokia WIN', 'adata hdd1tb', 'ADATA SSD', 'Kingston 1tb', 'kiNGston ssd',
            'GeForce RTX',
            'AMD', 'amd rx760', 'Intel HD', 'MacbOOk PRO', 'iMac', 'macbook air', 'lenovo', 'AMD', 'aMd ryzen']


def all_products(products):
    with open('all_prodicts.txt', 'w')as produc:
        for line in products:
            line = line.strip()
            line = line.lower()
            produc.write(line + '\n')


all_products(products)


def sort(phone, computer, hardcard, videocard):
    with open('all_prodicts.txt') as fproduct:
        list_of_product = fproduct.readlines()
        if phone == 'phone':
            with open('phone.txt', 'w') as gphone:
                for line in list_of_product:
                    if 'iphone' in line or 'samsung' in line or 'sony' in line or 'nokia' in line:
                        gphone.write(line)
        elif computer == "computer":
            with open('computer.txt', 'w') as gcomputer:
                for line in list_of_product:
                    if 'acer' in line or 'asus' in line or 'hp' in line or 'mac' in line or 'lenovo' in line:
                        gcomputer.write(line)
        elif videocard == 'videocard':
            with open('videocard.txt', 'w')as gvideocard:
                for line in list_of_product:
                    if 'geforce' in line or 'amd' in line or 'intel' in line:
                        gvideocard.write(line)
        elif hardcard == 'hardcard':
            with open('hardcard.txt', 'w')as ghardcard:
                for line in list_of_product:
                    if 'adata' in line or 'kingston' in line:
                        ghardcard.write(line)
        print('сортировака прошла успешно!!!')


phone = 'phone'
computer = 'computer'
hardcard = 'hardcard'
videocard = 'videocard'
sort(phone, computer, hardcard, videocard)


def my_input():
    my_input = input('введите продукт для введение в консоль: ')
    if my_input == 'phone':
        file_phone = open('phone.txt')
        file_phone = file_phone.readlines()
        print(file_phone)
    elif my_input == 'computer':
        file_computer = open('computer.txt')
        file_computer = file_computer.readlines()
        print(file_computer)
    elif my_input == 'videocard':
        file_videocard = open('videocard.txt')
        file_videocard = file_videocard.readlines()
        print(file_videocard)
    elif my_input == 'hardcard':
        file_hardcard = open('hardcard.txt')
        file_hardcard = file_hardcard.readlines()
        print(file_hardcard)
    else:
        print('вы ввели не правильный продукт')


my_input()
