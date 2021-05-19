from random import randint
number_input = input('Введите количество яблок : ')
school_child = input('Введите количество человек: ')
print(' Расчет равного количества яблок на одного человека:')
print('- Яблок в корзине ', number_input)
print('- Количество людей ', school_child )
number_apple = int(number_input) // int(school_child)
if int(number_input) < int(school_child):
    print('- Количество яблок меньше, чем количество людей, поэтому яблоки раздавать не будут !')
else:
    print("- Каждый человек получит по ", number_apple, 'яблок')
print('- В корзине останется ', int(number_input) % int(school_child) , 'яблок')
#for number in range(5):
#    print(number)
print("Вывод случайного целого числа ", randint(0, 100))




