import requests


class GetProduct:

    def get_product(self, pay_info_products: list) -> dict:

        """
        This method makes a request to the Product API by the URL and gets the product order.
        :param pay_info_products: Data from the requested API.
        :return: A dictionary of products with its content.
        """

        get_product_info = requests.get('http://192.168.0.82:5000/books/stock/verify',
                                        headers={"access-key": "3b68f1bcc0af5dafeefb2b650f4f35b8"},
                                        json=pay_info_products).json()

        return get_product_info

    def post_response(self, pay_info_products: list, purchased: bool) -> None:

        """
        This method informs API_Product if the purchase was successful or not
        :param pay_info_products: purchase product list
        :param purchased: whether the purchase was successful
        :return: None :)
        """

        response = dict(shopping_car=pay_info_products, purchased=purchased)
        return requests.post('http://192.168.0.82:5000/books/purchase/finish',
                             headers={"access-key": "3b68f1bcc0af5dafeefb2b650f4f35b8"},
                             json=response).json()
