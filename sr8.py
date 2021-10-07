def perevod (num,schisl) :
    x = ""
    while num > 0 :
        x+=str(num % schisl)
        num = num // schisl
    return  x[::-1]

try :
    num = int(input('Введите число : '))
    schisl = int (input('Введите желаемую систему счисления (цифрой) : '))
except ValueError :
    print('Введите целое число')
else :
    print (num, '--->',perevod(num,schisl))
