__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
from peewee import *
from datetime import date

# Searches product on given term in name and description of products
# Returns a list of matches (as dictionary)
def search(term):
    term = term.lower()
    matches = Products.select().where(Products.name.contains(term) | Products.description.contains(term))
    return list(matches.dicts()) 


# Returns a list with products sold by given seller 
def list_user_products(user_id):
    products = Products.select().where(Products.seller == user_id)
    return list(products.dicts())


# Returns list of dictionaries with products that matches with given tag
def list_products_per_tag(tag_id):
    if type(tag_id) is not str:
        print('Tag needs to be a string.. \n For example: list_products_per_tag("houtwerk")')
        return
    tag_id = tag_id.lower()
    match = Products.select().join(ProductTags).where(ProductTags.tag_id == tag_id).dicts()
    return list(match)


# Adds a product to the Betsy shop
def add_product_to_catalog(user_id, product: dict):
    product = product.lower()
    if not 'name' in product.keys():
        print("Please specify a name, as 'name': 'your_product_name' in the database")
        return
    if not 'description' in product.keys():
        print("Please specify a description, as 'description': 'your_product_description' in the database")
        return
    if not 'price' in product.keys():
        print("Please specify the price, as 'price': 'your_product_price' in the database")
        return
    if not 'stock' in product.keys():
        print("Please specify the stock, as 'stock': 'your_product_stock' in the database")
        return
    if not 'tags' in product.keys():
        print("Please specify tags, as 'tags': 'list_of_tags' in the database")
        return  
        
    product_id = Products.create(name=product['name'], 
                    seller=user_id, 
                    description=product['description'], 
                    unit_price=product['price'], 
                    current_stock=product['stock'])
    
    # Append all existing tags to a list
    existing_tags = []
    for tag in Tags.select():
        existing_tags.append(tag.name)
    
    # Check if tag already exist, if not add to list so it attaches to product
    for tag in product['tags']:
        if tag not in existing_tags:
            print(f'Adding tag {tag}')
            Tags.create(name=tag)
        #check = ProductTags.create(product_id=product_id, tag_id=tag)
        #print(check)


# Updates amount in stock for all products
def update_stock(product_id, new_quantity):
    try:
        product = Products.select().where(Products.product_id == product_id).get()
        product.current_stock = new_quantity
        product.save()    
    except DoesNotExist:
        print("Error: ", DoesNotExist)    


# Checks if product is in stock
# If so adds a tranction to the database
# Adjusts amount in stock
def purchase_product(product_id, buyer_id, quantity: int):
    available_quantity = Products.select().where(Products.product_id == product_id).get().current_stock
    print('Available quantity: ', available_quantity)
    if quantity <= available_quantity and quantity > 0:
        Transactions.create(date=date.today(), buyer_id=buyer_id, product_id=product_id, quantity=quantity)
        new_quantity = available_quantity - quantity
        update_stock(product_id, new_quantity)
        print('New quantity: ', new_quantity)

    else:
        print(f"Not enough stock for {quantity} products. Available amount: {available_quantity} products")


# Remove a specific product from the database
def remove_product(product_id):
    try:
        Products.get_by_id(product_id).delete_instance()
    except DoesNotExist:
        print("Error: ", DoesNotExist)


