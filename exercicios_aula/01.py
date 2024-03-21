print("Cálculo de média...")

p1 = float(input("Digite a PRIMEIRA nota: "))
p2 = float(input("Digite a SEGUNDA nota: "))

media = (p1 + p2) / 2 

print("-----------------")

print("A média final é", media)

print("-----------------")
if media >= 6.0:
    print("APROVADO")
elif (media >= 3.0):
    print("EXAME")
else:
    print("reprovado")
print("-----------------")