from wikipedia_adminiship_election.code.wikpedia_adminship_election_parser import WikipediaAdminshipElectionParser


def export_graph():
    path_origin = '../originals/'
    path_destination = '../dataset/'
    min_num_vertices_list = [100,500,1000,2500,5000]
    parser = WikipediaAdminshipElectionParser()
    graphs = parser.parse(path_origin)
    for graph in graphs:
        graph_anonymized, _, _ = graph.generate_numeric_graph()
        graph_anonymized.save_graph_to_file(path_destination)

        for min_num_vertices in min_num_vertices_list:
            subgraph= graph_anonymized.generate_subgraph(min_num_vertices)
            subgraph,_,_ = subgraph.generate_numeric_graph()
            subgraph.save_graph_to_file(path_destination)
            parser.export_graph_properties(path_destination, 'properties.txt', subgraph)

    parser.export_properties(path_destination, 'properties.txt', graphs)

if __name__ == '__main__':
    export_graph()
