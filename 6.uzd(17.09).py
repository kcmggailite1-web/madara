list = ["Mans", "vārds", "nav", "Rihards", "mans", "vārds", "ir"]
teksts = input("ievadi savu tekstu: ")
list = teksts.split()
print(list.count("Mans"))
print(list.count("vārds"))