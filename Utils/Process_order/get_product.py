import requests


class GetProduct:
    # products = dict(products=[dict(id="1", price="10.25", format="physical"), dict(id="2", price="10.25", format="digital")], total=20.50)#TEST
    def get_product(self, product_order: dict) -> dict:
        products = requests.get('http://127.0.0.1:5000/read/', params=product_order)
        return dict(products)
