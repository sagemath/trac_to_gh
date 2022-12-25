# Issue 6637: standardize the interface to TransitiveIdeal and friends

archive/issues_006637.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat @hivert\n\nKeywords: backtrack, enumerated set, transitive closure, days57\n\n1. Implement a single entry point for recursively enumerated sets:\n\n```\n     RecursivelyEnumeratedSet(seeds, successors, structure=..., enumeration=...)\n```\n\nwhere `structure` takes values in the set `[None, 'forest', 'graded', 'symmetric']` and `enumeration` takes values in the set `[None, 'depth', 'breadth', 'naive']`.\n\n2. Deprecate `TransitiveIdeal`, `TransitiveIdealGraded` and `SearchForest` as entry point.\n\n3. `TransitiveIdeal(succ, seeds)` keeps the same behavior as before and is now the same as `RecursivelyEnumeratedSet(seeds, succ, structure=None, enumeration='naive')`.\n\n4. `TransitiveIdealGraded(succ, seeds, max_depth)` keeps the same behavior as before and is now the same as `RecursivelyEnumeratedSet(seeds, succ, structure=None, enumeration='breadth', max_depth=max_depth)`.\n\nRemarks:\n\nA. For now the code of `SearchForest` is still in `sage/combinat/backtrack.py`. It should be moved in `sage/sets/recursively_enumerated_set.pyx`. See #16351.\n\nB. `TransitiveIdeal` and `TransitiveIealGraded` are used in the code of `sage/combinat`, `sage/categories` and `sage/groups` at least. These should be updated to use `RecursivelyEnumeratedSet` for speed improvements and also to avoid issues explained in C below. See #16352.\n\nC. Note that there were some issues with `TransitiveIdeal` and `TransitiveIdealGraded`, namely:\n\n   - Enumeration of `TransitiveIdeal` is claimed to be depth first search in the top level file `backtrack.py`, but in fact, it is neither breadth first neither depth first. It is what I call a naive search.\n   - Enumeration of `TransitiveIdealGraded` is indeed breadth first as claimed but it does not make use of the graded hypothesis at all because it remembers every generated elements.\n\nSee [my status report at SageDays57](http://www.liafa.univ-paris-diderot.fr/~labbe/blogue/2014/04/my-status-report-at-sage-days-57-recursivelyenumeratedset/) for more info.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6637\n\n",
    "closed_at": "2014-05-13T08:42:15Z",
    "created_at": "2009-07-27T12:10:47Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.3",
    "title": "standardize the interface to TransitiveIdeal and friends",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6637",
    "user": "https://github.com/nthiery"
}
```
Assignee: @mwhansen

CC:  sage-combinat @hivert

Keywords: backtrack, enumerated set, transitive closure, days57

1. Implement a single entry point for recursively enumerated sets:

```
     RecursivelyEnumeratedSet(seeds, successors, structure=..., enumeration=...)
