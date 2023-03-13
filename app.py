from flask import Flask
from service.neo4j_functions import Neo4JFunctions

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello, World!"

@app.route("/stds", methods=['GET'])
def stds():
    records = Neo4JFunctions.get_stds(['Burning when peeing', 'Rectal Discharge', 'Smelly discharge', 'Fatigue'])
    for std in records:
        print(std.data())
    return "Data is back!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)