from Utils.Process_order.get_product import GetProduct


class CheckProduct:

    def check_products(products_order: dict):
        """
        The method searches into the Product API if there are items available into the stock.
        If there aren't enough items the method returns an error and a massage.
        :param products_order: A dictionary of the order and its content.

        :return: A dictionary with the available products.
        """

        products = GetProduct().get_product(products_order)
        if products["products"]["stock"]:
            return products

        return dict(status=False, message="Product out of stock.", products=products["products"])