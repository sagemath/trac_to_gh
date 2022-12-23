# Issue 2597: [with patch, needs review] Add reduced adjacency matrix and alist file format support to BipartiteGraph

Issue created by migration from https://trac.sagemath.org/ticket/2597

Original creator: rhinton

Original creation time: 2008-03-19 15:26:24

Assignee: rlm

This patch allows a BipartiteGraph to be created from a reduced adjacency matrix and return the same.  Multi-edge or weighted constructions are supported.  Also, it adds support for creation, loading, and saving bipartite graphs in alist format.


---

Comment by rlm created at 2008-03-19 18:33:04

#2506 has been fixed, so you can probably simply that doctest (line 409 or so).

This looks good.


---

Comment by rlm created at 2008-03-19 18:33:30

err, simplify


---

Comment by rlm created at 2008-03-19 18:37:08

I would be very careful about creating the reduced adjacency matrix as a matrix over GF(2). We did this for graphs, and it messed up the characteristic polynomials. You should probably create it over !ZZ, following the "M[i,j] = number of paths from i to j" interpretation. Jason should give a second opinion on this point.


---

Comment by jason created at 2008-03-19 19:24:19

I would strongly encourage returning a matrix over ZZ instead of over GF(2) in the BipartiteGraph class.  However, if it is standard to have a parity check matrix over GF(2), I would create a separate wrapper called parity_check_matrix or something like that and return a matrix over GF(2).

In normal graph theory, adjacency matrices are not thought of as over finite fields.  This has caused us problems in the past too.


---

Comment by rhinton created at 2008-03-20 01:47:34

Per your comments I simplified the doctest given the != bug fix.  Also, reduced_adjacency_matrix() now returns a matrix over ZZ for all but weighted graphs (where the weights are used for the field elements in the original matrix). 

For parity check matrices we can call change_ring() on the returned matrix to get GF(2) elements.  Or we can create them weighted to begin with.  Personally, most of my matrices will go to file for the present, and the alist format is strictly GF(2).


---

Comment by jason created at 2008-03-20 15:33:55

In our comments above (just to be clear), we are distinguishing between a zero-one matrix over ZZ and a zero-one matrix over GF(2).  Is the alist format just a zero-one matrix format, or is it truly in GF(2) (i.e., 1+1=0)?

My strong preference is that all matrices returned for normal graph theory stuff be over ZZ, whether or not they are zero-one matrices.  Of course, for coding stuff, you may want matrices over GF(2) instead, but I would make the functions that return GF(2) matrices very clearly coding functions (i.e., "parity_check_matrix()" or something).


---

Comment by rhinton created at 2008-03-20 21:10:53

Yes, I think you were clear.  The reduced_adjacency_matrix() function right now returns zero-one matrices over ZZ for normal bipartite graphs.  For multigraphs it will return matrices over ZZ with some entries possibly > 1.  The only concession I made to coding theory is for weighted graphs.  If a weighted bipartite graph is created from a reduced adjacency matrix, it stores the original value as the label for each non-zero matrix element.  This will work fine for matrices over ZZ as well.  

But if you _start_ with a reduced adjacency matrix over GF(2^8), for instance, create a bipartite graph describing its structure, and then ask for the reduced adjacency matrix back, you will get back the original matrix over GF(2^8).  So the only way you can get a matrix over a ring besides ZZ is to _start_ with a matrix not over ZZ, create its bipartite graph, and then ask for the reduced adjacency matrix back.  

Actually that last statement is not entirely accurate.  Only weighted graphs will return a R.A.M. over a field other than ZZ.  Weighted graphs return a matrix over the field of the label of their first edge.  If they have no edges, they return a matrix over GF(2).

I'll try again.  I'll make the default matrix field ZZ even for weighted graphs without edges.  And I'll add a little more error handling code for the weighted case with edges.  (I'll post this later tonight.)


---

Comment by rlm created at 2008-03-20 21:30:01

RE:
"Weighted graphs return a matrix over the field of the label of their first edge."

There are smarter ways to approach this. First, you might take a look at the weighted adjacency matrix constructor in `graph.py`, which finds a suitable common parent implicitly, through the matrix constructor. What this basically does is construct a sequence, and retrieve its universe:


```
sage: Sequence([4/5, 3]).universe()
Rational Field
sage: i = CC(i)
sage: Sequence([4/5, 3, i]).universe()
Complex Field with 53 bits of precision
```



---

Comment by rhinton created at 2008-03-23 02:25:46

Patch 4 uses matrix() constructor to find ring for weighted graph constructions.  This patch depends on the fixes in #2651 (or equivalently #2649 and #2650).  I think the reduced_adjacency_matrix() code is shorter as well.


---

Attachment

In the future, when posting a new patch, please make sure to indicate whether it replaces old patches or builds on top of them. That makes it easier on people like mabshoff to look at the ticket without too much pain.

I'm getting some doctest failures after applying this patch. It looks like the matrix constructor doesn't know what ring to use when it's given an empty list (although I might be wrong). Also in the future, make sure to run doctests on all relevant code before posting a patch. We're all guilty of this one :-).


---

Comment by rhinton created at 2008-03-24 12:04:36

Thank you; sorry for the confusion.  Each patch supersedes the earlier patches, so only patch 4 should be applied.  

The doctest failure is actually a shortcoming in the matrix() constructor.  Patch 4 actually works as expected, but it depends on #2651 to fix the matrix() constructor for all the doctests to pass.


---

Comment by jason created at 2008-03-24 16:04:24

It will be a few days before #2651 is ready (it may not make it into 2.11).  Do you want to post your temporary patch for the current matrix() so that this ticket can go in?


---

Comment by rhinton created at 2008-03-24 20:13:54

patch to matrix/constructor.py to fix bug and allow all bipartite_graph doctests to pass


---

Attachment

Looks good, relevant tests pass.


---

Comment by mabshoff created at 2008-03-29 01:32:50

Resolution: fixed


---

Comment by mabshoff created at 2008-03-29 01:32:50

Merged both patches in Sage 2.11.alpha2
