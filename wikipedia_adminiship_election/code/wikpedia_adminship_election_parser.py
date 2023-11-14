import os
from typing import List, Tuple

from util.src.graph import Graph
from util.src.instance_parser_interface import InstanceParserInterface


class WikipediaAdminshipElectionParser(InstanceParserInterface):
    def parse(self, path: str) -> List[Graph]:
        graph_list = []
        graphs_str = self.read_graphs_from_path(path)
        for graph_str in graphs_str:
            graph_list.append(self.parse_content(graph_str))
        return graph_list

    def parse_content(self, content: Tuple[str, str]) -> Graph:
        name = content[0]
        graph_str = content[1]
        lines = graph_str.split('\n')
        edges = []
        users = set()

        # Parsing the content to extract edges and user IDs
        for line in lines:
            if line.startswith('V'):
                _, vote, user_id, _, _ = line.split('\t')
                user_id = int(user_id)
                if user_id not in users:
                    users.add(user_id)

                edges.append((vote, user_id))

        # Create an undirected graph
        graph = Graph(name=name, vertices=list(users), edges=[])

        # Determine edges and weights based on voting rules
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                vote1, user_id1 = edges[i]
                vote2, user_id2 = edges[j]

                # Checking voting rules
                if user_id1 != user_id2:
                    if vote1 == '1' and vote2 == '1':
                        graph.add_edge(user_id1, user_id2, 1)
                    elif vote1 == '-1' and vote2 == '-1':
                        graph.add_edge(user_id1, user_id2, -1)
                    elif vote1 == '1' and vote2 == '0':
                        graph.add_edge(user_id1, user_id2, 1)
                    elif vote1 == '-1' and vote2 == '0':
                        graph.add_edge(user_id1, user_id2, -1)
                    elif vote1 == '0' and vote2 == '1':
                        graph.add_edge(user_id1, user_id2, 1)
                    elif vote1 == '0' and vote2 == '-1':
                        graph.add_edge(user_id1, user_id2, -1)

        return graph
