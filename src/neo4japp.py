#!/usr/bin/env python

"""
Simple neo4j app

To illustrate relationships

This requires the neo4j

This assumes that you have a configuration file in a dir relative to this one:

.config/config

With the follwoing configuration in it:

[configuration]

neo4juser = your_graphenedb_username
neo4jpw = your_graphenedb_password

"""

import logging
from configparser import ConfigParser
from neo4j.v1 import GraphDatabase, basic_auth

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Simple app to illustrate Neo4j and relationships')

config = ConfigParser()
config.read('../.config/config')

username = config["configuration"]["neo4juser"]
password = config["configuration"]["neo4jpw"]

graphenedb_url = 'bolt://hobby-opmhmhgpkdehgbkejbochpal.dbs.graphenedb.com:24786'
graphenedb_user = username
graphenedb_pass = password

print("Using:", username, password)

driver = GraphDatabase.driver(graphenedb_url,
                              auth=basic_auth(graphenedb_user, graphenedb_pass))


def main():
    """
    Create some rel
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
