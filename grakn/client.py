"""Grakn python client."""

from typing import List, Dict, Any
import requests

Var = str
Concept = Dict[str, Any]
Result = Dict[Var, Concept]


class Graph:
    """Represents a Grakn graph, identified by a uri and a keyspace."""

    DEFAULT_URI: str = 'http://localhost:4567'

    def __init__(self, uri: str = DEFAULT_URI, keyspace: str = 'grakn'):
        self.uri = uri
        self.keyspace = keyspace

    def execute(self, query: str) -> List[Result]:
        """Execute a Graql query against the graph

        :param query: the Graql query string to execute against the graph
        :return: a list of query results
        """
        params = {'keyspace': self.keyspace, 'query': query,
                  'infer': False, 'materialise': False}
        headers = {'Accept': 'application/graql+json'}
        graql_url = f'{self.uri}/graph/graql'
        response = requests.get(graql_url, params, headers=headers)
        return response.json()['response']