```

where `structure` takes values in the set `[None, 'forest', 'graded', 'symmetric']` and `enumeration` takes values in the set `[None, 'depth', 'breadth', 'naive']`.

2. Deprecate `TransitiveIdeal`, `TransitiveIdealGraded` and `SearchForest` as entry point.

3. `TransitiveIdeal(succ, seeds)` keeps the same behavior as before and is now the same as `RecursivelyEnumeratedSet(seeds, succ, structure=None, enumeration='naive')`.

4. `TransitiveIdealGraded(succ, seeds, max_depth)` keeps the same behavior as before and is now the same as `RecursivelyEnumeratedSet(seeds, succ, structure=None, enumeration='breadth', max_depth=max_depth)`.

Remarks:

A. For now the code of `SearchForest` is still in `sage/combinat/backtrack.py`. It should be moved in `sage/sets/recursively_enumerated_set.pyx`. See #16351.

B. `TransitiveIdeal` and `TransitiveIealGraded` are used in the code of `sage/combinat`, `sage/categories` and `sage/groups` at least. These should be updated to use `RecursivelyEnumeratedSet` for speed improvements and also to avoid issues explained in C below. See #16352.

C. Note that there were some issues with `TransitiveIdeal` and `TransitiveIdealGraded`, namely:

   - Enumeration of `TransitiveIdeal` is claimed to be depth first search in the top level file `backtrack.py`, but in fact, it is neither breadth first neither depth first. It is what I call a naive search.
   - Enumeration of `TransitiveIdealGraded` is indeed breadth first as claimed but it does not make use of the graded hypothesis at all because it remembers every generated elements.

See [my status report at SageDays57](http://www.liafa.univ-paris-diderot.fr/~labbe/blogue/2014/04/my-status-report-at-sage-days-57-recursivelyenumeratedset/) for more info.

Issue created by migration from https://trac.sagemath.org/ticket/6637





---

archive/issue_comments_054275.json:
```json
{
    "body": "Here are some discussions related to this ticket:\n\n- [TransitiveIdeal vs TransitiveIdealGraded](https://groups.google.com/d/topic/sage-combinat-devel/5Be8FSY5w6I/discussion) on sage-combinat, Feb 2013.\n\n- [Comment of Nicolas Thi\u00e9ry at #14052](http://trac.sagemath.org/sage_trac/ticket/14052#comment:7), Feb 2013\n\n- [SearchForest and post_process...](https://groups.google.com/d/topic/sage-devel/97_5g0Pjuuw/discussion), on sage-devel, Oct. 2012.\n\n- [Sage modules and forking](https://groups.google.com/d/msg/sage-devel/5XHvEx89RlQ/Tb_QBWepC5YJ) on sage-devel, a comment by Florent Hivert, Oct. 2012.\n\n- #13580, patch available on sage-combinat : [trac_13580-map_reduce-fh.patch](http://combinat.sagemath.org/patches/file/7e81f6e12973/trac_13580-map_reduce-fh.patch)",
    "created_at": "2013-02-09T17:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54275",
    "user": "https://github.com/seblabbe"
}
```

Here are some discussions related to this ticket:

- [TransitiveIdeal vs TransitiveIdealGraded](https://groups.google.com/d/topic/sage-combinat-devel/5Be8FSY5w6I/discussion) on sage-combinat, Feb 2013.

- [Comment of Nicolas Thiéry at #14052](http://trac.sagemath.org/sage_trac/ticket/14052#comment:7), Feb 2013

- [SearchForest and post_process...](https://groups.google.com/d/topic/sage-devel/97_5g0Pjuuw/discussion), on sage-devel, Oct. 2012.

- [Sage modules and forking](https://groups.google.com/d/msg/sage-devel/5XHvEx89RlQ/Tb_QBWepC5YJ) on sage-devel, a comment by Florent Hivert, Oct. 2012.

- #13580, patch available on sage-combinat : [trac_13580-map_reduce-fh.patch](http://combinat.sagemath.org/patches/file/7e81f6e12973/trac_13580-map_reduce-fh.patch)



---

archive/issue_comments_054276.json:
```json
{
    "body": "In a tentative to find good choices for name and so on, here is how I see this.\n\n- Let X be a set.\n- Let R be a binary relation on X, that is R is a subset of the cartesian product of X times X.\n- Denote by xRy if x is R-related to y.\n\nNow\n\n- Let `seeds` be a subset of X.\n- Let `succ` be a callable python object `X -> 2^X` such that xRy if and only if y is in `succ(x)`.\n\nWe are interested in the subset S of X that can be generated from the `seeds` using the `succ` recursively. More precisely in the set \n\n S = {y : x = x1 R x2 R x3 R ... R xn = y and x in `seeds`}.\n\nMoreover, we are interested in the enumeration of S itself and we consider depth-first and breadth-first as different and both usefull.\n\nSuch a relation G = (X,R) can be seen as a directed graph. I think this remark is useful as it may provide some vocabulary. Indeed the set S is the connected components of the generators in the digraph G.\n\nI see some different cases :\n\n**1. We do not know anything more about the relation.** We need to save in memory all the `known` objects to avoid duplicates. This is what is currently done in `TransitiveIdeal` (depth-first search) and (curiously) in `TransitiveIdealGraded` (breadth-first search) also.\n\n**2. The directed graph S is a forest with given `seeds`.** Equivalently, one may say that S do not contain cycle (oriented or not). This is what is currently done in `SearchForest`.\n\n**3. The relation is graded.** By graded here I mean what I thought `TransitiveIdealGraded` was doing until I look more carefully at the doc and the code. More seriously, by graded I mean the following : for all (x1 in seeds) and (y1 in seeds), \n\n  if (x1 R x2 R ... R xn) and (y1 R y2 R ... R ym) and (xn=ym), then (n=m).\n\nThe relation is graded if all path from the origin to an element have the same length. In this case, we only need to save in memory the current level.\n\n**4. The relation is symmetric.** If the relation is symmetric, we only need to keep in memory the last two level of depth. This is what I needed and coded this week. And this is why I started to look more carefully at the code in `sage/combinat/backtrack.py`...\n\nThat is it for now!",
    "created_at": "2013-02-09T19:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54276",
    "user": "https://github.com/seblabbe"
}
```

In a tentative to find good choices for name and so on, here is how I see this.

- Let X be a set.
- Let R be a binary relation on X, that is R is a subset of the cartesian product of X times X.
- Denote by xRy if x is R-related to y.

Now

- Let `seeds` be a subset of X.
- Let `succ` be a callable python object `X -> 2^X` such that xRy if and only if y is in `succ(x)`.

We are interested in the subset S of X that can be generated from the `seeds` using the `succ` recursively. More precisely in the set 

 S = {y : x = x1 R x2 R x3 R ... R xn = y and x in `seeds`}.

Moreover, we are interested in the enumeration of S itself and we consider depth-first and breadth-first as different and both usefull.

Such a relation G = (X,R) can be seen as a directed graph. I think this remark is useful as it may provide some vocabulary. Indeed the set S is the connected components of the generators in the digraph G.

I see some different cases :

**1. We do not know anything more about the relation.** We need to save in memory all the `known` objects to avoid duplicates. This is what is currently done in `TransitiveIdeal` (depth-first search) and (curiously) in `TransitiveIdealGraded` (breadth-first search) also.

**2. The directed graph S is a forest with given `seeds`.** Equivalently, one may say that S do not contain cycle (oriented or not). This is what is currently done in `SearchForest`.

**3. The relation is graded.** By graded here I mean what I thought `TransitiveIdealGraded` was doing until I look more carefully at the doc and the code. More seriously, by graded I mean the following : for all (x1 in seeds) and (y1 in seeds), 

  if (x1 R x2 R ... R xn) and (y1 R y2 R ... R ym) and (xn=ym), then (n=m).

The relation is graded if all path from the origin to an element have the same length. In this case, we only need to save in memory the current level.

**4. The relation is symmetric.** If the relation is symmetric, we only need to keep in memory the last two level of depth. This is what I needed and coded this week. And this is why I started to look more carefully at the code in `sage/combinat/backtrack.py`...

That is it for now!



---

archive/issue_comments_054277.json:
```json
{
    "body": "I totally agree with the analysis!\n\nI don't know yet what would be the best name for the argument provided by the user to describe the relation. Behind the scene we are definitely modelling relation. But what the user provide is not the relation but a function that computes the (out) neighbors for this relation. If at the end of the day we choose \"TransitiveClosure\" as name for the main entry point, then \"neighbors\" would be consistent. If we go for \"RecursiveSet\" (or RecursiveEnumeratedSet or variant thereof) then \"operators\" would be consistent.\n\nCheers,\n                           Nicolas",
    "created_at": "2013-02-09T19:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54277",
    "user": "https://github.com/nthiery"
}
```

I totally agree with the analysis!

I don't know yet what would be the best name for the argument provided by the user to describe the relation. Behind the scene we are definitely modelling relation. But what the user provide is not the relation but a function that computes the (out) neighbors for this relation. If at the end of the day we choose "TransitiveClosure" as name for the main entry point, then "neighbors" would be consistent. If we go for "RecursiveSet" (or RecursiveEnumeratedSet or variant thereof) then "operators" would be consistent.

Cheers,
                           Nicolas



---

archive/issue_comments_054278.json:
```json
{
    "body": "I think `relation` would not be too bad for the name of the successor keyword and should be considered as well. In some sense, a binary relation is a function `f: X -> 2^X` and a function is a relation such that `|f(x)|=1` for all x.\n\nPossibilities for successor keyword :\n\n- `succ` : suitable for non symmetric relation, currently used in `TransitiveIdeal` and `TransitiveIdealGraded`\n- `successors`\n- `operators`\n- `neighbors` : suitable vocabulary for symmetric relation\n- `children` : suitable vocabulary for non symmetric relation, currently used in `SearchForest`.\n- `relatives` : suitable vocabulary for symmetric relation\n\nPossibilities for generators keyword :\n\n- `generators`\n- `gens`\n- `roots`\n- `seeds`",
    "created_at": "2013-02-09T20:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54278",
    "user": "https://github.com/seblabbe"
}
```

I think `relation` would not be too bad for the name of the successor keyword and should be considered as well. In some sense, a binary relation is a function `f: X -> 2^X` and a function is a relation such that `|f(x)|=1` for all x.

Possibilities for successor keyword :

- `succ` : suitable for non symmetric relation, currently used in `TransitiveIdeal` and `TransitiveIdealGraded`
- `successors`
- `operators`
- `neighbors` : suitable vocabulary for symmetric relation
- `children` : suitable vocabulary for non symmetric relation, currently used in `SearchForest`.
- `relatives` : suitable vocabulary for symmetric relation

Possibilities for generators keyword :

- `generators`
- `gens`
- `roots`
- `seeds`



---

archive/issue_comments_054279.json:
```json
{
    "body": "> If we go for RecursiveSet (or RecursiveEnumeratedSet or variant thereof) \n\n\nI like RecursiveSet. Maybe RecursiveEnumeratedSet is more related to what we do but is also longer.\n\nSome links:\n\n- http://en.wikipedia.org/wiki/Recursive_set\n- http://en.wikipedia.org/wiki/Recursively_enumerable_set",
    "created_at": "2013-02-09T20:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54279",
    "user": "https://github.com/seblabbe"
}
```

> If we go for RecursiveSet (or RecursiveEnumeratedSet or variant thereof) 


I like RecursiveSet. Maybe RecursiveEnumeratedSet is more related to what we do but is also longer.

Some links:

- http://en.wikipedia.org/wiki/Recursive_set
- http://en.wikipedia.org/wiki/Recursively_enumerable_set



---

archive/issue_comments_054280.json:
```json
{
    "body": "> I don't know yet what would be the best name for the argument provided by the user to describe the relation.\n\n\nFor the above 4 cases, I would suggest arguments like the following :\n\n```\nRecursiveSet(seeds, succ)\nRecursiveSet(seeds, succ, structure=\"forest\")\nRecursiveSet(seeds, succ, structure=\"graded\")\nRecursiveSet(seeds, succ, structure=\"symmetric\")\n```",
    "created_at": "2013-02-09T21:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54280",
    "user": "https://github.com/seblabbe"
}
```

> I don't know yet what would be the best name for the argument provided by the user to describe the relation.


For the above 4 cases, I would suggest arguments like the following :

```
RecursiveSet(seeds, succ)
RecursiveSet(seeds, succ, structure="forest")
RecursiveSet(seeds, succ, structure="graded")
RecursiveSet(seeds, succ, structure="symmetric")
```



---

archive/issue_comments_054281.json:
```json
{
    "body": "Attachment [trac_6637_recursive_set-sl.patch](tarball://root/attachments/some-uuid/ticket6637/trac_6637_recursive_set-sl.patch) by @seblabbe created at 2013-02-10 21:01:54",
    "created_at": "2013-02-10T21:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54281",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_6637_recursive_set-sl.patch](tarball://root/attachments/some-uuid/ticket6637/trac_6637_recursive_set-sl.patch) by @seblabbe created at 2013-02-10 21:01:54



---

archive/issue_comments_054282.json:
```json
{
    "body": "I just added a patch. It implements the `RecursiveSet_symmetric` class and creates factory called `RecursiveSet`. For now, `RecursiveSet` returns either an instance of `TransitiveIdeal`, `SearchForest` or `RecursiveSet_symmetric`. I started an empty class `RecursiveSet_graded`. See examples inside the docstring of the class `RecursiveSet`.\n\nIt is not ready for review, but comments are welcome to help me continue this work.\n\nActually, my questions are : \n\n- How should I merge `RecursiveSet` with `TransitiveIdeal` and `SearchForest`?\n- Do we like this interface?",
    "created_at": "2013-02-10T21:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54282",
    "user": "https://github.com/seblabbe"
}
```

I just added a patch. It implements the `RecursiveSet_symmetric` class and creates factory called `RecursiveSet`. For now, `RecursiveSet` returns either an instance of `TransitiveIdeal`, `SearchForest` or `RecursiveSet_symmetric`. I started an empty class `RecursiveSet_graded`. See examples inside the docstring of the class `RecursiveSet`.

It is not ready for review, but comments are welcome to help me continue this work.

Actually, my questions are : 

- How should I merge `RecursiveSet` with `TransitiveIdeal` and `SearchForest`?
- Do we like this interface?



---

archive/issue_events_015675.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6637#event-15675"
}
```



---

archive/issue_events_015676.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6637#event-15676"
}
```



