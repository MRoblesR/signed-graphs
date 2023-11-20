from typing import Dict, List, Tuple, Union
import os

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

    def get_degree(self, vertex: Union[str, int]) -> int:
        """
            This method `get_degree` is used to calculate the degree of a vertex in a Graph.

            :param vertex: The vertex whose degree needs to be calculated. It can be of type `int` or `str`.
            :return: Returns an integer representing the degree of the vertex.
        """
        degree: int = 0
        for edge in self._edges:
            if edge[0] == vertex or edge[1] == vertex:
                degree += 1
        return degree

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
            # For an undirected graph, add the line below to include the reverse direction
            # adjacency_list[edge[1]].append((edge[0], edge[2]))
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

    def save_graph_to_file(self, file_path: str):
        """
        Save the graph to a file in the specified format
        :param file_path: Path to the file to save the graph
        """
        file_name = file_path + self._name
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
