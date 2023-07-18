
#define string vazia
greeting = ""

#solicita que seja preenchido pelo menos um caracter
while len(greeting) < 1:
    greeting = input("Greeting: ")

#divide string em uma lista
list_greeting = greeting.strip().lower().split()


#verifica se primeiro caracter é um h
if list_greeting[0][0] == 'h':
    if 'hello' in list_greeting[0]:
        print('$0')
    else:
        print('$20')
else:
    print('$100')

