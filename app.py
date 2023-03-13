from flask import Flask, request, json
from service.neo4j_functions import Neo4JFunctions

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello, World!"

@app.route("/stds", methods=['POST'])
def stds():
    # requires a list of symptoms [""]
    data = json.loads(request.data)
    records = Neo4JFunctions.get_stds(data)
    for std in records:
        print(std.data())
    return "Data is back!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)