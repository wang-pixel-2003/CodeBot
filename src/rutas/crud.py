from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__) 
app.config['MONGO_URI']='mongodb+srv://robot:123@botcodeanalyzer.4rc8gsx.mongodb.net/BotAnalyzer'
mongo = PyMongo(app)

@app.route('/respuesta-nivel', methods=['POST'])
def create_user():
    # print(request.json)
    username = request.json['username']
    server = request.json['server']
    respuesta_nivel = request.json['respuesta']
    
    if username and server and respuesta_nivel: 
        id = mongo.db.Respuesta_Nivel.insert( #el .db permite acceder a la base de datos en si
            {'usuario': username, 'server': server, 'respuesta_nivel': respuesta_nivel}
        )
        response = {
            'id': str(id),
            'usuario': username,
            'server': server,
            'respuesta_nivel': respuesta_nivel
        }
        return response
    else:
        return not_found()
    
@app.route('/estructuras-ejemplos', methods=['GET'])
def get_ejemplos() :
    examples = mongo.db.Ejemplo_Estructuras.find() #obtener todos los datos dentro de la coleccions Ejemplo_Estructuras pero se devuelve en formato bson
    response = json_util.dumps(examples) #transforma el bson a un json
    return Response(response, mimetype='application/json') #Esto hace que se devuelva en formato json  

@app.route('/estructuras-ejemplos/<nombreEstructura>/<lenguaje>', methods=['GET'])
def get_ejemplo(nombreEstructura, lenguaje):
    ejemplo = mongo.db.Ejemplo_Estructuras.find_one({'nombreEstructura': nombreEstructura, 'lenguaje': lenguaje})
    response = json_util.dumps(ejemplo)
    return Response(response, mimetype='application/json')


@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'Resource Not Found: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(debug=True)     