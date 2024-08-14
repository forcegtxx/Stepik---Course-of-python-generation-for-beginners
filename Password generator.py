import random as r

def generate_password(lenght, chars):
    password = ''
    a = list(chars)
    r.shuffle(a)
    for _ in range(lenght):
        b = r.choice(a)
        if b.isalpha():
            if ABC_on == 'y' and abc_on == 'y':
                if r.randint(0, 1) == 1:
                    password += b.upper()
                else:
                    password += b
            else:
                if ABC_on == 'y':
                    password += b.upper()
                elif abc_on == 'y':
                    password += b
        else:
            password += b
        
    return password

cnt_passw = int(input('Укажите количество паролей для генерации:'))
lenght = int(input('Укажите длину одного пароля:'))
digit_on = input('Включать ли цифры 0123456789? (y/n)')
ABC_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abc_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
chars_on = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
exc_on = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')

chars = ''

if digit_on == 'y':
    if exc_on == 'y':
        chars += "23456789"
    else:
        chars += "0123456789"

if ABC_on == 'y' or abc_on == 'y':
    if exc_on == 'y':
        chars += "abcdefghjkmnpqrstuvwxyz"
    else:
        chars += "abcdefghijklmnopqrstuvwxyz"

if chars_on == 'y':
    chars += "!#$%&*+-=?@^_"
   
for _ in range(cnt_passw):
    print(generate_password(lenght, chars))