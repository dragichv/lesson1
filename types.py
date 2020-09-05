"""
a = 2
b = 0.5
print(a + b)

name = 'vitaly'
print('Привет,', name)
"""

#name = input('Введите ваше имя: ')
#print(f'Привет, {name}! Как дела? ')

#v = int(input('Введите число от 1 до 10: '))
#print(v + 10)

f = float('1')
print(type(f))

i = float('2.5')
f = int(i)
print(type(i))

try:
    i = int('2.5')
    print(i)
except Exception:
    print("Is not integer")

b = bool(1)
print(type(b))
print(b)

k = bool('')
print(k)