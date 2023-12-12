import os
from typing import Dict, List, Tuple, Union
import random


class Graph:
    """
    Graph
    =====

    :class:`Graph` is a class that represents a graph data structure. It supports various operations such as retrieving information about the graph, retrieving the adjacency list, getting adjacent vertices, and generating a numeric graph.

    Initialization
    --------------
        .. code-block:: python

            graph = Graph(name="", vertices=[], edges=[])

        - The ``name`` parameter is optional and defaults to an empty string.
        - The ``vertices`` parameter is optional and defaults to an empty list. It represents the vertices in the graph and can be a list of strings or integers.
        - The ``edges`` parameter is optional and defaults to an empty list. It represents the edges in the graph and can be a list of tuples. Each tuple contains three elements:
          - The source vertex, which can be either a string or an integer.
          - The destination vertex, which can be either a string or an integer.
          - The weight of the edge, represented as an integer.

    Methods
    -------
        .. code-block:: python

            graph.get_name() -> str
            graph.get_vertices() -> List[Union[str, int]]
            graph.get_edges() -> List[Tuple[Union[str, int], Union[str, int], int]]
            graph.get_adjacency_list() -> Dict[Union[str, int], List[Tuple[Union[str, int], int]]]
            graph.get_adjacent_vertices(vertex: Union[str, int]) -> List[Tuple[Union[str, int], int]]
            graph.get_degree(vertex: Union[str, int]) -> int
            graph.generate_numeric_graph() -> Tuple['Graph', Dict[str, int], Dict[int, str]]

        get_name()
            Returns the name of the graph.

        get_vertices()
            Returns a list of all vertices in the graph.

        get_edges()
            Returns a list of all edges in the graph.

        get_adjacency_list()
            Returns the adjacency list of the graph. The adjacency list is a dictionary where the keys represent the vertices of the graph. Each key is associated with a list of tuples, where each tuple contains information about the neighboring vertices and their respective edge weights.

        get_adjacent_vertices(vertex)
            Returns a list of tuples representing the adjacent vertices and their corresponding edge weights for a given vertex.

        get_degree(vertex)
            Returns the degree of a given vertex.

        generate_numeric_graph()
            Generates a numeric graph from the current graph. Returns a tuple containing the generated numeric graph object, a dictionary mapping vertex names to their corresponding numeric indices, and a dictionary mapping numeric indices to their corresponding vertex names.

    Attributes
    ----------
        graph._name : str
            The name of the graph.
        graph._vertices : List[Union[str, int]]
            The list of vertices in the graph.
        graph._edges : List[Tuple[Union[str, int], Union[str, int], int]]
            The list of edges in the graph.
        graph._adjacency_list : Dict[Union[str, int], List[Tuple[Union[str, int], int]]]
            The adjacency list of the graph.

    Private Methods
    ---------------
        graph.__generate_adjacency_list() -> Dict[Union[str, int], List[Tuple[Union[str, int], int]]]
            Generates the adjacency list for the graph.

    Example Usage
    -------------
        .. code-block:: python

            graph = Graph(name="my_graph", vertices=["A", "B", "C", "D"], edges=[("A", "B", 10), ("B", "C", 5), ("C", "D", 8), ("D", "A", 6)])
            print(graph.get_name())  # Output: "my_graph"
            print(graph.get_vertices())  # Output: ["A", "B", "C", "D"]
            print(graph.get_edges())  # Output: [("A", "B", 10), ("B", "C", 5), ("C", "D", 8), ("D", "A", 6)]
            print(graph.get_adjacency_list())
            # Output: {"A": [("B", 10), ("D", 6)], "B": [("A", 10), ("C", 5)], "C": [("B", 5), ("D", 8)], "D": [("C", 8), ("A", 6)]}
            print(graph.get_adjacent_vertices("A"))  # Output: [("B", 10), ("D", 6)]
            print(graph.get_degree("A"))  # Output: 2
            numeric_graph, str_to_int_map, int_to_str_map = graph.generate_numeric_graph()

    """

    def __init__(self, name: str = "", vertices: List[Union[str, int]] = None,
                 edges: List[Tuple[Union[str, int], Union[str, int], int]] = None):
        """
        Initializes a new instance of the Graph class with the specified parameters.

        :param name: The name of the graph. Defaults to an empty string.
        :type name: str
        :param vertices: A list of vertices in the graph. Each vertex can be a string or an integer.
        :type vertices: List[Union[str, int]]
        :param edges: A list of edges in the graph. Each edge is a tuple containing two vertices and a weight. The vertices can be either strings or integers, and the weight must be an integer.
        :type edges: List[Tuple[Union[str, int], Union[str, int], int]]
        """
        self._name: str = name
        self._vertices: List[Union[str, int]] = vertices if vertices else []
        self._edges: List[Tuple[Union[str, int], Union[str, int], int]] = edges if edges else []
        self._adjacency_list: Dict[
            Union[str, int], List[Tuple[Union[str, int], int]]] = self.__generate_adjacency_list()

    def get_name(self) -> str:
        """
        Returns the name of the graph.

        :return: The name of the graph.
        :rtype: str
        """
        return self._name

    def get_vertices(self) -> List[Union[str, int]]:
        """
        Return all vertices of the graph.

        :return: A list of vertices, where each vertex is represented as either a string or an integer.
        """
        return self._vertices

    def get_edges(self) -> List[Tuple[Union[str, int], Union[str, int], int]]:
        """
        Returns a list of edges in the graph.

        :return: A list of tuples representing the edges in the graph. Each tuple consists of three elements:
                 - The source vertex, which can be either a string or an integer.
                 - The destination vertex, which can be either a string or an integer.
                 - The weight of the edge, represented as an integer.
        """
        return self._edges

    def get_adjacency_list(self) -> Dict[Union[str, int], List[Tuple[Union[str, int], int]]]:
        """
        :return: Returns the adjacency list of the graph.

        The adjacency list is a dictionary where the keys represent the vertices of the graph. Each key is associated with a list of tuples, where each tuple contains information about the neighboring vertices and their respective edge weights.

        The adjacency list data structure is represented as:
            {
                vertex: [(neighbor1, weight1), (neighbor2, weight2), ...],
                vertex2: [(neighbor3, weight3), (neighbor4, weight4), ...],
                ...
            }

        :return: A dictionary with keys representing graph vertices and values representing a list of neighboring vertices with their edge weights.
        """
        return self._adjacency_list

    def get_adjacent_vertices(self, vertex: Union[str, int]) -> List[Tuple[Union[str, int], int]]:
        """
        :param vertex: The vertex for which adjacent vertices are to be retrieved. Can be either a string or an integer.
        :return: A list of tuples representing the adjacent vertices and their corresponding edge weights. Each tuple contains a vertex (string or integer) and an associated weight (integer).

        """
        return self._adjacency_list[vertex]

    def add_edge(self, u, v, weight):
        """
        Add an edge to the graph
        :param u: Source vertex
        :param v: Destination vertex
        :param weight: Weight of the edge
        """
        self._edges.append((u, v, weight))
        self._adjacency_list[u].append((v, weight))
        self._adjacency_list[v].append((u, weight))

    def __generate_adjacency_list(self) -> Dict[Union[str, int], List[Tuple[Union[str, int], int]]]:
        """
        Generates the adjacency list for the graph.

        :return: A dictionary representing the adjacency list.
        :rtype: Dict[Union[str, int], List[Tuple[Union[str, int], int]]]
        """
        adjacency_list: Dict[Union[str, int], List[Tuple[Union[str, int], int]]] = {}
        for vertex in self._vertices:
            adjacency_list[vertex] = []
        for edge in self._edges:
            adjacency_list[edge[0]].append((edge[1], edge[2]))
            # For a directed graph, comment the line below to exclude the reverse direction
            adjacency_list[edge[1]].append((edge[0], edge[2]))
        return adjacency_list

    def generate_numeric_graph(self) -> Tuple['Graph', Dict[str, int], Dict[int, str]]:
        """
        Generate a numeric graph from the current graph.

        Vertices goes from 1 to n, where n is the number of vertices in the graph.

        :return: A tuple containing the generated numeric graph object, a dictionary mapping vertex names to their corresponding numeric indices, and a dictionary mapping numeric indices to their corresponding vertex names.
        """
        numeric_graph = Graph(name=self._name, vertices=list(range(1, len(self._vertices) + 1)), edges=[])
        str_to_int_map: Dict[str, int] = {}
        int_to_str_map: Dict[int, str] = {}

        for i in range(len(self._vertices)):
            str_to_int_map[self._vertices[i]] = i + 1
            int_to_str_map[i + 1] = self._vertices[i]

        for edge in self._edges:
            numeric_graph.add_edge(str_to_int_map[edge[0]], str_to_int_map[edge[1]], edge[2])

        return numeric_graph, str_to_int_map, int_to_str_map

    def save_graph_to_file(self, file_path: str, file_name: str = None):
        """
        Save the graph to a file in the specified format
        :param file_path: Path to the file to save the graph
        """
        file_name = file_path + ((self._name if self._name != "" else "graph") if file_name is None else file_name)
        # if it does not end with .txt, add .txt
        if not file_name.endswith('.txt'):
            file_name += '.txt'

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_name, 'w') as file:
            num_vertices = len(self._vertices)
            num_edges = len(self._edges)
            file.write(f"{num_vertices} {num_edges}\n")

            for edge in self._edges:
                vertex_a, vertex_b, weight = edge
                file.write(f"{vertex_a} {vertex_b} {weight}\n")

    def read_graph_from_file(self, file_path: str) -> Tuple[int, int, List[Tuple[int, int, int]]]:
        """
        Read graph data from a file and initialize the graph.
        :param file_path: Path to the file containing graph data
        :return: Tuple containing number of vertices, number of edges, and edges list
        """
        with open(file_path, 'r') as file:
            # Read the first line to get the number of vertices and edges
            num_vertices, num_edges = map(int, file.readline().split())

            edges = []
            for line in file:
                vertex_a, vertex_b, weight = map(int, line.split())
                edges.append((vertex_a, vertex_b, weight))

            # Update the graph instance with the read data
            self._vertices = list(range(1, num_vertices + 1))  # Assuming vertices are labeled from 1 to num_vertices
            self._edges = edges
            self._adjacency_list = self.__generate_adjacency_list()

        return num_vertices, num_edges, edges

    def subgraph(self, vertex: "str or int") -> 'Graph':
        """
        Returns a subgraph of the current graph, containing only the specified vertex and its adjacent vertices.
        It also includes the edges between the adjacent vertices.
        :param vertex: The vertex for which the subgraph is to be generated.
        :return: A subgraph of the current graph, containing only the specified vertex and its adjacent vertices.
        """
        subgraph_vertices = set()
        subgraph_edges = set()
        subgraph_vertices.add(vertex)
        for edge in self._edges:
            if edge[0] == vertex or edge[1] == vertex:
                subgraph_edges.add(edge)
                subgraph_vertices.add(edge[0])
                subgraph_vertices.add(edge[1])
        # loop over the edges again to add the edges between the adjacent vertices
        for edge in self._edges:
            if edge[0] in subgraph_vertices and edge[1] in subgraph_vertices:
                subgraph_edges.add(edge)
        return Graph(name=self._name, vertices=list(subgraph_vertices), edges=list(subgraph_edges))

    def generate_subgraph(self, min_num_vertices):
        random.seed(42)
        new_graph = Graph(str(min_num_vertices)+self.get_name())
        unused_vertices = self.get_vertices().copy()

        while len(new_graph.get_vertices()) < min_num_vertices and unused_vertices:
            random_vertex= unused_vertices.pop(random.randint(0,len(unused_vertices)-1))
            new_graph=new_graph.union(self.subgraph(random_vertex))
            for v in self.get_adjacent_vertices(random_vertex):
                if v[0] in unused_vertices:
                    unused_vertices.remove(v[0])
        return new_graph
    def union(self, other: "Graph") -> "Graph":
        """
        Returns the union of the current graph and the specified graph.
        :param other: The graph to be unioned with the current graph.
        :return: The union of the current graph and the specified graph.
        """
        union_edges = self._edges + other.get_edges()
        union_vertices = self._vertices+other.get_vertices()
        return Graph(name=self._name, vertices=union_vertices, edges=union_edges)

    def print_graph(self, file_path: str = None, file_name: str = None):
        """
        Prints the graph as a png image using networkx and matplotlib.
        :param file_path: Path to the file to save the graph. If it is none, just show it
        :param file_name: Name of the file to save the graph. if its note, it will use the graph name. If graph name is none or "" just leavi it as graph
        """
        import networkx as nx
        import matplotlib.pyplot as plt

        G = nx.Graph()
        G.add_nodes_from(self._vertices)
        G.add_weighted_edges_from(self._edges)
        pos = nx.random_layout(G)
        nx.draw(G, pos, with_labels=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        if file_path is None:
            plt.show()
        else:
            file_name = file_path + ((self._name if self._name != "" else "graph") if file_name is None else file_name)
            # if it does not end with .png, add .png
            if not file_name.endswith('.png'):
                file_name += '.png'
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            plt.savefig(file_name)
            plt.close()

    def get_degree(self, vertex: Union[str, int] = None) -> int:
        """
            This method `get_degree` is used to calculate the degree of a vertex in a Graph.
            :param vertex: The vertex whose degree needs to be calculated. It can be of type `int` or `str`. If `None` is passed, the degree of all vertices will be calculated and returned the maximum degree of all vertices.
            :return: Returns an integer representing the degree of the vertex.
        """
        if vertex is None:
            return max([self.get_degree(vertex) for vertex in self._vertices])
        degree: int = 0
        for edge in self._edges:
            if edge[0] == vertex or edge[1] == vertex:
                degree += 1
        return degree

    def get_positive_degree(self, vertex: Union[str, int] = None) -> int:
        """
            This method `get_positive_degree` is used to calculate the positive degree of a vertex in a Graph.
            :param vertex: The vertex whose positive degree needs to be calculated. It can be of type `int` or `str`. If `None` is passed, the positive degree of all vertices will be calculated and returned the maximum positive degree of all vertices.
            :return: Returns an integer representing the positive degree of the vertex.
        """
        if vertex is None:
            return max([self.get_positive_degree(vertex) for vertex in self._vertices])
        degree: int = 0
        for edge in self._edges:
            if edge[0] == vertex or edge[1] == vertex:
                if edge[2] > 0:
                    degree += 1
        return degree

    def get_negative_degree(self, vertex: Union[str, int] = None) -> int:
        """
            This method `get_negative_degree` is used to calculate the negative degree of a vertex in a Graph.
            :param vertex: The vertex whose negative degree needs to be calculated. It can be of type `int` or `str`. If `None` is passed, the negative degree of all vertices will be calculated and returned the maximum negative degree of all vertices.
            :return: Returns an integer representing the negative degree of the vertex.
        """
        if vertex is None:
            return max([self.get_negative_degree(vertex) for vertex in self._vertices])
        degree: int = 0
        for edge in self._edges:
            if edge[0] == vertex or edge[1] == vertex:
                if edge[2] < 0:
                    degree += 1
        return degree

    def get_average_degree(self):
        """
        Returns the average degree of the graph.
        """
        return sum([self.get_degree(vertex) for vertex in self._vertices]) / len(self._vertices)

    def get_average_negative_degree(self):
        """
        Returns the average negative degree of the graph.
        """
        return sum([self.get_negative_degree(vertex) for vertex in self._vertices]) / len(self._vertices)

    def get_average_positive_degree(self):
        """
        Returns the average positive degree of the graph.
        """
        return sum([self.get_positive_degree(vertex) for vertex in self._vertices]) / len(self._vertices)

    def get_average_weight(self):
        """
        Returns the average weight of the graph.
        """
        return sum([edge[2] for edge in self._edges]) / len(self._edges)

    def get_density(self):
        """
        Returns the density of the graph.
        """
        return 2 * len(self._edges) / (len(self._vertices) * (len(self._vertices) - 1))

    def get_positive_density(self):
        """
        Returns the positive density of the graph.
        """
        return 2 * self.get_number_of_positives_edges() / (len(self._vertices) * (len(self._vertices) - 1))

    def get_negative_density(self):
        """
        Returns the negative density of the graph.

        """
        return 2 * self.get_number_of_negatives_edges() / (len(self._vertices) * (len(self._vertices) - 1))

    def get_number_of_positives_edges(self):
        """
        Calculates the number of positive edges in the graph.

        :return: The number of positive edges in the graph.
        :rtype: int
        """
        number_of_positives_edges = 0
        for edge in self._edges:
            if edge[2] > 0:
                number_of_positives_edges += 1
        return number_of_positives_edges

    def get_number_of_negatives_edges(self):
        """
        Returns the number of negative edges in the graph.

        :return: The number of negative edges.
        """
        number_of_negatives_edges = 0
        for edge in self._edges:
            if edge[2] < 0:
                number_of_negatives_edges += 1
        return number_of_negatives_edges

    def is_complete(self):
        """
        Returns true if the graph is complete.
        """
        for vertex in self._vertices:
            if self.get_degree(vertex) != len(self._vertices) - 1:
                return False
        return True
