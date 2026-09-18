x = int(input("Ievadi savu reizinātāju: "))
z = 1
rezultats = x *(z)
for z in range(1, 10+1):
    print(f"{x} * {z} = {x *(z)}")

i = 1
rezultats = x *(i)
while i < 10+1:
  print(f"{x} * {i} = {x *(i)}")
  i += 1