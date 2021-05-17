import json
from Utils.shipment.calculate_shipment import calculate_shipments

"""
File to test calculate_shipment, soon to be deleted.
"""


with open("Info/retorno_front_cartoes.json", "r") as file:
    address_test = json.load(file)
print(f"Frete de teste: {calculate_shipments(address_test)}")