---

archive/issue_events_015677.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6637#event-15677"
}
```



---

archive/issue_comments_054283.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-04-08T13:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54283",
    "user": "https://github.com/seblabbe"
}
```

New commits:



---

archive/issue_comments_054284.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-08T19:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54284",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_054285.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-09T10:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54285",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_054286.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-10T11:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54286",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_054287.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-10T12:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54287",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_054288.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-10T19:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54288",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_054289.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-11T00:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54289",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_054290.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-04-11T00:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54290",
    "user": "https://github.com/seblabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_054291.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-11T10:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54291",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_054292.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-13T20:22:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54292",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_054293.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-13T21:38:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54293",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_054294.json:
```json
{
    "body": "I think I will stop now. The next thing to do would be to move code from `sage/combinat/backtrack.py` to `sage/sets/recursively_enumerated_set.py` more precisely, the SearchForest code. But since it is mostly about moving code (does not change any functionality), I suggest to do it in a another ticket and review/merge this ticket now.\n\nNeeds review!\n\nS\u00e9bastien",
    "created_at": "2014-04-13T21:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54294",
    "user": "https://github.com/seblabbe"
}
```

I think I will stop now. The next thing to do would be to move code from `sage/combinat/backtrack.py` to `sage/sets/recursively_enumerated_set.py` more precisely, the SearchForest code. But since it is mostly about moving code (does not change any functionality), I suggest to do it in a another ticket and review/merge this ticket now.

