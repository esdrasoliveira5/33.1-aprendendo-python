def typeOfTriangle(a, b, c):

    if (a + b) > c:
        if a == b and c == a:
            return "Triângulo Equilátero"
        elif(a == b or b == c or c == a):
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "não é triangulo"


print(typeOfTriangle(-10, -15, 12))
