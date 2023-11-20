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
        edges = {}
        users = set()
        candidate_user_id = None
        # Parsing the content to extract edges and user IDs
        for line in lines:
            if line.startswith('U'):
                _, candidate_user_id, _ = line.split('\t')
                users.add(candidate_user_id)
            if line.startswith('V'):
                _, vote, voter_user_id, _, _ = line.split('\t')
                edges[voter_user_id, candidate_user_id] = int(vote)
                users.add(voter_user_id)

        # Create an undirected graph
        graph = Graph(name=name, vertices=list(users), edges=[])

        # Determine edges and weights based on voting rules
        list_of_users = list(users)
        for i in range(len(list_of_users)):
            for j in range(len(list_of_users)):
                # avoid u and v and then v and u
                if j <= i:
                    continue
                user_id1 = list_of_users[i]
                user_id2 = list_of_users[j]
                if user_id1 != user_id2:
                    vote1 = edges.get((user_id1, user_id2), 0)
                    vote2 = edges.get((user_id2, user_id1), 0)
                    if vote1 == 1 and vote2 == 1:
                        graph.add_edge(user_id1, user_id2, 1)
                    elif vote1 == -1 and vote2 == -1:
                        graph.add_edge(user_id1, user_id2, -1)
                    elif vote1 == 1 and vote2 == 0:
                        graph.add_edge(user_id1, user_id2, 1)
                    elif vote1 == -1 and vote2 == 0:
                        graph.add_edge(user_id1, user_id2, -1)
                    elif vote1 == 0 and vote2 == 1:
                        graph.add_edge(user_id1, user_id2, 1)
                    elif vote1 == 0 and vote2 == -1:
                        graph.add_edge(user_id1, user_id2, -1)

        return graph



