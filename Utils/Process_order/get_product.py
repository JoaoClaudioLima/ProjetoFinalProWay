import requests


class GetProduct:

    def get_product(self, product_order: dict) -> dict:
        """
        The method makes a request to the Product API by the URL and gets the product order.
        :param product_order: Data from the requested API.
        :return: A dictionary of products with its content.
        """
        try:
            products = requests.get('http://127.0.0.1:5000/read/', params=product_order)
            return dict(products)
        except Exception as Error:
            return dict(status=False, message=Error.args)
