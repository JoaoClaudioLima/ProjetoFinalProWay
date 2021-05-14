from Utils.Process_order.get_product import GetProduct


class CheckProduct:

    @staticmethod
    def check_products(products_order: dict):
        products = GetProduct().get_product(products_order)

        if "physical" in str(products["products"]):
            products.update(physical=True)
            return products
        elif products["status"]:
            products.update(physical=False)
            return products

        return dict(status=False, message="Product out of stock.", products=products["products"])
