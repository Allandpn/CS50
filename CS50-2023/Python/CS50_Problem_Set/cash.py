from cs50 import get_float

# inicia loop
while True:
    change = get_float("Change owed: ")

    if change > 0:
        break

coins = 0

# calcula numero de moedas
while change >= 0.25:
    change = change - 0.25
    coins += 1

# arredonda valor
change = round(change, 2)

# calcula numero de moedas
while change >= 0.10:
    change = change - 0.10
    coins += 1

# arredonda valor
change = round(change, 2)

# calcula numero de moedas
while change >= 0.05:
    change = change - 0.05
    coins += 1

# arredonda valor
change = round(change, 2)

# calcula numero de moedas
while change >= 0.01:
    change = change - 0.01
    coins += 1


print(coins)