from statistics import mean

# MAXIMO 5 EURO
def max5(lista):
    for product in lista:
        if product["Product_price"] > 5:
            product["Product_price"] = 5
    return lista


# MEDIA
# 1
# def average(lista):
#     total = 0
#     for product in lista:
#         total += product["Product_price"]
#     return total / len(lista)

# 2
# def average(lista):
#     return mean(product["Product_price"] for product in lista)

# 3
# def average(lista): 
#     return mean(list(map(lambda product : product["Product_price"], lista)))


# MAX PRECO
# 1
def max_price(lista):
    max_product = lista[0]
    for product in lista:
        if product["Product_price"] > max_product["Product_price"]:
            max_product = product
    return max_product

# 2
# def max_price(lista):
#     return max(lista, key=lambda product: product["Product_price"])


# MIN PRECO
# 1
def min_price(lista):
    min_product = lista[0]
    for product in lista:
        if product["Product_price"] < min_product["Product_price"]:
            min_product = product
    return min_product

# 2
# def min_price(lista):
#     return min(lista, key=lambda product: product["Product_price"])