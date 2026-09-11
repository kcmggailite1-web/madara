x = int(input("ievadi pirmo skaitli: "))
y = int(input("ievadi otro skaitli: "))

summa = 0

for i in range(x , y + 1):
    summa += i

print(f"abu skaitļu summa no {x} līdz {y} ir {summa}")