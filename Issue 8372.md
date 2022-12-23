# Issue 8372: split up incidence_matrix() over graph.py and digraph.py

Issue created by migration from https://trac.sagemath.org/ticket/8372

Original creator: mvngu

Original creation time: 2010-02-26 05:01:41

Assignee: rlm

CC:  wdj rbeezer dcoudert

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/b9e4114047427c2e):

```
For discussion purposes, let me toss out some ideas on improving the
interface for computing incidence matrices. For a graph object G, I
propose we add a keyword to G.incidence_matrix() so that the interface
is now changed to the following method signature:

def G.incidence_matrix(orientation=False)

The keyword "orientation" takes on a Boolean value. So
G.incidence_matrix(orientation=False) or G.incidence_matrix() returns
the unoriented incidence matrix of an undirected graph G. Furthermore,
G.incidence_matrix(orientation=True) returns the oriented incidence
matrix of an undirected graph G, which is the current behaviour. The
keyword "orientation" has no effect if G is a digraph. So
"orientation" is only meant to affect undirected graphs.

Let's consider whether or not to leave the method incidence_matrix()
in the module generic_graph.py. I consider it more appropriate for
graph.py (a module for undirected graphs) to deal with incidence
matrices for undirected graphs. Similarly, digraph.py can deal with
incidence matrices for digraphs. At the moment, incidence_matrix()
resides in generic_graph.py, a module with over 10 thousand lines. 
```



---

Comment by mvngu created at 2010-02-27 15:44:47

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-02-27 15:44:47

Here is a description of the changes in the patch [trac_8372-incidence-matrix.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8372/trac_8372-incidence-matrix.patch):

 * Add the module `digraph.py` to the reference manual.
 * Reorganize the module listing in the reference manual so that the module `cliquer.py` for cliques should not be the first one on the list. You want to first list undirected graphs, followed digraphs, etc.
 * Remove the method `incidence_matrix()` from `generic_graph.py`.
 * Implement `incidence_matrix()` both for undirected graphs as contained in `graph.py`, and for digraphs as contained in `digraph.py`.


---

Comment by rbeezer created at 2010-02-27 20:21:31

Changing status from needs_review to needs_info.


---

Comment by rbeezer created at 2010-02-27 20:21:31

Hi Minh,

This looks real nice on a first pass.  You are the king of documentation.  Two questions.

Columns of the matrix get sorted (as column vectors) once they are all built.  I recognize this is the current behavior, and that this makes a "pretty" matrix, highlighting structure.  But now it is much harder to connect columns back to the edges they correspond to.

For example, some of your tests work with vertex degrees.  You don't need to sort the outputs before checking equality because you know the results are in the order given by the vertex iterator.  Why not preserve that quality with respect to the columns/edges?  Anybody who wants sorted columns can do it themselves, but it strikes me it'll be harder to get the edges back from the adjacencies as written.

Second question.  I'm uncertain about putting a "2" into the incidence matrix for a loop.  I'd prefer to think of a loop in a digraph (one without multiple edges) as a directed edge back to the same vertex, so I'd sum +1 and -1 at that vertex (to get zero).

You can construct a `DiGraph` from an incidence matrix, and this form of construction explicitly checks for a single +1 and a single -1 in each column.  So the (hopefully) inverse processes below don't work.  My suggestion of a zero breaks also.  Maybe throw an error for a `DiGraph` with loops?  Using a zero preserves the property that the sum of the rows of the matrix is the all-zeros vector, which I think is as important some of the column-sum properties.  Haven't thought about how all this affects getting the Laplacian as the product of the incidence matrix with its transpose (which might make a nice doctest).


```
sage: D=DiGraph({0:[0], 1:[2]})
sage: D.incidence_matrix()
[ 0  2]
[-1  0]
[ 1  0]
sage: E=DiGraph(D.incidence_matrix())
<BOOM>
ValueError: Non-symmetric or non-square matrix assumed to be an incidence matrix: There must be two nonzero entries (-1 & 1) per column.
```


Rob


---

Comment by wdj created at 2010-02-27 22:30:50

I just want to say that sage -testall passed on a 10.6.2 mac, so i have no bug reports to add.


---

Attachment

based on Sage 4.3.3


---

Comment by mvngu created at 2010-02-28 19:54:58

Changing status from needs_info to needs_work.


---

Comment by mvngu created at 2010-02-28 19:54:58

