from wikipedia_adminiship_election.code.wikpedia_adminship_election_parser import WikipediaAdminshipElectionParser


def export_graph():
    path_origin = '../originals/'
    path_destination = '../dataset/'
    parser = WikipediaAdminshipElectionParser()
    graphs = parser.parse(path_origin)
    for graph in graphs:
        graph.save_graph_to_file(path_destination)


if __name__ == '__main__':
    export_graph()