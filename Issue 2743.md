# Issue 2743: make symbolic equalities and inequalities callable

archive/issues_002743.json:
```json
{
    "body": "Assignee: mabshoff\n\nIt would be nice if the following worked:\n\n\n```\nsage: f = x>3\nsage: f(2)\nFalse\nsage: f(4)\nTrue\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2743\n\n",
    "created_at": "2008-03-31T20:36:25Z",
    "labels": [
        "Cygwin",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "make symbolic equalities and inequalities callable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2743",
    "user": "@jasongrout"
}
```
Assignee: mabshoff

It would be nice if the following worked:


```
sage: f = x>3
sage: f(2)
False
sage: f(4)
True
```



Issue created by migration from https://trac.sagemath.org/ticket/2743





---

archive/issue_comments_018856.json:
```json
{
    "body": "Changing assignee from mabshoff to @williamstein.",
    "created_at": "2008-03-31T20:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2743#issuecomment-18856",
    "user": "@jasongrout"
}
```

Changing assignee from mabshoff to @williamstein.



---

archive/issue_comments_018857.json:
```json
{
    "body": "Changing component from Cygwin to calculus.",
    "created_at": "2008-03-31T20:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2743#issuecomment-18857",
    "user": "@jasongrout"
}
```

Changing component from Cygwin to calculus.



---

archive/issue_comments_018858.json:
```json
{
    "body": "original\n\n```\nsage: var('x y')\n(x, y)\nsage: eq=x<y\nsage: %timeit eq(x=2, y=3)\n10 loops, best of 3: 54.6 \u00b5s per loop\n```\n\n\n\nAfter\n\n```\nsage: var('x y')\n(x, y)\nsage: eq=x<y\nsage: %timeit eq(x=2, y=3)\n10 loops, best of 3: 78.9 ms per loop\n```\n",
    "created_at": "2008-04-02T06:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2743#issuecomment-18858",
    "user": "@jasongrout"
}
```

original

```
sage: var('x y')
(x, y)
sage: eq=x<y
sage: %timeit eq(x=2, y=3)
10 loops, best of 3: 54.6 µs per loop
```



After

```
sage: var('x y')
(x, y)
sage: eq=x<y
sage: %timeit eq(x=2, y=3)
10 loops, best of 3: 78.9 ms per loop
```




---

archive/issue_comments_018859.json:
```json
{
    "body": "Attachment [trac-2743-sym-eq-call.patch](tarball://root/attachments/some-uuid/ticket2743/trac-2743-sym-eq-call.patch) by @jasongrout created at 2008-04-02 07:09:30",
    "created_at": "2008-04-02T07:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2743#issuecomment-18859",
    "user": "@jasongrout"
}
```

Attachment [trac-2743-sym-eq-call.patch](tarball://root/attachments/some-uuid/ticket2743/trac-2743-sym-eq-call.patch) by @jasongrout created at 2008-04-02 07:09:30



---

archive/issue_comments_018860.json:
```json
{
    "body": "While there currently is callable functionality, it is broken.  See the doctests in the patch for several breakages of the current functionality.\n\nThis patch hands all the work off to symbolic matrices.  That makes it really slow, but it works.  The next thing to do would be to write the functionality directly into this class.",
    "created_at": "2008-04-02T07:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2743#issuecomment-18860",
    "user": "@jasongrout"
}
```

While there currently is callable functionality, it is broken.  See the doctests in the patch for several breakages of the current functionality.

This patch hands all the work off to symbolic matrices.  That makes it really slow, but it works.  The next thing to do would be to write the functionality directly into this class.



---

archive/issue_comments_018861.json:
```json
{
    "body": "Yep, this works well for me. It looks like the matrix is used to ensure that substitutions are to the correct variables, and that works well.",
    "created_at": "2008-04-06T06:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2743#issuecomment-18861",
    "user": "@robertwb"
}
```

Yep, this works well for me. It looks like the matrix is used to ensure that substitutions are to the correct variables, and that works well.



---

archive/issue_comments_018862.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T06:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2743#issuecomment-18862",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018863.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T06:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2743#issuecomment-18863",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2
