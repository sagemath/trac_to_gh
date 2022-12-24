# Issue 5184: nonzero_positions is broken for sparse vectors

archive/issues_005184.json:
```json
{
    "body": "Assignee: was\n\nHere is an illustration:\n\n```\nsage: v = vector({1: 1, 3: -1})\nsage: w = vector({1: -1, 3: 0})\nsage: v\n(0, 1, 0, -1)\nsage: w\n(0, -1, 0, 0)\nsage: v+w\n(0, 0, 0, -1)\nsage: (v+w).nonzero_positions()\n[1, 3]\n```\n\n(I don't think this is related to #4648.  nonzero_positions for sums of sparse matrices seems to behave well in the one example I tried.)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5184\n\n",
    "created_at": "2009-02-05T03:07:15Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "nonzero_positions is broken for sparse vectors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5184",
    "user": "jhpalmieri"
}
```
Assignee: was

Here is an illustration:

```
sage: v = vector({1: 1, 3: -1})
sage: w = vector({1: -1, 3: 0})
sage: v
(0, 1, 0, -1)
sage: w
(0, -1, 0, 0)
sage: v+w
(0, 0, 0, -1)
sage: (v+w).nonzero_positions()
[1, 3]
```

(I don't think this is related to #4648.  nonzero_positions for sums of sparse matrices seems to behave well in the one example I tried.)



Issue created by migration from https://trac.sagemath.org/ticket/5184





---

archive/issue_comments_039749.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2009-02-05T03:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5184#issuecomment-39749",
    "user": "jhpalmieri"
}
```

Changing priority from minor to major.



---

archive/issue_comments_039750.json:
```json
{
    "body": "Maybe this is related:\n\n```\nsage: v = vector({1: 1, 3: -1})\nsage: w = vector({1: -1, 3: 1})\nsage: v+w\n(0, 0, 0, 0)\nsage: (v+w).is_zero()\nFalse\n```\n",
    "created_at": "2009-02-05T03:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5184#issuecomment-39750",
    "user": "jhpalmieri"
}
```

Maybe this is related:

```
sage: v = vector({1: 1, 3: -1})
sage: w = vector({1: -1, 3: 1})
sage: v+w
(0, 0, 0, 0)
sage: (v+w).is_zero()
False
```




---

archive/issue_comments_039751.json:
```json
{
    "body": "No, they're not related.  I'm putting the \"is_zero\" issue into #5185.  This ticket should only deal with nonzero_positions.",
    "created_at": "2009-02-05T04:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5184#issuecomment-39751",
    "user": "jhpalmieri"
}
```

No, they're not related.  I'm putting the "is_zero" issue into #5185.  This ticket should only deal with nonzero_positions.



---

archive/issue_comments_039752.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-17T21:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5184#issuecomment-39752",
    "user": "jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039753.json:
```json
{
    "body": "Changing assignee from was to jhpalmieri.",
    "created_at": "2009-02-17T21:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5184#issuecomment-39753",
    "user": "jhpalmieri"
}
```

Changing assignee from was to jhpalmieri.



---

archive/issue_comments_039754.json:
```json
{
    "body": "Here's a patch.  This doesn't actually change `nonzero_positions` (except for adding a doctest); instead it changes addition, subtraction, and scalar multiplication for sparse free module elements so that these only keep nonzero dictionary entries.",
    "created_at": "2009-02-17T21:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5184#issuecomment-39754",
    "user": "jhpalmieri"
}
```

Here's a patch.  This doesn't actually change `nonzero_positions` (except for adding a doctest); instead it changes addition, subtraction, and scalar multiplication for sparse free module elements so that these only keep nonzero dictionary entries.



---

archive/issue_comments_039755.json:
```json
{
    "body": "Attachment [5184.patch](tarball://root/attachments/some-uuid/ticket5184/5184.patch) by cwitty created at 2009-02-20 02:47:24\n\nInstead of tests like `if a != 0:`, it should use `if a:`.   The code is a little uglier and harder to understand, but it's much faster; these are approximations of the sorts of timing differences you would see:\n\n```\nsage: foo = QQbar(3)\nsage: timeit('bool(foo)')\n625 loops, best of 3: 1.24 \u00b5s per loop\nsage: timeit('foo != 0r')\n625 loops, best of 3: 100 \u00b5s per loop\nsage: foo = 3\nsage: timeit('bool(foo)')\n625 loops, best of 3: 286 ns per loop\nsage: timeit('foo != 0r')\n625 loops, best of 3: 4.2 \u00b5s per loop\n```\n\n\n(Also, in the places where you deleted \"A dense a sparse\", is it worth adding a note that says something like \"(This is true even if one is sparse and the other is dense.)\"?)",
    "created_at": "2009-02-20T02:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5184#issuecomment-39755",
    "user": "cwitty"
}
```

Attachment [5184.patch](tarball://root/attachments/some-uuid/ticket5184/5184.patch) by cwitty created at 2009-02-20 02:47:24

Instead of tests like `if a != 0:`, it should use `if a:`.   The code is a little uglier and harder to understand, but it's much faster; these are approximations of the sorts of timing differences you would see:

```
sage: foo = QQbar(3)
sage: timeit('bool(foo)')
625 loops, best of 3: 1.24 µs per loop
sage: timeit('foo != 0r')
625 loops, best of 3: 100 µs per loop
sage: foo = 3
sage: timeit('bool(foo)')
625 loops, best of 3: 286 ns per loop
sage: timeit('foo != 0r')
625 loops, best of 3: 4.2 µs per loop
```


(Also, in the places where you deleted "A dense a sparse", is it worth adding a note that says something like "(This is true even if one is sparse and the other is dense.)"?)



---

archive/issue_comments_039756.json:
```json
{
    "body": "only apply this one",
    "created_at": "2009-02-21T17:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5184#issuecomment-39756",
    "user": "jhpalmieri"
}
```

only apply this one



---

archive/issue_comments_039757.json:
```json
{
    "body": "Attachment [5184-new.patch](tarball://root/attachments/some-uuid/ticket5184/5184-new.patch) by jhpalmieri created at 2009-02-21 17:26:21\n\nI changed the tests from `a != 0` to `a`, and I put in a comment about sparse vs. dense -- actually, I put it in twice.  I had to rebase the patch, also (and it will probably have to be rebased after the ReST changes, too...).",
    "created_at": "2009-02-21T17:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5184#issuecomment-39757",
    "user": "jhpalmieri"
}
```

Attachment [5184-new.patch](tarball://root/attachments/some-uuid/ticket5184/5184-new.patch) by jhpalmieri created at 2009-02-21 17:26:21

I changed the tests from `a != 0` to `a`, and I put in a comment about sparse vs. dense -- actually, I put it in twice.  I had to rebase the patch, also (and it will probably have to be rebased after the ReST changes, too...).



---

archive/issue_comments_039758.json:
```json
{
    "body": "rebased against 3.4.alpha0; apply only this patch",
    "created_at": "2009-02-25T23:57:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5184#issuecomment-39758",
    "user": "jhpalmieri"
}
```

rebased against 3.4.alpha0; apply only this patch



---

archive/issue_comments_039759.json:
```json
{
    "body": "Attachment [5184-rebased.patch](tarball://root/attachments/some-uuid/ticket5184/5184-rebased.patch) by jhpalmieri created at 2009-02-25 23:58:29\n\nHere's a new patch, rebased against 3.4.alpha0.",
    "created_at": "2009-02-25T23:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5184#issuecomment-39759",
    "user": "jhpalmieri"
}
```

Attachment [5184-rebased.patch](tarball://root/attachments/some-uuid/ticket5184/5184-rebased.patch) by jhpalmieri created at 2009-02-25 23:58:29

Here's a new patch, rebased against 3.4.alpha0.



---

archive/issue_comments_039760.json:
```json
{
    "body": "Code looks good, doctests pass.  Positive review.  (Apply only 5184-rebased.patch .)",
    "created_at": "2009-02-26T00:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5184#issuecomment-39760",
    "user": "cwitty"
}
```

Code looks good, doctests pass.  Positive review.  (Apply only 5184-rebased.patch .)



---

archive/issue_comments_039761.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T21:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5184#issuecomment-39761",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039762.json:
```json
{
    "body": "Merged 5184-rebased.patch in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T21:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5184#issuecomment-39762",
    "user": "mabshoff"
}
```

Merged 5184-rebased.patch in Sage 3.4.rc0.

Cheers,

Michael
