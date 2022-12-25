# Issue 2888: matrix slicing fails in degenerate cases

archive/issues_002888.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: slice\n\nThe following should return [] but it throws an exception instead:\n\n\n```\nsage: M = matrix(3, 4, range(12))\nsage: M[0:3, 2:2]\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/opt/sage-3.0.alpha2/devel/sage-main/<ipython console> in <module>()\n\n/opt/sage-3.0.alpha2/devel/sage-main/matrix0.pyx in sage.matrix.matrix0.Matrix.__getitem__()\n\n<type 'exceptions.ValueError'>: max() arg is an empty sequence\n```\n\n\nSame problem if I try M[0:0, 0:0].  This is an obstacle in doing #2616, since submatrix() does handle these cases properly.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2888\n\n",
    "created_at": "2008-04-12T00:47:43Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "matrix slicing fails in degenerate cases",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2888",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

Keywords: slice

The following should return [] but it throws an exception instead:


```
sage: M = matrix(3, 4, range(12))
sage: M[0:3, 2:2]
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/opt/sage-3.0.alpha2/devel/sage-main/<ipython console> in <module>()

/opt/sage-3.0.alpha2/devel/sage-main/matrix0.pyx in sage.matrix.matrix0.Matrix.__getitem__()

<type 'exceptions.ValueError'>: max() arg is an empty sequence
```


Same problem if I try M[0:0, 0:0].  This is an obstacle in doing #2616, since submatrix() does handle these cases properly.


Issue created by migration from https://trac.sagemath.org/ticket/2888





---

archive/issue_comments_019816.json:
```json
{
    "body": "Changing assignee from @williamstein to @dfdeshom.",
    "created_at": "2008-04-12T16:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2888#issuecomment-19816",
    "user": "https://github.com/dfdeshom"
}
```

Changing assignee from @williamstein to @dfdeshom.



---

archive/issue_comments_019817.json:
```json
{
    "body": "Attachment [2888.patch](tarball://root/attachments/some-uuid/ticket2888/2888.patch) by @dfdeshom created at 2008-04-13 03:08:37\n\npatch against alpha3",
    "created_at": "2008-04-13T03:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2888#issuecomment-19817",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [2888.patch](tarball://root/attachments/some-uuid/ticket2888/2888.patch) by @dfdeshom created at 2008-04-13 03:08:37

patch against alpha3



---

archive/issue_comments_019818.json:
```json
{
    "body": "A patch has been made against 3.0-alpha3",
    "created_at": "2008-04-13T03:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2888#issuecomment-19818",
    "user": "https://github.com/dfdeshom"
}
```

A patch has been made against 3.0-alpha3



---

archive/issue_comments_019819.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-04-13T03:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2888#issuecomment-19819",
    "user": "https://github.com/aghitza"
}
```

Looks good.



---

archive/issue_comments_019820.json:
```json
{
    "body": "Hi,\n\nthe patch doesn't apply cleanly against my merge tree:\n\n```\nsage-3.0.alpha4/devel/sage$ patch -p1 --dry-run < trac_2888.patch\npatching file sage/matrix/matrix0.pyx\nHunk #1 FAILED at 613.\nHunk #2 succeeded at 694 (offset 21 lines).\n1 out of 2 hunks FAILED -- saving rejects to file sage/matrix/matrix0.pyx.rej\n```\n\nThe first hunk are the added doctests, so it is easy enough to do. I won't mind if somebody beasts me to it.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T04:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2888#issuecomment-19820",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi,

the patch doesn't apply cleanly against my merge tree:

```
sage-3.0.alpha4/devel/sage$ patch -p1 --dry-run < trac_2888.patch
patching file sage/matrix/matrix0.pyx
Hunk #1 FAILED at 613.
Hunk #2 succeeded at 694 (offset 21 lines).
1 out of 2 hunks FAILED -- saving rejects to file sage/matrix/matrix0.pyx.rej
```

The first hunk are the added doctests, so it is easy enough to do. I won't mind if somebody beasts me to it.

Cheers,

Michael



---

archive/issue_comments_019821.json:
```json
{
    "body": "Attachment [2888-incoming-alpha4.patch](tarball://root/attachments/some-uuid/ticket2888/2888-incoming-alpha4.patch) by @dfdeshom created at 2008-04-13 04:37:02\n\npatch against upcoming alpha release",
    "created_at": "2008-04-13T04:37:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2888#issuecomment-19821",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [2888-incoming-alpha4.patch](tarball://root/attachments/some-uuid/ticket2888/2888-incoming-alpha4.patch) by @dfdeshom created at 2008-04-13 04:37:02

patch against upcoming alpha release



---

archive/issue_comments_019822.json:
```json
{
    "body": "Merged 2888-incoming-alpha4.patch in Sage 3.0.alpha4",
    "created_at": "2008-04-13T05:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2888#issuecomment-19822",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2888-incoming-alpha4.patch in Sage 3.0.alpha4



---

archive/issue_events_006609.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-13T05:09:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2888",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2888#event-6609"
}
```



---

archive/issue_comments_019823.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-13T05:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2888#issuecomment-19823",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