Needs review!

Sébastien



---

archive/issue_comments_054295.json:
```json
{
    "body": "Changing keywords from \"backtrack, enumerated set, transitive closure\" to \"backtrack, enumerated set, transitive closure, days57\".",
    "created_at": "2014-04-15T19:40:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54295",
    "user": "https://github.com/seblabbe"
}
```

Changing keywords from "backtrack, enumerated set, transitive closure" to "backtrack, enumerated set, transitive closure, days57".



---

archive/issue_events_015678.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6637#event-15678"
}
```



---

archive/issue_events_015679.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6637#event-15679"
}
```



---

archive/issue_comments_054296.json:
```json
{
    "body": "your commits remove completely combinat/all.py ....",
    "created_at": "2014-05-10T14:59:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54296",
    "user": "https://github.com/fchapoton"
}
```

your commits remove completely combinat/all.py ....



---

archive/issue_comments_054297.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-05-10T14:59:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54297",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_054298.json:
```json
{
    "body": "Replying to [comment:28 chapoton]:\n> your commits remove completely combinat/all.py ....\n\n\nI see. It is strange because I can't see which commit did that... I will investigate.",
    "created_at": "2014-05-10T17:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54298",
    "user": "https://github.com/seblabbe"
}
```

Replying to [comment:28 chapoton]:
> your commits remove completely combinat/all.py ....


