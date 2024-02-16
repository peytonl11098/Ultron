from flask import Blueprint, jsonify
from flask import Flask # import flask to enable endpoints
from flask_restful import Resource, Api, reqparse, abort, marshal, fields
#Initialize flask
def InitInvent_app():
    app = Flask (__name__)
    api = Api(app)
inventory_api = Blueprint(‘inventory_api’, __name__,
                   url_prefix=‘/api/inventory’)
api = Api(inventory_api)
# Categories lists - this will be entered in dynamodb
# and additional fields like description, images etc will be included
categories = [{
    “cid”: “1",
    “name”: “fullName”
},
{
    “cid”: “2",
    “name”: “email”
},
{
    “cid”: “3",
    “name”: “phoneNumber”
}
]
# Fruits list - this will be entered in dynamodb
# and additional fields like description, images etc will be included
fruits =[{
    “pid”: 1,
    “name”: “Red Apples 10lbs”,
    “unitCost”: 35.00
},
{
    “pid”: 2,
    “name”: “Fuji Apples 10lbs”,
    “unitCost”: 12.00
},
{
    “pid”: 3,
    “name”: “Red Oranges 5lbs”,
    “unitCost”: 18.50
},
{
    “pid”: 4,
    “name”: “Tangerines 5lbs”,
    “unitCost”: 17.00
},
{
    “pid”: 5,
    “name”: “Bananas 1ct”,
    “unitCost”: 0.75
},
{
    “pid”: 6,
    “name”: “Mangos 1lbs”,
    “unitCost”: 23.00
},
{
    “pid”: 7,
    “name”: “Kiwi 1lbs”,
    “unitCost”: 12.25
},
{
    “pid”: 8,
    “name”: “Grapes 5lbs”,
    “unitCost”: 4.50
},
{
    “pid”: 9,
    “name”: “Pineapple 1ct”,
    “unitCost”: 12.75
},
{
    “pid”: 10,
    “name”: “Cherries 12oz”,
    “unitCost”: 13.00
},
{
    “pid”: 11,
    “name”: “Avocado 1lbs”,
    “unitCost”: 8.25
},
{
    “pid”: 12,
    “name”: “Blueberries 8oz”,
    “unitCost”: 4.00
},
{
    “pid”: 13,
    “name”: “Lemons 1ct”,
    “unitCost”: 1.00
},
{
    “pid”: 14,
    “name”: “Guava 1lbs”,
    “unitCost”: 42.00
},
{
    “pid”: 15,
    “name”: “Raspberries 1lbs”,
    “unitCost”: 25.00
},
{
    “pid”: 16,
    “name”: “Papaya 1lbs”,
    “unitCost”: 8.00
},
{
    “pid”: 17,
    “name”: “Durian 6oz”,
    “unitCost”: 13.00
},
{
    “pid”: 18,
    “name”: “Figs 1lbs”,
    “unitCost”: 9.00
},
{
    “pid”: 19,
    “name”: “Jackfruit 1ct”,
    “unitCost”: 6.50
},
{
    “pid”: 20,
    “name”: “Loganberry 12oz”,
    “unitCost”: 14.00
}]
# Veggies list - this will be entered in dynamodb
# and additional fields like description, images etc will be included
veggies = [{
    “pid”: 1,
    “name”: “Carrots 1lbs”,
    “unitCost”: 2.75
},
{
    “pid”: 2,
    “name”: “Cucumber 1ct”,
    “unitCost”: 2.00
},
{
    “pid”: 3,
    “name”: “Tomatoes 1lbs”,
    “unitCost”: 4.50
},
{
    “pid”: 4,
    “name”: “Red Onions 1lbs”,
    “unitCost”: 6.00
},
{
    “pid”: 5,
    “name”: “White Onions 1lbs”,
    “unitCost”: 6.50
},
{
    “pid”: 6,
    “name”: “Scallions 1lbs”,
    “unitCost”: 3.00
},
{
    “pid”: 7,
    “name”: “Lettuce 1lbs”,
    “unitCost”: 2.25
},
{
    “pid”: 8,
    “name”: “Ginger 20oz”,
    “unitCost”: 7.00
},
{
    “pid”: 9,
    “name”: “Garlic 1ct”,
    “unitCost”: 0.75
},
{
    “pid”: 10,
    “name”: “Aspargus 1bunch”,
    “unitCost”: 3.00
},
{
    “pid”: 11,
    “name”: “Artichoke 1ct”,
    “unitCost”: 14.00
},
{
    “pid”: 12,
    “name”: “Ash Gourd 1ct”,
    “unitCost”: 12.00
},
{
    “pid”: 13,
    “name”: “Bamboo Shoots 1bunch”,
    “unitCost”: 7.00
},
{
    “pid”: 14,
    “name”: “Broccoli 1lbs”,
    “unitCost”: 2.00
},
{
    “pid”: 15,
    “name”: “Cabbage 1ct”,
    “unitCost”: 5.00
},
{
    “pid”: 16,
    “name”: “Chives 1lbs”,
    “unitCost”: 5.00
},
{
    “pid”: 17,
    “name”: “Coriander 1bunch”,
    “unitCost”: 1.00
},
{
    “pid”: 18,
    “name”: “Eggplant 1lbs”,
    “unitCost”: 9.00
},
{
    “pid”: 19,
    “name”: “Green Beans 1lbs”,
    “unitCost”: 6.00
},
{
    “pid”: 20,
    “name”: “Habanero Peppers 8oz”,
    “unitCost”: 4.00
}
    ]
