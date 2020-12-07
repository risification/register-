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


username = input('Please input your username: ')
password = input('Please input your password: ')
check_password = input('Please input your password again: ')
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
        if username1 == check_nameuser_auth:
            if password1 == check_password:
                print('вы успешно вошли!!!')
                break
            else:
                print('пароль не сопадает пожалуйста повторите пароль')
        else:
            print("логин не совпадает повторите логин")
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


def sort(option):
    with open('all_prodicts.txt') as fproduct:
        list_of_product = fproduct.readlines()
        if option == 'phone':
            with open('phone.txt', 'w') as gphone:
                for line in list_of_product:
                    if 'iphone' in line or 'samsung' in line or 'sony' in line or 'nokia' in line:
                        gphone.write(line)
        elif option == "computer":
            with open('computer.txt', 'w') as gcomputer:
                for line in list_of_product:
                    if 'acer' in line or 'asus' in line or 'hp' in line or 'mac' in line or 'lenovo' in line:
                        gcomputer.write(line)
        elif option == 'vedeocard':
            with open('videocard.txt', 'w')as gvideocard:
                for line in list_of_product:
                    if 'geforce' in line or 'amd' in line or 'intel' in line:
                        gvideocard.write(line)
        elif option == 'hardcard':
            with open('hardcard.txt', 'w')as ghardcard:
                for line in list_of_product:
                    if 'adata' in line or 'kingston' in line:
                        ghardcard.write(line)
        print('сортировака прошла успешно!!!')


def my_input():
    my_input = input('введите продукт: ')
    sort(my_input)


my_input()
