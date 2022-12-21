# Issue 6085: [with patch, not ready] Finish full implementation of c_graphs

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-05-19 17:06:07

Assignee: rlm

CC:  rdingman mvngu saliola boothby

The goal is for c_graphs to be able to take over as the default implementation of graphs in Sage. With the first patch, all that remains to be done is:

1. We need support for arbitrary hashable vertices.

2. We need support for arbitrary edge labels.

3. We need pickling.


---

Comment by rlm created at 2009-05-19 18:34:45

Some notes for posterity:

```
1. hashable vertices
 - have a list to go from an int to a label
 - a dict will go the other way
 - a stack will keep track of "unused" vertices leftover from deletion
 - these will be listed as "None" in the list

2. arbitrary edge labels
 - this will simply be a dict, going from ints to objects
 - since edge labels need not be hashable, we will need to do a search
   when trying to find the int for a label, but if we fail to find one,
   we will have a new int label for this new edge label

3. pickling
 - this will be little more than a sparse6 string
```



---

Attachment


---

Attachment

Add myself so I receive updates on this ticket :-)


---

Attachment

These patches applied cleanly against 4.0.1.a0 on an amd64 ubuntu 9.04 machine. After running "sage -b" and then "sage -testall", there were the following failures:


```
The following tests failed:                                                                                         


        sage -t  "devel/sage/doc/en/constructions/graph_theory.rst"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
        sage -t  "devel/sage/sage/graphs/print_graphs.py"                       
        sage -t  "devel/sage/sage/graphs/graph_database.py"                     
        sage -t  "devel/sage/sage/graphs/graph_list.py"                         
        sage -t  "devel/sage/sage/graphs/linearextensions.py"                   
        sage -t  "devel/sage/sage/graphs/planarity.pyx"                         
        sage -t  "devel/sage/sage/graphs/bipartite_graph.py"                    
        sage -t  "devel/sage/sage/graphs/schnyder.py"                           
        sage -t  "devel/sage/sage/graphs/graph_bundle.py"                       
        sage -t  "devel/sage/sage/graphs/graph_plot.py"                         
        sage -t  "devel/sage/sage/graphs/graph_generators.py"                   
        sage -t  "devel/sage/sage/graphs/graph_coloring.py"                     
        sage -t  "devel/sage/sage/graphs/graph_fast.pyx"                        
        sage -t  "devel/sage/sage/graphs/graph.py"                              
        sage -t  "devel/sage/sage/graphs/chrompoly.pyx"                         
        sage -t  "devel/sage/sage/graphs/base/c_graph.pyx"                      
        sage -t  "devel/sage/sage/graphs/base/sparse_graph.pyx"                 
        sage -t  "devel/sage/sage/graphs/graph_isom.pyx"                        
        sage -t  "devel/sage/sage/crypto/mq/mpolynomialsystem.py"               
        sage -t  "devel/sage/sage/matrix/constructor.py"                        
        sage -t  "devel/sage/sage/geometry/polyhedra.py"                        
        sage -t  "devel/sage/sage/geometry/lattice_polytope.py"                 
        sage -t  "devel/sage/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx"
        sage -t  "devel/sage/sage/plot/plot.py"                                   
        sage -t  "devel/sage/sage/homology/simplicial_complex.py"                 
        sage -t  "devel/sage/sage/combinat/posets/poset_examples.py"              
        sage -t  "devel/sage/sage/combinat/posets/posets.py"                      
        sage -t  "devel/sage/sage/combinat/posets/elements.py"                    
        sage -t  "devel/sage/sage/combinat/posets/lattices.py"                    
        sage -t  "devel/sage/sage/combinat/posets/hasse_diagram.py"               
        sage -t  "devel/sage/sage/combinat/partition_algebra.py"                  
        sage -t  "devel/sage/sage/combinat/skew_partition.py"                     
        sage -t  "devel/sage/sage/combinat/ribbon.py"                             
        sage -t  "devel/sage/sage/combinat/skew_tableau.py"                       
        sage -t  "devel/sage/sage/combinat/words/suffix_trees.py"                 
        sage -t  "devel/sage/sage/combinat/root_system/type_G.py"                 
        sage -t  "devel/sage/sage/combinat/root_system/type_E.py"                 
        sage -t  "devel/sage/sage/combinat/root_system/root_system.py"            
        sage -t  "devel/sage/sage/combinat/root_system/type_D.py"                 
        sage -t  "devel/sage/sage/combinat/root_system/root_lattice_realization.py"
        sage -t  "devel/sage/sage/combinat/root_system/type_B.py"                  
        sage -t  "devel/sage/sage/combinat/root_system/type_F.py"                  
        sage -t  "devel/sage/sage/combinat/root_system/type_C.py"                  
        sage -t  "devel/sage/sage/combinat/root_system/type_A.py"                  
        sage -t  "devel/sage/sage/combinat/root_system/cartan_type.py"             
        sage -t  "devel/sage/sage/combinat/root_system/weight_space.py"            
        sage -t  "devel/sage/sage/combinat/root_system/coxeter_matrix.py"          
        sage -t  "devel/sage/sage/combinat/root_system/weight_lattice_realization.py"
        sage -t  "devel/sage/sage/combinat/root_system/type_dual.py"                 
        sage -t  "devel/sage/sage/combinat/root_system/weyl_group.py"                "devel/sage/sage/misc/html.py" 
        sage -t  "devel/sage/sage/combinat/root_system/type_reducible.py"            
        sage -t  "devel/sage/sage/combinat/root_system/dynkin_diagram.py"            
        sage -t  "devel/sage/sage/combinat/root_system/root_space.py"                
        sage -t  "devel/sage/sage/combinat/root_system/cartan_matrix.py"             
        sage -t  "devel/sage/sage/combinat/permutation.py"                           
        sage -t  "devel/sage/sage/combinat/species/species.py"                       
        sage -t  "devel/sage/sage/combinat/species/recursive_species.py"             
        sage -t  "devel/sage/sage/combinat/species/sum_species.py"                   
        sage -t  "devel/sage/sage/combinat/species/product_species.py"               
        sage -t  "devel/sage/sage/combinat/crystals/fast_crystals.py"                
        sage -t  "devel/sage/sage/combinat/crystals/tensor_product.py"               
        sage -t  "devel/sage/sage/combinat/crystals/spins.py"                        
        sage -t  "devel/sage/sage/combinat/crystals/letters.py"                      
        sage -t  "devel/sage/sage/combinat/crystals/crystals.py"                     
        sage -t  "devel/sage/sage/combinat/graph_path.py"                            
        sage -t  "devel/sage/sage/databases/database.py"                             
        sage -t  "devel/sage/sage/misc/html.py"                                      
        sage -t  "devel/sage/sage/misc/functional.py"                                
        sage -t  "devel/sage/sage/misc/classgraph.py"     
```

