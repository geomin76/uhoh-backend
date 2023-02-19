import json
from service.neo4j_client import Neo4JClient

neo4j = Neo4JClient().db()

with open('./std_data.json', 'r') as f:
  std_data = json.load(f)

# getting all symptoms from each std
symptom_list = []
for std in std_data:
  symptom_list += std_data[std]
# making sure symptoms are unique before inserting to graphdb
symptom_list = set(symptom_list)
print(symptom_list)