Replying to [comment:2 rbeezer]:
> Columns of the matrix get sorted (as column vectors) once they are all built.  I recognize this is the current behavior, and that this makes a "pretty" matrix, highlighting structure.  But now it is much harder to connect columns back to the edges they correspond to.

To me, it doesn't make any difference whether or not we have the statements

```python
cols.sort()
return matrix(cols, sparse=sparse).transpose()
```

to sort the columns before feeding them to the matrix constructor. I don't see any benefits either way mainly because to me incidence matrices don't care about edge labels. For undirected graphs, the incidence matrix with sorted columns

```
[0 0 1]
[0 1 0]
[1 0 0]
[1 1 1]
```

and the incidence matrix without sorted columns

```
[1 0 0]
[0 1 0]
[0 0 1]
[1 1 1]
```

result in isomorphic graphs. I have commented out the line that sorts the columns. If in the future anyone wants to sort the columns as per the above two lines, they could add a keyword, say, `sort=[True|False]` which defaults to `False`. For the moment, I leave this enhancement out of the patch as it is beyond the scope of what this ticket is about.





> Second question.  I'm uncertain about putting a "2" into the incidence matrix for a loop.  I'd prefer to think of a loop in a digraph (one without multiple edges) as a directed edge back to the same vertex, so I'd sum +1 and -1 at that vertex (to get zero).

Here are some motivations for having "2" designating self-loops: 

 * For an undirected graph `G` with unoriented incidence matrix `M`, a row sum corresponds to the degree of a vertex. This holds even if `G` has self-loops or `G` is a multi-undirected graph. Any column sum is equal to 2 for the following cases: `G` is simple, `G` has self-loops, or `G` is a multi-undirected graph. If self-loops are ignored, i.e. assigned the value "0" to the relevant entry in a row, I see no easy way to reconstruct the original graph from the incidence matrix.
 * Let `G` be an undirected (or multi-undirected) graph with oriented incidence matrix `M`, and say we use "2" to designate self-loops. We can use the follow method to recover the vertex degree. For each row `r` of `M`, let `n` (meaning "negative") be the frequency of "-1" in `r`, let `p` (meaning "positive") be the frequency of "1" in `r`, and let `t` (meaning "two") be twice the frequency of "2" in `r` because a self-loop contributes two to the total degree of a vertex. Then the degree of the vertex corresponding to `r` is given by `n + p + t`. Using "0" for self-loops, I don't see any easy way to recover the degree of a vertex. Now in general, each column sum of `M` is not always zero. But this loss is compensated for by the knowledge that: the degree of any vertex is recoverable; if the sum of any column `c` is 2, then `c` corresponds to a self-loop. Using "0" for self-loops would result in the loss of two vital pieces of information: the exact degree of each vertex; and whether or not an edge is a self-loop. Another loss is that we cannot easily (accurately) recover `G` from `M`.
 * The argument for the case of digraphs (or multidigraphs) is similar to that for the oriented incidence matrix of an undirected (or multi-undirected) graph. That is, using "0" for self-loops would result in the loss of such information as: the exact degree of each vertex; whether a column represents a self-loop; and no easy way to accurately recover the original (multi)digraph from its incidence matrix.





> You can construct a `DiGraph` from an incidence matrix, and this form of construction explicitly checks for a single +1 and a single -1 in each column.  So the (hopefully) inverse processes below don't work.  My suggestion of a zero breaks also.  Maybe throw an error for a `DiGraph` with loops?  Using a zero preserves the property that the sum of the rows of the matrix is the all-zeros vector, which I think is as important some of the column-sum properties. 

The more I delve into the graph theory code to enhance the incidence matrix implementation, the greater is the urge to first update NetworkX to version 1.0.1. With the definition of incidence matrix as documented in the patch, one could rely on that definition to modify the graph and digraph constructors to take account of the case where "2" represents self-loops. I have thought about implementing this. But half way through my modification of the relevant constructors, I get the feeling that any more patches to the graph theory module of Sage would result in more bit rotting of the patches at ticket #7608 for upgrading to NetworkX 1.0.1, and more work to get NetworkX upgraded.





> Haven't thought about how all this affects getting the Laplacian as the product of the incidence matrix with its transpose (which might make a nice doctest).

I believe the modification I proposed won't affect the computation of Laplacian matrices from incidence matrices of undirected loopless graphs.






```
sage: D=DiGraph({0:[0], 1:[2]})
sage: D.incidence_matrix()
[ 0  2]
[-1  0]
[ 1  0]
sage: E=DiGraph(D.incidence_matrix())
<BOOM>
ValueError: Non-symmetric or non-square matrix assumed to be an incidence matrix: There must be two nonzero entries (-1 & 1) per column.
```


