
"""
    simple neo4j app
    Illustrate relationships

"""
import configparser
from neo4j.v1 import GraphDatabase, basic_auth
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Simple app to illustrate Neo4j and relationships')
config = configparser.ConfigParser()
config.read('../.config/config')
pw = config.get("configuration", "neo4jpw").strip("'")  # configparser adds extra quotes so strip them
graphenedb_url = 'bolt://hobby-opmhmhgpkdehgbkejbochpal.dbs.graphenedb.com:24786'
graphenedb_user = 'andy'
graphenedb_pass = pw
driver = GraphDatabase.driver(graphenedb_url, auth=basic_auth(graphenedb_user, graphenedb_pass))


def main():
    """
        Create some related records
    """
    session = driver.session()

    logger.info('Here we add a Person who has the name Bob. Note: care with quotes!')

    session.run("CREATE (n:Person {name:'Bob'})")

    logger.info('Now lets see if we can find Bob')

    result = session.run("MATCH (n:Person) RETURN n.name AS name")

    logger.info('And print what we find')

    for record in result:
        print(record["name"])

    session.close()

    logger.info('Note - this needs some exception handling!')

if __name__ == '__main__':
    main()
