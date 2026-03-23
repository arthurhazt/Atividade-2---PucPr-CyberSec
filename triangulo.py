a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))

if a + b > c and a + c > b and b + c > a:
    print("Forma um triângulo")

    if a == b == c:
        print("Equilátero")
    elif a == b or a == c or b == c:
        print("Isósceles")
    else:
        print("Escaleno")

    lados = sorted([a, b, c])
    if lados[2]**2 == lados[0]**2 + lados[1]**2:
        print("Triângulo retângulo")

else:
    print("Não forma um triângulo")