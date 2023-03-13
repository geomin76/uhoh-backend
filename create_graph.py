import json
from service.neo4j_client import Neo4JClient

neo4j = Neo4JClient()

with open('./std_data.json', 'r') as f:
  std_data = json.load(f)

# getting all symptoms from each std
symptom_list = []
for std in std_data:
  symptom_list += std_data[std]
# making sure symptoms are unique before inserting to graphdb
symptom_list = set(symptom_list)

# creates symptom node
def create_symptom(tx, symptom_name):
  query = (
    "CREATE (s1:Symptom { name: $symptom_name }) "
  )
  result = tx.run(query, symptom_name=symptom_name)
  print(result)

# creates std node
def create_std(tx, std_name):
  query = (
    "CREATE (d1:STD { name: $std_name }) "
  )
  result = tx.run(query, std_name=std_name)
  print(result)

def symptom_std_relationship(tx, std_name, symptom_name):
  query = (
    """
    MATCH
        (s1:Symptom { name: $symptom_name }),
        (d1:STD { name: $std_name })
    CREATE (s1)-[:`SYMPTOM`]->(d1)
    """
  )
  result = tx.run(query, std_name=std_name, symptom_name=symptom_name)
  print(result)

# # inserts all the symptoms
# with neo4j.db().session(database="neo4j") as session:
#   for name in symptom_list:
#     result = session.execute_write(create_symptom, name)

# # inserts all STDs and relationships of symptoms -> STDs
# with neo4j.db().session(database="neo4j") as session:
#   for std_name in std_data:
#     session.execute_write(create_std, std_name)
#     for symptom_name in std_data[std_name]:
#       session.execute_write(symptom_std_relationship, std_name, symptom_name)

neo4j.close()