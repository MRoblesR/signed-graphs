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

        # number of edges
        self.assertEqual(len(self.graph.get_edges()), 4)

        # number of positive edges
        self.assertEqual(2, self.graph.get_number_of_positives_edges())

        # number of negative edges
        self.assertEqual(2, self.graph.get_number_of_positives_edges())

    def test_get_adjacency_list(self):
        # Test adjacency list for a specific vertex
        adjacency_list = self.graph.get_adjacency_list()
        self.assertEqual(adjacency_list[1], [(2, 1), (3, 1)])  # Expected adjacency list for vertex 1

    def test_get_adjacent_vertices(self):
        # Test adjacent vertices for a specific vertex
        adjacent_vertices = self.graph.get_adjacent_vertices(2)
        self.assertEqual([(1, 1), (3, -1)], adjacent_vertices)

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
        self.graph.save_graph_to_file('test_graphs_folder/', 'test_graph_save.txt')

        # Create a new graph and read data from the file
        new_graph = Graph()
        num_vertices, num_edges, edges = new_graph.read_graph_from_file('test_graphs_folder/test_graph_save.txt')

        # Assertions to check if the read data matches the original graph data
        self.assertEqual(num_vertices, len(self.vertices))
        self.assertEqual(num_edges, len(self.edges))
        self.assertListEqual(edges, self.edges)

        # Clean up
        import os
        os.remove('test_graphs_folder/test_graph_save.txt')

    def test_subgraph(self):
        # Test subgraph
        """
        1 2 1
        1 3 1
        2 3 -1
        4 5 -1
        """
        subgraph = self.graph.subgraph(1)
        self.assertIsInstance(subgraph, Graph)
        self.assertEqual([1, 2, 3], subgraph.get_vertices())
        self.assertEqual([(1, 2, 1), (1, 3, 1), (2, 3, -1)], subgraph.get_edges())


    def test_print_graph(self):
        # check that the file is created and then deleted
        import os
        subgraph = self.graph.subgraph(1)
        subgraph.print_graph('test_graphs_folder/', 'test_graph_print.txt')
        self.assertTrue(os.path.exists('test_graphs_folder/test_graph_print.txt.png'))
        os.remove('test_graphs_folder/test_graph_print.txt.png')


    def test_degree(self):
        """
        Testing functions:
        get_degree (of the graph and of a specific vertex)
        get_positive_degree (of the graph and of a specific vertex)
        get_negative_degree (of the graph and of a specific vertex)
        get_average_degree
        get_average_negative_degree
        get_average_positive_degree
        Using the following graph:
        1 2 1
        1 3 1
        2 3 -1
        4 5 -1
        """
        # Test get_degree of the graph
        self.assertEqual(2, self.graph.get_degree())

        # Test get degree of a specific vertex
        self.assertEqual(2, self.graph.get_degree(1))
        self.assertEqual(2, self.graph.get_degree(2))
        self.assertEqual(2, self.graph.get_degree(3))
        self.assertEqual(1, self.graph.get_degree(4))
        self.assertEqual(1, self.graph.get_degree(5))

        # Test get_positive_degree of the graph
        self.assertEqual(2, self.graph.get_positive_degree())

        # Test get_positive_degree of a specific vertex
        self.assertEqual(2, self.graph.get_positive_degree(1))
        self.assertEqual(1, self.graph.get_positive_degree(2))
        self.assertEqual(1, self.graph.get_positive_degree(3))
        self.assertEqual(0, self.graph.get_positive_degree(4))
        self.assertEqual(0, self.graph.get_positive_degree(5))

        # Test get_negative_degree of the graph
        self.assertEqual(1, self.graph.get_negative_degree())

        # Test get_negative_degree of a specific vertex
        self.assertEqual(0, self.graph.get_negative_degree(1))
        self.assertEqual(1, self.graph.get_negative_degree(2))
        self.assertEqual(1, self.graph.get_negative_degree(3))
        self.assertEqual(1, self.graph.get_negative_degree(4))
        self.assertEqual(1, self.graph.get_negative_degree(5))

        # Test get_average_degree
        self.assertEqual((2+2+2+1+1)/5, self.graph.get_average_degree())

        # Test get_average_positive_degree
        self.assertEqual((2+1+1+0+0)/5, self.graph.get_average_positive_degree())

        # Test get_average_negative_degree
        self.assertEqual((0+1+1+1+1)/5, self.graph.get_average_negative_degree())


    def test_density(self):
        """
        Testing functions:
        get_density
        get_positive_density
        get_negative_density
        Using the following graph:
        1 2 1
        1 3 1
        2 3 -1
        4 5 -1
        """
        # Test get_density
        self.assertEqual((2*4)/(5*(5-1)), self.graph.get_density())

        # Test get_positive_density
        self.assertEqual((2*2)/(5*(5-1)), self.graph.get_positive_density())

        # Test get_negative_density
        self.assertEqual((2*2)/(5*(5-1)), self.graph.get_negative_density())



if __name__ == '__main__':
    unittest.main()
