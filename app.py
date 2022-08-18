import requests

URL = "https://formdworks.com/"

req = requests.get(URL + "/products.json").json()

allProducts = {}
SKU_Availability = {}
test = {}

for product in req["products"]:
    if (product["title"] != "Shipping Adjustment" and product["title"] != "Manuals + Guides"):
        test[product["title"]] = {}
        for variant in product["variants"]:
            current = None
            if (variant["title"] == "Default Title"):
                allProducts[product["title"]] = variant["sku"]
                current = product["title"]
                SKU_Availability[variant["sku"]] = variant["available"]
                test[product["title"]][variant["option1"]] = { 
                    variant["option2"]: {
                        variant["option3"]: variant["available"]
                    }
                }
            else:
                allProducts[product["title"] + " " + variant["title"]] = variant["sku"]
                current = product["title"] + " " + variant["title"]
                SKU_Availability[variant["sku"]] = variant["available"]
                test[product["title"]][variant["option1"]] = { 
                    variant["option2"]: {
                        variant["option3"]: variant["available"]
                    }
                }
            
            SKU_Availability[current] = variant["sku"]

print(SKU_Availability)