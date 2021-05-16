number_input = input('Введите количество яблок : ')
school_child = input('Введите количество человек: ')
print(' Расчет равного количества яблок на одного человека:')
print('- Яблок в корзине ', number_input)
print('- Количество людей ', school_child )
number_apple = int(number_input) // int(school_child)
if int(number_input) < int(school_child):
    print('- Количество яблок меньше, чем количество людей, поэтому яблоки раздавать не будут !')
else:
    print("- Each student will receive", number_apple, 'apples')
print('- Will remain in the basket ', int(number_input) % int(school_child) , 'apples')




