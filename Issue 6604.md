# Issue 6604: Polish the use of iterators in C graphs

archive/issues_006604.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @kliem @tscrim\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6604\n\n",
    "created_at": "2009-07-23T15:56:41Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.5",
    "title": "Polish the use of iterators in C graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6604",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

CC:  @kliem @tscrim



Issue created by migration from https://trac.sagemath.org/ticket/6604





---

archive/issue_comments_053964.json:
```json
{
    "body": "I am right now watching a talk on closures in Cython, which are all but finished. Then, yield statements in Cython will soon follow! So don't work on this ticket for now...",
    "created_at": "2010-01-09T00:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6604#issuecomment-53964",
    "user": "https://github.com/rlmill"
}
```

I am right now watching a talk on closures in Cython, which are all but finished. Then, yield statements in Cython will soon follow! So don't work on this ticket for now...



---

archive/issue_comments_053965.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6604#issuecomment-53965",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_053966.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-12-03T17:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6604#issuecomment-53966",
    "user": "https://github.com/dcoudert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053967.json:
```json
{
    "body": "It seems there is little remaining to do for iterators in backends now, so let's do it.\n\nBefore\n\n```\nsage: a = DiGraph(graphs.CompleteGraph(100))\nsage: b = a._backend\nsage: %timeit L = list(b.iterator_nbrs(30))\n28.3 \u00b5s \u00b1 1.44 \u00b5s per loop (mean \u00b1 std. dev. of 7 runs, 10000 loops each)\n```\n\n\nAfter\n\n```\nsage: a = DiGraph(graphs.CompleteGraph(100))\nsage: b = a._backend\nsage: %timeit L = list(b.iterator_nbrs(30))\n18.6 \u00b5s \u00b1 698 ns per loop (mean \u00b1 std. dev. of 7 runs, 100000 loops each)\n```\n\n----\nNew commits:",
    "created_at": "2021-12-03T17:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6604#issuecomment-53967",
    "user": "https://github.com/dcoudert"
}
```

It seems there is little remaining to do for iterators in backends now, so let's do it.

Before

```
sage: a = DiGraph(graphs.CompleteGraph(100))
sage: b = a._backend
sage: %timeit L = list(b.iterator_nbrs(30))
28.3 µs ± 1.44 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```


After

```
sage: a = DiGraph(graphs.CompleteGraph(100))
sage: b = a._backend
sage: %timeit L = list(b.iterator_nbrs(30))
18.6 µs ± 698 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

----
New commits:



---

archive/issue_comments_053968.json:
```json
{
    "body": "That is quite a decent speedup and will likely have effects in other methods. Looks like some trivial failures due to slight differences in how the iteration is done:\n\n```\nsage -t --long --random-seed=210304412354021215508062896360889570175 src/sage/graphs/generic_graph.py\n**********************************************************************\nFile \"src/sage/graphs/generic_graph.py\", line 10654, in sage.graphs.generic_graph.GenericGraph.neighbor_iterator\nFailed example:\n    list(D.neighbor_iterator(0))\nExpected:\n    [1, 2, 3]\nGot:\n    [3, 1, 2]\n**********************************************************************\nFile \"src/sage/graphs/generic_graph.py\", line 17591, in sage.graphs.generic_graph.GenericGraph.?\nFailed example:\n    list(D.depth_first_search(1, ignore_direction=True, edges=True))\nExpected:\n    [(1, 4), (4, 5), (5, 6), (5, 2), (4, 3)]\nGot:\n    [(1, 3), (3, 4), (4, 5), (5, 6), (5, 2)]\n```\n\nThis one I am not sure if it is because of the random seed or this ticket:\n\n```\nsage -t --long --random-seed=210304412354021215508062896360889570175 src/sage/schemes/toric/sheaf/klyachko.py\n**********************************************************************\nFile \"src/sage/schemes/toric/sheaf/klyachko.py\", line 950, in sage.schemes.toric.sheaf.klyachko.KlyachkoBundle_class.random_deformation\nFailed example:\n    Vtilde.cohomology(dim=True, weight=(0,))\nExpected:\n    (1, 0)\nGot:\n    (0, 0)\n```\n\nin either case, it should be a trivial fix.",
    "created_at": "2021-12-04T04:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6604#issuecomment-53968",
    "user": "https://github.com/tscrim"
}
```

That is quite a decent speedup and will likely have effects in other methods. Looks like some trivial failures due to slight differences in how the iteration is done:

```
sage -t --long --random-seed=210304412354021215508062896360889570175 src/sage/graphs/generic_graph.py
**********************************************************************
File "src/sage/graphs/generic_graph.py", line 10654, in sage.graphs.generic_graph.GenericGraph.neighbor_iterator
Failed example:
    list(D.neighbor_iterator(0))
Expected:
    [1, 2, 3]
Got:
    [3, 1, 2]
**********************************************************************
File "src/sage/graphs/generic_graph.py", line 17591, in sage.graphs.generic_graph.GenericGraph.?
Failed example:
    list(D.depth_first_search(1, ignore_direction=True, edges=True))
Expected:
    [(1, 4), (4, 5), (5, 6), (5, 2), (4, 3)]
Got:
    [(1, 3), (3, 4), (4, 5), (5, 6), (5, 2)]
```

This one I am not sure if it is because of the random seed or this ticket:

```
sage -t --long --random-seed=210304412354021215508062896360889570175 src/sage/schemes/toric/sheaf/klyachko.py
**********************************************************************
File "src/sage/schemes/toric/sheaf/klyachko.py", line 950, in sage.schemes.toric.sheaf.klyachko.KlyachkoBundle_class.random_deformation
Failed example:
    Vtilde.cohomology(dim=True, weight=(0,))
Expected:
    (1, 0)
Got:
    (0, 0)
```

in either case, it should be a trivial fix.



---

archive/issue_comments_053969.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2021-12-04T10:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6604#issuecomment-53969",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_053970.json:
```json
{
    "body": "I fixed the doctests in `generic_graph.py`. \n\nI cannot reproduce the error in `klyachko.py`. It occurs in method `random_deformation`. Some help might be helpful here.",
    "created_at": "2021-12-04T10:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6604#issuecomment-53970",
    "user": "https://github.com/dcoudert"
}
```

I fixed the doctests in `generic_graph.py`. 

I cannot reproduce the error in `klyachko.py`. It occurs in method `random_deformation`. Some help might be helpful here.



---

archive/issue_comments_053971.json:
```json
{
    "body": "Actually, this random error in `klyachko.py` has already been reported in #32773.",
    "created_at": "2021-12-04T11:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6604#issuecomment-53971",
    "user": "https://github.com/dcoudert"
}
```

Actually, this random error in `klyachko.py` has already been reported in #32773.



---

archive/issue_comments_053972.json:
```json
{
    "body": "Thank you. LGTM.",
    "created_at": "2021-12-05T07:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6604#issuecomment-53972",
    "user": "https://github.com/tscrim"
}
```

Thank you. LGTM.



---

archive/issue_comments_053973.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-12-05T07:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6604#issuecomment-53973",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053974.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2021-12-12T15:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6604#issuecomment-53974",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
