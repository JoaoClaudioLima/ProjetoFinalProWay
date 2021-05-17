import pymongo


class LogConnectionMongo:

    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.conn["ecommerceDb"]
        self.log = self.db["log_vendas"]
