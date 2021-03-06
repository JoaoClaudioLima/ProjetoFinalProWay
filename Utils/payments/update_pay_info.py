from Utils.Process_order.get_product import GetProduct
from Utils.Process_order.check_product import CheckProduct


def update_pay_info(pay_info: dict) -> dict:
    """
    this method updates pay_info with informations from API_Products of books,
    prices, stock, and if all books are digitals
    :param pay_info:
    :return: pay_info
    """

    products_list = pay_info["products"]
    get_product_info = GetProduct().get_product(products_list)
    if CheckProduct().check_products(get_product_info):
        book_list = get_product_info["books_stocks"]
        for i in range(len(book_list)):
            products_list[i]["title"] = book_list[i]["title"]
            products_list[i]["item_price"] = book_list[i]["item_price"]
        pay_info["digital_books"] = get_product_info["digital"]
        return pay_info
    else:
        pay_info['message'] = "products out of stock."
        return pay_info
