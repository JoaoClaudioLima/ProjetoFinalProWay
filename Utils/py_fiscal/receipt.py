import os
from Utils.decrypt_user_data import decrypt_user_data
from datetime import datetime
from Utils.py_fiscal.PyInvoice.pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from Utils.py_fiscal.PyInvoice.pyinvoice.templates import SimpleInvoice
from Utils.SubmitEmail import submit_email


def receipt_generator(pay_info: dict, id_order: str):
    """
    The function receives data from path_info and id_order to generate
    receipt of the user's request, then send it to the submit_email function
    and delete the receipt in the local directory
    :param pay_info: Datas of user's order
    :param id_order: id of user's order
    """
    user_data = decrypt_user_data(pay_info["user"]["user_id"])
    receipt_name = "receipt" + str(id_order)
    if not os.path.exists("../SubmitEmail/receipts/"):
        os.mkdir("../SubmitEmail/receipts/")
    doc = SimpleInvoice(f'../SubmitEmail/receipts/{receipt_name}.pdf')

    doc.invoice_info = InvoiceInfo(id_order, datetime.now())

    doc.service_provider_info = ServiceProviderInfo(
        name='Livros LTDA',
        street='7 de Setembro',
        city='Blumenau',
        state='Santa Catarina',
        country='Brasil',
        post_code='88456-100',
    )
    doc.client_info = ClientInfo(email=user_data["email"], name=f"{user_data['first_name']} {user_data['last_name']}", cpf=user_data["cpf"])

    for product in pay_info["products"]:
        doc.add_item(Item(product["title"], product["quantity_purchased"], product["item_price"]))

    doc.set_item_tax_rate(pay_info["shipping_price"])
    doc.add_transaction(Transaction(pay_info["method"], id_order, datetime.now()))
    doc.finish()

    send_email_with_receipt = dict(email_client='j.claudiobl@gmail.com',
                                   email_title=f"{receipt_name} Livros para Todxs",
                                   file_path=doc.filename,
                                   type=receipt_name
                                   )

    submit_email.SubmitEmail().submit(send_email_with_receipt)
    os.remove(doc.filename)
    return True


