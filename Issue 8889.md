# Issue 8889: multidim'l enumeration over variable length tuples

archive/issues_008889.json:
```json
{
    "body": "Assignee: jason\n\nCC:  sage-combinat\n\nI would like a function that takes\nInput: range (a list)\n       dim (a positive integer)\nOutput: a list of vectors or tuples of length dim including all combinations of range, but with replacement\n\nExample: generate the vertices of the centered unit cube [-1/2,1/2]^dim, where dim is variable\n\nThe functions in sage.misc.mrange almost do this, except it seems that they require having dim specified ahead of time, whereas I want a function that I can call in another function where dim will vary.\n\nThe function Arrangements in sage.combinat.permutation almost does what I want, but the list that the digits of the tuple are chosen from must be larger than dim, and Arrangements selects without replacement.  I can solve my example problem using Arrangements as follows:\n\n```\nprelist=[]\nfor i in range(2**d):\n    if i-2**(d-1) >= 0: prelist.append(1)\n        else: prelist.append(-1)\nlist = (1/2)*matrix(Arrangements(prelist,d).list())\n```\n\nbut it seems like there should be one specific function for this.\n\n(Combinations and Permutations are also related, but don't quite do what I want.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8889\n\n",
    "created_at": "2010-05-05T15:55:21Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "multidim'l enumeration over variable length tuples",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8889",
    "user": "ecurry"
}
```
Assignee: jason

CC:  sage-combinat

I would like a function that takes
Input: range (a list)
       dim (a positive integer)
Output: a list of vectors or tuples of length dim including all combinations of range, but with replacement

Example: generate the vertices of the centered unit cube [-1/2,1/2]^dim, where dim is variable

The functions in sage.misc.mrange almost do this, except it seems that they require having dim specified ahead of time, whereas I want a function that I can call in another function where dim will vary.

The function Arrangements in sage.combinat.permutation almost does what I want, but the list that the digits of the tuple are chosen from must be larger than dim, and Arrangements selects without replacement.  I can solve my example problem using Arrangements as follows:

```
prelist=[]
for i in range(2**d):
    if i-2**(d-1) >= 0: prelist.append(1)
        else: prelist.append(-1)
list = (1/2)*matrix(Arrangements(prelist,d).list())
```

but it seems like there should be one specific function for this.

