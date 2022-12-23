# Issue 6258: Improve accuracy of graph eigenvalues

Issue created by migration from https://trac.sagemath.org/ticket/6258

Original creator: rbeezer

Original creation time: 2009-06-11 03:02:30

Assignee: rbeezer

CC:  jason

Eigenspaces and eigenvalues of graphs are computed by converting the adjacency matrix to have RDF as the base ring, but there are now better routines in place for eigenvalues of integer matrices, so the `eigenspaces()` and `eigenvalues()` methods should be using those.

At present, the approximate values of the eigenvalues lead to eigenspaces "splitting" into pieces (i.e. several eigenspaces that should all be one), so in that regard current results are inaccurate.


---

Comment by rbeezer created at 2009-06-30 06:07:47

Changing priority from minor to critical.


---

Attachment

The patch generally improves graph eigenvalues by not altering the adjacency matrix and therefore allowing new routines to take advantage of the adjacency matrix being a matrix of integers.  It also corrects a serious bug for eigenvalues of digraphs.  More specifically

1.  The adjacency matrix is no longer converted to a matrix of reals or complexes.

2.  Eigenspaces are now more abstract (but are exact).  More numerical results come from the new `eigenvectors()` method.

3.  Any complex part of an eigenvalue was previously being stripped, as if a graph could never be a digraph.  This has been corrected and a simple doctest added.

4.  While in the neighborhood, the `characteristic_polynomial()` got some cosmetic changes in its docstring.

5.  Long-term, the `spectrum()` command should return some sort of object, like a `Factorization` object, as discussed on sage-devel.  Then the current `spectrum()` could be renamed as `eigenvalues()`.


---

Comment by saliola created at 2009-06-30 09:39:20

Looks good. And great job with the documentation!

Patch applies cleanly to 4.1.alpha2; testing in progress on sage-math. I'll report back soon.


---

Comment by saliola created at 2009-06-30 11:19:15

No new doctest failures are introduced by this patch on 4.1.alpha2. 

Positive review.


---

Comment by rlm created at 2009-07-02 20:34:00

Resolution: fixed