# Grains list - this will be entered in dynamodb
# and additional fields like description, images etc will be included
grains=[{
    “pid”: 1,
    “name”: “Basmati Rice 10lbs”,
    “unitCost”: 35.00
},
{
    “pid”: 2,
    “name”: “Jasmine Rice 10lbs”,
    “unitCost”: 12.00
},
{
    “pid”: 3,
    “name”: “Jasmine Rice 5lbs”,
    “unitCost”: 8.50
},
{
    “pid”: 4,
    “name”: “Quinoa 5lbs”,
    “unitCost”: 7.00
},
{
    “pid”: 5,
    “name”: “Barley 10lbs”,
    “unitCost”: 16.50
},
{
    “pid”: 6,
    “name”: “Millet 1lbs”,
    “unitCost”: 13.00
},
{
    “pid”: 7,
    “name”: “Buckwheat 1lbs”,
    “unitCost”: 2.25
},
{
    “pid”: 8,
    “name”: “Oats 5lbs”,
    “unitCost”: 17.00
},
{
    “pid”: 9,
    “name”: “Rye 2lbs”,
    “unitCost”: 2.75
},
{
    “pid”: 10,
    “name”: “Whole Oats 20lbs”,
    “unitCost”: 23.00
},
{
    “pid”: 11,
    “name”: “Bulgur Wheat 5lbs”,
    “unitCost”: 18.25
},
{
    “pid”: 12,
    “name”: “Whole Barley 10lbs”,
    “unitCost”: 4.00
},
{
    “pid”: 13,
    “name”: “Spelt 5lbs”,
    “unitCost”: 17.00
},
{
    “pid”: 14,
    “name”: “Brown Rice 10lbs”,
    “unitCost”: 22.00
},
{
    “pid”: 15,
    “name”: “Parboiled Rice 20lbs”,
    “unitCost”: 15.00
},
{
    “pid”: 16,
    “name”: “Arborio Rice 15lbs”,
    “unitCost”: 18.00
},
{
    “pid”: 17,
    “name”: “Coriander 1bunch”,
    “unitCost”: 1.00
},
{
    “pid”: 18,
    “name”: “Black Rice 10lbs”,
    “unitCost”: 19.00
},
{
    “pid”: 19,
    “name”: “Bomba Rice 5lbs”,
    “unitCost”: 5.00
},
{
    “pid”: 20,
    “name”: “Long Grain White Rice 5lbs”,
    “unitCost”: 4.00
}]
# Get all veggies
class Veggie(Resource):
    def get(self):
        return {“veggies”: veggies}
# Get all categories
class Categories(Resource):
    def get(self):
        return {“categories”: categories}
# Get all grains
class Grains(Resource):
    def get(self):
        return {“grains”: grains}
# Get all fruits
class Fruits(Resource):
    def get(self):
        return {“fruits”: fruits}
 # Adding endpoints for Veggies, fruits, categories, grains
api.add_resource(Veggie, “/veggies”)
api.add_resource(Categories, “/categories”)
api.add_resource(Fruits, “/fruits”)
api.add_resource(Grains, “/grains”)
# main
if __name__ == “__main__“:
    server = “http://127.0.0.1:8350”
    url = server + “/api/inventory”
    responses = []
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print(“unknown error”)
# Initialize the Flasks app and start the server
InitInvent_app()