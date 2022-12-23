# Issue 6858: [with patch, needs review] Cayley graph connecting set

Issue created by migration from https://trac.sagemath.org/ticket/6858

Original creator: rlm

Original creation time: 2009-09-02 01:11:38

Assignee: rlm

Reported by Chris Godsil.


---

Comment by ncohen created at 2009-09-05 08:19:32

Hmmm.. I may have done something wrong, but here is what I tried 


```
sage: g=PermutationGroup([(i+1,j+1) for i in range(5) for j in range(5) if j!=i])
sage: (1,2) in g
True
sage: (2,3) in g
True
sage: g.cayley_graph(connecting_set=[(1,2),(2,3)])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/user/ncohen/home/.sage/temp/rebelote.inria.fr/4013/_user_ncohen_home__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/groups/group.so in sage.groups.group.FiniteGroup.cayley_graph (sage/groups/group.c:2157)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.MonoidElement.__mul__ (sage/structure/element.c:8537)()

TypeError: unsupported operand parent(s) for '*': 'Permutation Group with generators [(4,5), (3,4), (3,5), (2,3), (2,4), (2,5), (1,2), (1,3), (1,4), (1,5)]' and '<type 'tuple'>'

```


Even though it's apparent I know very few about groups in Sage as I had to build S_n by enumerating generators ( I guess there is a command to do that with only the cardinal ? ) ^^;


---

Attachment

OK, this new patch should do the trick.


---

Comment by ncohen created at 2009-09-11 14:53:59

Applies fine, documented,does its job.... Positive review ! ;-)

When testing the patch, I tried ( among others ) :

```
sage: len(g.cayley_graph(connecting_set=[(1,2)]).connected_components())
60
sage: len(g.cayley_graph(connecting_set=[(1,2),(2,3)]).connected_components())
20
sage: len(g.cayley_graph(connecting_set=[(1,2),(2,3),(3,4)]).connected_components())
5
```


If you think it useful, it could also be included in the examples contained in the docstring, even though there are already two and it may not be necessary at all :-)

Nathann


---

Comment by mvngu created at 2009-09-11 17:10:25

Resolution: fixed