I see. It is strange because I can't see which commit did that... I will investigate.



---

archive/issue_comments_054299.json:
```json
{
    "body": "I believe that's an error with the trac plugin (I've seen that before).\n\nCan I make a feature request for this ticket, could we also cythonize this for speed (or at least make the new file a `.pyx` file)?",
    "created_at": "2014-05-10T17:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54299",
    "user": "https://github.com/tscrim"
}
```

I believe that's an error with the trac plugin (I've seen that before).

Can I make a feature request for this ticket, could we also cythonize this for speed (or at least make the new file a `.pyx` file)?



---

archive/issue_comments_054300.json:
```json
{
    "body": "Indeed, there is some gain. I did one example:\n\nPython:\n\n```\nsage: f = lambda a: [a-1,a+1]\nsage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')\nsage: it = iter(C)\nsage: %time L = [next(it) for _ in xrange(10^6)]\nCPU times: user 5.82 s, sys: 239 ms, total: 6.06 s\nWall time: 6.07 s\n```\n\nCython:\n\n```\nsage: f = lambda a: [a-1,a+1]\nsage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')\nsage: it = iter(C)\nsage: %time L = [next(it) for _ in xrange(10^6)]\nCPU times: user 4.47 s, sys: 408 ms, total: 4.88 s\nWall time: 4.89 s\n```",
    "created_at": "2014-05-10T21:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54300",
    "user": "https://github.com/seblabbe"
}
```

Indeed, there is some gain. I did one example:

Python:

```
sage: f = lambda a: [a-1,a+1]
sage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')
sage: it = iter(C)
sage: %time L = [next(it) for _ in xrange(10^6)]
CPU times: user 5.82 s, sys: 239 ms, total: 6.06 s
Wall time: 6.07 s
```

Cython:

```
sage: f = lambda a: [a-1,a+1]
sage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')
sage: it = iter(C)
sage: %time L = [next(it) for _ in xrange(10^6)]
CPU times: user 4.47 s, sys: 408 ms, total: 4.88 s
Wall time: 4.89 s
```



---

archive/issue_comments_054301.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-10T22:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54301",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_054302.json:
```json
{
    "body": "I keep the status of the ticket to needs work because I realized that some doctest were broken in the sage library. I am working on it.",
    "created_at": "2014-05-10T23:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54302",
    "user": "https://github.com/seblabbe"
}
```

I keep the status of the ticket to needs work because I realized that some doctest were broken in the sage library. I am working on it.



---

archive/issue_comments_054303.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-11T00:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54303",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_054304.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-05-11T00:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54304",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054305.json:
```json
{
    "body": "Some more speedup by doing some more cythonization. Before:\n\n```\nsage: f = lambda a: [a-1,a+1]\nsage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')\nsage: it = iter(C)\nsage: %time L = [next(it) for _ in xrange(10^6)]\nCPU times: user 9.68 s, sys: 147 ms, total: 9.83 s\nWall time: 9.81 s\n```\nWith my commit:\n\n```\nsage: f = lambda a: [a-1,a+1]\nsage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')\nsage: it = iter(C)\nsage: %time L = [next(it) for _ in xrange(10^6)]\nCPU times: user 8.02 s, sys: 103 ms, total: 8.13 s\nWall time: 8.15 s\n```\nI'm sure I haven't done the best cythonization job on this, but it works and all tests pass. If you're happy with my changes, then positive review.\n\n---\nNew commits:",
    "created_at": "2014-05-11T01:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54305",
    "user": "https://github.com/tscrim"
}
```

Some more speedup by doing some more cythonization. Before:

```
sage: f = lambda a: [a-1,a+1]
sage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')
sage: it = iter(C)
sage: %time L = [next(it) for _ in xrange(10^6)]
CPU times: user 9.68 s, sys: 147 ms, total: 9.83 s
Wall time: 9.81 s
```
With my commit:

```
sage: f = lambda a: [a-1,a+1]
sage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')
sage: it = iter(C)
sage: %time L = [next(it) for _ in xrange(10^6)]
CPU times: user 8.02 s, sys: 103 ms, total: 8.13 s
Wall time: 8.15 s
```
I'm sure I haven't done the best cythonization job on this, but it works and all tests pass. If you're happy with my changes, then positive review.

---
New commits:



---

