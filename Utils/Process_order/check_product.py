from flask import Flask, redirect, url_for
import generate_log

class CheckProduct:

    def check_products(self):#, products_order:dict):
        # products = redirect(url_for("mongodb://localhost:27017/ROUTE", keys=x, obj=products_order)) ATUAL
        products = dict(status=True, products=[dict(id="1", price="10.25", format="physicst"), dict(id="2", price="10.25", format="digital")], total=20.50)#TEST
        # if "physicist" in str(products["products"]):
        #     return products
        #     print("physicist" in str(products["products"]))
        if products["status"]:
            return products

        return dict(status=False, message="Product out of stock", products=products["products"])


c = CheckProduct()
print(c.check_products())