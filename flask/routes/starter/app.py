from flask import Flask, make_response, jsonify, request, g
import json

app = Flask(__name__)



@app.before_request
def load_data():
    with open("db.json") as f: #open file
        g.data: dict = json.load(f) # stored data in here "data: dict" is the establishing type of input



# @app.after_request
# def save_data():
#    with open('db.json', 'w') as f:
#       json.dump(g.data, f, indent=4)


@app.route("/")
def root():
    return "<h1>Welcome to the simple json server<h1>"



#@app.route('/langs', methods=['GET'])
@app.get("/langs")
def get_langs():
    print(g.data['langs'])
    return make_response(jsonify(g.data['langs']), 200)



@app.get("/langs/<int:id>")
def get_lang_by_id(id: int):
    if id >= len(g.data['langs']):
        return make_response(jsonify({"Error": "NO IMAGE"}), 404)
    return make_response(jsonify(g.data['langs'][id]), 200)


# TODO: write post route
@app.post('/langs')
def post_lang():

    #1. get data from request
    data = request.json
    max_id = max([lang['id'] for lang in g.data['langs']])
    g.data['langs'].append(data)

    #2. wtire langs back tot h db
    with open('db.json', 'w') as f:
        json.dump(g.data, f, indent=4)

    #3. return response of {}
    return make_response(jsonify(data),201)





# TODO: write delete route
@app.delete('/langs/<int:d>')
def delete_lang():
    #1. filter the langs sp we get LIST OF ALL LANGS w/o the given id (USE LIST COMPREHENSION)
    filtered_langs = [lang for lang in g.data['lang'] if lang['id'] !=id]
        # you can add code to handle if the id doesn't exist


    g.data['langs'] = filtered_langs
    #2. wtire langs back tot h db
    with open('db.json', 'w') as f:
        json.dump(g.data, f, indent=4)
   

    #3. return response of {}
    return make_response(jsonify({}), 200)




# TODO: write patch route
@app.patch('/langs/<int:id>')
def patch_lang(id):
    #1. get data from request
    #2. find lang that matches id
    #3. for key:value pair in the request directtory
    #4. se the value of lang[key] to request value
    pass



if __name__ == "__main__":
    app.run(port=5555, debug=True)
