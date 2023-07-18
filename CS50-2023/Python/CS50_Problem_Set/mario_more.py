from cs50 import get_int


# verifica se o valor inserido esta entre 1 e 8
while True:
    height = get_int('Height: ')
    if height in range(1, 9):
        break

# intera o valor inserido e imprime a piramede
for i in range(1, height + 1):
    # print first-half of pyramid
    for a in range(height - i):
        print(' ', end='')
    for b in range(i):
        print('#', end='')
    # print space betwen pyramid
    print(' ', end='')
    print(' ', end='')
    # print second-half of pyramid
    for c in range(i):
        print('#', end='')
    for d in range(i - height):
        print(' ', end='')

    print('')