"""Cha-ching."""
amount = int(input("Enter a sum: "))
coins = 0

while amount >= 50:
    amount -= 50
    coins += 1

while amount >= 20:
    amount -= 20
    coins += 1

while amount >= 10:
    amount -= 10
    coins += 1

while amount >= 5:
    amount -= 5
    coins += 1

while amount > 0:
    amount -= 1
    coins += 1

print(f"Amount of coins needed: {coins}")
