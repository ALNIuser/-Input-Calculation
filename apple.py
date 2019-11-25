number_input = input('Enter the number of apples : ')
school_child = input('Enter the number of students : ')
print('Расчет равного количества яблок на каждого ученика :')
print('- Яблок в корзине было', number_input)
print('- Школьников', school_child, 'человек')
number_apple = int(number_input) // int(school_child)
if int(number_input) < int(school_child):
    print('- Количество яблок меньше количества учеников, поэтому, яблоки раздаваться не будут')
else:
    print("- Каждый ученик получит по", number_apple, 'яблок')
print('- В корзине останется ', int(number_input) % int(school_child) , 'яблок')




