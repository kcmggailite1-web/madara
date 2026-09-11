x = int(input("Ievadiet pirmo skaitli: "))
y = int(input("Ievadiet otro skaitli: "))

print(f"Pāra sakitļi no {x} un {y} ir: ")

for i in range(x , y + 1):
  
    if i %2 == 0:
      print(i)