(I suspect that "devel/sage/sage/misc/html.py" failing was already reported as a separate issue. The others seem new.) In particular, there was the following:


```
wdj`@`hera:~/sagefiles/sage-4.0.1.alpha0$ ./sage -t  "devel/sage/doc/en/constructions/graph_theory.rst"
sage -t  "devel/sage/doc/en/constructions/graph_theory.rst"                                          
**********************************************************************                               
File "/home/wdj/sagefiles/sage-4.0.1.alpha0/devel/sage/doc/en/constructions/graph_theory.rst", line 31:
    sage: D = DiGraph( { 0: [1], 1: [2], 2: [0]} )                                                     
Exception raised:                                                                                      
    Traceback (most recent call last):                                                                 
      File "/home/wdj/sagefiles/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test 
        self.run_one_example(test, example, filename, compileflags)                                    
      File "/home/wdj/sagefiles/sage-4.0.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                  
      File "/home/wdj/sagefiles/sage-4.0.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_1[2]>", line 1, in <module>                                        
        D = DiGraph( { Integer(0): [Integer(1)], Integer(1): [Integer(2)], Integer(2): [Integer(0)]} )###line 31:
    sage: D = DiGraph( { 0: [1], 1: [2], 2: [0]} )                                                               
      File "/home/wdj/sagefiles/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 10117, in __init__
        self.add_vertices(verts)
      File "/home/wdj/sagefiles/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 2923, in add_vertices
        self._backend.add_vertices(vertices)
      File "sparse_graph.pyx", line 1627, in sage.graphs.base.sparse_graph.SparseGraphBackend.add_vertices (sage/graphs/base/sparse_graph.c:15334)
      File "sparse_graph.pyx", line 404, in sage.graphs.base.sparse_graph.SparseGraph.add_vertices (sage/graphs/base/sparse_graph.c:5294)
      File "sparse_graph.pyx", line 424, in sage.graphs.base.sparse_graph.SparseGraph.add_vertices (sage/graphs/base/sparse_graph.c:5217)
    TypeError: 'int' object is not iterable
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_1
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wdj/sagefiles/sage-4.0.1.alpha0/tmp/.doctest_graph_theory.py
         [3.3 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/doc/en/constructions/graph_theory.rst"

```


