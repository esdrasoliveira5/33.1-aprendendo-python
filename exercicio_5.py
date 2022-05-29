def tinta(metros):
    litros = metros / 3
    latas = litros / 18
    preco = latas * 80.00

    return [latas, preco]


result = tinta(540)
print(result)