This can be fixed by modifying the constructors of graph and digraph.




As much as I want to get the incidence matrix enhancement patch into Sage as soon as possible, I think the upgrading to NetworkX 1.0.1 now takes high priority on my todo list. Producing a new patch for the incidence matrix enhancement is easy, but the more difficult task is to ensure that patches at #7608 don't bit rot. After taking a day off thinking about this matter, I'll postpone the current ticket and instead work on #7608. I have uploaded a half-finished patch that improves on the previous version. I want to put it here so that I could resume work on it later on. Sorry for having troubled you to review the code so far.


---

Comment by rbeezer created at 2010-03-02 05:30:34

Hi Minh,

Makes sense to wait on this (and it was no trouble to have a look inpreparation for the eventual review).

I should have been clearer - my hesitations on a "2" for a loop is *only* for the case of a digraph.  It make abundant good sense for an undirected graph.

Suppose a digraph only allows for at most a single directed edge between any pair of vertices (ie, no multiple directed edges).  Then shouldn't a loop have a head and a tail and contribute a +1 and a -1 there?  I agree totally that this is a loss of information, since we can't recover the loop from the matrix.  But I also prefer that these matrices have nice algebraic properties (like constant row sum, or constant column sums), so I don't view them totally as simply carriers of enough information to reconstruct the graph.  I can see both sides of the argument.

I'll get back to this once you are ready to return to it.

Rob


---

Comment by @vipul79321 created at 2020-03-02 05:48:14

I suggest that:\\

1).We can split up current incidence_matrix method in graph.py and digraph.py.\\
2).

> {{{
> sage: D=DiGraph({0:[0], 1:[2]})
> sage: D.incidence_matrix()
> [ 0  2]
> [-1  0]
> [ 1  0]
> sage: E=DiGraph(D.incidence_matrix())
> <BOOM>
> ValueError: Non-symmetric or non-square matrix assumed to be an incidence matrix: There must be two nonzero entries (-1 & 1) per column.
> }}}
> 
This can be fixed by modifying the constructors of digraph or `from_oriented_incidence_matrix` method in graph_input by returning loop less version of that graph by dropping column containing all zeros.\\

 
Shall I proceed to implement proposed changes or is there anything else that can be done?


---

Comment by dcoudert created at 2020-03-03 09:31:25

Before splitting the method, we have 2 issues to fix:
- the error in `from_oriented_incidence_matrix` you mention
- the fact that the method is not Python3 compliant. For instance, it breaks for `G = DiGraph({0: ['a']})`.

You should open a new ticket to fix these issues (and mention that ticket here).


---

Comment by @vipul79321 created at 2020-03-03 13:59:29

Replying to [comment:12 dcoudert]:
Just wanted to confirm that:
> Before splitting the method, we have 2 issues to fix:
> - the error in `from_oriented_incidence_matrix` you mention
Expectation from this ticket should be that `from_oriented_incidence_matrix` should be able to handle column with all zero entries by returning loop less version of that graph.
> - the fact that the method is not Python3 compliant. For instance, it breaks for `G = DiGraph({0: ['a']})`.
> 
Expectation from this ticket should be that `incidence_matrix` should be able to handle case when sorting is not possible by returning incidence matrix along with vertex labels.


---

Comment by dcoudert created at 2020-03-03 16:25:50

Replying to [comment:13 gh-vipul79321]:
> Replying to [comment:12 dcoudert]:
> Expectation from this ticket should be that `from_oriented_incidence_matrix` should be able to handle column with all zero entries by returning loop less version of that graph.
yes

> Expectation from this ticket should be that `incidence_matrix` should be able to handle case when sorting is not possible by returning incidence matrix along with vertex labels.

Actually, part of the sorting problem will be resolved with #22349, i.e., deprecate sorting by default. But the 'reorder` internal method is a problem.


---

Comment by @vipul79321 created at 2020-03-03 19:29:59

Replying to [comment:12 dcoudert]:
> You should open a new ticket to fix these issues (and mention that ticket here).
I have created ticket #29275, #29276, #29277


---

Comment by mkoeppe created at 2020-04-14 19:41:51

Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.


---

Comment by mkoeppe created at 2021-02-13 20:51:01

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.


---

Comment by mkoeppe created at 2021-07-19 00:44:56

Setting a new milestone for this ticket based on a cursory review.
