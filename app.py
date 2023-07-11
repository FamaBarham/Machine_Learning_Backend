from flask import Flask, jsonify
from flask_restful import Api, Resource,request
from model import generate_Cloud,comptage
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/worldCLoud', methods=['POST'])
def prepare_worldCloud():
    data = request.get_json()['reponses']
    datas = generate_Cloud(data)
    return datas

@app.route('/sentimentAnalysis', methods=['POST'])
def prepare_sentimentAnalysis():
    data = request.get_json()['reponses']
    datas = comptage(data)
    return datas


# if __name__ == "__main__":
#     app.run()





