from barcode import Code128


def generate_barcode(barcode: str):
    number = str(barcode).strip()
    my_code = Code128(number)
    my_code.save(str(barcode).strip())


# generate_barcode("23700.99999 05132021.125047 213931361184089670357388609302949910791")