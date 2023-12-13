from congress_parser import CongressParser


def export_graph():
    path_origin = '../original/'
    path_destination = '../dataset/'
    parser = CongressParser()
    graphs = parser.parse(path_origin)
    for graph in graphs:
        graph_anonymized, _, _ = graph.generate_numeric_graph()
        graph_anonymized.save_graph_to_file(path_destination)

    parser.export_properties(path_destination, 'properties.txt', graphs)

if __name__ == '__main__':
    export_graph()
