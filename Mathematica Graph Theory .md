



# Graph theory features in Mathematica and Sage

Attached is a spreadsheet listing the Sage graph library functions and the equivalent functions in Combinatorica.  I've also put a few notes in about the implementation differences and other notes suggesting changes to Sage functions.

In the following list, I tried to make the functions link to the official documentation at the Wolfram website.  I hope it all worked right.



## Construction and representations



### Graphs and components


 * Edges
   * Sage
     * [http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.edge_iterator graphs.generic_graph.GenericGraph]
       * [http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.edge_iterator edge_iterator]
       * [http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.edges edges]
       * [http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.multiple_edges multiple_edges]
     * [http://www.sagemath.org/doc/reference/sage/graphs/base/sparse_graph.html#sage.graphs.base.sparse_graph.SparseGraphBackend graphs.base.sparse_graph.SparseGraphBackend]
       * [http://www.sagemath.org/doc/reference/sage/graphs/base/sparse_graph.html#sage.graphs.base.sparse_graph.SparseGraphBackend.iterator_edges iterator_edges]
       * [http://www.sagemath.org/doc/reference/sage/graphs/base/sparse_graph.html#sage.graphs.base.sparse_graph.SparseGraphBackend.iterator_in_edges iterator_in_edges]
       * [http://www.sagemath.org/doc/reference/sage/graphs/base/sparse_graph.html#sage.graphs.base.sparse_graph.SparseGraphBackend.iterator_out_edges iterator_out_edges]
     * [http://www.sagemath.org/doc/reference/sage/graphs/base/dense_graph.html#sage.graphs.base.dense_graph.DenseGraphBackend graphs.base.dense_graph.DenseGraphBackend]
       * [http://www.sagemath.org/doc/reference/sage/graphs/base/dense_graph.html#sage.graphs.base.dense_graph.DenseGraphBackend.iterator_edges iterator_edges]
       * [http://www.sagemath.org/doc/reference/sage/graphs/base/dense_graph.html#sage.graphs.base.dense_graph.DenseGraphBackend.iterator_in_edges iterator_in_edges]
       * [http://www.sagemath.org/doc/reference/sage/graphs/base/dense_graph.html#sage.graphs.base.dense_graph.DenseGraphBackend.iterator_out_edges iterator_out_edges]
   * Mathematica --- [Edges](http://reference.wolfram.com/mathematica/Combinatorica/ref/Edges.html)[g] gives the list of edges in g. 

 * Graph
   * Sage
     * [http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html generic graphs]
     * [http://www.sagemath.org/doc/reference/sage/graphs/graph.html undirected graphs]
     * [http://www.sagemath.org/doc/reference/sage/graphs/digraph.html directed graphs]
     * [http://www.sagemath.org/doc/reference/sage/graphs/base/c_graph.html fast compiled graphs]
     * [http://www.sagemath.org/doc/reference/sage/graphs/base/sparse_graph.html fast sparse graphs]
     * [http://www.sagemath.org/doc/reference/sage/graphs/base/dense_graph.html fast dense graphs]
   * Mathematica --- [Graph](http://reference.wolfram.com/mathematica/Combinatorica/ref/Graph.html)[e, v, opts] represents a graph object where e is the list of edges annotated with graphics options, v is a list of vertices annotated with graphics options, and opts is a set of global graph options.

 * Number of edges
   * Sage
     * [http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph graphs.generic_graph.GenericGraph]
       * [http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.num_edges num_edges]
       * [http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.size size]
     * [http://www.sagemath.org/doc/reference/sage/graphs/base/c_graph.html#sage.graphs.base.c_graph.CGraphBackend graphs.base.c_graph.CGraphBackend]
       * [http://www.sagemath.org/doc/reference/sage/graphs/base/c_graph.html#sage.graphs.base.c_graph.CGraphBackend.num_edges num_edges]
   * Mathematica --- [M](http://reference.wolfram.com/mathematica/Combinatorica/ref/M.html)[g] gives the number of edges in the graph g. 

 * Number of vertices
   * Sage
     * [http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph graphs.generic_graph.GenericGraph]
       * [http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.num_verts num_verts]
       * [http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.order order]
     * [http://www.sagemath.org/doc/reference/sage/graphs/base/c_graph.html#sage.graphs.base.c_graph.CGraphBackend graphs.base.c_graph.CGraphBackend]
       * [http://www.sagemath.org/doc/reference/sage/graphs/base/c_graph.html#sage.graphs.base.c_graph.CGraphBackend.num_verts num_verts]
   * Mathematica --- [V](http://reference.wolfram.com/mathematica/Combinatorica/ref/V.html)[g] gives the order or number of vertices of the graph g.

 * Vertices
   * Sage
     * [http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph graphs.generic_graph.GenericGraph]
       * [http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.vertex_iterator vertex_iterator]
       * [http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.vertices vertices]
     * [http://www.sagemath.org/doc/reference/sage/graphs/base/c_graph.html#sage.graphs.base.c_graph.CGraph graphs.base.c_graph.CGraph]
       * [http://www.sagemath.org/doc/reference/sage/graphs/base/c_graph.html#sage.graphs.base.c_graph.CGraph.verts verts]
     * [http://www.sagemath.org/doc/reference/sage/graphs/base/c_graph.html#sage.graphs.base.c_graph.CGraphBackend graphs.base.c_graph.CGraphBackend]
       * [http://www.sagemath.org/doc/reference/sage/graphs/base/c_graph.html#sage.graphs.base.c_graph.CGraphBackend.iterator_verts iterator_verts]
   * Mathematica --- [Vertices](http://reference.wolfram.com/mathematica/Combinatorica/ref/Vertices.html)[g] gives the coordinates of each vertex of graph g embedded in a plane.
   


### Graph representations


 * From adjacency lists
   * Sage ---
   * Mathematica --- [FromAdjacencyLists](http://reference.wolfram.com/mathematica/Combinatorica/ref/FromAdjacencyLists.html)[l] constructs an edge list representation for a graph from the given adjacency lists l, using a circular embedding. 

 * From adjacency matrix
   * Sage ---
   * Mathematica --- [FromAdjacencyMatrix](http://reference.wolfram.com/mathematica/Combinatorica/ref/FromAdjacencyMatrix.html)[m] constructs a graph from a given adjacency matrix m, using a circular embedding. 

 * From ordered pairs
   * Sage ---
   * Mathematica --- [FromOrderedPairs](http://reference.wolfram.com/mathematica/Combinatorica/ref/FromOrderedPairs.html)[l] constructs an edge list representation from a list of ordered pairs l, using a circular embedding. 
   
 * From unordered pairs
   * Sage ---
   * Mathematica --- [FromUnorderedPairs](http://reference.wolfram.com/mathematica/Combinatorica/ref/FromUnorderedPairs.html)[l] constructs an edge list representation from a list of unordered pairs l, using a circular embedding.

 * Incidence matrix
   * Sage ---
   * Mathematica --- [IncidenceMatrix](http://reference.wolfram.com/mathematica/Combinatorica/ref/IncidenceMatrix.html)[g] returns the (0,1)-matrix of graph g, which has a row for each vertex and a column for each edge and (v,e)=1 if and only if vertex v is incident upon edge e. For a directed graph, (v,e)=1 if edge e is outgoing from v.

 * To adjacency lists
   * Sage ---
   * Mathematica --- [ToAdjacencyLists](http://reference.wolfram.com/mathematica/Combinatorica/ref/ToAdjacencyLists.html)[g] constructs an adjacency list representation for graph g. It allows an option called Type that takes on values All or Simple. Type -> All is the default setting of the option, and this permits self-loops and multiple edges to be reported in the adjacency lists. Type -> Simple deletes self-loops and multiple edges from the constructed adjacency lists. [ToAdjacencyLists](http://reference.wolfram.com/mathematica/Combinatorica/ref/ToAdjacencyLists.html)[g, [EdgeWeight](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeWeight.html)] returns an adjacency list representation along with edge weights.

 * To adjacency matrix
   * Sage ---
   * Mathematica --- [ToAdjacencyMatrix](http://reference.wolfram.com/mathematica/Combinatorica/ref/ToAdjacencyMatrix.html)[g] constructs an adjacency matrix representation for graph g. 

 * To ordered pairs
   * Sage ---
   * Mathematica --- [ToOrderedPairs](http://reference.wolfram.com/mathematica/Combinatorica/ref/ToOrderedPairs.html)[g] constructs a list of ordered pairs representing the edges of the graph g. If g is undirected each edge is interpreted as two ordered pairs. An option called Type that takes on values Simple or All can be used to affect the constructed representation. Type -> Simple forces the removal of multiple edges and self-loops. Type -> All keeps all information and is the default option.

 * To unordered pairs
   * Sage ---
   * Mathematica --- [ToUnorderedPairs](http://reference.wolfram.com/mathematica/Combinatorica/ref/ToUnorderedPairs.html)[g] constructs a list of unordered pairs representing the edges of graph g. Each edge, directed or undirected, results in a pair in which the smaller vertex appears first. An option called Type that takes on values All or Simple can be used, and All is the default value. Type -> Simple ignores multiple edges and self-loops in g.



### Displaying graphs


 * Animate graph
   * Sage ---
   * Mathematica --- [AnimateGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/AnimateGraph.html)[g, l] displays graph g with each element in the list l successively highlighted. Here l is a list containing vertices and edges of g. An optional flag, which takes on the values All and One, can be used to inform the function about whether objects highlighted earlier will continue to be highlighted or not. The default value of flag is All. All the options allowed by the function Highlight are permitted by [AnimateGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/AnimateGraph.html), as well. See the usage message of Highlight for more details.

 * Change edges
   * Sage ---
   * Mathematica --- [ChangeEdges](http://reference.wolfram.com/mathematica/Combinatorica/ref/ChangeEdges.html)[g, e] replaces the edges of graph g with the edges in e. e can have the form {{s1, t1}, {s2, t2}, ...} or the form { {{s1, t1}, gr1}, {{s2, t2}, gr2}, ...}, where {s1, t1}, {s2, t2}, ... are endpoints of edges and gr1, gr2, ... are graphics information associated with edges.

 * Change vertices
   * Sage ---
   * Mathematica --- [ChangeVertices](http://reference.wolfram.com/mathematica/Combinatorica/ref/ChangeVertices.html)[g, v] replaces the vertices of graph g with the vertices in the given list v. v can have the form {{x1, y1}, {x2, y2}, ...} or the form {{{x1, y1}, gr1}, {{x2, y2}, gr2}, ...}, where {x1, y1}, {x2, y2}, ... are coordinates of points and gr1, gr2, ... are graphics information associated with vertices.

 * Circular embedding
   * Sage ---
   * Mathematica --- [CircularEmbedding](http://reference.wolfram.com/mathematica/Combinatorica/ref/CircularEmbedding.html)[n] constructs a list of n points equally spaced on a circle. [CircularEmbedding](http://reference.wolfram.com/mathematica/Combinatorica/ref/CircularEmbedding.html)[g] embeds the vertices of g equally spaced on a circle.

 * Edge color
   * Sage ---
   * Mathematica --- [EdgeColor](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeColor.html) is an option that allows the user to associate colors with edges. Black is the default color. EdgeColor can be set as part of the graph data structure or in ShowGraph.

 * Edge direction
   * Sage ---
   * Mathematica --- [EdgeDirection](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeDirection.html) is an option that takes on values True or False allowing the user to specify whether the graph is directed or not. EdgeDirection can be set as part of the graph data structure or in ShowGraph.

 * Edge label
   * Sage ---
   * Mathematica --- [EdgeLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeLabel.html) is an option that can take on values True or False, allowing the user to associate labels to edges. By default, there are no edge labels. The EdgeLabel option can be set as part of the graph data structure or in ShowGraph.

 * Edge label color
   * Sage ---
   * Mathematica --- [EdgeLabelColor](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeLabelColor.html) is an option that allows the user to associate different colors to edge labels. Black is the default color. EdgeLabelColor can be set as part of the graph data structure or in ShowGraph.

 * Edge label position
   * Sage ---
   * Mathematica --- [EdgeLabelPosition](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeLabelPosition.html) is an option that allows the user to place an edge label in a certain position relative to the midpoint of the edge. LowerLeft is the default value of this option. EdgeLabelPosition can be set as part of the graph data structure or in ShowGraph.

 * Edge style
   * Sage ---
   * Mathematica --- [EdgeStyle](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeStyle.html) is an option that allows the user to associate different sizes and shapes to edges. A line segment is the default edge. EdgeStyle can be set as part of the graph data structure or in ShowGraph.

 * Edge weight
   * Sage ---
   * Mathematica --- [EdgeWeight](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeWeight.html) is an option that allows the user to associate weights with edges. 1 is the default weight. [EdgeWeight](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeWeight.html) can be set as part of the graph data structure.

 * Graph options
   * Sage ---
   * Mathematica --- [GraphOptions](http://reference.wolfram.com/mathematica/Combinatorica/ref/GraphOptions.html)[g] returns the display options associated with g. 

 * Highlight
   * Sage ---
   * Mathematica --- Highlight[g, p] displays g with elements in p highlighted. The second argument p has the form {s1, s2,...}, where the sis are disjoint subsets of vertices and edges of g. The options, [HighlightedVertexStyle](http://reference.wolfram.com/mathematica/Combinatorica/ref/HighlightedVertexStyle.html), [HighlightedEdgeStyle](http://reference.wolfram.com/mathematica/Combinatorica/ref/HighlightedEdgeStyle.html), [HighlightedVertexColors](http://reference.wolfram.com/mathematica/Combinatorica/ref/HighlightedVertexColors.html), and [HighlightedEdgeColors](http://reference.wolfram.com/mathematica/Combinatorica/ref/HighlightedEdgeColors.html) are used to determine the appearance of the highlighted elements of the graph. The default settings of the style options are [HighlightedVertexStyle](http://reference.wolfram.com/mathematica/Combinatorica/ref/HighlightedVertexStyle.html)->Disk[Large] and [HighlightedEdgeStyle](http://reference.wolfram.com/mathematica/Combinatorica/ref/HighlightedEdgeStyle.html)->Thick. The options [HighlightedVertexColors](http://reference.wolfram.com/mathematica/Combinatorica/ref/HighlightedVertexColors.html) and [HighlightedEdgeColors](http://reference.wolfram.com/mathematica/Combinatorica/ref/HighlightedEdgeColors.html) are both set to {Black, Red, Blue, Green, Yellow, Purple, Brown, Orange, Olive, Pink, [DeepPink](http://reference.wolfram.com/mathematica/Combinatorica/ref/DeepPink.html), [DarkGreen](http://reference.wolfram.com/mathematica/Combinatorica/ref/DarkGreen.html), Maroon, Navy}. The colors are chosen from the palette of colors with color 1 used for s1, color 2 used for s2, and so on. If there are more parts than colors, then the colors are used cyclically. The function permits all the options that [SetGraphOptions](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetGraphOptions.html) permits, for example, [VertexColor](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexColor.html), [VertexStyle](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexStyle.html), [EdgeColor](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeColor.html), and [EdgeStyle](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeStyle.html). These options can be used to control the appearance of the non-highlighted vertices and edges.

 * Highlighted edge colors
   * Sage ---
   * Mathematica --- [HighlightedEdgeColors](http://reference.wolfram.com/mathematica/Combinatorica/ref/HighlightedEdgeColors.html) is an option to Highlight that determines which colors are used for the highlighted edges.

 * Highlighted edge style
   * Sage ---
   * Mathematica --- [HighlightedEdgeStyle](http://reference.wolfram.com/mathematica/Combinatorica/ref/HighlightedEdgeStyle.html) is an option to Highlight that determines how the highlighted edges are drawn.

 * Highlighted vertex colors
   * Sage ---
   * Mathematica --- [HighlightedVertexColors](http://reference.wolfram.com/mathematica/Combinatorica/ref/HighlightedVertexColors.html) is an option to Highlight that determines which colors are used for the highlighted vertices.

 * Highlighted vertex style
   * Sage ---
   * Mathematica --- [HighlightedVertexStyle](http://reference.wolfram.com/mathematica/Combinatorica/ref/HighlightedVertexStyle.html) is an option to Highlight that determines how the highlighted vertices are drawn.

 * Loop position
   * Sage ---
   * Mathematica --- [LoopPosition](http://reference.wolfram.com/mathematica/Combinatorica/ref/LoopPosition.html) is an option to ShowGraph whose values tell ShowGraph where to position a loop around a vertex. This option can take on values UpperLeft, UpperRight, LowerLeft, and LowerRight.

 * Ranked embedding
   * Sage ---
   * Mathematica --- [RankedEmbedding](http://reference.wolfram.com/mathematica/Combinatorica/ref/RankedEmbedding.html)[l] takes a set partition l of vertices {1, 2,..., n} and returns an embedding of the vertices in the plane such that the vertices in each block occur on a vertical line with block 1 vertices on the leftmost line, block 2 vertices in the next line, and so on. [RankedEmbedding](http://reference.wolfram.com/mathematica/Combinatorica/ref/RankedEmbedding.html)[g, l] takes a graph g and a set partition l of the vertices of g and returns the graph g with vertices embedded according to [RankedEmbedding](http://reference.wolfram.com/mathematica/Combinatorica/ref/RankedEmbedding.html)[l]. [RankedEmbedding](http://reference.wolfram.com/mathematica/Combinatorica/ref/RankedEmbedding.html)[g, s] takes a graph g and a set s of vertices of g and returns a ranked embedding of g in which vertices in s are in block 1, vertices at distance 1 from any vertex in block 1 are in block 2, and so on.

 * Radial embedding
   * Sage ---
   * Mathematica --- [RadialEmbedding](http://reference.wolfram.com/mathematica/Combinatorica/ref/RadialEmbedding.html)[g, v] constructs a radial embedding of the graph g in which vertices are placed on concentric circles around v depending on their distance from v. [RadialEmbedding](http://reference.wolfram.com/mathematica/Combinatorica/ref/RadialEmbedding.html)[g] constructs a radial embedding of graph g, radiating from the center of the graph.

 * Rank graph
   * Sage ---
   * Mathematica --- [RankGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/RankGraph.html)[g, l] partitions the vertices into classes based on the shortest geodesic distance to a member of list l.

 * Rooted embedding
   * Sage ---
   * Mathematica --- [RootedEmbedding](http://reference.wolfram.com/mathematica/Combinatorica/ref/RootedEmbedding.html)[g, v] constructs a rooted embedding of graph g with vertex v as the root. [RootedEmbedding](http://reference.wolfram.com/mathematica/Combinatorica/ref/RootedEmbedding.html)[g] constructs a rooted embedding with a center of g as the root.

 * Rotate vertices
   * Sage ---
   * Mathematica --- [RotateVertices](http://reference.wolfram.com/mathematica/Combinatorica/ref/RotateVertices.html)[v, theta] rotates each vertex position in list v by theta radians about the origin (0, 0). [RotateVertices](http://reference.wolfram.com/mathematica/Combinatorica/ref/RotateVertices.html)[g, theta] rotates the embedding of the graph g by theta radians about the origin (0, 0).

 * Set edge labels
   * Sage ---
   * Mathematica --- [SetEdgeLabels](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetEdgeLabels.html)[g, l] assigns the labels in l to edges of g. 

 * Set edge weights
   * Sage ---
   * Mathematica --- [SetEdgeWeights](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetEdgeWeights.html)[g] assigns random real weights in the range [0,1] to edges in g. 

 * Set graph options
   * Sage ---   
   * Mathematica --- [SetGraphOptions](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetGraphOptions.html)[g, opts] returns g with the options opts set. [SetGraphOptions](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetGraphOptions.html)[g, {v1, v2, ..., vopts}, gopts] returns the graph with the options vopts set for vertices v1, v2, ... and the options gopts set for the graph g. [SetGraphOptions](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetGraphOptions.html)[g, {e1, e2,..., eopts}, gopts], with edges e1, e2,..., works similarly. [SetGraphOptions](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetGraphOptions.html)[g, {{elements1, opts1}, {elements2, opts2},...}, opts] returns g with the options opts1 set for the elements in the sequence elements1, the options opts2 set for the elements in the sequence elements2, and so on. Here, elements can be a sequence of edges or a sequence of vertices. A tag that takes on values One or All can also be passed in as an argument before any options. The default value of the tag is All and it is useful if the graph has multiple edges. It informs the function about whether all edges that connect a pair of vertices are to be affected or only one edge is affected.

 * Set vertex labels
   * Sage ---
   * Mathematica --- [SetVertexLabels](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetVertexLabels.html)[g, l] assigns the labels in l to vertices of g. If l is shorter than the number of vertices in g, then labels get assigned cyclically. If l is longer than the number of vertices in g, then the extra labels are ignored." 

 * Set vertex weights
   * Sage ---
   * Mathematica --- [SetVertexWeights](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetVertexWeights.html)[g] assigns random real weights in the range [0, 1] to vertices in g. [SetVertexWeights](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetVertexWeights.html) accepts options [WeightingFunction](http://reference.wolfram.com/mathematica/Combinatorica/ref/WeightingFunction.html) and [WeightRange](http://reference.wolfram.com/mathematica/Combinatorica/ref/WeightRange.html). [WeightingFunction](http://reference.wolfram.com/mathematica/Combinatorica/ref/WeightingFunction.html) can take values Random, [RandomInteger](http://reference.wolfram.com/mathematica/Combinatorica/ref/RandomInteger.html), or any pure function that takes two arguments, an integer as the first argument and a pair {number, number} as the second argument. [WeightRange](http://reference.wolfram.com/mathematica/Combinatorica/ref/WeightRange.html) can be an integer range or a real range. The default value for [WeightingFunction](http://reference.wolfram.com/mathematica/Combinatorica/ref/WeightingFunction.html) is Random and the default value for [WeightRange](http://reference.wolfram.com/mathematica/Combinatorica/ref/WeightRange.html) is [0, 1]. [SetVertexWeights](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetVertexWeights.html)[g, w] assigns the weights in the weight list w to the vertices of g. [SetVertexWeights](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetVertexWeights.html)[g, vs, w] assigns the weights in the weight list w to the vertices in the vertex list vs.

 * Shake graph
   * Sage ---
   * Mathematica --- [ShakeGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/ShakeGraph.html)[g, d] performs a random perturbation of the vertices of graph g, with each vertex moving, at most, a distance d from its original position.

 * Show graph
   * Sage ---
   * Mathematica --- [ShowGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/ShowGraph.html)[g] displays the graph g. 

 * Show graph array
   * Sage ---
   * Mathematica --- [ShowGraphArray](http://reference.wolfram.com/mathematica/Combinatorica/ref/ShowGraphArray.html)[{g1, g2, ...}] displays a row of graphs. 

 * Show labeled graph
   * Sage ---
   * Mathematica --- [ShowLabeledGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/ShowLabeledGraph.html)[g] displays graph g according to its embedding, with each vertex labeled with its vertex number. [ShowLabeledGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/ShowLabeledGraph.html)[g, l] uses the ith element of list l as the label for vertex i.

 * Spring embedding
   * Sage ---
   * Mathematica --- [SpringEmbedding](http://reference.wolfram.com/mathematica/Combinatorica/ref/SpringEmbedding.html)[g] beautifies the embedding of graph g by modeling the embedding as a system of springs. [SpringEmbedding](http://reference.wolfram.com/mathematica/Combinatorica/ref/SpringEmbedding.html)[g, step, increment] can be used to refine the algorithm. The value of step tells the function for how many iterations to run the algorithm. The value of increment tells the function the distance to move the vertices at each step. The default values are 10 and 0.15 for step and increment, respectively.

 * Translate vertices
   * Sage ---
   * Mathematica --- [TranslateVertices](http://reference.wolfram.com/mathematica/Combinatorica/ref/TranslateVertices.html)[v, {x, y}] adds the vector {x, y} to the vertex embedding location of each vertex in list v. [TranslateVertices](http://reference.wolfram.com/mathematica/Combinatorica/ref/TranslateVertices.html)[g, {x, y}] translates the embedding of the graph g by the vector {x, y}.

 * Vertex color
   * Sage ---
   * Mathematica --- [VertexColor](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexColor.html) is an option that allows the user to associate colors with vertices. 

 * Vertex label
   * Sage ---
   * Mathematica --- [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html) is an option that can take on values True or False, allowing the user to set and display vertex labels. 

 * Vertex label color
   * Sage ---
   * Mathematica --- [VertexLabelColor](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabelColor.html) is an option that allows the user to associate different colors to vertex labels.

 * Vertex label position
   * Sage ---
   * Mathematica --- [VertexLabelPosition](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabelPosition.html) is an option that allows the user to place a vertex label in a certain position relative to the vertex. 

 * Vertex number
   * Sage ---
   * Mathematica --- [VertexNumber](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexNumber.html) is an option that can take on values True or False. This can be used in ShowGraph to display or suppress vertex numbers. 

 * Vertex number color
   * Sage ---
   * Mathematica --- [VertexNumberColor](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexNumberColor.html) is an option that can be used in ShowGraph to associate different colors to vertex numbers. 

 * Vertex number position
   * Sage ---
   * Mathematica --- [VertexNumberPosition](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexNumberPosition.html) is an option that can be used in ShowGraph to display a vertex number in a certain position relative to the vertex. 

 * Vertex style
   * Sage ---
   * Mathematica --- [VertexStyle](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexStyle.html) is an option that allows the user to associate different sizes and shapes to vertices.

 * Vertex weight
   * Sage ---
   * Mathematica --- [VertexWeight](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexWeight.html) is an option that allows the user to associate weights with vertices. 0 is the default weight. [VertexWeight](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexWeight.html) can be set as part of the graph data structure.

 * Zoom
   * Sage ---   
   * Mathematica --- [Zoom](http://reference.wolfram.com/mathematica/Combinatorica/ref/Zoom.html)[{i, j, k, ...}] is a value that the [PlotRange](http://reference.wolfram.com/mathematica/Combinatorica/ref/PlotRange.html) option can take on in [ShowGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/ShowGraph.html). Setting [PlotRange](http://reference.wolfram.com/mathematica/Combinatorica/ref/PlotRange.html) to this value zooms the display to contain the specified subset of vertices, i, j, k, ....



### Constructing graphs


 * Add edge
   * Sage ---
   * Mathematica --- [AddEdge](http://reference.wolfram.com/mathematica/Combinatorica/ref/AddEdge.html)[g, e] returns a graph g with the new edge e added. e can have the form {a,b} or the form {{a,b},options}.

 * Add edges
   * Sage ---
   * Mathematica --- [AddEdges](http://reference.wolfram.com/mathematica/Combinatorica/ref/AddEdges.html)[g, edgeList] gives graph g with the new edges in edgeList added. edgeList can have the form {a,b} to add a single edge {a,b} or the form {{a,b},{c,d},...}, to add edges {a,b},{c,d},... or the form {{{a,b},x},{{c,d},y},...}, where x and y can specify graphics information associated with {a,b} and {c,d}, respectively.

 * Add vertex
   * Sage ---
   * Mathematica --- [AddVertex](http://reference.wolfram.com/mathematica/Combinatorica/ref/AddVertex.html)[g] adds one disconnected vertex to graph g. 

 * Add vertices
   * Sage ---
   * Mathematica --- [AddVertices](http://reference.wolfram.com/mathematica/Combinatorica/ref/AddVertices.html)[g, n] adds n disconnected vertices to graph g. 

 * Approximate vertex cover
   * Sage ---
   * Mathematica --- [ApproximateVertexCover](http://reference.wolfram.com/mathematica/Combinatorica/ref/ApproximateVertexCover.html)[g] produces a vertex cover of graph g whose size is guaranteed to be within twice the optimal size.

 * Cartesian product
   * Sage ---
   * Mathematica --- [CartesianProduct](http://reference.wolfram.com/mathematica/Combinatorica/ref/CartesianProduct.html)[l1, l2] gives the Cartesian product of lists l_1 and l_2.

 * Code to labeled tree
   * Sage ---
   * Mathematica --- [CodeToLabeledTree](http://reference.wolfram.com/mathematica/Combinatorica/ref/CodeToLabeledTree.html)[l] constructs the unique labeled tree on n vertices from the Prufer code l, which consists of a list of n-2 integers between 1 and n.

 * Complete binary tree
   * Sage ---
   * Mathematica --- [CompleteBinaryTree](http://reference.wolfram.com/mathematica/Combinatorica/ref/CompleteBinaryTree.html)[n] returns a complete binary tree on n vertices.

 * Complete k-ary tree
   * Sage ---
   * Mathematica --- [CompleteKaryTree](http://reference.wolfram.com/mathematica/Combinatorica/ref/CompleteKaryTree.html)[n, k] returns a complete k-ary tree on n vertices.

 * Contract
   * Sage ---
   * Mathematica --- [Contract](http://reference.wolfram.com/mathematica/Combinatorica/ref/Contract.html)[g, {x, y}] gives the graph resulting from contracting the pair of vertices {x, y} of graph g.

 * Delete cycle
   * Sage ---
   * Mathematica --- [DeleteCycle](http://reference.wolfram.com/mathematica/Combinatorica/ref/DeleteCycle.html)[g, c] deletes a simple cycle c from graph g. c is specified as a sequence of vertices in which the first and last vertices are identical. g can be directed or undirected. If g does not contain c, it is returned unchanged; otherwise g is returned with c deleted." 

 * Delete edge
   * Sage ---
   * Mathematica --- [DeleteEdge](http://reference.wolfram.com/mathematica/Combinatorica/ref/DeleteEdge.html)[g, e] gives graph g minus e. If g is undirected, then e is treated as an undirected edge; otherwise it is treated as a directed edge. If there are multiple edges between the specified vertices, only one edge is deleted. 

 * Delete edges
   * Sage ---
   * Mathematica --- [DeleteEdges](http://reference.wolfram.com/mathematica/Combinatorica/ref/DeleteEdges.html)[g, edgeList] gives graph g minus the list of edges edgeList. If g is undirected, then the edges in edgeList are treated as undirected edges; otherwise they are treated as directed edges. If there are multiple edges that qualify, then only one edge is deleted. 

 * Delete vertex
   * Sage ---
   * Mathematica --- [DeleteVertex](http://reference.wolfram.com/mathematica/Combinatorica/ref/DeleteVertex.html)[g, v] deletes a single vertex v from graph g. Here v is a vertex number.

 * Delete vertices
   * Sage ---
   * Mathematica --- [DeleteVertices](http://reference.wolfram.com/mathematica/Combinatorica/ref/DeleteVertices.html)[g, vList] deletes vertices in vList from graph g. vList has the form {i,j,...}, where i,j,... are vertex numbers.

 * Exact random graph
   * Sage ---
   * Mathematica --- [ExactRandomGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/ExactRandomGraph.html)[n, e] constructs a random labeled graph of exactly e edges and n vertices.

 * Functional graph
   * Sage ---
   * Mathematica --- [FunctionalGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/FunctionalGraph.html)[f, v] takes a set v and a function f from v to v and constructs a directed graph with vertex set v and edges (x, f(x)) for each x in v. [FunctionalGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/FunctionalGraph.html)[f, v], where f is a list of functions, constructs a graph with vertex set v and edge set (x, fi(x)) for every fi in f. An option called Type that takes on the values Directed and Undirected is allowed. Type -> Directed is the default, while Type -> Undirected returns the corresponding underlying undirected graph. [FunctionalGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/FunctionalGraph.html)[f, n] takes a nonnegative integer n and a function f from {0,1,..., n-1} onto itself and produces the directed graph with vertex set {0, 1,..., n-1} and edge set {x, f(x)} for each vertex x." 

 * Graph complement
   * Sage ---
   * Mathematica --- [GraphComplement](http://reference.wolfram.com/mathematica/Combinatorica/ref/GraphComplement.html)[g] gives the complement of graph g.

 * Graph difference
   * Sage ---
   * Mathematica --- [GraphDifference](http://reference.wolfram.com/mathematica/Combinatorica/ref/GraphDifference.html)[g, h] constructs the graph resulting from subtracting the edges of graph h from the edges of graph g.

 * Graph intersection
   * Sage ---
   * Mathematica --- [GraphIntersection](http://reference.wolfram.com/mathematica/Combinatorica/ref/GraphIntersection.html)[g1, g2, ...] constructs the graph defined by the edges that are in all the graphs g1, g2, ....

 * Graph join
   * Sage ---
   * Mathematica --- [GraphJoin](http://reference.wolfram.com/mathematica/Combinatorica/ref/GraphJoin.html)[g1, g2, ...] constructs the join of graphs g1, g2, and so on. This is the graph obtained by adding all possible edges between different graphs to the graph union of g1, g2, ....

 * Graph product
   * Sage ---
   * Mathematica --- [GraphProduct](http://reference.wolfram.com/mathematica/Combinatorica/ref/GraphProduct.html)[g1, g2, ...] constructs the product of graphs g_1, g_2, and so forth.

 * Graph sum
   * Sage ---
   * Mathematica --- [GraphSum](http://reference.wolfram.com/mathematica/Combinatorica/ref/GraphSum.html)[g1, g2, ...] constructs the graph resulting from joining the edge lists of graphs g1, g2, and so forth.

 * Graph union
   * Sage ---
   * Mathematica --- [GraphUnion](http://reference.wolfram.com/mathematica/Combinatorica/ref/GraphUnion.html)[g1, g2, ...] constructs the union of graphs g_1, g_2, and so forth. 

 * Greedy vertex cover
   * Sage --- Unavailable
   * Mathematica --- [GreedyVertexCover](http://reference.wolfram.com/mathematica/Combinatorica/ref/GreedyVertexCover.html)[g] returns a vertex cover of graph g constructed using the greedy algorithm. This is a natural heuristic for constructing a vertex cover, but it can produce poor vertex covers.

 * Independent set q
   * Sage ---
   * Mathematica --- [IndependentSetQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/IndependentSetQ.html)[g, i] yields True if the vertices in list i define an independent set in graph g.

 * Induce subgraph
   * Sage ---
   * Mathematica --- [InduceSubgraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/InduceSubgraph.html)[g, s] constructs the subgraph of graph g induced by the list of vertices s.

 * Interval graph
   * Sage --- #8284
   * Mathematica --- [IntervalGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/IntervalGraph.html)[l] constructs the interval graph defined by the list of intervals l.

 * Labeled tree to code
   * Sage ---
   * Mathematica --- [LabeledTreeToCode](http://reference.wolfram.com/mathematica/Combinatorica/ref/LabeledTreeToCode.html)[g] reduces the tree g to its Prufer code.

 * Line graph
   * Sage ---
   * Mathematica --- [LineGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/LineGraph.html)[g] constructs the line graph of graph g.

 * Make directed
   * Sage ---
   * Mathematica --- [MakeDirected](http://reference.wolfram.com/mathematica/Combinatorica/ref/MakeDirected.html)[g] constructs a directed graph from a given undirected graph g by replacing each undirected edge in g by two directed edges pointing in opposite directions. 

 * Make graph
   * Sage ---
   * Mathemaica --- [MakeGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/MakeGraph.html)[v, f] constructs the graph whose vertices correspond to v and edges between pairs of vertices x and y in v for which the binary relation defined by the Boolean function f is True. [MakeGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/MakeGraph.html) takes two options, Type and [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html). Type can be set to Directed or Undirected and this tells [MakeGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/MakeGraph.html) whether to construct a directed or an undirected graph. The default setting is Directed. [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html) can be set to True or False, with False being the default setting. Using [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html) -> True assigns labels derived from v to the vertices of the graph.

 * Make simple
   * Sage ---   
   * Mathematica --- [MakeSimple](http://reference.wolfram.com/mathematica/Combinatorica/ref/MakeSimple.html)[g] gives the undirected graph, free of multiple edges and self-loops derived from graph g.

 * Make undirected
   * Sage ---
   * Mathematica --- [MakeUndirected](http://reference.wolfram.com/mathematica/Combinatorica/ref/MakeUndirected.html)[g] gives the underlying undirected graph of the given directed graph g.

 * Maximum clique
   * Sage --- [clique_maximum](http://www.sagemath.org/doc/reference/sage/graphs/graph.html#sage.graphs.graph.Graph.clique_maximum)
   * Mathematica --- [MaximumClique](http://reference.wolfram.com/mathematica/Combinatorica/ref/MaximumClique.html)[g] finds a largest clique in graph g. 

 * Maximum independent set
   * Sage --- [independent_set](http://www.sagemath.org/doc/reference/sage/graphs/graph.html#sage.graphs.graph.Graph.independent_set)
   * Mathematica --- [MaximumIndependentSet](http://reference.wolfram.com/mathematica/Combinatorica/ref/MaximumIndependentSet.html)[g] finds a largest independent set of graph g.

 * Minimum vertex cover
   * Sage --- 
   * Mathematica --- [MinimumVertexCover](http://reference.wolfram.com/mathematica/Combinatorica/ref/MinimumVertexCover.html)[g] finds a minimum vertex cover of graph g. For bipartite graphs, the function uses the polynomial-time Hungarian algorithm. For everything else, the function uses brute force.

 * Non-line graphs
   * Sage ---   
   * Mathematica --- [NonLineGraphs](http://reference.wolfram.com/mathematica/Combinatorica/ref/NonLineGraphs.html) returns a graph whose connected components are the 9 graphs whose presence as a vertex-induced subgraph in a graph g makes g a nonline graph.

 * Normalize vertices
   * Sage ---
   * Mathematica --- [NormalizeVertices](http://reference.wolfram.com/mathematica/Combinatorica/ref/NormalizeVertices.html)[v] gives a list of vertices with a similar embedding as v but with all coordinates of all points scaled to be between 0 and 1.

 * nth pair
   * Sage ---
   * Mathemaica --- [NthPair](http://reference.wolfram.com/mathematica/Combinatorica/ref/NthPair.html)[n] returns the `n^(th)` unordered pair of distinct positive integers, when sequenced to minimize the size of the larger integer. Pairs that have the same larger integer are sequenced in increasing order of their smaller integer.

 * Path
   * Sage ---
   * Mathematica --- [Path](http://reference.wolfram.com/mathematica/Combinatorica/ref/Path.html)[n] constructs a tree consisting only of a path on n vertices.

 * Permute subgraph
   * Sage ---
   * Mathematica --- [PermuteSubgraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/PermuteSubgraph.html)[g, p] permutes the vertices of a subgraph of g induced by p according to p.

 * Random graph
   * Sage ---
   * Mathematica --- [RandomGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/RandomGraph.html)[n, p] constructs a random labeled graph on n vertices with an edge probability of p. 

 * Random tree
   * Sage ---
   * Mathematica --- [RandomTree](http://reference.wolfram.com/mathematica/Combinatorica/ref/RandomTree.html)[n] constructs a random labeled tree on n vertices.

 * Random vertices
   * Sage ---
   * Mathematica --- [RandomVertices](http://reference.wolfram.com/mathematica/Combinatorica/ref/RandomVertices.html)[g] assigns a random embedding to graph g.

 * Regular graph
   * Sage ---
   * Mathematica --- [RegularGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/RegularGraph.html)[k, n] constructs a semirandom k-regular graph on n vertices, if such a graph exists.

 * Regular q
   * Sage ---
   * Mathematica --- [RegularQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/RegularQ.html)[g] yields True if g is a regular graph.

 * Remove multiple edges
   * Sage ---
   * Mathematica --- [RemoveMultipleEdges](http://reference.wolfram.com/mathematica/Combinatorica/ref/RemoveMultipleEdges.html)[g] returns the graph obtained by deleting multiple edges from g.

 * Remove self-loops
   * Sage ---
   * Mathematica --- [RemoveSelfLoops](http://reference.wolfram.com/mathematica/Combinatorica/ref/RemoveSelfLoops.html)[g] returns the graph obtained by deleting self-loops in g.

 * Reverse edges
   * Sage ---
   * Mathematica --- [ReverseEdges](http://reference.wolfram.com/mathematica/Combinatorica/ref/ReverseEdges.html)[g] flips the directions of all edges in a directed graph.

 * Smallest cyclic group graph
   * Sage ---
   * Mathematica --- [SmallestCyclicGroupGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/SmallestCyclicGroupGraph.html) returns a smallest nontrivial graph whose automorphism group is cyclic.

 * Tree isomorphism q
   * Sage ---
   * Mathematica --- [TreeIsomorphismQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/TreeIsomorphismQ.html)[t1, t2] yields True if the trees t1 and t2 are isomorphic. It yields False otherwise.

 * Tree to certificate
   * Sage ---
   * Mathematica --- [TreeToCertificate](http://reference.wolfram.com/mathematica/Combinatorica/ref/TreeToCertificate.html)[t] returns a binary string that is a certificate for the tree t such that trees have the same certificate if and only if they are isomorphic.

 * Tree q
   * Sage ---
   * Mathematica --- [TreeQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/TreeQ.html)[g] yields True if graph g is a tree.

 * Vertex cover
   * Sage ---
   * Mathematica --- [VertexCover](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexCover.html)[g] returns a vertex cover of the graph g. An option Algorithm that can take on values Greedy, Approximate, or Optimum is allowed. The default setting is Algorithm -> Approximate. Different algorithms are used to compute a vertex cover depending on the setting of the option Algorithm.

 * Vertex cover q
   * Sage ---   
   * Mathematica --- [VertexCoverQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexCoverQ.html)[g, c] yields True if the vertices in list c define a vertex cover of graph g.



### Input and output


 * Read graph
   * Sage ---
   * Mathematica ---  [ReadGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/ReadGraph.html)[f] reads a graph represented as edge lists from file f and returns a graph object.
   
 * Write graph
   * Sage ---
   * Mathematica --- [WriteGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/WriteGraph.html)[g, f] writes graph g to file f using an edge list representation.



### Built-in graphs


 * Butterfly graph
   * Sage ---
   * Mathematica --- [ButterflyGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/ButterflyGraph.html)[n] returns the n-dimensional butterfly graph, a directed graph whose vertices are pairs (w, i), where w is a binary string of length n and i is an integer in the range 0 through n and whose edges go from vertex (w, i) to (w', i+1), if w' is identical to w in all bits with the possible exception of the (i+1)th bit. Here bits are counted left to right. An option [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html), with default setting False, is allowed. When this option is set to True, vertices are labeled with strings (w, i).

 * Cage graph
   * Sage ---
   * Mathematica --- [CageGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/CageGraph.html)[k, r] gives a smallest k-regular graph of girth r for certain small values of k and r. [CageGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/CageGraph.html)[r] gives [CageGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/CageGraph.html)[3, r]. For k = 3, r can be 3, 4, 5, 6, 7, 8, or 10. For k = 4 or 5, r can be 3, 4, 5, or 6.

 * Chvatal graph
   * Sage ---
   * Mathematica --- [ChvatalGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/ChvatalGraph.html) returns a smallest triangle-free, 4-regular, 4-chromatic graph.

 * Circulant graph
   * Sage ---
   * Mathematica --- [CirculantGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/CirculantGraph.html)[n, l] constructs a circulant graph on n vertices, meaning the ith vertex is adjacent to the (i+j)th and (i-j)th vertices, for each j in list l. [CirculantGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/CirculantGraph.html)[n, l], where l is an integer, returns the graph with n vertices in which each i is adjacent to (i+l) and (i-l).

 * Complete graph
   * Sage ---
   * Mathematica --- [CompleteGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/CompleteGraph.html)n] creates a complete graph on n vertices. An option Type that takes on the values Directed or Undirected is allowed. The default setting for this option is Type->Undirected.

 * Complete k-partite graph
   * Sage ---
   * Mathematica --- [CompleteKPartiteGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/CompleteKPartiteGraph.html)[a, b, c, ...] creates a complete k-partite graph of the prescribed shape, provided the k arguments a,b,c,... are positive integers. An option Type that takes on the values Directed or Undirected is allowed. The default setting for this option is Type->Undirected.

 * Coxeter graph
   * Sage ---
   * Matheamtica --- [CoxeterGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/CoxeterGraph.html) gives a non-Hamiltonian graph with a high degree of symmetry such that there is a graph automorphism taking any path of length 3 to any other.

 * Cube connected cycle
   * Sage ---
   * Mathematica --- [CubeConnectedCycle](http://reference.wolfram.com/mathematica/Combinatorica/ref/CubeConnectedCycle.html)[d] returns the graph obtained by replacing each vertex in a d-dimensional hypercube by a cycle of length d. Cube-connected cycles share many properties with hypercubes but have the additional desirable property that for d > 1 every vertex has degree 3.

 * Cubical graph
   * Sage ---
   * Mathematica --- [CubicalGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/CubicalGraph.html) returns the graph corresponding to the cube, a Platonic solid.

 * Cycle
   * Sage ---
   * Mathematica --- [Cycle](http://reference.wolfram.com/mathematica/Combinatorica/ref/Cycle.html)[n] constructs the cycle on n vertices, the 2-regular connected graph. An option Type that takes on values Directed or Undirected is allowed. The default setting is Type->Undirected.

 * De Bruijn graph
   * Sage ---
   * Mathematica --- [DeBruijnGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/DeBruijnGraph.html)[m, n] constructs the n-dimensional De Bruijn graph with m symbols for integers m > 0 and n > 1. [DeBruijnGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/DeBruijnGraph.html)[alph, n] constructs the n-dimensional De Bruijn graph with symbols from alph. Here alph is nonempty and n > 1 is an integer. In the latter form, the function accepts an option [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html), with default value False, which can be set to True, if users want to associate strings on alph to the vertices as labels.

 * Dodecahedral graph
   * Sage ---
   * Mathematica --- [DodecahedralGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/DodecahedralGraph.html) returns the graph corresponding to the dodecahedron, a Platonic solid.

 * Empty graph
   * Sage ---
   * Mathematica --- [EmptyGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/EmptyGraph.html)[n] generates an empty graph on n vertices. An option Type that can take on values Directed or Undirected is provided. The default setting is Type->Undirected.

 * Folkman graph
   * Sage ---
   * Mathematica --- [FolkmanGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/FolkmanGraph.html) returns a smallest graph that is edge-transitive but not vertex-transitive.

 * Franklin graph
   * Sage ---
   * Mathematica --- [FranklinGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/FranklinGraph.html) returns a 12-vertex graph that represents a 6-chromatic map on the Klein bottle. It is the sole counterexample to Heawood's map coloring conjecture.

 * Frucht graph
   * Sage ---
   * Mathematica --- [FruchtGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/FruchtGraph.html) returns the smallest 3-regular graph whose automorphism group consists of only the identity.

 * Generalized Petersen graph
   * Sage ---
   * Mathematica --- [GeneralizedPetersenGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/GeneralizedPetersenGraph.html)[n, k] returns the generalized Petersen graph, for integers n > 1 and k > 0, which is the graph with vertices {u1, u2, ..., un} and {v1, v2, ..., vn} and edges {ui, u(i+1)}, {vi, v(i+k)}, and {ui, vi}. The Petersen graph is identical to the generalized Petersen graph with n = 5 and k = 2.

 * Gray graph
   * Sage ---
   * Mathematica --- [GrayGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/GrayGraph.html) returns a 3-regular, 54-vertex graph that is edge-transitive but not vertex-transitive; the smallest known such example." 

 * Grid graph
   * Sage ---
   * Mathematica --- [GridGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/GridGraph.html)[n, m] constructs an n*m grid graph, the product of paths on n and m vertices. 

 * Groetzsch graph
   * Sage ---
   * Mathematica --- [GroetzschGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/GroetzschGraph.html) returns the smallest triangle-free graph with chromatic number 4. This is identical to [MycielskiGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/MycielskiGraph.html)[4].

 * Harary graph
   * Sage ---
   * Mathematica --- [Harary](http://reference.wolfram.com/mathematica/Combinatorica/ref/Harary.html)[k, n] constructs the minimal k-connected graph on n vertices.

 * Heawood graph
   * Sage ---
   * Mathematica --- [HeawoodGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/HeawoodGraph.html) returns a smallest (6,3)-cage, a 3-regular graph with girth 6.

 * Herschel graph
   * Sage ---
   * Mathematica --- [HerschelGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/HerschelGraph.html) returns a graph object that represents a Herschel graph.

 * Hypercube
   * Sage ---
   * Mathematica --- [Hypercube](http://reference.wolfram.com/mathematica/Combinatorica/ref/Hypercube.html)[n] constructs an n-dimensional hypercube.

 * Icosahedral graph
   * Sage ---
   * Mathematica --- [IcosahedralGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/IcosahedralGraph.html) returns the graph corresponding to the icosahedron, a Platonic solid.

 * Knight's tour graph
   * Sage ---
   * Mathematica --- [KnightsTourGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/KnightsTourGraph.html)[m, n] returns a graph with m*n vertices in which each vertex represents a square in an m x n chessboard and each edge corresponds to a legal move by a knight from one square to another.

 * Levi graph
   * Sage ---
   * Mathematica --- [LeviGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/LeviGraph.html) returns the unique (8, 3)-cage, a 3-regular graph whose girth is 8.

 * McGee graph
   * Sage ---
   * Mathematica --- [McGeeGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/McGeeGraph.html) returns the unique (7, 3)-cage, a 3-regular graph with girth 7.

 * Meredith graph
   * Sage ---
   * Mathematica --- [MeredithGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/MeredithGraph.html) returns a 4-regular, 4-connected graph that is not Hamiltonian, providing a counterexample to a conjecture by C. St. J. A. Nash-Williams.

 * Mycielski graph
   * Sage ---
   * Mathematica --- [MycielskiGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/MycielskiGraph.html)[k] returns a triangle-free graph with chromatic number k, for any positive integer k.

 * Octahedral graph
   * Sage ---
   * Mathematica --- [OctahedralGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/OctahedralGraph.html) returns the graph corresponding to the octahedron, a Platonic solid.

 * Odd graph
   * Sage ---   
   * Mathematica --- [OddGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/OddGraph.html)[n] returns the graph whose vertices are the size-(n-1) subsets of a size-(2n-1) set and whose edges connect pairs of vertices that correspond to disjoint subsets. [OddGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/OddGraph.html)[3] is the Petersen graph.

 * Petersen graph
   * Sage ---
   * Mathematica --- [PetersenGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/PetersenGraph.html) returns the Petersen graph, a graph whose vertices can be viewed as the size-2 subsets of a size-5 set with edges connecting disjoint subsets.

 * Robertson graph
   * Sage ---
   * Mathematica --- [RobertsonGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/RobertsonGraph.html) returns a 19-vertex graph that is the unique (4, 5)-cage graph.

 * Shuffle exchange graph
   * Sage ---
   * Mathematica --- [ShuffleExchangeGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/ShuffleExchangeGraph.html)[n] returns the n-dimensional shuffle-exchange graph whose vertices are length n binary strings with an edge from w to w' if (i) w' differs from w in its last bit or (ii) w' is obtained from w by a cyclic shift left or a cyclic shift right. An option [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html) is provided, with default setting False, which can be set to True, if the user wants to associate the binary strings to the vertices as labels." 

 * Star
   * Sage ---
   * Mathematica --- [Star](http://reference.wolfram.com/mathematica/Combinatorica/ref/Star.html)[n] constructs a star on n vertices, which is a tree with one vertex of degree n-1.

 * Tetrahedral graph
   * Sage ---
   * Mathematica --- [TetrahedralGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/TetrahedralGraph.html) returns the graph corresponding to the tetrahedron, a Platonic solid.

 * Thomassen graph
   * Sage ---
   * Mathematica --- [ThomassenGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/ThomassenGraph.html) returns a hypotraceable graph, a graph G that has no Hamiltonian path but whose subgraph G-v for every vertex v has a Hamiltonian path.

 * Turan
   * Sage ---   
   * Mathematica --- [Turan](http://reference.wolfram.com/mathematica/Combinatorica/ref/Turan.html)[n, p] constructs the Turan graph, the extremal graph on n vertices that does not contain [CompleteGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/CompleteGraph.html)[p].

 * Tutte graph
   * Sage ---
   * Mathematica --- [TutteGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/TutteGraph.html) returns the Tutte graph, the first known example of a 3-connected, 3-regular, planar graph that is non-Hamiltonian.

 * Uniquely 3-colorable graph
   * Sage ---
   * Mathematica --- [Uniquely3ColorableGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/Uniquely3ColorableGraph.html) returns a 12-vertex, triangle-free graph with chromatic number 3 that is uniquely 3-colorable.

 * Unitransitive graph
   * Sage ---
   * Mathematica --- [UnitransitiveGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/UnitransitiveGraph.html) returns a 20-vertex, 3-unitransitive graph discovered by Coxeter, that is not isomorphic to a 4-cage or a 5-cage.

 * Walther graph
   * Sage ---
   * Mathematica --- [WaltherGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/WaltherGraph.html) returns the Walther graph.

 * Wheel
   * Sage ---
   * Mathematica --- [Wheel](http://reference.wolfram.com/mathematica/Combinatorica/ref/Wheel.html)[n] constructs a wheel on n vertices, which is the join of CompleteGraph[1] and Cycle[n-1].



## Graph algorithms



### Shortest paths

 * All pairs shortest path
   * Sage --- [shortest_path_all_vertices](http://www.sagemath.org/doc/reference/sage/graphs/base/c_graph.html#sage.graphs.base.c_graph.CGraphBackend.shortest_path_all_vertices)
   * Mathematica --- [AllPairsShortestPath](http://reference.wolfram.com/mathematica/Combinatorica/ref/AllPairsShortestPath.html)[g] gives a matrix, where the `(i,j)^(th)` entry is the length of a shortest path in g  between vertices i  and j.

 * Bellman-Ford algorithm
    * Sage --- #8714
    * Mathematica --- [http://reference.wolfram.com/mathematica/Combinatorica/ref/BellmanFord.html BellmanFord][g, v] gives a shortest-path spanning tree and associated distances from vertex v of graph g. The shortest-path spanning tree is given by a list in which element i is the predecessor of vertex i in the shortest-path spanning tree. [http://reference.wolfram.com/mathematica/Combinatorica/ref/BellmanFord.html BellmanFord] works correctly even when the edge weights are negative, provided there are no negative cycles.

 * Diameter
   * Sage ---
   * Mathematica --- [Diameter](http://reference.wolfram.com/mathematica/Combinatorica/ref/Diameter.html)[g] gives the diameter of graph g, the maximum length, among all pairs of vertices in g, of a shortest path between each pair.

 * Dijkstra's algorithm
  * Sage --- [bidirectional_dijkstra](http://www.sagemath.org/doc/reference/sage/graphs/base/c_graph.html#sage.graphs.base.c_graph.CGraphBackend.bidirectional_dijkstra)
  * Mathematica --- [Dijkstra](http://reference.wolfram.com/mathematica/Combinatorica/ref/Dijkstra.html)[g, v] gives a shortest-path spanning tree and associated distances from vertex v of graph g. The shortest-path spanning tree is given by a list in which element i is the predecessor of vertex i in the shortest-path spanning tree. Dijkstra does not work correctly when the edge weights are negative; [BellmanFord](http://reference.wolfram.com/mathematica/Combinatorica/ref/BellmanFord.html) should be used in this case.

 * Eccentricity
   * Sage ---
   * Mathematica --- [Eccentricity](http://reference.wolfram.com/mathematica/Combinatorica/ref/Eccentricity.html)[g] gives the eccentricity of each vertex v  of graph g, the maximum length among all shortest paths from v.

 * Girth
   * Sage ---
   * Mathematica --- [Girth](http://reference.wolfram.com/mathematica/Combinatorica/ref/Girth.html)[g] gives the length of a shortest cycle in a simple graph g.

 * Graph center
   * Sage ---
   * Mathematica --- [GraphCenter](http://reference.wolfram.com/mathematica/Combinatorica/ref/GraphCenter.html)[g] gives a list of the vertices of graph g with minimum eccentricity.

 * Graph power
   * Sage ---
   * Mathematica --- [GraphPower](http://reference.wolfram.com/mathematica/Combinatorica/ref/GraphPower.html)[g, k] gives the kth power of graph g. This is the graph whose vertex set is identical to the vertex set of g and that contains an edge between vertices i and j for each path in g between vertices i and j of length at most k.

 * Parents to paths
   * Sage ---
   * Mathematica --- [ParentsToPaths](http://reference.wolfram.com/mathematica/Combinatorica/ref/ParentsToPaths.html)[l, i, j] takes a list of parents l and returns the path from i to j encoded in the parent list. [ParentsToPaths](http://reference.wolfram.com/mathematica/Combinatorica/ref/ParentsToPaths.html)[l, i] returns the paths from i to all vertices.

 * Radius
   * Sage ---
   * Mathematica --- [Radius](http://reference.wolfram.com/mathematica/Combinatorica/ref/Radius.html)[g] gives the radius of graph g, the minimum eccentricity of any vertex of g.

 * Shortest path
   * Sage --- [shortest_path](http://www.sagemath.org/doc/reference/sage/graphs/base/c_graph.html#sage.graphs.base.c_graph.CGraphBackend.shortest_path)
   * Mathematica --- [ShortestPath](http://reference.wolfram.com/mathematica/Combinatorica/ref/ShortestPath.html)[g, start, end] finds a shortest path between vertices start and end in graph g.



### Minimum spanning trees


 * Cofactor
   * Sage ---
   * Mathematica --- [Cofactor](http://reference.wolfram.com/mathematica/Combinatorica/ref/Cofactor.html)[m, {i, j}] calculates the `(i,j)^(th)` cofactor of matrix m.

 * Find set
   * Sage ---
   * Mathematica --- [FindSet](http://reference.wolfram.com/mathematica/Combinatorica/ref/FindSet.html)[n, s] gives the root of the set containing n in union-find data structure s.

 * Initialize union find
   * Sage ---
   * Mathematica --- [InitializeUnionFind](http://reference.wolfram.com/mathematica/Combinatorica/ref/InitializeUnionFind.html)[n] initializes a union-find data structure for n elements.
   
 * Maximum spanning tree
   * Sage ---
   * Mathematica --- [MaximumSpanningTree](http://reference.wolfram.com/mathematica/Combinatorica/ref/MaximumSpanningTree.html)[g] uses Kruskal's algorithm to find a maximum spanning tree of graph g.

 * Minimum spanning tree
   * Sage --- [min_spanning_tree](http://www.sagemath.org/doc/reference/sage/graphs/graph.html#sage.graphs.graph.Graph.min_spanning_tree)
   * Mathematica --- [MinimumSpanningTree](http://reference.wolfram.com/mathematica/Combinatorica/ref/MinimumSpanningTree.html)[g] uses Kruskal's algorithm to find a minimum spanning tree of graph g.

 * Number of spanning trees
   * Sage ---
   * Mathematica --- [NumberOfSpanningTrees](http://reference.wolfram.com/mathematica/Combinatorica/ref/NumberOfSpanningTrees.html)[g] gives the number of labeled spanning trees of graph g.

 * Shortest path spanning tree
   * Sage ---
   * Mathematica --- [ShortestPathSpanningTree](http://reference.wolfram.com/mathematica/Combinatorica/ref/ShortestPathSpanningTree.html)[g, v] constructs a shortest-path spanning tree rooted at v, so that a shortest path in graph g from v to any other vertex is a path in the tree. An option Algorithm that takes on the values Automatic, Dijkstra, or [BellmanFord](http://reference.wolfram.com/mathematica/Combinatorica/ref/BellmanFord.html) is provided. This allows a choice between Dijkstra's algorithm and the Bellman-Ford algorithm. The default is Algorithm -> Automatic. In this case, depending on whether edges have negative weights and depending on the density of the graph, the algorithm chooses between Bellman-Ford and Dijkstra.

 * Union set
   * Sage ---
   * Mathematica --- [UnionSet](http://reference.wolfram.com/mathematica/Combinatorica/ref/UnionSet.html)[a, b, s] merges the sets containing a and b in union-find data structure s.



### Network flow


 * Networkflow
   * Sage --- [flow](http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.flow)
   * Mathematica --- [NetworkFlow](http://reference.wolfram.com/mathematica/Combinatorica/ref/NetworkFlow.html)[g, source, sink] returns the value of a maximum flow through graph g from source to sink. [NetworkFlow](http://reference.wolfram.com/mathematica/Combinatorica/ref/NetworkFlow.html)[g, source, sink, Edge] returns the edges in g that have positive flow along with their flows in a maximum flow from source to sink. [NetworkFlow](http://reference.wolfram.com/mathematica/Combinatorica/ref/NetworkFlow.html)[g, source, sink, Cut] returns a minimum cut between source and sink. [NetworkFlow](http://reference.wolfram.com/mathematica/Combinatorica/ref/NetworkFlow.html)[g, source, sink, All] returns the adjacency list of g along with flows on each edge in a maximum flow from source to sink. g can be a directed or an undirected graph.

 * Residual flow graph
   * Sage ---
   * Mathematica --- [ResidualFlowGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/ResidualFlowGraph.html)[g, flow] returns the directed residual flow graph for graph g with respect to flow.



### Matching


 * Alternating paths
   * Sage ---
   * Mathematica --- [AlternatingPaths](http://reference.wolfram.com/mathematica/Combinatorica/ref/AlternatingPaths.html)[g, start, ME] returns the alternating paths in graph g with respect to the matching ME, starting at the vertices in the list start. The paths are returned in the form of a forest containing trees rooted at vertices in start.

 * Bipartite matching
   * Sage ---
   * Mathematica --- [BipartiteMatching](http://reference.wolfram.com/mathematica/Combinatorica/ref/BipartiteMatching.html)[g] gives the list of edges associated with a maximum matching in bipartite graph g. If the graph is edge weighted, then the function returns a matching with maximum total weight.

 * Bipartite matching and cover
   * Sage ---
   * Mathematica --- [BipartiteMatchingAndCover](http://reference.wolfram.com/mathematica/Combinatorica/ref/BipartiteMatchingAndCover.html)[g] takes a bipartite graph g and returns a matching with maximum weight along with the dual vertex cover. If the graph is not weighted, it is assumed that all edge weights are 1.

 * Maximal matching
   * Sage --- [matching](http://www.sagemath.org/doc/reference/sage/graphs/generic_graph.html#sage.graphs.generic_graph.GenericGraph.matching)
   * Mathematica --- [MaximalMatching](http://reference.wolfram.com/mathematica/Combinatorica/ref/MaximalMatching.html)[g] gives the list of edges associated with a maximal matching of graph g.

 * No perfect matching graph
   * Sage ---   
   * Mathematica --- [NoPerfectMatchingGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/NoPerfectMatchingGraph.html) returns a connected graph with 16 vertices that contains no perfect matching.

 * Stable marriange
   * Sage ---
   * Mathematica --- [StableMarriage](http://reference.wolfram.com/mathematica/Combinatorica/ref/StableMarriage.html)[mpref, fpref] finds the male optimal stable marriage defined by lists of permutations describing male and female preferences.



### Graph traversals


 * Breadth-first search
   * Sage --- [breadth_first_search](http://www.sagemath.org/doc/reference/sage/graphs/base/c_graph.html#sage.graphs.base.c_graph.CGraphBackend.breadth_first_search)
   * Mathematica --- [BreadthFirstTraversal](http://reference.wolfram.com/mathematica/Combinatorica/ref/BreadthFirstTraversal.html)[g, v] performs a breadth-first traversal of graph g starting from vertex v, and gives the breadth-first numbers of the vertices. 

 * Depth-first search
   * Sage --- [depth_first_search](http://www.sagemath.org/doc/reference/sage/graphs/base/c_graph.html#sage.graphs.base.c_graph.CGraphBackend.depth_first_search)
   * Mathematica --- [DepthFirstTraversal](http://reference.wolfram.com/mathematica/Combinatorica/ref/DepthFirstTraversal.html)[g, v] performs a depth-first traversal of graph g starting from vertex v, and gives a list of vertices in the order in which they were encountered. 



### Partial orders


 * Antisymmetric q
   * Sage ---
   * Mathematica --- [AntiSymmetricQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/AntiSymmetricQ.html)[g] yields True if the adjacency matrix of g represents an anti-symmetric binary relation.

 * Boolean algebra
   * Sage ---
   * Mathematica --- [BooleanAlgebra](http://reference.wolfram.com/mathematica/Combinatorica/ref/BooleanAlgebra.html)[n] gives a Hasse diagram for the Boolean algebra on n elements. The function takes two options: Type and [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html), with default values Undirected and False, respectively. When Type is set to Directed, the function produces the underlying directed acyclic graph. When [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html) is set to True, labels are produced for the vertices.

 * Dominating integer partition q
   * Sage ---
   * Mathematica --- [DominatingIntegerPartitionQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/DominatingIntegerPartitionQ.html)[a, b] yields True if integer partition a dominates integer partition b, that is, the sum of a size-t prefix of a is no smaller than the sum of a size-t prefix of b for every t.

 * Domination lattice
   * Sage ---
   * Mathematica --- [DominationLattice](http://reference.wolfram.com/mathematica/Combinatorica/ref/DominationLattice.html)[n] returns a Hasse diagram of the partially ordered set on integer partitions of n in which p < q if q dominates p. The function takes two options: Type and [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html), with default values Undirected and False, respectively. When Type is set to Directed, the function produces the underlying directed acyclic graph. When [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html) is set to True, labels are produced for the vertices.

 * Equivalence classes
   * Sage ---
   * Mathematica --- [EquivalenceClasses](http://reference.wolfram.com/mathematica/Combinatorica/ref/EquivalenceClasses.html)[r] identifies the equivalence classes among the elements of matrix r.

 * Equivalence relation q
   * Sage ---
   * Mathematica --- [EquivalenceRelationQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/EquivalenceRelationQ.html)[r] yields True if the matrix r defines an equivalence relation. [EquivalenceRelationQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/EquivalenceRelationQ.html)[g] tests whether the adjacency matrix of graph g defines an equivalence relation.

 * Hasse diagram
   * Sage ---
   * Mathematica --- [HasseDiagram](http://reference.wolfram.com/mathematica/Combinatorica/ref/HasseDiagram.html)[g] constructs a Hasse diagram of the relation defined by directed acyclic graph g.

 * Inversion poset
   * Sage ---
   * Mathematica --- [InversionPoset](http://reference.wolfram.com/mathematica/Combinatorica/ref/InversionPoset.html)[n] returns a Hasse diagram of the partially ordered set on size-n permutations in which p < q if q can be obtained from p by an adjacent transposition that places the larger element before the smaller. The function takes two options: Type and [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html), with default values Undirected and False, respectively. When Type is set to Directed, the function produces the underlying directed acyclic graph. When [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html) is set to True, labels are produced for the vertices.

 * Isomorphic q
   * Sage ---
   * Mathematica --- [IsomorphicQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/IsomorphicQ.html)[g, h] yields True if graphs g and h are isomorphic. 

 * Maximum antichain
   * Sage ---
   * Mathematica --- [MaximumAntichain](http://reference.wolfram.com/mathematica/Combinatorica/ref/MaximumAntichain.html)[g] gives a largest set of unrelated vertices in partial order g.

 * Minimum chain partition
   * Sage ---
   * Mathematica --- [MinimumChainPartition](http://reference.wolfram.com/mathematica/Combinatorica/ref/MinimumChainPartition.html)[g] partitions partial order g into a minimum number of chains.

 * Partial order q
   * Sage ---
   * Mathematica --- [PartialOrderQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/PartialOrderQ.html)[g] yields True if the binary relation defined by edges of the graph g is a partial order, meaning it is transitive, reflexive, and antisymmetric. 

 * Partition lattice
   * Sage ---
   * Mathematica --- [PartitionLattice](http://reference.wolfram.com/mathematica/Combinatorica/ref/PartitionLattice.html)[n] returns a Hasse diagram of the partially ordered set on set partitions of 1 through n in which p < q if q is finer than p, that is, each block in q is contained in some block in p. The function takes two options: Type and [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html), with default values Undirected and False, respectively. When Type is set to Directed, the function produces the underlying directed acyclic graph. When [VertexLabel](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexLabel.html) is set to True, labels are produced for the vertices.

 * Symmetric q
   * Sage ---
   * Mathematica --- [SymmetricQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/SymmetricQ.html)[r] tests if a given square matrix r represents a symmetric relation. [SymmetricQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/SymmetricQ.html)[g] tests if the edges of a given graph represent a symmetric relation.

 * Topological sort
   * Sage ---
   * Mathematica --- [TopologicalSort](http://reference.wolfram.com/mathematica/Combinatorica/ref/TopologicalSort.html)[g] gives a permutation of the vertices of the directed acyclic graph g such that an edge (i,j) implies that vertex i appears before vertex j.

 * Transitive closure
   * Sage ---
   * Mathematica --- [TransitiveClosure](http://reference.wolfram.com/mathematica/Combinatorica/ref/TransitiveClosure.html)[g] finds the transitive closure of graph g, the supergraph of g that contains edge {x, y} if and only if there is a path from x to y.

 * Transitive reduction
   * Sage ---
   * Mathematica [TransitiveReduction](http://reference.wolfram.com/mathematica/Combinatorica/ref/TransitiveReduction.html)[g] finds a smallest graph that has the same transitive closure as g.



### Graph isomorphism


 * Degrees of 2-neighborhood
   * Sage ---
   * Mathematica --- [DegreesOf2Neighborhood](http://reference.wolfram.com/mathematica/Combinatorica/ref/DegreesOf2Neighborhood.html)[g, v] returns the sorted list of degrees of vertices of graph g within a distance of 2 from v.

 * Distances
   * Sage ---
   * Mathematica --- [Distances](http://reference.wolfram.com/mathematica/Combinatorica/ref/Distances.html)[g, v] returns the distances in nondecreasing order from vertex v to all vertices in g, treating g as an unweighted graph.

 * Equivalences
   * Sage ---
   * Mathematica --- Equivalences[g, h] lists the vertex equivalence classes between graphs g and h defined by their vertex degrees. Equivalences[g] lists the vertex equivalences for graph g defined by the vertex degrees. Equivalences[g, h, f1, f2, ...] and Equivalences[g, f1, f2, ...] can also be used, where f1, f2, ... are functions that compute other vertex invariants. It is expected that for each function fi, the call fi[g, v] returns the corresponding invariant at vertex v in graph g. The functions f1, f2, ... are evaluated in order, and the evaluation stops either when all functions have been evaluated or when an empty equivalence class is found. Three vertex invariants, [DegreesOf2Neighborhood](http://reference.wolfram.com/mathematica/Combinatorica/ref/DegreesOf2Neighborhood.html), [NumberOf2Paths](http://reference.wolfram.com/mathematica/Combinatorica/ref/NumberOf2Paths.html), and Distances are Combinatorica functions and can be used to refine the equivalences.

 * Identical q
   * Sage ---
   * Mathematica --- [IdenticalQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/IdenticalQ.html)[g, h] yields True if graphs g and h have identical edge lists, even though the associated graphics information need not be the same.

 * Isomorphism
   * Sage ---
   * Mathematica --- Isomorphism[g, h] gives an isomorphism between graphs g and h if one exists. Isomorphism[g, h, All] gives all isomorphisms between graphs g and h. Isomorphism[g] gives the automorphism group of g. This function takes an option Invariants -> {f1, f2, ...}, where f1, f2, ... are functions that are used to compute vertex invariants. These functions are used in the order in which they are specified. The default value of Invariants is {[DegreesOf2Neighborhood](http://reference.wolfram.com/mathematica/Combinatorica/ref/DegreesOf2Neighborhood.html), [NumberOf2Paths](http://reference.wolfram.com/mathematica/Combinatorica/ref/NumberOf2Paths.html), Distances}.

 * Isomorphism q
   * Sage ---
   * Mathematica --- [IsomorphismQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/IsomorphismQ.html)[g, h, p] tests if permutation p defines an isomorphism between graphs g and h.

 * Neighborhood
   * Sage ---
   * Mathematica --- [Neighborhood](http://reference.wolfram.com/mathematica/Combinatorica/ref/Neighborhood.html)[g, v, k] returns the subset of vertices in g that are at a distance of k or less from vertex v. 

 * Number of 2-paths
   * Sage ---
   * Mathematica --- [NumberOf2Paths](http://reference.wolfram.com/mathematica/Combinatorica/ref/NumberOf2Paths.html)[g, v] returns a sorted list that contains the number of paths of length 2 to different vertices of g from v.

 * Number of k-paths
   * Sage ---
   * Mathematica --- [NumberOfKPaths](http://reference.wolfram.com/mathematica/Combinatorica/ref/NumberOfKPaths.html)[g, v, k] returns a sorted list that contains the number of paths of length k to different vertices of g from v. [NumberOfKPaths](http://reference.wolfram.com/mathematica/Combinatorica/ref/NumberOfKPaths.html)[al, v, k] behaves identically, except that it takes an adjacency list al as input.

 * Self-complementary q
   * Sage ---
   * Mathematica --- [SelfComplementaryQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/SelfComplementaryQ.html)[g] yields True if graph g is self-complementary, meaning it is isomorphic to its complement.



## Graph properties



### Degrees


 * Degrees
   * Sage ---
   * Mathematica --- [Degrees](http://reference.wolfram.com/mathematica/Combinatorica/ref/Degrees.html)[g] returns the degrees of vertex 1,2,3,... in that order.

 * Degree sequence
   * Sage ---
   * Mathematica --- [DegreeSequence](http://reference.wolfram.com/mathematica/Combinatorica/ref/DegreeSequence.html)[g] gives the sorted degree sequence of graph g.

 * Graphic q
   * Sage ---
   * Mathematica --- [GraphicQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/GraphicQ.html)[s] yields True if the list of integers s is a graphic sequence, and thus represents a degree sequence of some graph.

 * Indegree
   * Sage ---
   * Mathematica --- [InDegree](http://reference.wolfram.com/mathematica/Combinatorica/ref/InDegree.html)[g, n] returns the in-degree of vertex n in directed graph g. 

 * Outdegree
   * Sage ---
   * Mathematica --- [OutDegree](http://reference.wolfram.com/mathematica/Combinatorica/ref/OutDegree.html)[g, n] returns the out-degree of vertex n in directed graph g. 

 * Realize degree sequence
   * Sage ---
   * Mathematica --- [RealizeDegreeSequence](http://reference.wolfram.com/mathematica/Combinatorica/ref/RealizeDegreeSequence.html)[s] constructs a semirandom graph with degree sequence s.

 * Spectrum
   * Sage ---
   * Mathematica --- [Spectrum](http://reference.wolfram.com/mathematica/Combinatorica/ref/Spectrum.html)[g] gives the eigenvalues of graph g.



### Miscellaneous


 * Graph polynomial
   * Sage ---
   * Mathematica --- [GraphPolynomial](http://reference.wolfram.com/mathematica/Combinatorica/ref/GraphPolynomial.html)[n, x] returns a polynomial in x in which the coefficient of x^m is the number of nonisomorphic graphs with n vertices and m edges. [GraphPolynomial](http://reference.wolfram.com/mathematica/Combinatorica/ref/GraphPolynomial.html)[n, x, Directed] returns a polynomial in x in which the coefficient of x^m is the number of nonisomorphic directed graphs with n vertices and m edges.

 * List graphs
   * Sage ---
   * Mathematica --- [ListGraphs](http://reference.wolfram.com/mathematica/Combinatorica/ref/ListGraphs.html)[n, m] returns all nonisomorphic undirected graphs with n vertices and m edges. [ListGraphs](http://reference.wolfram.com/mathematica/Combinatorica/ref/ListGraphs.html)[n, m, Directed] returns all nonisomorphic directed graphs with n vertices and m edges. [ListGraphs](http://reference.wolfram.com/mathematica/Combinatorica/ref/ListGraphs.html)[n] returns all nonisomorphic undirected graphs with n vertices. [ListGraphs](http://reference.wolfram.com/mathematica/Combinatorica/ref/ListGraphs.html)[n, Directed] returns all nonisomorphic directed graphs with n vertices.

 * List necklaces
   * Sage ---
   * Mathematica --- [ListNecklaces](http://reference.wolfram.com/mathematica/Combinatorica/ref/ListNecklaces.html)[n, c, Cyclic] returns all distinct necklaces whose beads are colored by colors from c. Here c is a list of n, not necessarily distinct colors, and two colored necklaces are considered equivalent if one can be obtained by rotating the other. 

 * Necklace polynomial
   * Sage ---
   * Mathematica --- [NecklacePolynomial](http://reference.wolfram.com/mathematica/Combinatorica/ref/NecklacePolynomial.html)[n, c, Cyclic] returns a polynomial in the colors in c whose coefficients represent numbers of ways of coloring an n-bead necklace with colors chosen from c, assuming that two colorings are equivalent if one can be obtained from the other by a rotation. 

 * Number of directed graphs
   * Sage ---
   * Mathematica --- [NumberOfDirectedGraphs](http://reference.wolfram.com/mathematica/Combinatorica/ref/NumberOfDirectedGraphs.html)[n] returns the number of nonisomorphic directed graphs with n vertices. [NumberOfDirectedGraphs](http://reference.wolfram.com/mathematica/Combinatorica/ref/NumberOfDirectedGraphs.html)[n, m] returns the number of nonisomorphic directed graphs with n vertices and m edges.

 * Number of graphs
   * Sage ---
   * Mathematica --- [NumberOfGraphs](http://reference.wolfram.com/mathematica/Combinatorica/ref/NumberOfGraphs.html)[n] returns the number of nonisomorphic undirected graphs with n vertices. [NumberOfGraphs](http://reference.wolfram.com/mathematica/Combinatorica/ref/NumberOfGraphs.html)[n, m] returns the number of nonisomorphic undirected graphs with n vertices and m edges.

 * Number of necklaces
   * Sage ---
   * Mathematica --- [NumberOfNecklaces](http://reference.wolfram.com/mathematica/Combinatorica/ref/NumberOfNecklaces.html) [n, nc, Cyclic] returns the number of distinct ways in which an n-bead necklace can be colored with nc colors, assuming that two colorings are equivalent if one can be obtained from the other by a rotation. 



### Cycles and connectivity


 * Acyclic q
   * Sage ---
   * Mathematica --- [AcyclicQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/AcyclicQ.html)[g] yields True if graph g is acyclic.

 * Articulation vertices
   * Sage ---
   * Mathematica --- [ArticulationVertices](http://reference.wolfram.com/mathematica/Combinatorica/ref/ArticulationVertices.html)[g] gives a list of all articulation vertices in graph g. These are vertices whose removal will disconnect the graph.

 * Biconnected components
   * Sage ---
   * Mathematica --- [BiconnectedComponents](http://reference.wolfram.com/mathematica/Combinatorica/ref/BiconnectedComponents.html)[g] gives a list of the biconnected components of graph g. If g is directed, the underlying undirected graph is used.

 * Biconnected q
   * Sage ---
   * Mathematica --- [BiconnectedQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/BiconnectedQ.html)[g] yields True if graph g is biconnected. If g is directed, the underlying undirected graph is used.

 * Bridges
   * Sage ---
   * Mathematica --- Bridges[g] gives a list of the bridges of graph g, where each bridge is an edge whose removal disconnects the graph.

 * Connected components
   * Sage ---
   * Mathematica --- [ConnectedComponents](http://reference.wolfram.com/mathematica/Combinatorica/ref/ConnectedComponents.html)[g] gives the vertices of graph g partitioned into connected components.

 * Connected q
   * Sage ---
   * Mathematica --- [ConnectedQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/ConnectedQ.html)[g] yields True if undirected graph g is connected. If g is directed, the function returns True if the underlying undirected graph is connected. 

 * De Bruijn sequence
   * Sage --- 
   * Mathematica --- [DeBruijnSequence](http://reference.wolfram.com/mathematica/Combinatorica/ref/DeBruijnSequence.html)[a, n] returns a De Bruijn sequence on the alphabet a, a shortest sequence in which every string of length n on alphabet a occurs as a contiguous subsequence.

 * Edge connectivity
   * Sage ---
   * Mathematica --- [EdgeConnectivity](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeConnectivity.html)[g] gives the minimum number of edges whose deletion from graph g disconnects it. [EdgeConnectivity](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeConnectivity.html)[g, Cut] gives a set of edges of minimum size whose deletion disconnects the graph.

 * Eulerian cycle
   * Sage ---
   * Mathematica --- [EulerianCycle](http://reference.wolfram.com/mathematica/Combinatorica/ref/EulerianCycle.html)[g] finds an Eulerian cycle of g if one exists.

 * Eulerian q
   * Sage ---
   * Mathematica --- [EulerianQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/EulerianQ.html)[g] yields True if graph g is Eulerian, meaning there exists a tour that includes each edge exactly once.

 * Extract cycles
   * Sage ---
   * Mathematica --- [ExtractCycles](http://reference.wolfram.com/mathematica/Combinatorica/ref/ExtractCycles.html)[g] gives a maximal list of edge-disjoint cycles in graph g.

 * Find cycle
   * Sage ---
   * Mathematica --- [FindCycle](http://reference.wolfram.com/mathematica/Combinatorica/ref/FindCycle.html)[g] finds a list of vertices that define a cycle in graph g.

 * Hamiltonian cycle
   * Sage ---
   * Mathematica --- [HamiltonianCycle](http://reference.wolfram.com/mathematica/Combinatorica/ref/HamiltonianCycle.html)[g] finds a Hamiltonian cycle in graph g if one exists. [HamiltonianCycle](http://reference.wolfram.com/mathematica/Combinatorica/ref/HamiltonianCycle.html)[g, All] gives all Hamiltonian cycles of graph g.

 * Hamiltonian q
   * Sage ---
   * Mathematica --- [HamiltonianQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/HamiltonianQ.html)[g] yields True if there exists a Hamiltonian cycle in graph g, or in other words, if there exists a cycle that visits each vertex exactly once.

 * Orient graph
   * Sage ---
   * Mathematica --- [OrientGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/OrientGraph.html)[g] assigns a direction to each edge of a bridgeless, undirected graph g, so that the graph is strongly connected.

 * Strongly connected components
   * Sage ---
   * Mathematica --- [StronglyConnectedComponents](http://reference.wolfram.com/mathematica/Combinatorica/ref/StronglyConnectedComponents.html)[g] gives the strongly connected components of directed graph g as lists of vertices.

 * Traveling salesman
   * Sage ---
   * Mathematica --- [TravelingSalesman](http://reference.wolfram.com/mathematica/Combinatorica/ref/TravelingSalesman.html)[g] finds an optimal traveling salesman tour in a Hamiltonian graph g.

 * Traveling salesman bounds
   * Sage ---
   * Mathematica --- [TravelingSalesmanBounds](http://reference.wolfram.com/mathematica/Combinatorica/ref/TravelingSalesmanBounds.html)[g] gives upper and lower bounds on a minimum cost traveling salesman tour of graph g.

 * Vertex connectivity
   * Sage ---
   * Mathematica --- [VertexConnectivity](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexConnectivity.html)[g] gives the minimum number of vertices whose deletion from graph g disconnects it. [VertexConnectivity](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexConnectivity.html)[g, Cut] gives a set of vertices of minimum size, whose removal disconnects the graph.

 * Vertex connectivity graph
   * Sage ---
   * Mathematica --- [VertexConnectivityGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexConnectivityGraph.html)[g] returns a directed graph that contains an edge corresponding to each vertex in g and in which edge disjoint paths correspond to vertex disjoint paths in g.

 * Weakly connected components
   * Sage ---
   * Mathematica --- [WeaklyConnectedComponents](http://reference.wolfram.com/mathematica/Combinatorica/ref/WeaklyConnectedComponents.html)[g] gives the weakly connected components of directed graph g as lists of vertices.



### Graph coloring


 * Backtrack
   * Sage ---
   * Mathematica --- [Backtrack](http://reference.wolfram.com/mathematica/Combinatorica/ref/Backtrack.html)[s, partialQ, solutionQ] performs a backtrack search of the state space s, expanding a partial solution so long as partialQ is True and returning the first complete solution, as identified by solutionQ.

 * Bipartite q
   * Sage ---
   * Mathematica --- [BipartiteQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/BipartiteQ.html)[g] yields True if graph g is bipartite.

 * Brelaz coloring
   * Sage ---
   * Mathematica --- [BrelazColoring](http://reference.wolfram.com/mathematica/Combinatorica/ref/BrelazColoring.html)[g] returns a vertex coloring in which vertices are greedily colored with the smallest available color in decreasing order of vertex degree.

 * Chromatic number
   * Sage --- [chromatic_number](http://www.sagemath.org/doc/reference/sage/graphs/graph_coloring.html#sage.graphs.graph_coloring.chromatic_number)
   * Mathematica --- [ChromaticNumber](http://reference.wolfram.com/mathematica/Combinatorica/ref/ChromaticNumber.html)[g] gives the chromatic number of the graph, which is the fewest number of colors necessary to color the graph.

 * Chromatic polynomial
   * Sage ---
   * Mathematica --- [ChromaticPolynomial](http://reference.wolfram.com/mathematica/Combinatorica/ref/ChromaticPolynomial.html)[g, z] gives the chromatic polynomial P(z) of graph g, which counts the number of ways to color g with, at most, z colors.

 * Edge chromatic number
   * Sage --- [edge_coloring](http://www.sagemath.org/doc/reference/sage/graphs/graph_coloring.html#sage.graphs.graph_coloring.edge_coloring)
   * Mathematica --- [EdgeChromaticNumber](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeChromaticNumber.html)[g] gives the fewest number of colors necessary to color each edge of graph g, so that no two edges incident on the same vertex have the same color.

 * Edge coloring
   * Sage --- [edge_coloring](http://www.sagemath.org/doc/reference/sage/graphs/graph_coloring.html#sage.graphs.graph_coloring.edge_coloring)
   * Mathematica --- [EdgeColoring](http://reference.wolfram.com/mathematica/Combinatorica/ref/EdgeColoring.html)[g] uses Brelaz's heuristic to find a good, but not necessarily minimal, edge coloring of graph g.

 * Minimum vertex coloring
   * Sage --- [vertex_coloring](http://www.sagemath.org/doc/reference/sage/graphs/graph_coloring.html#sage.graphs.graph_coloring.vertex_coloring)
   * Mathematica --- [MinimumVertexColoring](http://reference.wolfram.com/mathematica/Combinatorica/ref/MinimumVertexColoring.html)[g] returns a minimum vertex coloring of g. [MinimumVertexColoring](http://reference.wolfram.com/mathematica/Combinatorica/ref/MinimumVertexColoring.html)[g, k] returns a k-coloring of g, if one exists.

 * Perfect q
   * Sage ---
   * Mathematica --- [PerfectQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/PerfectQ.html)[g] yields True if g is a perfect graph, meaning that for every induced subgraph of g the size of a largest clique equals the chromatic number.

 * Two coloring
   * Sage ---
   * Mathematica --- [TwoColoring](http://reference.wolfram.com/mathematica/Combinatorica/ref/TwoColoring.html)[g] finds a two-coloring of graph g if g is bipartite. It returns a list of the labels 1 and 2 corresponding to the vertices. This labeling is a valid coloring if and only the graph is bipartite.

 * Vertex coloring
   * Sage ---
   * Mathematica --- [VertexColoring](http://reference.wolfram.com/mathematica/Combinatorica/ref/VertexColoring.html)[g] uses Brelaz's heuristic to find a good, but not necessarily minimal, vertex coloring of graph g. An option Algorithm that can take on the values Brelaz or Optimum is allowed. The setting Algorithm -> Brelaz is the default, while the setting Algorithm -> Optimum forces the algorithm to do an exhaustive search to find an optimum vertex coloring.



### Graph predicates


 * Clique q
   * Sage ---
   * Mathematica --- [CliqueQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/CliqueQ.html)[g, c] yields True if the list of vertices c defines a clique in graph g.

 * Complete q
   * Sage ---
   * Mathematica --- [CompleteQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/CompleteQ.html)[g] yields True if graph g is complete. This means that between any pair of vertices there is an undirected edge or two directed edges going in opposite directions.

 * Empty q
   * Sage ---
   * Mathematica --- [EmptyQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/EmptyQ.html)[g] yields True if graph g contains no edges.

 * Multiple edges q
   * Sage ---
   * Mathematica --- [MultipleEdgesQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/MultipleEdgesQ.html)[g] yields True if g has multiple edges between pairs of vertices. It yields False otherwise.

 * Planar q
   * Sage ---
   * Mathematica --- [PlanarQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/PlanarQ.html)[g] yields True if graph g is planar, meaning it can be drawn in the plane so no two edges cross.

 * Pseudograph q
   * Sage ---
   * Mathematica --- [PseudographQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/PseudographQ.html)[g] yields True if graph g is a pseudograph, meaning it contains self-loops.

 * Self-loops q
   * Sage ---
   * Mathematica --- [SelfLoopsQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/SelfLoopsQ.html)[g] yields True if graph g has self-loops.

 * Simple q
   * Sage ---
   * Mathematica --- [SimpleQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/SimpleQ.html)[g] yields True if g is a simple graph, meaning it has no multiple edges and contains no self-loops.

 * Triangle inequality q
   * Sage ---
   * Mathematica --- [TriangleInequalityQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/TriangleInequalityQ.html)[g] yields True if the weights assigned to the edges of graph g satisfy the triangle inequality.

 * Undirected q
   * Sage ---
   * Mathematica --- [UndirectedQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/UndirectedQ.html)[g] yields True if graph g is undirected.

 * Unweighted q
   * Sage ---
   * Mathematica --- [UnweightedQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/UnweightedQ.html)[g] yields True if all edge weights are 1 and False otherwise.




## Others


 * [CostOfPath](http://reference.wolfram.com/mathematica/Combinatorica/ref/CostOfPath.html)[g, p] sums up the weights of the edges in graph g defined by the path p.

 * [DilateVertices](http://reference.wolfram.com/mathematica/Combinatorica/ref/DilateVertices.html)[v, d] multiplies each coordinate of each vertex position in list v by d, thus dilating the embedding. [DilateVertices](http://reference.wolfram.com/mathematica/Combinatorica/ref/DilateVertices.html)[g, d] dilates the embedding of graph g by the factor d.

 * [FiniteGraphs](http://reference.wolfram.com/mathematica/Combinatorica/ref/FiniteGraphs.html) produces a convenient list of all the interesting, finite, parameterless graphs built into Combinatorica.

 * [GetEdgeWeights](http://reference.wolfram.com/mathematica/Combinatorica/ref/GetEdgeWeights.html)[g] returns the list of weights of the edges of g. [GetEdgeWeights](http://reference.wolfram.com/mathematica/Combinatorica/ref/GetEdgeWeights.html)[g, es] returns the list of weights in graph g of the edges in es.

 * [GetVertexLabels](http://reference.wolfram.com/mathematica/Combinatorica/ref/GetVertexLabels.html)[g] returns the list of labels of vertices of g. [GetVertexLabels](http://reference.wolfram.com/mathematica/Combinatorica/ref/GetVertexLabels.html)[g, vs] returns the list of labels in graph g of the vertices specified in list vs.

 * [GetVertexWeights](http://reference.wolfram.com/mathematica/Combinatorica/ref/GetVertexWeights.html)[g] returns the list of weights of vertices of g. [GetVertexWeights](http://reference.wolfram.com/mathematica/Combinatorica/ref/GetVertexWeights.html)[g, vs] returns the list of weights in graph g of the vertices in vs.

 * [HamiltonianPath](http://reference.wolfram.com/mathematica/Combinatorica/ref/HamiltonianPath.html)[g] finds a Hamiltonian path in graph g if one exists. [HamiltonianPath](http://reference.wolfram.com/mathematica/Combinatorica/ref/HamiltonianPath.html)[g, All] gives all Hamiltonian paths of graph g.

 * [MinimumChangePermutations](http://reference.wolfram.com/mathematica/Combinatorica/ref/MinimumChangePermutations.html)[l] constructs all permutations of list l such that adjacent permutations differ by only one transposition.

 * [NetworkFlowEdges](http://reference.wolfram.com/mathematica/Combinatorica/ref/NetworkFlowEdges.html)[g, source, sink] returns the edges of the graph with positive flow, showing the distribution of a maximum flow from source to sink in graph g. This is obsolete, and [NetworkFlow](http://reference.wolfram.com/mathematica/Combinatorica/ref/NetworkFlow.html)[g, source, sink, Edge] should be used instead.

 * [PartialOrderQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/PartialOrderQ.html)[g] yields True if the binary relation defined by edges of the graph g is a partial order, meaning it is transitive, reflexive, and antisymmetric. [PartialOrderQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/PartialOrderQ.html)[r] yields True if the binary relation defined by the square matrix r is a partial order.

 * [PermutationGraph](http://reference.wolfram.com/mathematica/Combinatorica/ref/PermutationGraph.html)[p] gives the permutation graph for the permutation p.

 * [ReflexiveQ](http://reference.wolfram.com/mathematica/Combinatorica/ref/ReflexiveQ.html)[g] yields True if the adjacency matrix of g represents a reflexive binary relation.

 * [SetEdgeWeights](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetEdgeWeights.html)[g] assigns random real weights in the range [0, 1] to edges in g. [SetEdgeWeights](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetEdgeWeights.html) accepts options [WeightingFunction](http://reference.wolfram.com/mathematica/Combinatorica/ref/WeightingFunction.html) and [WeightRange](http://reference.wolfram.com/mathematica/Combinatorica/ref/WeightRange.html). [WeightingFunction](http://reference.wolfram.com/mathematica/Combinatorica/ref/WeightingFunction.html) can take values Random, [RandomInteger](http://reference.wolfram.com/mathematica/Combinatorica/ref/RandomInteger.html), Euclidean, or LNorm[n] for nonnegative n, or any pure function that takes two arguments, each argument having the form {Integer, {Number, Number}}. [WeightRange](http://reference.wolfram.com/mathematica/Combinatorica/ref/WeightRange.html) can be an integer range or a real range. The default value for [WeightingFunction](http://reference.wolfram.com/mathematica/Combinatorica/ref/WeightingFunction.html) is Random and the default value for [WeightRange](http://reference.wolfram.com/mathematica/Combinatorica/ref/WeightRange.html) is [0, 1]. [SetEdgeWeights](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetEdgeWeights.html)[g, e] assigns edge weights to the edges in the edge list e. [SetEdgeWeights](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetEdgeWeights.html)[g, w] assigns the weights in the weight list w to the edges of g. [SetEdgeWeights](http://reference.wolfram.com/mathematica/Combinatorica/ref/SetEdgeWeights.html)[g, e, w] assigns the weights in the weight list w to the edges in edge list e.

 * Vertices[g] gives the embedding of graph g, that is, the coordinates of each vertex in the plane. Vertices[g, All] gives the embedding of the graph along with graphics options associated with each vertex.
