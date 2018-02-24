
"""
    test and learn neo4
    Note the imports - refer to the Neo4j introductory text.

"""
import configparser
from neo4j.v1 import GraphDatabase, basic_auth
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Basic access to Neo4j instance')
logger.info('First get the password credential from the configparser secrets file')

config = configparser.ConfigParser()
config.read('../.config/config')

logger.info('Notice how the string matches the contents of the file')

pw = config.get("configuration", "neo4jpw").strip("'")  # configparser adds extra quotes so strip them

logger.info('Now we set the url that we obtained from graphenedb.com')

graphenedb_url = 'bolt://hobby-opmhmhgpkdehgbkejbochpal.dbs.graphenedb.com:24786'

logger.info('Here I hard coded the username. I should read that from the file too in a real app')
graphenedb_user = 'andy'
graphenedb_pass = pw

logger.info('And now, get the Neo4j database')

driver = GraphDatabase.driver(graphenedb_url, auth=basic_auth(graphenedb_user, graphenedb_pass))


def main():
    logger.info('Establish a session with the database')
    session = driver.session()

    logger.info('Here we add a Person who has the name Bob. Note: care with quotes!')

    session.run("CREATE (n:Person {name:'Bob'})")

    logger.info('Now lets see if we can find Bob')

    result = session.run("MATCH (n:Person) RETURN n.name AS name")

    logger.info('And print what we find')

    for record in result:
        print(record["name"])
    session.close()

    logger.info('Note - this need some excpetion handling!')

if __name__ == '__main__':
    main()
