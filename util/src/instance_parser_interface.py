import os
from abc import ABC, abstractmethod
from typing import List, Tuple

from util.src.graph import Graph


class InstanceParserInterface(ABC):

    @abstractmethod
    def parse(self, path: str) -> 'Graph':
        """
        Parses the content string and returns a Graph object.
        :param content: String representation of the graph data
        :return: Graph object
        """
        pass

    def read_graph_from_file(self, path: str) -> Tuple[str, str]:
        """
        Reads a graph from a file and returns the name and content of the file.
        :param path: Path to the file containing the graph data
        :return: Tuple containing the name and content of the file (both as strings)
        """
        with open(path, 'r', errors='ignore') as file:
            file_content = file.read()
            file_name = os.path.basename(path)
        return file_name, file_content

    def read_graphs_from_path(self, path: str) -> List[Tuple[str, str]]:
        """
        Reads all the graphs from a directory and returns a list of tuples with name and content of each file.
        :param path: Path to the directory containing the graph data
        :return: List of tuples containing the name and content of each file (both as strings)
        """
        graphs = []
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isfile(file_path):
                file_name, file_content = self.read_graph_from_file(file_path)
                graphs.append((file_name, file_content))
        return graphs

    def export_graph_properties(self, path: str, file_name: str, graph: Graph):
        l=[graph]
        self.export_properties(path,file_name,l)

    def export_properties(self, path: str, file_name: str, graphs: List[Graph]):
        """
        Exports the properties of the graphs to a file.
        The format of the properties is as follows:
        Header --> Graph name  vertices   edges   density degree average_degree  average_pos_degree average_neg_degree average_weight complete
        Row 1  --> <graph_name>  <num_vertices>  <num_edges> <density>   <degree>    <average_degree>    <average_pos_degree>   <average_neg_degree>   <average_weight>    <complete>
        Row 2  --> <graph_name>  <num_vertices>  <num_edges> <density>   <degree>    <average_degree>    <average_pos_degree>   <average_neg_degree>   <average_weight>    <complete>
        :param path: Path to the file where the properties should be exported to
        :param file_name: Name of the file where the properties should be exported to. If the file exists,
        it will contain the properties in addition to the existing content. If the file does not exist, it will be created and will also add the header.
        :param graphs: List of graphs whose properties should be exported
        """
        with open(os.path.join(path, file_name), 'a') as file:
            if os.stat(os.path.join(path, file_name)).st_size == 0:
                file.write(
                    'Graph name\tvertices\tedges\tdensity\tdegree\taverage_degree\taverage_pos_degree\taverage_neg_degree\taverage_weight\tcomplete\n')
            for graph in graphs:
                name = graph.get_name()
                num_vertices = len(graph.get_vertices())
                num_edges = len(graph.get_edges())
                density = graph.get_density()
                degree = graph.get_degree()
                average_degree = graph.get_average_degree()
                average_pos_degree = graph.get_average_positive_degree()
                average_neg_degree = graph.get_average_negative_degree()
                average_weight = graph.get_average_weight()
                complete = graph.is_complete()
                file.write(
                    f'{name}\t{num_vertices}\t{num_edges}\t{density}\t{degree}\t{average_degree}\t{average_pos_degree}\t{average_neg_degree}\t{average_weight}\t{complete}\n')
