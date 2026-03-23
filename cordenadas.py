x = int(input("Defina um ponto x: "))
y = int(input("Defina um ponto y: "))

if 0 < x < 10 and 0 < y < 10:
    print("Dentro do quadrado!")
elif (x == 0 or x == 10) and (0 <= y <= 10) or (y == 0 or y == 10) and (0 <= x <= 10):
    print("Na fronteira!")
else:
    print("Fora do quadrado!")
