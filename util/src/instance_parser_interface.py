import os
from abc import ABC, abstractmethod
from typing import List, Tuple


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
        with open(path, 'r') as file:
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
