from lib2to3.pytree import Base
from peewee import *

db = SqliteDatabase('BetsyWebshop.db')

class BaseModel(Model):
    class Meta:
        database = db

class Users(BaseModel):
    user_id = AutoField()
    name = CharField()
    adress = CharField()
    billing_info = IntegerField()
    
class Products(BaseModel):
    product_id = AutoField()
    name = CharField()
    seller = ForeignKeyField(Users, backref="products")
    description = TextField()
    unit_price = DecimalField(auto_round=False, decimal_places=2)
    current_stock = IntegerField()
    
class Transactions(BaseModel):
    transaction_id = AutoField()
    date = DateField()
    buyer_id = ForeignKeyField(Users, backref="purchases")
    product_id = ForeignKeyField(Products, backref="sales")
    quantity = IntegerField()
    
class Tags(BaseModel):
    tag_id = AutoField()
    name = CharField()

class ProductTags(BaseModel):
    product_id = ForeignKeyField(Products, backref="tags")
    tag_id = ForeignKeyField(Tags, backref="products")