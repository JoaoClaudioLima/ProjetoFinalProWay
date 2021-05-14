from barcode import Code128


def generate_barcode(barcode: str):
    """
    create a barcode img format svg with the barcode code
    :param barcode: barcode
    :return:
    """
    number = str(barcode).strip()
    my_code = Code128(number)
    my_code.save(str(barcode).strip())
