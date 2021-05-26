import pymongo


class LogConnectionMongo:

    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb+srv://Jao:jaojao@cluster0.hb5l7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.conn["ecommerceDb"]
        self.log = self.db["log_vendas"]
