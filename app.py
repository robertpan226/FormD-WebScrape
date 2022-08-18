import requests

URL = "https://formdworks.com/"

req = requests.get(URL + "/products.json").json()

availableProducts = {}
SKUs = {}

for product in req["products"]:
    if (product["title"] != "Shipping Adjustment" and product["title"] != "Manuals + Guides"):
        for variant in product["variants"]:
            current = None
            if (variant["title"] == "Default Title"):
                availableProducts[product["title"]] = variant["available"]
                current = product["title"]
            else:
                availableProducts[product["title"] + " " + variant["title"]] = variant["available"]
                current = product["title"] + " " + variant["title"]
            
            SKUs[current] = variant["sku"]

for i in SKUs:
    print(i, SKUs[i])