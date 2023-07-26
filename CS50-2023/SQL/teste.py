import cs50

db = SQL("sqlite:///favorites.db")

favorite = input("Name: ")

rows = db.execute("SELECT * FROM favorites WHERE problem = 'Dennis Howard'")

for row in rows:
    print (row)