archive/issue_comments_054306.json:
```json
{
    "body": "I do gain one more second with your improvements. Great!\n\n```\nsage: sage: f = lambda a: [a-1,a+1]                                         \nsage: sage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')\nsage: sage: it = iter(C)                                                    \nsage: sage: %time L = [next(it) for _ in xrange(10^6)]                      \nCPU times: user 3.49 s, sys: 246 ms, total: 3.74 s                          \nWall time: 3.79 s   \n```\n\nI do not like factory function in general and was happy to use for the first time the metaclass stuff. But apparently, it is not as efficient? Did you check if only removing the metaclass stuff was giving a speedup?",
    "created_at": "2014-05-11T09:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54306",
    "user": "https://github.com/seblabbe"
}
```

I do gain one more second with your improvements. Great!

```
sage: sage: f = lambda a: [a-1,a+1]                                         
sage: sage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')
sage: sage: it = iter(C)                                                    
sage: sage: %time L = [next(it) for _ in xrange(10^6)]                      
CPU times: user 3.49 s, sys: 246 ms, total: 3.74 s                          
Wall time: 3.79 s   
```

I do not like factory function in general and was happy to use for the first time the metaclass stuff. But apparently, it is not as efficient? Did you check if only removing the metaclass stuff was giving a speedup?



---

archive/issue_comments_054307.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-11T09:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54307",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_054308.json:
```json
{
    "body": "Travis, did you check that the doc was building fine? I am not able to, I get :\n\n```\n$ sage -docbuild reference/structure html\n   [structure] WARNING: intersphinx inventory '/Users/slabbe/Applications/sage-git/src/doc/output/html/en/reference/quivers/objects.inv' not fetchable due to <type 'exceptions.IOError'>: [Errno 2] No such file or directory: '/Users/slabbe/Applications/sage-git/src/doc/output/html/en/reference/quivers/objects.inv'\n   Error building the documentation.\n\n   Note: incremental documentation builds sometimes cause spurious\n   error messages. To be certain that these are real errors, run\n   \"make doc-clean\" first and try again.\n   Traceback (most recent call last):\n     File \"/Users/slabbe/Applications/sage-git/src/doc/common/builder.py\", line 1477, in <module>\n         getattr(get_builder(name), type)()\n           File \"/Users/slabbe/Applications/sage-git/src/doc/common/builder.py\", line 699, in _wrapper\n               getattr(DocBuilder, build_type)(self, *args, **kwds)\n                 File \"/Users/slabbe/Applications/sage-git/src/doc/common/builder.py\", line 94, in f\n                     execfile(sys.argv[0])\n                       File \"/Users/slabbe/Applications/sage-git/src/doc/common/custom-sphinx-build.py\", line 210, in <module>\n                           raise OSError(ERROR_MESSAGE)\n                           OSError: [structure] WARNING: intersphinx inventory '/Users/slabbe/Applications/sage-git/src/doc/output/html/en/reference/quivers/objects.inv' not fetchable due to <type 'exceptions.IOError'>: [Errno 2] No such file or directory: '/Users/slabbe/Applications/sage-git/src/doc/output/html/en/reference/quivers/objects.inv'\n```\n\nOnce, I may confirm the docs does build fine. I will set this to positive review.",
    "created_at": "2014-05-11T10:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54308",
    "user": "https://github.com/seblabbe"
}
```

Travis, did you check that the doc was building fine? I am not able to, I get :

```
$ sage -docbuild reference/structure html
   [structure] WARNING: intersphinx inventory '/Users/slabbe/Applications/sage-git/src/doc/output/html/en/reference/quivers/objects.inv' not fetchable due to <type 'exceptions.IOError'>: [Errno 2] No such file or directory: '/Users/slabbe/Applications/sage-git/src/doc/output/html/en/reference/quivers/objects.inv'
   Error building the documentation.

   Note: incremental documentation builds sometimes cause spurious
   error messages. To be certain that these are real errors, run
   "make doc-clean" first and try again.
   Traceback (most recent call last):
     File "/Users/slabbe/Applications/sage-git/src/doc/common/builder.py", line 1477, in <module>
         getattr(get_builder(name), type)()
           File "/Users/slabbe/Applications/sage-git/src/doc/common/builder.py", line 699, in _wrapper
               getattr(DocBuilder, build_type)(self, *args, **kwds)
                 File "/Users/slabbe/Applications/sage-git/src/doc/common/builder.py", line 94, in f
                     execfile(sys.argv[0])
                       File "/Users/slabbe/Applications/sage-git/src/doc/common/custom-sphinx-build.py", line 210, in <module>
                           raise OSError(ERROR_MESSAGE)
                           OSError: [structure] WARNING: intersphinx inventory '/Users/slabbe/Applications/sage-git/src/doc/output/html/en/reference/quivers/objects.inv' not fetchable due to <type 'exceptions.IOError'>: [Errno 2] No such file or directory: '/Users/slabbe/Applications/sage-git/src/doc/output/html/en/reference/quivers/objects.inv'
