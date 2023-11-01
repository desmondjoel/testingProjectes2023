products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Smartphone", "price": 500},
    {"name": "Tablet", "price": 300},
    {"name": "Headphones", "price": 100},
]

print(type(products))
print(type(products[0]))

def is_affordable(item):
    return item["price"]<=500

affordable_list= list(filter(is_affordable,products))
for i in affordable_list:
    print(str(i["price"])+ i["name"])
