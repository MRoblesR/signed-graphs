# signed-graphs

In this repository, there are signed undirected graphs. These graphs are directly taken or adapted from other graphs.

This is the structure of the repository:

* `README.md`: this file.
* `LICENSE`: the license file.
* `datasets/`: directory containing the datasets.
* `code/`: directory containing the source code.
* `original/`: directory containing the original datasets.

Then, for each instance within the dataset directory, there is also a repository with the same name in the `code/`
directory.
This repository contains the source code used to generate the instance. Similarly, there is a repository with the same
name in the `original/` directory. This repository contains the original instance.

## Format

The input files are plain text files, each with the following structure:

The first line contains the number of vertices (`V`) and edges (`E`) in the graph, in the format `V E`.  
The remaining lines represent the edges in the graph, in the format `VertexA VertexB Weight`, where `VertexA`
and `VertexB` are integers from 1 to V, and Weight is an integer from $-1$ to $1$.  
For example, a graph with $5$ vertices and $3$ edges would be represented as follows:

    `5 3  
    1 2 1  
    1 3 1  
    2 3 -1`  

The edge between vertices $1$ and $2$ has a weight of $1$, the edge between vertices $1$ and $3$ has a weight of $1$,
and the edge between vertices $2$ and $3$ has a weight of $-1$.

## Datasets

Here we describe the datasets that are available in this repository.

Index:

* [Wikipedia adminship election data](#wikipedia-adminship-election-data)

### Wikipedia adminship election data

#### Dataset description

Wikipedia is a free encyclopedia written collaboratively by volunteers around the world. A small part of Wikipedia
contributors are administrators, who are users with access to additional technical features that aid in maintenance. In
order for a user to become an administrator a Request for adminship (RfA) is issued and the Wikipedia community via a
public discussion or a vote decides who to promote to adminship. Using the latest complete dump of Wikipedia page edit
history (from January 3 2008) we extracted all administrator elections and vote history data. This gave us nearly 2,800
elections with around 100,000 total votes and about 7,000 users participating in the elections (either casting a vote or
being voted on). Out of these 1,200 elections resulted in a successful promotion, while about 1,500 elections did not
result in the promotion. About half of the votes in the dataset are by existing admins, while the other half comes from
ordinary Wikipedia users.

#### Dataset conversion

We converted the dataset to the format described in the [Format](#format) section. In particular we need to convert the
directed graph to an undirected graph. To do so, we have to decide the weight of the edges. We do so as follows:

* If both users voted positively, we add an edge with weight 1.
* if both users voted negatively, we add an edge with weight -1.
* If one user voted positively and the other negatively, we DO NOT add an edge.
* If one user voted positively and the other did not vote, we add an edge with weight 1.
* If one user voted negatively and the other did not vote, we add an edge with weight -1.

#### Source

* J. Leskovec, D. Huttenlocher, J. Kleinberg. Signed Networks in Social Media. CHI 2010.
* J. Leskovec, D. Huttenlocher, J. Kleinberg. Predicting Positive and Negative Links in Online Social Networks. WWW
  2010.
* https://snap.stanford.edu/data/wiki-Elec.html