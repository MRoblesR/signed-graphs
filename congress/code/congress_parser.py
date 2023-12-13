import os
from typing import List, Tuple

from util.src.graph import Graph
from util.src.instance_parser_interface import InstanceParserInterface


def get_numbers(line):
    return map(int, line.split())


class CongressParser(InstanceParserInterface):

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
        vertices = list(range(1,219+1))
        # Create an undirected graph
        graph = Graph(name=name, vertices=vertices, edges=[])
        # Parsing the content to extract edges and user IDs
        for line in lines[2:]:
            v, u, w = get_numbers(line)
            if not self.is_edge_already_added(graph,u,v):
                if w > 0:
                    graph.add_edge(u, v, 1)
                else:
                    graph.add_edge(u, v, -1)

        return graph

    def is_edge_already_added(self,graph,u,v):
        for edge in graph.get_edges():
            if (edge[0]==u and edge[1]==v) or (edge[1]==u and edge[0]==v):
                return True
        return False