(Combinations and Permutations are also related, but don't quite do what I want.)

Issue created by migration from https://trac.sagemath.org/ticket/8889





---

archive/issue_comments_081723.json:
```json
{
    "body": "Does this do what you want?\n\n\n```\nsage: l = [1/2, -1/2]\nsage: CartesianProduct(*([l]*3)).list()\n[[1/2, 1/2, 1/2], [1/2, 1/2, -1/2], [1/2, -1/2, 1/2], [1/2, -1/2, -1/2], [-1/2, 1/2, 1/2], [-1/2, 1/2, -1/2], [-1/2, -1/2, 1/2], [-1/2, -1/2, -1/2]]\nsage: CartesianProduct(*([l]*2)).list()\n[[1/2, 1/2], [1/2, -1/2], [-1/2, 1/2], [-1/2, -1/2]]\n```\n",
    "created_at": "2010-05-05T17:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8889#issuecomment-81723",
    "user": "mhansen"
}
```

Does this do what you want?


```
sage: l = [1/2, -1/2]
sage: CartesianProduct(*([l]*3)).list()
[[1/2, 1/2, 1/2], [1/2, 1/2, -1/2], [1/2, -1/2, 1/2], [1/2, -1/2, -1/2], [-1/2, 1/2, 1/2], [-1/2, 1/2, -1/2], [-1/2, -1/2, 1/2], [-1/2, -1/2, -1/2]]
sage: CartesianProduct(*([l]*2)).list()
[[1/2, 1/2], [1/2, -1/2], [-1/2, 1/2], [-1/2, -1/2]]
```




---

archive/issue_comments_081724.json:
```json
{
    "body": "It would be really nice if CartesianProduct supported a repeat keyword, like the python itertools product function does:\n\n\n```\n\nsage: import itertools                      \nsage: list(itertools.product([1/2,-1/2],repeat=3))\n[(1/2, 1/2, 1/2), (1/2, 1/2, -1/2), (1/2, -1/2, 1/2), (1/2, -1/2, -1/2), (-1/2, 1/2, 1/2), (-1/2, 1/2, -1/2), (-1/2, -1/2, 1/2), (-1/2, -1/2, -1/2)]\n```\n\n\nThat would make a common case (cartesian product of a set with itself) much easier to read.",
    "created_at": "2010-05-05T17:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8889#issuecomment-81724",
    "user": "jason"
}
```

It would be really nice if CartesianProduct supported a repeat keyword, like the python itertools product function does:


```

sage: import itertools                      
sage: list(itertools.product([1/2,-1/2],repeat=3))
[(1/2, 1/2, 1/2), (1/2, 1/2, -1/2), (1/2, -1/2, 1/2), (1/2, -1/2, -1/2), (-1/2, 1/2, 1/2), (-1/2, 1/2, -1/2), (-1/2, -1/2, 1/2), (-1/2, -1/2, -1/2)]
```


That would make a common case (cartesian product of a set with itself) much easier to read.



---

archive/issue_comments_081725.json:
```json
{
    "body": "That does!  Sorry for opening the unnecessary ticket then.\n-Eva\n\nReplying to [comment:1 mhansen]:\n> Does this do what you want?\n> \n> {{{\n> sage: l = [1/2, -1/2]\n> sage: CartesianProduct(*([l]*3)).list()\n> [[1/2, 1/2, 1/2], [1/2, 1/2, -1/2], [1/2, -1/2, 1/2], [1/2, -1/2, -1/2], [-1/2, 1/2, 1/2], [-1/2, 1/2, -1/2], [-1/2, -1/2, 1/2], [-1/2, -1/2, -1/2]]\n> sage: CartesianProduct(*([l]*2)).list()\n> [[1/2, 1/2], [1/2, -1/2], [-1/2, 1/2], [-1/2, -1/2]]\n> }}}",
    "created_at": "2010-05-05T17:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8889#issuecomment-81725",
    "user": "ecurry"
}
```

That does!  Sorry for opening the unnecessary ticket then.
-Eva

Replying to [comment:1 mhansen]:
> Does this do what you want?
> 
> {{{
> sage: l = [1/2, -1/2]
> sage: CartesianProduct(*([l]*3)).list()
> [[1/2, 1/2, 1/2], [1/2, 1/2, -1/2], [1/2, -1/2, 1/2], [1/2, -1/2, -1/2], [-1/2, 1/2, 1/2], [-1/2, 1/2, -1/2], [-1/2, -1/2, 1/2], [-1/2, -1/2, -1/2]]
> sage: CartesianProduct(*([l]*2)).list()
> [[1/2, 1/2], [1/2, -1/2], [-1/2, 1/2], [-1/2, -1/2]]
> }}}



---

archive/issue_comments_081726.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-05T18:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8889#issuecomment-81726",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081727.json:
```json
{
    "body": "Attachment [trac_8889.patch](tarball://root/attachments/some-uuid/ticket8889/trac_8889.patch) by mhansen created at 2010-05-05 18:53:57\n\nI've added a patch which adds the repeat keyword.",
    "created_at": "2010-05-05T18:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8889#issuecomment-81727",
    "user": "mhansen"
}
```

Attachment [trac_8889.patch](tarball://root/attachments/some-uuid/ticket8889/trac_8889.patch) by mhansen created at 2010-05-05 18:53:57

I've added a patch which adds the repeat keyword.



---

archive/issue_comments_081728.json:
```json
{
    "body": "Changing component from misc to combinatorics.",
    "created_at": "2010-05-05T18:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8889#issuecomment-81728",
    "user": "mhansen"
}
```

Changing component from misc to combinatorics.



---

archive/issue_comments_081729.json:
```json
{
    "body": "There is also Tuples in sage.combinat.tuple:\nhttp://sagemath.org/doc/reference/sage/combinat/tuple.html",
    "created_at": "2010-05-06T00:25:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8889#issuecomment-81729",
    "user": "ecurry"
}
```

There is also Tuples in sage.combinat.tuple:
http://sagemath.org/doc/reference/sage/combinat/tuple.html



---

archive/issue_comments_081730.json:
```json
{
    "body": "Replying to [comment:6 ecurry]:\n> There is also Tuples in sage.combinat.tuple:\n> http://sagemath.org/doc/reference/sage/combinat/tuple.html\n\nHeh, I should have known about that since it was likely I who wrote it :-)",
    "created_at": "2010-05-06T01:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8889#issuecomment-81730",
    "user": "mhansen"
}
```

Replying to [comment:6 ecurry]:
> There is also Tuples in sage.combinat.tuple:
> http://sagemath.org/doc/reference/sage/combinat/tuple.html

Heh, I should have known about that since it was likely I who wrote it :-)



---

archive/issue_comments_081731.json:
```json
{
    "body": "I'm going to close this as invalid for now.  If we have a discussion and decide we really want to repeat option to CartesianProduct, then we can add it.",
    "created_at": "2010-06-22T21:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8889#issuecomment-81731",
    "user": "mhansen"
}
```

I'm going to close this as invalid for now.  If we have a discussion and decide we really want to repeat option to CartesianProduct, then we can add it.



---

archive/issue_comments_081732.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-06-22T21:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8889#issuecomment-81732",
    "user": "mhansen"
}
```

Resolution: invalid



---

archive/issue_comments_081733.json:
```json
{
    "body": "Wait!  Are you closing it because no one has reviewed it?  If so, I'll review it.  I've been wanting the repeat keyword for a long time, as it just feels like a big mess when I want to take the cartesian product of a set with itself a number of times.  It's much easier with the repeat keyword, especially since python supports that in the python equivalent.",
    "created_at": "2010-06-23T00:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8889#issuecomment-81733",
    "user": "jason"
}
```

Wait!  Are you closing it because no one has reviewed it?  If so, I'll review it.  I've been wanting the repeat keyword for a long time, as it just feels like a big mess when I want to take the cartesian product of a set with itself a number of times.  It's much easier with the repeat keyword, especially since python supports that in the python equivalent.
