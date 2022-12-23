# Issue 6000: Sets enumerated by exploring a search space with a (lazy) tree or graph structure

Issue created by migration from https://trac.sagemath.org/ticket/6000

Original creator: nthiery

Original creation time: 2009-05-06 19:31:56

Assignee: nthiery

CC:  sage-combinat

Keywords: enumerate sets, depth first search, ideal of a relation

This patches extend the sage.combinat.backtrack library with other
generic tools for constructing large sets whose elements can be
enumerated by exploring a search space with a (lazy) tree or graph
structure.

 - SearchForest:
   Depth first search through a tree descrived by a `child` function
 - GenericBacktracker: (was readilly there)
   Depth first search through a tree descrived by a `child` function, with branch pruning, ...
 - TransitiveIdeal:
   Depth first search through a graph described by a `neighbours` relation
 - TransitiveIdealGraded:
   Breath first search through a graph described by a `neighbours` relation

Todo: the names are crappy and inconsistent, because they come from
different point of views. We need to find a good naming scheme!!! 

Do we want to emphasize the underlying graph/tree structure?  The
branch&bound aspect? The transitive closure of a relation point of
view?


---

Attachment


---

Comment by nthiery created at 2009-05-19 06:26:40

Changing status from new to assigned.


---

Comment by rbeezer created at 2009-05-21 05:05:47

Apply on top of main patch


---

Attachment

Passes tests:   ./sage -t devel/sage-backtrack/sage/combinat/

Reviewer patch adds two doctests, and some general cleanup, so apply on top of the main patch.

In the case of a search tree (not a graph), options for "leaves only" would be useful.  Then the generators could be checked for a first element when using a search tree for existence questions.

Building a single function to call these routines as variants might ease the question of names and interfaces.

Positive review.


---

Comment by mhansen created at 2009-06-01 00:02:26

Merged in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-06-01 00:02:26

Resolution: fixed
