import csv 

with open('favorite.csv', 'r') as file:
    reader = csv.DictReader(file)

    counts = {}

    for row in reader:
        favorite = row['OwnerName']
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

    for i in counts:
        print(i)

favorite = input('favorite: ')

if favorite in counts:
    print(f'{favorite}: {counts[favorite]}')