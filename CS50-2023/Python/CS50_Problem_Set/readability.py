from cs50 import get_string

# solicita texto
text = get_string('Text: ')

# define variaveis
s = 0
w = 1
l = 0

# itera sobre cada letra
for word in text:
    if word == '.' or word == '?' or word == '!':
        s += 1
    if word.isspace():
        w += 1
    if word.isalpha():
        l += 1

L = (100 * l) / w
S = (100 * s) / w

# calcula formula de Coleman-Liau
index = (0.0588 * L) - (0.296 * S) - 15.8

# imprime texto na tela
if (index >= 16):
    print("Grade 16+")

elif (index < 1):
    print("Before Grade 1")

else:
    print("Grade ", round(index))