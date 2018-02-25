"""
    andy's standard
"""

from setuptools import setup
setup(
    name='dbs-neo4j',
    description='Neo4j examples',
    author='Andy Miles',
    author_email='akmiles@icloud.com',
    url='https://github.com/milesak60/dbs-neo4j',
    setup_requires=[
        'pytest-runner',
        'pytest-pylint',
    ],
    tests_require=[
        'pytest',
        'pylint',
    ],
)