Hope this helps.


---

Comment by rlm created at 2009-06-03 14:56:39

David,

I appreciate your enthusiasm, but these patches are not ready. There is no point in testing until they are. There are several more patches coming before anything is going to actually work.


---

Comment by wdj created at 2009-06-03 17:18:41

Sorry, I just read your email to sage-devel and missed the "not ready" title of your ticket... I'll try to read more carefully next time:-)


---

Comment by rlm created at 2009-06-03 20:49:17

Latest version is the closest I've seen to the whole test quite passing, but there are persisting memory issues (`malloc: *** error for object 0x8a26660: incorrect checksum for freed object - object was probably modified after being freed.`). The following example exposes this best, due to having to double the allocation several times:


```
G = Graph()
G.add_vertices(range(5000))
```



---

Attachment


---

Comment by rlm created at 2009-06-04 12:47:25

OK, latest version passes memory testing, and passes all tests except where pickling is involved... So there will be probably one more patch, with this and more documentation and other random cleanup.


---

Attachment

Part 6 brings dense graphs up to speed. Still need pickling.


---

Comment by rlm created at 2009-06-05 17:34:45

After patch 7, the only test failures in `graphs` I can find are related to the planarity code Emily Kirkman and John Bober wrote. I can imagine that the problem is that CGraphs used to require to have vertices in a consecutive range, and now, e.g. you can have the vertex set = {1, 7, 9}:

