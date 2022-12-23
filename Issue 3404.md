# Issue 3404: graph.automorphism_group returns permutations with the wrong number of elements.

Issue created by migration from https://trac.sagemath.org/ticket/3404

Original creator: jason

Original creation time: 2008-06-12 18:09:14

Assignee: rlm

Both of the graphs below are the path graph on 3 vertices.  The problem is that the first labeling returns a permutation group of degree 2, when it should be of degree 3.


```
sage: g=Graph('Bo')
sage: print g.automorphism_group().degree()
2
sage: h=Graph('Bg')
sage: print h.automorphism_group().degree()
3
sage: g.is_isomorphic(h)
True
```



---

Comment by rlm created at 2008-06-12 19:02:54

Unfortunately, since permutation groups are (currently) simply wrappers for GAP permutation groups, the object itself carries no notion of what it acts on, only a cycle representation of its generators.


```
sage: g=Graph('Bo')
sage: G=g.automorphism_group()
sage: G.degree?
Type:		instancemethod
Base Class:	<type 'instancemethod'>
String Form:	<bound method PermutationGroup_generic.degree of Permutation Group with generators [(1,2)]>
Namespace:	Interactive
File:		/Users/rlmill/sage-3.0.2/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py
Definition:	G.degree(self)
Docstring:
    
            Synonym for largest_moved_point().
    
            EXAMPLES:
                sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
                sage: G.degree()
                5
}}} 

However, you can do:
{{{
sage: g.automorphism_group(translation=True, orbits=True)
(Permutation Group with generators [(1,2)], {0: 3, 1: 1, 2: 2}, [[0], [1, 2]])
}}}

The second is telling you which vertex of the graph is thought of as which integer by the group (here GAP thinks of this as 3 fixed, 4 fixed, 5 fixed, ...) and the third are the actual orbits of all the vertices.

This is a problem in permutation groups, not graphs.


---

Comment by rlm created at 2008-06-12 19:24:25

Changing status from new to assigned.


---

Comment by rlm created at 2008-06-12 19:24:25

Changing component from graph theory to basic arithmetic.


---

Comment by mhansen created at 2009-06-04 22:53:53

Resolution: invalid


---

Comment by mhansen created at 2009-06-04 22:53:53

This has been fixed.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: g=Graph('Bo')
sage: sage: print g.automorphism_group().degree()
3
sage: g.automorphism_group()
Permutation Group with generators [(1,2)]
```

