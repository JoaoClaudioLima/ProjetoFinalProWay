from bson import ObjectId
from flask import Flask, redirect
import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["ecommerceDb"]
log = db["log_vendas"]

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/read/")


@app.route("/read/")
def read():
    return str(log.find({"_id": ObjectId("609d1a1ebb16e5a3476fd09f")}))


if __name__ == "__main__":
    app.run(debug=True)
