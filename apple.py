number_input = input('Введите количество яблок : ')
school_child = input('Введите количество человек: ')
print(' Расчет равного количества яблок на одного человека:')
print('- Яблок в корзине ', number_input)
print('- Количество людей ', school_child )
number_apple = int(number_input) // int(school_child)
if int(number_input) < int(school_child):
    print('-The number of apples is less than the number of students, therefore, apples will not be distributed !')
else:
    print("- Each student will receive", number_apple, 'apples')
print('- Will remain in the basket ', int(number_input) % int(school_child) , 'apples')




