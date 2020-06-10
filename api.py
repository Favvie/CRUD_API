import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

inventory = {
  '1': {'item': 'Biscuits', 'price': '$20'},
  '2': {'item': 'sugar', 'price': '$10'},
  '3': {'item': 'soap', 'price': '$101'},
}
#app.route maps the uri to the funcion
@app.route('/', methods=['GET'])
def home():
    return "<h1>SHOP INVENTORY</h1><p>This is a list of all the items in our collection.</p>" 
	
@app.route('/inventory', methods=['GET'])
def api_all():
    return jsonify(inventory)

@app.route('/inventory/add', methods=['POST', 'GET'])
def add_item():
    if request.method == 'POST':
        items = request.form.get('item')
        prices = request.form.get('price')
        inv_id = int(max(inventory.keys())) + 1
        inv_id = '%i' % inv_id
        inventory[inv_id] = {
                'item': items,
                'price': prices
                }
        return inventory[inv_id], 201

    return '''<form method = "POST">
    item<input type = "text" name = "item">
    price<input type="text" name = "price">
    <input type = "submit">
    </form>'''
        
@app.route('/inventory/<inv_id>',methods = ['GET'])
def item(inv_id):
    if inv_id not in inventory:
        return "Not found", 404
    else:
        return inventory[inv_id]


@app.route('/inventory/delete/<inv_id>',methods = ['GET','DELETE'])
def delete(inv_id):
    if inv_id not in inventory:
        return "Not found", 404
    else:
        del inventory[inv_id]
        return inventory, 200
        

@app.route('/inventory/update/<inv_id>/',methods = ['PUT'])
def update(inv_id):
    items = request.get_json()
    inventory[inv_id] = items
    return jsonify(inventory[inv_id]), 200
    
app.run()