```
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/graphs/graph.py", line 2246:
    sage: g.set_planar_positions(test=True)
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_45[3]>", line 1, in <module>
        g.set_planar_positions(test=True)###line 2246:
    sage: g.set_planar_positions(test=True)
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 2324, in set_planar_positions
        raise Exception('BUG: Triangulation returned face: %s'%face)
    Exception: BUG: Triangulation returned face: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 1), (1, 0)]
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/graphs/graph.py", line 2249:
    sage: g.set_planar_positions(test=True)
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_45[5]>", line 1, in <module>
        g.set_planar_positions(test=True)###line 2249:
    sage: g.set_planar_positions(test=True)
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 2324, in set_planar_positions
        raise Exception('BUG: Triangulation returned face: %s'%face)
    Exception: BUG: Triangulation returned face: [(11, 103), (103, 104), (104, 95), (95, 11)]
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/graphs/graph.py", line 2252:
    sage: g.set_planar_positions(test=True)
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_45[7]>", line 1, in <module>
        g.set_planar_positions(test=True)###line 2252:
    sage: g.set_planar_positions(test=True)
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 2332, in set_planar_positions
        tree_nodes = _realizer( G, label)
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/schnyder.py", line 397, in _realizer
        _compute_coordinates(realizer, (tree_nodes, (v1, v2, v3)))
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/schnyder.py", line 467, in _compute_coordinates
        p = tree_nodes[v][(i + 1) % 3]
    KeyError: None
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/graphs/graph.py", line 2366:
    sage: D.set_planar_positions()
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_46[3]>", line 1, in <module>
        D.set_planar_positions()###line 2366:
    sage: D.set_planar_positions()
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 2332, in set_planar_positions
        tree_nodes = _realizer( G, label)
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/schnyder.py", line 397, in _realizer
        _compute_coordinates(realizer, (tree_nodes, (v1, v2, v3)))
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/schnyder.py", line 467, in _compute_coordinates
        p = tree_nodes[v][(i + 1) % 3]
    KeyError: None
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/graphs/graph.py", line 2367:
    sage: D.is_drawn_free_of_edge_crossings()
Expected:
    True
Got:
    False
**********************************************************************
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/graphs/schnyder.py", line 153:
    sage: _realizer(g, tn)
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[8]>", line 1, in <module>
        _realizer(g, tn)###line 153:
    sage: _realizer(g, tn)
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/schnyder.py", line 397, in _realizer
        _compute_coordinates(realizer, (tree_nodes, (v1, v2, v3)))
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/schnyder.py", line 467, in _compute_coordinates
        p = tree_nodes[v][(i + 1) % 3]
    KeyError: None
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/graphs/schnyder.py", line 350:
    sage: _realizer(g, tn)
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[8]>", line 1, in <module>
        _realizer(g, tn)###line 350:
    sage: _realizer(g, tn)
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/schnyder.py", line 397, in _realizer
        _compute_coordinates(realizer, (tree_nodes, (v1, v2, v3)))
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/schnyder.py", line 467, in _compute_coordinates
        p = tree_nodes[v][(i + 1) % 3]
    KeyError: None
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/graphs/schnyder.py", line 430:
    sage: r = _realizer(g, tn)
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[8]>", line 1, in <module>
        r = _realizer(g, tn)###line 430:
    sage: r = _realizer(g, tn)
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/schnyder.py", line 397, in _realizer
        _compute_coordinates(realizer, (tree_nodes, (v1, v2, v3)))
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/schnyder.py", line 467, in _compute_coordinates
        p = tree_nodes[v][(i + 1) % 3]
    KeyError: None
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/graphs/schnyder.py", line 431:
    sage: _compute_coordinates(g,r)
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[9]>", line 1, in <module>
        _compute_coordinates(g,r)###line 431:
    sage: _compute_coordinates(g,r)
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/schnyder.py", line 437, in _compute_coordinates
        tree_nodes, (v1, v2, v3) = x
    ValueError: too many values to unpack
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/graphs/schnyder.py", line 432:
    sage: g.get_pos()
Expected:
    {0: [5, 1], 1: [0, 5], 2: [1, 0], 3: [1, 4], 4: [2, 1], 5: [2, 3], 6: [3, 2]}
Got nothing
**********************************************************************
```


This one probably results from ordering being different:

```
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/combinat/posets/posets.py", line 924:
    sage: [(v,P.rank(v)) for v in P]
Expected:
    [(1234, 0),
     (2134, 1),
    ...
     (4231, 5),
     (4321, 6)]
Got:
    [(1234, 0), (1243, 1), (1324, 1), (2134, 1), (2314, 2), (1423, 2), (3124, 2), (3214, 3), (1342, 2), (1432, 3), (2143, 2), (2341, 3), (4123, 3), (3142, 3), (4132, 4), (3241, 4), (2413, 3), (3412, 4), (2431, 4), (3421, 5), (4213, 4), (4231, 5), (4312, 5), (4321, 6)]
**********************************************************************
```


Not sure about these ones:

```
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/combinat/species/species.py", line 667:
    sage: list(sorted(labels.items()))
Expected:
    [(Combinatorial species, 0),
     (Product of (Combinatorial species) and (Combinatorial species), 2),
     (Singleton species, 1),
     (Sum of (Singleton species) and (Product of (Combinatorial species) and (Combinatorial species)), 3)]
Got:
    [(('o', Combinatorial species), 0), (('o', Product of (Combinatorial species) and (Combinatorial species)), 2), (('o', Singleton species), 1), (('o', Sum of (Singleton species) and (Product of (Combinatorial species) and (Combinatorial species))), 3), (('x', 0), 4), (('x', 1), 5), (Combinatorial species, Combinatorial species), (Product of (Combinatorial species) and (Combinatorial species), Product of (Combinatorial species) and (Combinatorial species)), (Singleton species, Singleton species), (Sum of (Singleton species) and (Product of (Combinatorial species) and (Combinatorial species)), Sum of (Singleton species) and (Product of (Combinatorial species) and (Combinatorial species)))]
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/combinat/species/species.py", line 672:
    sage: g.edges()
Expected:
    [(0, 3, None), (2, 0, None), (2, 0, None), (3, 1, None), (3, 2, None)]
Got:
    [(Combinatorial species, Sum of (Singleton species) and (Product of (Combinatorial species) and (Combinatorial species)), None), (Product of (Combinatorial species) and (Combinatorial species), Combinatorial species, None), (Product of (Combinatorial species) and (Combinatorial species), Combinatorial species, None), (Sum of (Singleton species) and (Product of (Combinatorial species) and (Combinatorial species)), Product of (Combinatorial species) and (Combinatorial species), None), (Sum of (Singleton species) and (Product of (Combinatorial species) and (Combinatorial species)), Singleton species, None)]
**********************************************************************
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1337:
    sage: s.edges()
Expected:
    [(0, 3, word: ca), (0, 5, word: a), (0, 7, word: o), (3, 1, word: cao), (3, 4, word: o), (5, 2, word: cao), (5, 6, word: o)]
Got:
    [(0, 1, word: cacao), (0, 2, word: acao), (0, 3, word: ca), (0, 5, word: a), (0, 7, word: o), (3, 1, word: cao), (3, 4, word: o), (5, 2, word: cao), (5, 6, word: o)]
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1345:
    sage: s.edges()
Expected:
    [(0, 3, word: 01), (0, 5, word: 1), (3, 1, word: 011), (3, 4, word: 1), (5, 2, word: 011), (5, 6, word: 1)]
Got:
    [(0, 1, word: 01011), (0, 2, word: 1011), (0, 3, word: 01), (0, 5, word: 1), (0, 7, word: 1), (3, 1, word: 011), (3, 4, word: 1), (5, 2, word: 011), (5, 6, word: 1), (7, 2, word: 011)]
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1389:
    sage: NST.word_to_node(0, W("ca"))
Expected:
    ('node', 17, word: )
Got:
    ('implicit', ((0, 5, word: cabaabaca), 2), word: )
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1391:
    sage: NST.word_to_node(0, W("cab"))
Expected:
    ('implicit', ((17, 5, word: baabaca), 1), word: )
Got:
    ('implicit', ((0, 5, word: cabaabaca), 3), word: )
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1393:
    sage: NST.word_to_node(17, W("b"))
Expected:
    ('implicit', ((17, 5, word: baabaca), 1), word: )
Got:
    ('node', 17, word: b)
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1395:
    sage: NST.word_to_node(15, W("baabacabca"))
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_41[8]>", line 1, in <module>
        NST.word_to_node(Integer(15), W("baabacabca"))###line 1395:
    sage: NST.word_to_node(15, W("baabacabca"))
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/combinat/words/suffix_trees.py", line 1400, in word_to_node
        for v in self.successor_iterator(node):
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 10434, in successor_iterator
        return iter(set(self._backend.iterator_out_nbrs(vertex)))
      File "c_graph.pyx", line 615, in sage.graphs.base.c_graph.CGraphBackend.iterator_out_nbrs (sage/graphs/base/c_graph.c:7952)
    KeyError: 15
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1464:
    sage: NaiveSuffixTree(Word("abacabaabaca")).plot()
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_43[3]>", line 1, in <module>
        NaiveSuffixTree(Word("abacabaabaca")).plot()###line 1464:
    sage: NaiveSuffixTree(Word("abacabaabaca")).plot()
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/combinat/words/suffix_trees.py", line 1477, in plot
        *args, **kwds)
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/plot/misc.py", line 325, in wrapper
        return func(*args, **options)
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 6513, in plot
        return GraphPlot(graph=self, options=options).plot()
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/graph_plot.py", line 84, in __init__
        self.set_pos()
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/graph_plot.py", line 148, in set_pos
        raise RuntimeError("Cannot use tree layout on this graph: self.is_tree() returns False.")
    RuntimeError: Cannot use tree layout on this graph: self.is_tree() returns False.
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1469:
    sage: type(NaiveSuffixTree(Word("abacabaabaca")).plot())
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.0.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_43[5]>", line 1, in <module>
        type(NaiveSuffixTree(Word("abacabaabaca")).plot())###line 1469:
    sage: type(NaiveSuffixTree(Word("abacabaabaca")).plot())
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/combinat/words/suffix_trees.py", line 1477, in plot
        *args, **kwds)
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/plot/misc.py", line 325, in wrapper
        return func(*args, **options)
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 6513, in plot
        return GraphPlot(graph=self, options=options).plot()
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/graph_plot.py", line 84, in __init__
        self.set_pos()
      File "/Users/rlmill/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/graphs/graph_plot.py", line 148, in set_pos
        raise RuntimeError("Cannot use tree layout on this graph: self.is_tree() returns False.")
    RuntimeError: Cannot use tree layout on this graph: self.is_tree() returns False.
**********************************************************************
File "/Users/rlmill/sage-4.0.rc0/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1487:
    sage: NaiveSuffixTree(Word("abacabaabaca")).node_to_word(17)
Expected:
    word: ca
Got:
    word: aca
**********************************************************************
```



