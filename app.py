from flask import Flask, request, json, jsonify
from service.neo4j_functions import Neo4JFunctions
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def main():
    return "Hello, World!"

@app.route("/stds", methods=['POST'])
def stds():
    # requires a list of symptoms [""]
    data = json.loads(request.data)
    # get unique stds from graphDB
    records = set(Neo4JFunctions.get_stds(data))
    res = []
    for std in records:
        symptoms, symptoms_length = Neo4JFunctions.symptom_intersection(data, std.data()['s.name'])

        # appending length of symptoms, the name and list of symptoms
        res.append(
            {
                "symptom_length": symptoms_length, 
                "symptom_name": std.data()['s.name'], 
                "symptom_list": list(symptoms)
            }
        )
    return jsonify(res)

@app.route("/all", methods=['GET'])
def all_stds():
    records = set(Neo4JFunctions.all_stds())
    res = [std.data()['s']['name'] for std in records]
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)