number_input = input('Enter the number of apples : ')
school_child = input('Enter the number of students : ')
print('Calculation of an equal number of apples per student :')
print('- The apple in the basket was ', number_input)
print('- Schoolchildren ', school_child, 'человек')
number_apple = int(number_input) // int(school_child)
if int(number_input) < int(school_child):
    print('- 
The number of apples is less than the number of students, therefore, apples will not be distributed ! ')
else:
    print("- Каждый ученик получит по", number_apple, 'яблок')
print('- В корзине останется ', int(number_input) % int(school_child) , 'яблок')




