# signed-graphs

In this repository, there are signed undirected graphs. These graphs are directly taken or adapted from other graphs.

## Format

The files are stored in plain text. Each one of them has a first line "_vertices: <#Vertices> edges: <#Edges>_", where <#Vertices> and <#Edges> represent the number of vertices and edges respectively. The rest of the lines represent each one an edge of the graph, the format is "_<VertexA> <VertexB> \[1,-1\]_", where both \<VertexA> and \<VertexB> are integers from 1 to \<#Vertices>, and \[1,-1\] represent either a positive or negative connection. For example, a positive connection between vertices 5 and 8 is represented as "5 8 1", and a negative one as "5 8 -1".

Each one of the edges is unique and undirected, so if an edge "\<VertexA> \<VertexB>" exists already, the same edge "\<VertexB> \<VertexA>" should not exist.

