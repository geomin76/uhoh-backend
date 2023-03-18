from service.neo4j_client import Neo4JClient
import json

neo4j = Neo4JClient()

with open('./std_data.json', 'r') as f:
  std_data = json.load(f)

class Neo4JFunctions:
    def get_stds(std_list):
        with neo4j.db().session(database="neo4j") as session:
            records = session.execute_read(Neo4JFunctions.query, std_list)
            return records
        
    def all_stds():
        with neo4j.db().session(database="neo4j") as session:
            records = session.execute_read(Neo4JFunctions.all_query)
            return records

    def query(tx, std_list):
        query = (
            """
            MATCH (p:Symptom) 
            WHERE p.name IN $std_list
            MATCH (p)-[r:SYMPTOM]->(s)
            RETURN s.name
            """
        )
        result = tx.run(query, std_list=std_list)
        records = list(result)
        return records
    
    def all_query(tx):
        query = (
            """
            MATCH (s:Symptom)
            RETURN s
            """
        )
        result = tx.run(query)
        records = list(result)
        return records
    
    def symptom_intersection(symptom_list, std_name):
        std_data_list = std_data[std_name]
        result = set(symptom_list).intersection(std_data_list)
        return result, len(result)

