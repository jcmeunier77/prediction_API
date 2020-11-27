from flask import Flask, render_template, url_for, request, redirect, send_file, make_response, jsonify
from flask_restx import Api, Resource, abort, fields
from werkzeug.middleware.proxy_fix import ProxyFix
from api.src import Construct3D, LaunchEstim

# Create the API
app = Flask(__name__, static_url_path='', static_folder='../static', template_folder='../templates')
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
api = Api(app, version='1.0', title='Prediction API',
          description='API that returns price estimation, map location, and 3D reconstruction for a building in Belgium',
          default='V1', default_label='first test')


# return {
#         street: 'True',
#         city: 'The v2 API server is alive.',
#         en3D:'connerie'
#     }, 200

#  Route index projet prediction

resource_fields1 = api.model('map', {
    'street' : fields.String,
    'city' : fields.String,
    })

resource_fields2 = api.model('estimate', {
    'building' : fields.String,
    'Postalcode' : fields.Integer,
    'house_area' : fields.Integer,
    'surf_land' : fields.Integer,
    'numb_facades' : fields.Integer,
    'numb_rooms' : fields.Integer,
    'garden' : fields.Integer,
    'terrace' : fields.Integer,
    'terrace_area' : fields.Integer,
    'equip_kitch' : fields.Integer,
    'fire' : fields.Integer,
    'pool' : fields.Integer,
    'Sas_new' : fields.Integer,
    'Sjust_renov' : fields.Integer,
    'Sgood' : fields.Integer,
    'Sto_refresh' : fields.Integer,
    'Sto_renov' : fields.Integer,
    'Sto_restor' : fields.Integer,
    })

# @api.route("/", methods=["GET"])
# class
# def index():
#     return 'the website is alive'

@api.route('/status', methods=['GET'])
@api.doc(description='Prediction API is alive !')
class status(Resource):
    def get(self):
        result = {
            'status' : True,
            'message' : 'The server is running!'
        }
        return jsonify(result)

@api.route("/estimate", methods=["POST"])
@api.doc(body=resource_fields2, description='Enter these parameters to get a price estimation of the building.')
class estimate(Resource):
    """
    should receive json in the following format :
    {"building":"house", "Postalcode":7830, "house_area":196, "surf_land":125,"numb_facades":4, "numb_rooms":3, "garden":1,
    "terrace":0, "terrace_area":10, "equip_kitch":1, "fire":1, "pool":1, "Sas_new":1, "Sjust_renov":0,
    "Sgood":0, "Sto_refresh":0, "Sto_renov":0, "Sto_restor":0}
    """
    def post(self):
        long_form = request.get_json()
        features = list(long_form.values())
        return LaunchEstim(features[0],features[1],features[2],features[3],features[4],features[5],features[6],
                          features[7],features[8],features[9],features[10],features[11],features[12],features[13],
                          features[14],features[15],features[16],features[17]).go_estim()

@api.route("/map", methods=["POST"])
@api.doc(body=resource_fields1, description='Enter these parameters to locate building on map.')
class map(Resource):
    def post(self):
        address = request.get_json()
        Construct3D(address["street"], address["city"]).map()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('map.html'), 200, headers)

@api.route("/showmap", methods=["GET"])
@api.doc(description='rendering page showing building on map.')
class showmap(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('map.html'), 200, headers)

    # def get_map():
    #     """
    #     should receive json in the following format :
    #     {"street":"Gouwberg 19", "city":"2370 Arendonck"}
    #     """
    #     if request.method == 'GET':
    #         pass
    #     if request.method == 'POST':
    #         address = request.get_json()
    #         Construct3D(address["street"], address["city"]).map()
    #         return render_template('map.html')

@api.route("/3d", methods=["POST"])
@api.doc(body=resource_fields1, description='Enter these parameters to view à 3D reconstruction of building (open3d).')
class view_3d(Resource):
    """
    should receive json in the following format :
    {"street":"Gouwberg 19", "city":"2370 Arendonck"}
    """
    def post(self):
        address = request.get_json()
        return Construct3D(address["street"], address["city"]).constructor()

@api.route("/threejs", methods=["POST"])
@api.doc(body=resource_fields1, description='Enter these parameters to view à 3D reconstruction of building (threejs).')
class threejs(Resource):
    def post(self):
        address = request.get_json()
        Construct3D(address["street"], address["city"]).constructorhtml()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('3dhouse.html'), 200, headers)

@api.route("/showthreejs", methods=["GET"])
@api.doc(description='rendering page showing 3D reconstruction building.')
class showthreejs(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('3dhouse.html'), 200, headers)




"""
# creating route for typing address
@app.route("/", methods=["GET"])
def adress_form():
    return render_template('index.html')

@app.route("/3d/<street>/<city>/<en3D>")
def view_3d(street, city, en3D):
    if en3D == "submit":
        return Construct3D(street, city).constructor()

@app.route("/map/<street1>/<city1>/<enMap>")
def view_map(street1, city1, enMap):
    if enMap == "encode":
        Construct3D(street1, city1).map()
        return render_template('map.html')



        # print(TargetToMap(51.319986, 5.077554).to_map())
        #
        # targetLL = AddressToCrs(street1, city1).to_long_latt()
        # mappy = folium.Map(location=[targetLL[0], targetLL[1]], zoom_start=17)
        # folium.CircleMarker(location=[targetLL[0], targetLL[1]], radius=30, popup='Your address', color='#3186cc',
        #                     fill=True, fill_color='#3186cc').add_to(mappy)
        # mappy.save('map.html')
        # return render_template()


        #Construct3D(street1, city1).map()
        #return render_template("map.html")

    #print ({street:"rue", city:"rrr"})
    # print(street, city, en3D)
    # if en3D.value == 'submit':
    #return Construct3D(street, city).constructor()
         # return {
         #         street1: 'True',
         #         city1: 'The v2 API server is alive.',
         #         enMap:'connerie'
         #     }, 200


# creating route for showing 3d building
# @app.route("/map3d")
# def map3d():
#    return render_template("map3d.html")

"""
