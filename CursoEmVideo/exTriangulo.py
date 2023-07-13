a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("As medidas informadas formam um triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("As medidas informadas formam um triângulo isósceles.")
    elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("As medidas informadas formam um triângulo retângulo.")
    else:
        print("As medidas informadas formam um triângulo escaleno.")
else:
    print("As medidas informadas não podem formar um triângulo.")
