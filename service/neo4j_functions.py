from service.neo4j_client import Neo4JClient

neo4j = Neo4JClient()

class Neo4JFunctions:
    def get_stds(std_list):
        with neo4j.db().session(database="neo4j") as session:
            records = session.execute_read(Neo4JFunctions.query, std_list)
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
