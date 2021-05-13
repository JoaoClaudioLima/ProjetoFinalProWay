

def calculate_total(items: list, shipping_price: float) -> float:
    """
    calculates the total of the cart
    :param items: list of itens
    :param shipping_price: price
    :return: total price of the cart
    """
    total = 0

    for item in items:
        total += item['item_price'] * item['item_quantity']

    if total > 0:
        total += shipping_price

    return total


#
# item1 = {
#     "_id": "",
#     "title": "Building Microservices: Designing Fine-Grained Systems",
#     "deion": "",
#     "language": "English",
#     "category": [
#         "Computação",
#         "Informática",
#         "Mídias Digitais"
#     ],
#     "author": [
#         {
#             "name": "Martin",
#             "lastname": "Fowler",
#             "country": "United States of America"
#         },
#         {
#             "name": "Thiago",
#             "lastname": "Alexandre",
#             "country": "Brazil"
#         }
#     ],
#     "publisher": {
#         "name": "O'Reilly Media",
#         "country": "United States of America"
#     },
#     "isbn-10": "1491950358",
#     "isbn-13": "978-1491950357",
#     "format": "Fisical",
#     "published_at": "2015-02-20",
#     "item_price": 302.01,
#     "item_quantity": 1,
#     "classification": [
#         {
#             "author_name": "Carlos Eduardo Ribeiro",
#             "comment": "Muito bom...",
#             "classification": 5,
#             "created_at": "2021-05-11"
#         },
#         {
#             "author_name": "Gabriela Cristofolini",
#             "comment": "Excelente didática...",
#             "classification": 4,
#             "created_at": "2021-05-11"
#         },
#         {
#             "author_name": "Jeff Silva",
#             "comment": "Autor explica muito...",
#             "classification": 5,
#             "created_at": "2021-05-11"
#         }
#     ],
#     "size": {
#         "height": 17.78,
#         "lenght": 23.54,
#         "width": 1.5
#     },
#     "weight": 1.5,
#     "page_quantity": 270
# }
# item2 = {
#     "_id": "",
#     "title": "Building Microservices: Designing Fine-Grained Systems",
#     "deion": "",
#     "language": "English",
#     "category": [
#         "Computação",
#         "Informática",
#         "Mídias Digitais"
#     ],
#     "author": [
#         {
#             "name": "Martin",
#             "lastname": "Fowler",
#             "country": "United States of America"
#         },
#         {
#             "name": "Thiago",
#             "lastname": "Alexandre",
#             "country": "Brazil"
#         }
#     ],
#     "publisher": {
#         "name": "O'Reilly Media",
#         "country": "United States of America"
#     },
#     "isbn-10": "1491950358",
#     "isbn-13": "978-1491950357",
#     "format": "Fisical",
#     "published_at": "2015-02-20",
#     "item_price": 302.01,
#     "item_quantity": 4,
#     "classification": [
#         {
#             "author_name": "Carlos Eduardo Ribeiro",
#             "comment": "Muito bom...",
#             "classification": 5,
#             "created_at": "2021-05-11"
#         },
#         {
#             "author_name": "Gabriela Cristofolini",
#             "comment": "Excelente didática...",
#             "classification": 4,
#             "created_at": "2021-05-11"
#         },
#         {
#             "author_name": "Jeff Silva",
#             "comment": "Autor explica muito...",
#             "classification": 5,
#             "created_at": "2021-05-11"
#         }
#     ],
#     "size": {
#         "height": 17.78,
#         "lenght": 23.54,
#         "width": 1.5
#     },
#     "weight": 1.5,
#     "page_quantity": 270
# }
#
# cart = [item1, item2]
#
# ship = 40
#
# print(calculate_total(items=cart, shipping_price=ship))
