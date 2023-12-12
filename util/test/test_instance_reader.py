import unittest

from util.src.instance_parser_interface import InstanceParserInterface


class DummyInstanceParser(InstanceParserInterface):
    def parse(self, content: str):
        pass


class TestInstanceParserInterface(unittest.TestCase):
    def setUp(self):
        self.parser = DummyInstanceParser()

    def test_read_graph_from_file(self):
        file_path = 'test_graphs_folder/graph1.txt'
        expected_name = 'graph1.txt'
        expected_content = '1 2 1\n1 3 1\n2 3 -1\n4 5 -1\n'
        name, content = self.parser.read_graph_from_file(file_path)
        self.assertEqual(name, expected_name)
        self.assertEqual(content, expected_content)

    def test_read_graphs_from_path(self):
        dir_path = 'test_graphs_folder'
        expected_files = ['graph1.txt', 'graph2.txt', 'graph3.txt']
        expected_content = '1 2 1\n1 3 1\n2 3 -1\n4 5 -1\n'
        expected_contents = [
            expected_content,
            expected_content,
            expected_content
        ]

        files = self.parser.read_graphs_from_path(dir_path)
        file_names = [file[0] for file in files]
        file_contents = [file[1] for file in files]

        self.assertCountEqual(file_names, expected_files)
        self.assertCountEqual(file_contents, expected_contents)


if __name__ == '__main__':
    unittest.main()
