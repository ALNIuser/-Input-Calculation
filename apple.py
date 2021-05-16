number_input = input('Введите количество яблок : ')
school_child = input('Enter the number of students: ')
print('Calculation of an equal number of apples per student :')
print('- The apple in the basket was ', number_input)
print('- Number of students ', school_child, 'человек')
number_apple = int(number_input) // int(school_child)
if int(number_input) < int(school_child):
    print('-The number of apples is less than the number of students, therefore, apples will not be distributed !')
else:
    print("- Each student will receive", number_apple, 'apples')
print('- Will remain in the basket ', int(number_input) % int(school_child) , 'apples')




