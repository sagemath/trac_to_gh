# Issue 9575: Grundy coloring of a graph

Issue created by migration from https://trac.sagemath.org/ticket/9575

Original creator: ncohen

Original creation time: 2010-07-22 06:58:15

Assignee: jason, ncohen, rlm

This patch adds the function ``grundy_coloring``, which computes the worst case of a first-fit coloring algorithm. Here are some explanations from the function's help :

    A first-fit coloring is obtained by sequentially coloring the
    vertices of a graph, assigning them the smallest color not already
    assigned to one of its neighbors. The result is clearly a proper
    coloring, which usually requires much more colors than an optimal
    vertex coloring of the graph, and heavily depends on the ordering
    of the vertices.

    The number of colors required by the worst-case application of
    this algorithm on a graph `G` is called the Grundy number, written
    `\Gamma (G)`.

    Equivalent formulation :

    Equivalently, a Grundy coloring is a proper vertex coloring such
    that any vertex colored with `i` has, for every `j<i`, a neighbor
    colored with `j`. This can define a Linear Program, which is used
    here to compute the Grundy number of a graph.

Nathann




---

Attachment


---

Comment by ncohen created at 2010-07-22 07:08:23

Changing status from new to needs_review.


---

Comment by lsampaio created at 2010-07-28 05:47:25

Changing status from needs_review to positive_review.


---

Comment by lsampaio created at 2010-07-28 05:47:25

It works, the documentation is ok. 
I believe it can be accepted.


---

Comment by ncohen created at 2010-07-28 05:51:21

Yeahhhhhhhhhhhhhhhhhhhh !!!!!!

Thank youuuuuuuuuuuuuu !

Nathann


---

Comment by mpatel created at 2010-08-09 09:46:18

Please remember to update the Author(s) and Reviewer(s) fields.  I've entered guesses.  lsampaio, could you update [the account-name map on the main Sage Trac wiki page](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames) with your information?  Thanks!


---

Comment by mpatel created at 2010-08-09 09:46:18

Resolution: fixed
