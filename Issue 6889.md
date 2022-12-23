# Issue 6889: Algebra of multivariate polynomials invariant under the action of a permutation group

archive/issues_006889.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat tscrim\n\nKeywords: invariants, permutation, group, ring, orbit, evaluation\n\nFirst implementation of the Algebra of multivariate polynomials invariant under the action of a permutation group.\n\nFrom a permutation group and a ring, the goal is to implement an algebra on which one can ask the primary invariants, a minimal generating set and (irreducible)secondary invariants... \n\nUsing the category framework, we construct the abstract algebra of PermutationGroupInvariantRing and two representations of it : the graded algebra of multivariate polynomials view as combination of orbit sum of monomials (here #6812 is needed) and the polynomials view as vector evaluated in a collection of points.\n\nThis is a long run work but first implementation is comming in one or two months.\n\n\n```\nsage: mupad('package(\"Combinat\")')                                    \nsage: G = mupad.Dom.PermutationGroup(3, [[[1,2,3]]])\nsage: I = mupad.Dom.PermutationGroupInvariantRing(mupad.Dom.Rational, G)\nsage: I\n\nDom::PermutationGroupInvariantRing(Dom::Rational,Dom::PermutationGroup(3, [[[1, 2, 3]]]))\n\nsage: I.minimalGeneratingSet()\n         3 = [o([1, 1, 1]), o([2, 0, 1])],\n         2 = [o([1, 1, 0])],\n         1 = [o([1, 0, 0])]\n\nsage: I.basisIndices.list(3)\n         [[1, 1, 1], [2, 0, 1], [2, 1, 0], [3, 0, 0]]\n\nsage: I.HilbertSeries()\n\n                                  2            1\n                           - ---------- - ----------\n                                 3                 3\n                             3 (z  - 1)   3 (z - 1)\n```\n\n\n\ndepends on #6812 and #5891\n\nIssue created by migration from https://trac.sagemath.org/ticket/6889\n\n",
    "created_at": "2009-09-04T14:06:25Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Algebra of multivariate polynomials invariant under the action of a permutation group",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6889",
    "user": "nborie"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/6889





---

archive/issue_comments_056932.json:
```json
{
    "body": "Changing assignee from mhansen to nborie.",
    "created_at": "2009-09-04T14:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6889#issuecomment-56932",
    "user": "nborie"
}
```

Changing assignee from mhansen to nborie.



---

archive/issue_comments_056933.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-04T14:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6889#issuecomment-56933",
    "user": "nborie"
}
```

Changing status from new to assigned.



---

archive/issue_comments_056934.json:
```json
{
    "body": "Note that Sage (via Singular) can compute minimal generating sets for invariant rings of permutation groups. But the result is not implemented as a ring on its own (i.e., it is a method that returns a list of generators).",
    "created_at": "2018-09-11T16:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6889#issuecomment-56934",
    "user": "SimonKing"
}
```

Note that Sage (via Singular) can compute minimal generating sets for invariant rings of permutation groups. But the result is not implemented as a ring on its own (i.e., it is a method that returns a list of generators).