```

Once, I may confirm the docs does build fine. I will set this to positive review.



---

archive/issue_comments_054309.json:
```json
{
    "body": "`make doc-clean` fixed the error. Doc builds fine.",
    "created_at": "2014-05-11T10:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54309",
    "user": "https://github.com/seblabbe"
}
```

`make doc-clean` fixed the error. Doc builds fine.



---

archive/issue_comments_054310.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-05-11T10:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54310",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054311.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2014-05-11T14:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54311",
    "user": "https://github.com/nthiery"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_054312.json:
```json
{
    "body": "Sebastien wants to double check the Metaclass thingy.",
    "created_at": "2014-05-11T14:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54312",
    "user": "https://github.com/nthiery"
}
```

Sebastien wants to double check the Metaclass thingy.



---

archive/issue_comments_054313.json:
```json
{
    "body": "As I recall, metaclasses are not supported in extension classes by Cython. The metaclass should not change the speed since it's only called/used upon object creation.",
    "created_at": "2014-05-11T15:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54313",
    "user": "https://github.com/tscrim"
}
```

As I recall, metaclasses are not supported in extension classes by Cython. The metaclass should not change the speed since it's only called/used upon object creation.



---

archive/issue_comments_054314.json:
```json
{
    "body": "Also FTR, I liked your usage of the metaclass (and I can't check the doc until I get my docbuilder to actually work again... `:/` ).",
    "created_at": "2014-05-11T21:31:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54314",
    "user": "https://github.com/tscrim"
}
```

Also FTR, I liked your usage of the metaclass (and I can't check the doc until I get my docbuilder to actually work again... `:/` ).



---

archive/issue_comments_054315.json:
```json
{
    "body": "If you agree Travis, I will try to put the metaclass use back in. Also, maybe Florent can say a word about it. He coached me on how to implement it.",
    "created_at": "2014-05-12T08:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54315",
    "user": "https://github.com/seblabbe"
}
```

If you agree Travis, I will try to put the metaclass use back in. Also, maybe Florent can say a word about it. He coached me on how to implement it.



---

archive/issue_comments_054316.json:
```json
{
    "body": "Replying to [comment:45 tscrim]:\n> As I recall, metaclasses are not supported in extension classes by Cython. The metaclass should not change the speed since it's only called/used upon object creation.\n\n\nOk, now I see what you mean. When the class is `cdef`, then the `__classcall_private__` do not get called instead of the `__init__`:\n\n```\nsage: f = lambda a: [a-1,a+1]\nsage: RecursivelyEnumeratedSet([0], f)\nA recursively enumerated set (depth first search)\nsage: RecursivelyEnumeratedSet([0], f, structure='symmetric')\nTraceback (most recent call last):\n...\nTypeError: __init__() got an unexpected keyword argument 'structure'\n```\n\nI also saw in the [doc](http://www.sagemath.org/doc/reference/misc/sage/misc/classcall_metaclass.html) that: \"*For a Cython class (not cdef since they doesn\u2019t allows metaclasses)*\"",
    "created_at": "2014-05-12T09:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54316",
    "user": "https://github.com/seblabbe"
}
```

Replying to [comment:45 tscrim]:
> As I recall, metaclasses are not supported in extension classes by Cython. The metaclass should not change the speed since it's only called/used upon object creation.


Ok, now I see what you mean. When the class is `cdef`, then the `__classcall_private__` do not get called instead of the `__init__`:

```
sage: f = lambda a: [a-1,a+1]
sage: RecursivelyEnumeratedSet([0], f)
A recursively enumerated set (depth first search)
sage: RecursivelyEnumeratedSet([0], f, structure='symmetric')
Traceback (most recent call last):
...
TypeError: __init__() got an unexpected keyword argument 'structure'
```

I also saw in the [doc](http://www.sagemath.org/doc/reference/misc/sage/misc/classcall_metaclass.html) that: "*For a Cython class (not cdef since they doesn’t allows metaclasses)*"



---

archive/issue_comments_054317.json:
```json
{
    "body": "I pushed on my [branch](http://git.sagemath.org/sage.git/diff/?id2=fa885d90d609c8311d8fa52deac1340cd558b5a9&id=38a82f820d5314890a34d0707851c40ea5eb5b67) a [commit](http://git.sagemath.org/sage.git/commit/?h=u/slabbe/6637&id=38a82f820d5314890a34d0707851c40ea5eb5b67) using metaclass. In the end, I had to create a factory def outside of the class...",
    "created_at": "2014-05-12T09:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54317",
    "user": "https://github.com/seblabbe"
}
```

I pushed on my [branch](http://git.sagemath.org/sage.git/diff/?id2=fa885d90d609c8311d8fa52deac1340cd558b5a9&id=38a82f820d5314890a34d0707851c40ea5eb5b67) a [commit](http://git.sagemath.org/sage.git/commit/?h=u/slabbe/6637&id=38a82f820d5314890a34d0707851c40ea5eb5b67) using metaclass. In the end, I had to create a factory def outside of the class...



---

archive/issue_comments_054318.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-12T14:59:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54318",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_054319.json:
```json
{
    "body": "Looking at your commit, I don't see any benefit in using the metaclass. However I'm not opposed to the renaming, so I've just pushed that.",
    "created_at": "2014-05-12T15:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54319",
    "user": "https://github.com/tscrim"
}
```

Looking at your commit, I don't see any benefit in using the metaclass. However I'm not opposed to the renaming, so I've just pushed that.



---

archive/issue_comments_054320.json:
```json
{
    "body": "Replying to [comment:51 tscrim]:\n> Looking at your commit, I don't see any benefit in using the metaclass. \n\n\nYes exactly. I needed to play with it to understand what you meant.\n\n> However I'm not opposed to the renaming, so I've just pushed that.\n\n\nWell, the renaming was just an easy way for me to check that `sage -t recursively_enumerated_set.pyx` was ok after I realised that `__classcall_private__` was ignored by `cdef` class. It was not a suggestion, but it would not be the first renamed function:\n\n```\nsage: import_statements(sum)\nfrom sage.misc.functional import symbolic_sum\n```\n\nSo, we go with commit \u200bdd72bfc instead of \u200b3191690 ?",
    "created_at": "2014-05-12T20:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54320",
    "user": "https://github.com/seblabbe"
}
```

Replying to [comment:51 tscrim]:
> Looking at your commit, I don't see any benefit in using the metaclass. 


Yes exactly. I needed to play with it to understand what you meant.

> However I'm not opposed to the renaming, so I've just pushed that.


Well, the renaming was just an easy way for me to check that `sage -t recursively_enumerated_set.pyx` was ok after I realised that `__classcall_private__` was ignored by `cdef` class. It was not a suggestion, but it would not be the first renamed function:

```
sage: import_statements(sum)
from sage.misc.functional import symbolic_sum
```

So, we go with commit ​dd72bfc instead of ​3191690 ?



---

archive/issue_comments_054321.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2014-05-12T20:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54321",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_054322.json:
```json
{
    "body": "If that's okay with you.",
    "created_at": "2014-05-12T20:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54322",
    "user": "https://github.com/tscrim"
}
```

If that's okay with you.



---

archive/issue_comments_054323.json:
```json
{
    "body": "Replying to [comment:53 tscrim]:\n> If that's okay with you.\n\n\nThe more I think about it, the less I like it. I think \u200bdd72bfc can be confusing for someone looking at the file for the first time. Until that person looks at the file sage/sets/all.py he will not understand how the `__init__` handles the structure argument. And the key will always be hidden in some other file `sage/sets/all.py`. I suggest we go with your initial factory function. More precisely with commit \u200b3191690. Do you agree?\n\nIf so, I do not know what should we do then (git question). Should we update the commit field? Should we reset the HEAD of the branch? Should we create a new branch pointing to the commit?",
    "created_at": "2014-05-12T20:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54323",
    "user": "https://github.com/seblabbe"
}
```

Replying to [comment:53 tscrim]:
> If that's okay with you.


The more I think about it, the less I like it. I think ​dd72bfc can be confusing for someone looking at the file for the first time. Until that person looks at the file sage/sets/all.py he will not understand how the `__init__` handles the structure argument. And the key will always be hidden in some other file `sage/sets/all.py`. I suggest we go with your initial factory function. More precisely with commit ​3191690. Do you agree?

If so, I do not know what should we do then (git question). Should we update the commit field? Should we reset the HEAD of the branch? Should we create a new branch pointing to the commit?



---

archive/issue_comments_054324.json:
```json
{
    "body": "Good point. What we'll do is create a new branch which just points to the old commit (afterwards we can delete our old branches). Do you want to do this or should I?",
    "created_at": "2014-05-12T20:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54324",
    "user": "https://github.com/tscrim"
}
```

Good point. What we'll do is create a new branch which just points to the old commit (afterwards we can delete our old branches). Do you want to do this or should I?



---

archive/issue_comments_054325.json:
```json
{
    "body": "Let me try.",
    "created_at": "2014-05-12T20:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54325",
    "user": "https://github.com/seblabbe"
}
```

Let me try.



---

archive/issue_comments_054326.json:
```json
{
    "body": "The following did the trick:\n\n```\ngit checkout 3191690 -b t/6637a\n```",
    "created_at": "2014-05-12T21:10:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54326",
    "user": "https://github.com/seblabbe"
}
```

The following did the trick:

```
git checkout 3191690 -b t/6637a
```



---

archive/issue_comments_054327.json:
```json
{
    "body": "Then let's get this in. Thanks S\u00e9bastien.",
    "created_at": "2014-05-12T21:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54327",
    "user": "https://github.com/tscrim"
}
```

Then let's get this in. Thanks Sébastien.



---

archive/issue_comments_054328.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-05-12T21:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54328",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054329.json:
```json
{
    "body": "Thanks for the review and cython improvements!",
    "created_at": "2014-05-12T21:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54329",
    "user": "https://github.com/seblabbe"
}
```

Thanks for the review and cython improvements!



---

archive/issue_comments_054330.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-05-13T08:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6637#issuecomment-54330",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_015680.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-05-13T08:42:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6637",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6637#event-15680"
}
```
