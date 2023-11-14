import unittest

from util.src.graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        # Creating a sample graph for testing
        self.vertices = [1, 2, 3, 4, 5]
        self.edges = [
            (1, 2, 1),
            (1, 3, 1),
            (2, 3, -1),
            (4, 5, -1)
        ]
        self.graph = Graph(vertices=self.vertices, edges=self.edges)

    def test_get_vertices(self):
        self.assertEqual(self.graph.get_vertices(), self.vertices)

    def test_get_edges(self):
        self.assertEqual(self.graph.get_edges(), self.edges)

    def test_get_adjacency_list(self):
        # Test adjacency list for a specific vertex
        adjacency_list = self.graph.get_adjacency_list()
        self.assertEqual(adjacency_list[1], [(2, 1), (3, 1)])  # Expected adjacency list for vertex 1

    def test_get_adjacent_vertices(self):
        # Test adjacent vertices for a specific vertex
        adjacent_vertices = self.graph.get_adjacent_vertices(2)
        self.assertEqual(adjacent_vertices, [(3, -1)])  # Expected adjacent vertices for vertex 2

    def test_get_degree(self):
        # Test the degree of a specific vertex
        degree = self.graph.get_degree(1)
        self.assertEqual(degree, 2)  # Expected degree for vertex 1

    def test_generate_numeric_graph(self):
        # Test generating a numeric graph
        numeric_graph, _, _ = self.graph.generate_numeric_graph()
        self.assertIsInstance(numeric_graph, Graph)

    def test_save_and_read_graph(self):
        # Save the graph to a file
        self.graph.save_graph_to_file('graph1.txt')

        # Create a new graph and read data from the file
        new_graph = Graph()
        num_vertices, num_edges, edges = new_graph.read_graph_from_file('graph1.txt')

        # Assertions to check if the read data matches the original graph data
        self.assertEqual(num_vertices, len(self.vertices))
        self.assertEqual(num_edges, len(self.edges))
        self.assertListEqual(edges, self.edges)

        # Clean up
        import os
        os.remove('graph1.txt')



if __name__ == '__main__':
    unittest.main()
