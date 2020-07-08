# Lobby Centrality


In a graph, given a set of neighbors from a vertex _v_, the Lobby
centrality or h-index is calculated by ranking the neighbors according
to their degrees in a decreasing order, and selecting the last
position where its degree is less or equal than its position value.

For example, if we have the following list of neighbors, the Lobby
index is **3** because it is the last position where the degree of
the neighbor is greater than its position in the ranking.


| neighbor | position | degree |
|:--------:|:--------:|:------:|
| "e"      | 1        | 21     |
| "d"      | 2        | 18     |
| "b"      | **3**    | **4**  |
| "c"      | 4        | 3      |


![Alt text](https://g.gravizo.com/source/custom_mark10?https:%2F%2Fraw.githubusercontent.com%2Fajholanda%2Flobby-centrality%2Fmaster%2FREADME.md)
<details>
<summary></summary>
custom_mark10
  digraph G {
    size ="4,4";
    main [shape=box];
    main -> parse [weight=8];
    parse -> execute;
    main -> init [style=dotted];
    main -> cleanup;
    execute -> { make_string; printf};
    init -> make_string;
    edge [color=red];
    main -> printf [style=bold,label="100 times"];
    make_string [label="make a string"];
    node [shape=box,style=filled,color=".7 .3 1.0"];
    execute -> compare;
  }
custom_mark10
</details>


The Python3 code to process the data should be

````
def lobby(v2degs):
    '''Return the Lobby index from a dictionary of vertices and degrees'''
    l = 0 # Lobby index
    # Sort the degree values
    degs = sorted(v2degs.values(), reverse=True)
    for deg in degs:
        l += 1
        if deg <= l: # Found Lobby index
            break
    return l

v2degs = {"b": 4, "c": 3, "d": 18, "e": 21 }
print("The lobby index is {}".format(lobby(v2degs)))

````

## References

1. Hirsch, J. E. ["An index to quantify an individual's scientific
   research
   output"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1283832/). PNAS
   102 (46), 2005.

2.  A. Korn, A. Schubert, A. Telcs. [Lobby index in
    networks](https://www.sciencedirect.com/science/article/abs/pii/S0378437109001587)
    Physica A, 388 (11), 2009.

3. M. G. Campiteli, A. J. Holanda, L. D. H. Soares, P. R. C. Soles, O. Kinouchi.
  [Lobby index as a network centrality measure](Lobby index as a network centrality measure).
  Physica A, 394, 2014.
