# Issue 4713: make an apply_map function for vectors

archive/issues_004713.json:
```json
{
    "body": "Assignee: @williamstein\n\nMatrices have the function; it would be handy for vectors to also have this utility function.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4713\n\n",
    "created_at": "2008-12-05T08:08:13Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "make an apply_map function for vectors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4713",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

Matrices have the function; it would be handy for vectors to also have this utility function.

Issue created by migration from https://trac.sagemath.org/ticket/4713





---

archive/issue_comments_035460.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2008-12-05T08:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4713#issuecomment-35460",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_035461.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-05T08:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4713#issuecomment-35461",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035462.json:
```json
{
    "body": "You could also do this in the first example:\n\n```\nsage: m = vector(ZZ, 9, range(9)) \nsage: k.<a> = GF(9) \nsage: m.apply_map(k)\n(0, 1, 2, 0, 1, 2, 0, 1, 2)\n```\n\n\nI think it would be nice to have a really simple first example, that requires much less knowledge of \"abstract algebra\".  Maybe the first example could be for engineers or something?\n\n```\nsage: m = vector([1,x,sin(x+1)])\nsage: m.apply_map(x^2)\n(1, x^2, sin(x + 1)^2)\nsage: m.apply_map(sin)\n(sin(1), sin(x), sin(sin(x + 1)))\n```\n",
    "created_at": "2008-12-06T23:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4713#issuecomment-35462",
    "user": "https://github.com/williamstein"
}
```

You could also do this in the first example:

```
sage: m = vector(ZZ, 9, range(9)) 
sage: k.<a> = GF(9) 
sage: m.apply_map(k)
(0, 1, 2, 0, 1, 2, 0, 1, 2)
```


I think it would be nice to have a really simple first example, that requires much less knowledge of "abstract algebra".  Maybe the first example could be for engineers or something?

```
sage: m = vector([1,x,sin(x+1)])
sage: m.apply_map(x^2)
(1, x^2, sin(x + 1)^2)
sage: m.apply_map(sin)
(sin(1), sin(x), sin(sin(x + 1)))
```




---

archive/issue_comments_035463.json:
```json
{
    "body": "By the way, definitely positive review pending adding the doctests suggested above.",
    "created_at": "2008-12-06T23:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4713#issuecomment-35463",
    "user": "https://github.com/williamstein"
}
```

By the way, definitely positive review pending adding the doctests suggested above.



---

archive/issue_comments_035464.json:
```json
{
    "body": "Attachment [vector_apply_map.patch](tarball://root/attachments/some-uuid/ticket4713/vector_apply_map.patch) by @jasongrout created at 2008-12-06 23:45:23\n\nupdated patch with the suggestions.  Accordingly, marking this positive review.",
    "created_at": "2008-12-06T23:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4713#issuecomment-35464",
    "user": "https://github.com/jasongrout"
}
```

Attachment [vector_apply_map.patch](tarball://root/attachments/some-uuid/ticket4713/vector_apply_map.patch) by @jasongrout created at 2008-12-06 23:45:23

updated patch with the suggestions.  Accordingly, marking this positive review.



---

archive/issue_comments_035465.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-07T09:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4713#issuecomment-35465",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035466.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha1",
    "created_at": "2008-12-07T09:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4713#issuecomment-35466",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha1