---

Attachment


---

Comment by rlm created at 2009-06-06 07:11:46

Species doctests now passing. The `sage/combinat/words` errors are a bit more mysterious to me, because of the class structure there...


---

Attachment

A benchmark:


```
sage: time G = Graph(1000000)
CPU times: user 7.31 s, sys: 0.29 s, total: 7.60 s
Wall time: 7.65 s
```



```
sage: time G = Graph(1000000)
CPU times: user 0.05 s, sys: 0.09 s, total: 0.13 s
Wall time: 0.14 s
```



---

Attachment


---

Attachment

Apply patches in *numerical* order, not the order listed. Patches are rebased on sage-4.0.2.rc2.


---

Comment by rlm created at 2009-06-17 20:04:35

Equivalent to applying parts 1 through 9


---

Attachment

One last bugfix in bitsets


---

Comment by boothby created at 2009-06-25 03:47:54

I can't apply this to 4.1.alpha0.


```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6085/trac_6085-flattened.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6085/trac_6085-flattened.patch
Loading: [..................................]
cd "/space/boothby/sage-4.1.a0/devel/sage" && hg status
cd "/space/boothby/sage-4.1.a0/devel/sage" && hg status
cd "/space/boothby/sage-4.1.a0/devel/sage" && hg import   "/home/boothby/.sage/temp/geom/12604/tmp_1.patch"
applying /home/boothby/.sage/temp/geom/12604/tmp_1.patch
unable to find 'sage/graphs/graph_isom.pyx' for patching
3 out of 3 hunks FAILED -- saving rejects to file sage/graphs/graph_isom.pyx.rej
abort: patch failed to apply
```



---

Attachment

Python 2.6 formatting changes


---

Comment by rlm created at 2009-06-25 10:05:58

Since I have rebased this ticket around the Python 2.6.2 changes, and since the Python 2.6.2 upgrade has uncovered some problems, I'm flagging this as needs work until some resolution regarding Python 2.6 is reached. At that point, I'll post a flat patch which will be appropriate, whichever way we end up going.


---

Comment by boothby created at 2009-06-25 17:49:16

Works for me!


---

Comment by rlm created at 2009-06-25 17:52:35

Resolution: fixed
