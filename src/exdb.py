
"""
	test and learn heroku neo4
"""
import configparser

from neo4j.v1 import GraphDatabase, basic_auth

config = configparser.ConfigParser()
config.read('../.config/config')
pw = config.get("configuration", "neo4jpw").strip("'")  # cp adds extra quotes
graphenedb_url = 'bolt://localhost:7687'
graphenedb_user = 'neo4j'
graphenedb_pass = pw

driver = GraphDatabase.driver(graphenedb_url, auth=basic_auth(graphenedb_user, graphenedb_pass))


def main():
	session = driver.session()

	session.run("CREATE (n:Person {name:'Bob'})")
	result = session.run("MATCH (n:Person) RETURN n.name AS name")
	for record in result:
		print(record["name"])
	session.close()

if __name__ == '__main__':
	main()
