# Issue 6889: Algebra of multivariate polynomials invariant under the action of a permutation group

Issue created by migration from https://trac.sagemath.org/ticket/6889

Original creator: nborie

Original creation time: 2009-09-04 14:06:25

Assignee: mhansen

CC:  sage-combinat tscrim

Keywords: invariants, permutation, group, ring, orbit, evaluation

First implementation of the Algebra of multivariate polynomials invariant under the action of a permutation group.

From a permutation group and a ring, the goal is to implement an algebra on which one can ask the primary invariants, a minimal generating set and (irreducible)secondary invariants... 

Using the category framework, we construct the abstract algebra of PermutationGroupInvariantRing and two representations of it : the graded algebra of multivariate polynomials view as combination of orbit sum of monomials (here #6812 is needed) and the polynomials view as vector evaluated in a collection of points.

This is a long run work but first implementation is comming in one or two months.


```
sage: mupad('package("Combinat")')                                    
sage: G = mupad.Dom.PermutationGroup(3, [[[1,2,3]]])
sage: I = mupad.Dom.PermutationGroupInvariantRing(mupad.Dom.Rational, G)
sage: I

Dom::PermutationGroupInvariantRing(Dom::Rational,Dom::PermutationGroup(3, [[[1, 2, 3]]]))

sage: I.minimalGeneratingSet()
         3 = [o([1, 1, 1]), o([2, 0, 1])],
         2 = [o([1, 1, 0])],
         1 = [o([1, 0, 0])]

sage: I.basisIndices.list(3)
         [[1, 1, 1], [2, 0, 1], [2, 1, 0], [3, 0, 0]]

sage: I.HilbertSeries()

                                  2            1
                           - ---------- - ----------
                                 3                 3
                             3 (z  - 1)   3 (z - 1)
```



depends on #6812 and #5891


---

Comment by nborie created at 2009-09-04 14:06:46

Changing assignee from mhansen to nborie.


---

Comment by nborie created at 2009-09-04 14:06:46

Changing status from new to assigned.


---

Comment by SimonKing created at 2018-09-11 16:03:34

Note that Sage (via Singular) can compute minimal generating sets for invariant rings of permutation groups. But the result is not implemented as a ring on its own (i.e., it is a method that returns a list of generators).
