a = ("17-+01+-91-+-+--")
a = a.replace("-", "Z")
a = a.replace("+", "-")
a = a.replace("Z", "+")

print(a)