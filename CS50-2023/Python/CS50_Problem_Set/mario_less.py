from cs50 import get_int


# verifica se o valor inserido esta entre 1 e 8
while True:
    height = get_int('Height: ')
    if height in range(1, 9):
        break

# intera o valor inserido e imprime a piramede
for i in range(height):
    for j in range(height - i - 1):
        print(' ', end='')
    for l in range(i):
        print('#', end='')
    print('#')
