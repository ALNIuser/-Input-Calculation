from random import randint
#number_input = input('Введите количество яблок : ')
#school_child = input('Введите количество человек: ')
#print(' Расчет равного количества яблок на одного человека:')
#print('- Яблок в корзине ', number_input)
#print('- Количество людей ', school_child)
#number_apple = int(number_input) // int(school_child)
#if int(number_input) < int(school_child):
#    print('- Количество яблок меньше, чем количество людей, поэтому яблоки раздавать не будут !')
#else:
#    print("- Каждый человек получит по ", number_apple, 'яблок')
#print('- В корзине останется ', int(number_input) % int(school_child) , 'яблок')

def zz():
 y = randint(1, 30)
 x = y + randint(50, 100)
 #   if x < y:
 z = x // y
 print('test', str(z))
 return z
for number in range(3):
  x = zz()
  print(x)
  x += randint(50, 100)
  print(x)
#print("Вывод случайного целого числа ", randint(0, 100))




