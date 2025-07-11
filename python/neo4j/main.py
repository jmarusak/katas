from neo4j import GraphDatabase

def main():
    uri = 'bolt://localhost:7687'
    auth = ('neo4j', 'secretgraph')

    driver = GraphDatabase.driver(uri, auth=auth)
    driver.verify_connectivity()

    summary = driver.execute_query("""
        CREATE (a:Person {name: $name})
        CREATE (b:Person {name: $friendName})
        CREATE (a)-[:KNOWS]->(b)
        """,
        name="Alice", friendName="David",
        database_="lineage",
    ).summary
    print("Created {nodes_created} nodes in {time} ms.".format(
        nodes_created=summary.counters.nodes_created,
        time=summary.result_available_after
    ))

    driver.close()

if __name__ == '__main__':
    main()
