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


def setup_db():
    """
    sets up the connection to the neo4j DB

    configuration (username and password) is read from:

    ../.config/config
    """

    config = ConfigParser()
    config.read('../.config/config')

    graphenedb_user = config["configuration"]["neo4juser"]
    graphenedb_pass = config["configuration"]["neo4jpw"]
    # graphenedb_url = 'bolt://hobby-opmhmhgpkdehgbkejbochpal.dbs.graphenedb.com:24786'
    graphenedb_url = 'bolt://hobby-khhgnhgpkdehgbkeoldljpal.dbs.graphenedb.com:24786'

    driver = GraphDatabase.driver(graphenedb_url,
                                  auth=basic_auth(graphenedb_user, graphenedb_pass))

    return driver


def clear_all(driver):
    """
    This clears the entire database, so we can start over

    NOTE: The Docs say about this:

    "This query isn’t for deleting large amounts of data, but is nice
    when playing around with small example data sets."

    I suppose if you have a really big datbase, you should just throw
    it away and make a new one.
    """
    logger.info("Running clear_all")

    with driver.session() as session:
        logger.info("Before clearing: all the records")
        result = session.run("MATCH (n) RETURN n")
        msg = ("There are these records:" +
               "\n".join([str(rec) for rec in result]))
        session.run("MATCH (n) DETACH DELETE n")


def test1(driver):
    """
    Create some relations
    """
    with driver.session() as session:
        logger.info('Here we add a Person who has the name Bob. Note: care with quotes!')

        session.run("CREATE (n:Person {name:'Bob'})")

        logger.info('Now lets see if we can find Bob')

        result = session.run("MATCH (n:Person) RETURN n.name AS name")

        logger.info('And print what we find')

        for record in result:
            print(record["name"])

        print(dir(record))

        logger.info('Note - this needs some exception handling!')


if __name__ == '__main__':
    driver = setup_db()
    test1(driver)

