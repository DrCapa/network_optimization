# Minimum cost flow problem
We consider a network consists of five nodes and a set of arcs. There are two supply nodes (1 and 2) and two demand nodes (4 and 5). Note 3 is a transshipment node. 
```mermaid
graph LR;
    1((1))-->2;
    1-->3;
    1-->4;
    2((2))-->3;
    3((3))-->5;
    5((5))-->4;
    4((4))-->5;
```
In the input file are the given informations
* costs per unit flow through the arcs,
* maximal capacities for the arcs,
* net flow generated at the nodes.

The aim is to minimize the total costs of sending the available supply through the network to satisfy the demand. 