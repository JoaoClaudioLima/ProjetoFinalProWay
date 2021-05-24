class CheckProduct:

    def check_products(self, get_product_info: dict):
        """
        The method searches into the Product API if there are items available into the stock.
        If there aren't enough items the method returns an error and a massage.
        :param get_product_info: A dictionary of the order and its content.
        :return: bool.
        """

        if get_product_info["products"]["stock"]:
            return True
        return False
