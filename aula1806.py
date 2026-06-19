from aula1806_utils import max5, average, max_price, min_price
import datetime
# datetime.datetime("2026-12-31")

products : list = [
    {"Product_id" : 21312,
     "Product_name" : "Produto1",
     "Product_valid_date" : "31-12-2026",
     "Product_price" : 10.99},

     {"Product_id" : 21313,
     "Product_name" : "Produto2",
     "Product_valid_date" : "31-11-2026",
     "Product_price" : 5.99},

     {"Product_id" : 21314,
     "Product_name" : "Produto3",
     "Product_valid_date" : "31-12-2025",
     "Product_price" : 4.99}
    ]

for product in products:
    if product["Product_price"] > 5:
        print(product["Product_name"])

# lista = max5(products)
# print(lista)

average_price = average(products)
print(f"Average price: {average_price}")
max_product = max_price(products)
print(f"Max product: {max_product}")
min_product = min_price(products)
print(f"Min product: {min_product}")