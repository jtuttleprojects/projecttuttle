#John Tuttle
#2025/10/09
#Project #4
#user inputs number the program tells a joke :)


print('welcome to my joke telling game!')
print()
print('pick a joke number:')
print('1. science joke')
print('2. dad joke')
print('3. programming joke')
print('4. animal joke')
print('5. food joke')

choice = input('enter your choice (1-5): ')

if choice == '1':
    print('What did one tectonic plate say when he bumped into the other?')
    input('...press enter to proceed')
    print('oops my fault!')

elif choice == '2':
    print('Did you hear about the guy who had the whole left side of his body amputated?')
    input('...press enter to proceed')
    print('he is alright now')

elif choice == '3':
    print('why do programmers not like nature?')
    input('...press enter to proceed')
    print('too many bugs')

elif choice == '4':
    print('what is the difference a hippo and a zippo?')
    input('...press enter to proceed')
    print('one is really heavy, the other is a little lighter')

elif choice == '5':
    print('what did the baby corn say to the mama corn?')
    input('...press enter to proceed')
    print('popcorn')

else:
    print('ERROR')

input('Press RETURN to finish')
