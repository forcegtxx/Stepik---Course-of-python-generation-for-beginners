def cezar_shifr(stroka, shifr, lang, shift):
    s = ''

    if shifr == 'd':
        shift = -shift

    for i in stroka:
        if i.isalpha():
            if (lang.index(i.lower())+shift) >= len(lang):
                shift -= len(lang)
            if i.isupper():
                s += (lang[lang.index(i.lower())+shift]).upper()
            elif i.islower():
                s += lang[lang.index(i)+shift]
        else:
            s += i

    return s

ru = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
en = "abcdefghijklmnopqrstuvwxyz"

stroka = input('Введите строку:')
lang = input('Выберите, русский или английский алфавит(ru/en):')
if lang == "ru":
    lang = ru
elif lang == "en":
    lang = en
shifr = input('Выберите, шифрование или дешифрование(s/d):')
podbor_shift = 'm'
if shifr == 'd':
    podbor_shift = input('Введите, автоматический подбор шага или ручной(a/m):')
if podbor_shift == 'm':
    shift = int(input('Введите шаг сдвига:'))

if podbor_shift =='m':
    print(cezar_shifr(stroka, shifr, lang, shift))
elif podbor_shift =='a':
    for d in range(len(lang)):
        print(cezar_shifr(stroka, shifr, lang, (d+1)))
        if input('Похоже на строку?(y/n)') == 'y':
            print(f"Шаг дешифрования равен: {d+1}")
            break