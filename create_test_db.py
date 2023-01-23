from models import *

# Code that generates data that can be used with the Betsy Workshop Program
# Run to populate test database
def populate_test_database():

    db.connect()

    db.create_tables([Users, Products, Transactions, Tags, ProductTags])
    
    test_users = [
        {'name': 'Karel Kroket',
        'adress': 'Kasteel 11, Kralingen',
        'billing_information': 12345678},
        {'name': 'Willie Wartaal',
        'adress': 'Wormen 22, Warmerdam',
        'billing_information': 98765432},
        {'name': 'Freek Frikandel',
        'adress': 'Fluister 77, Fijnaart',
        'billing_information': 10203040},
        {'name': 'Bert Bamibal',
        'adress': 'Bezemweg 34, Baak',
        'billing_information': 10011012},
        {'name': 'Otto Ooievaar',
        'adress': 'Vogelweg 81, Vogelaar',
        'billing_information': 97531264},
    ]

    for user in test_users:
        Users.create(name=user['name'], adress=user['adress'], billing_info=user['billing_information'])
    
    example_products = [
        {'name': 'Zwaard',
        'description': 'Zelf gesmeden zwaard',
        'price_per_unit': 250,
        'quantity': 10,
        'seller': 1,
        'tags': ['middeleeuwen', 'wapen', 'smederij', 'staal']
        },
        {'name': 'Bijl',
        'description': 'Zelf gesmeden bijl',
        'price_per_unit': 130,
        'quantity': 18,
        'seller': 1,
        'tags': ['middeleeuwen', 'wapen', 'smederij', 'staal']
        },
        {'name': 'Pijlen',
        'description': 'Zelf gemaakte pijl',
        'price_per_unit': 17.50,
        'quantity': 153,
        'seller': 1,
        'tags': ['middeleeuwen', 'wapen', 'smederij', 'staal']
        },
        {'name': 'Ruitenwisser',
        'description': 'Ruitenwisser maat 32',
        'price_per_unit': 27.50,
        'quantity': 6,
        'seller': 2,
        'tags': ['auto', 'tweedehands', 'rubber']
        },
        {'name': 'Autoband 200 mm',
        'description': 'Autoband breedte 20 cm ',
        'price_per_unit': 40,
        'quantity': 52,
        'seller': 2,
        'tags': ['auto', 'tweedehands', 'rubber']
        },
        {'name': 'Stuur',
        'description': 'Stuur voor auto',
        'price_per_unit': 25,
        'quantity': 4,
        'seller': 2,
        'tags': ['auto', 'tweedehands', 'rubber']
        },
        {'name': 'Slagroomtaart',
        'description': 'Zelf gemaakte slagroomtaart',
        'price_per_unit': 12.50,
        'quantity': 3,
        'seller': 3,
        'tags': ['gebak', 'bakker', 'voedsel']
        },
        {'name': 'Appeltaart',
        'description': 'Zelf gemaakte appeltaart met kaneel',
        'price_per_unit': 10.25,
        'quantity': 3,
        'seller': 3,
        'tags': ['gebak', 'bakker', 'voedsel']
        },
        {'name': 'Monchoutaart',
        'description': 'Zelf gemaakte monchoutaart',
        'price_per_unit': 9.50,
        'quantity': 3,
        'seller': 3,
        'tags': ['gebak', 'bakker', 'voedsel']
        },
        {'name': 'Sjaal',
        'description': 'Zelf gebreide sjaal',
        'price_per_unit': 11,
        'quantity': 14,
        'seller': 4,
        'tags': ['breiwerk', 'kleding', 'wol']
        },
        {'name': 'Trui',
        'description': 'Zelf gebreide trui',
        'price_per_unit': 22,
        'quantity': 8,
        'seller': 4,
        'tags': ['breiwerk', 'kleding', 'wol']
        },
        {'name': 'stoel',
        'description': 'Handgemaakte houten stoel',
        'price_per_unit': 55,
        'quantity': 16,
        'seller': 5,
        'tags': ['houtwerk', 'meubel']
        },
        {'name': 'tafel',
        'description': 'Handgemaakte houtel tafel',
        'price_per_unit': 110,
        'quantity': 2,
        'seller': 5,
        'tags': ['houtwerk', 'meubel']
        },
    ]

    for product in example_products:
        Products.create(name=product['name'], description=product['description'], unit_price=product['price_per_unit'], current_stock=product['quantity'], seller=product['seller'])
    
    tags = []

    for product in example_products:
        for item in product['tags']:
            tags.append(item)
    
    for tag in tags:
        Tags.create(name=tag)

    for count, product in enumerate(example_products, 0):
        product_id = count
        for tag in product['tags']:
            ProductTags.create(tag_id=tag, product_id=product_id)
    
    db.close()

populate_test_database()