from flask import Flask, request, json, jsonify
from service.neo4j_functions import Neo4JFunctions

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello, World!"

@app.route("/stds", methods=['POST'])
def stds():
    # requires a list of symptoms [""]
    data = json.loads(request.data)
    records = set(Neo4JFunctions.get_stds(data))
    res = []
    for std in records:
        symptoms, symptoms_length = Neo4JFunctions.symptom_intersection(data, std.data()['s.name'])
        res.append(
            (symptoms_length, std.data()['s.name'], list(symptoms))
        )
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)