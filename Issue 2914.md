# Issue 2914: integers are immutable but set_str breaks that -- having this function is a *major* bug.

archive/issues_002914.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is *terrible*\n\n\n```\nsage: n = 10\nsage: n.set_str('15')\nsage: n\n15\n```\n\n\nThe set_str function must be made __ or removed.\n\nLook at what evil can occur:\n\n```\nsage: a = matrix(ZZ,2,[1,2,3,4]); d = a.det(); d\n-2\nsage: d.set_str('10')\nsage: a.det()\n10\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2914\n\n",
    "created_at": "2008-04-14T04:01:26Z",
    "labels": [
        "Cygwin",
        "blocker",
        "bug"
    ],
    "title": "integers are immutable but set_str breaks that -- having this function is a *major* bug.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2914",
    "user": "was"
}
```
Assignee: mabshoff

This is *terrible*


```
sage: n = 10
sage: n.set_str('15')
sage: n
15
```


The set_str function must be made __ or removed.

Look at what evil can occur:

```
sage: a = matrix(ZZ,2,[1,2,3,4]); d = a.det(); d
-2
sage: d.set_str('10')
sage: a.det()
10
```


Issue created by migration from https://trac.sagemath.org/ticket/2914





---

archive/issue_comments_020068.json:
```json
{
    "body": "Changing component from Cygwin to basic arithmetic.",
    "created_at": "2008-04-14T04:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2914#issuecomment-20068",
    "user": "mabshoff"
}
```

Changing component from Cygwin to basic arithmetic.



---

archive/issue_comments_020069.json:
```json
{
    "body": "Changing assignee from mabshoff to somebody.",
    "created_at": "2008-04-14T04:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2914#issuecomment-20069",
    "user": "mabshoff"
}
```

Changing assignee from mabshoff to somebody.



---

archive/issue_comments_020070.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-14T04:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2914#issuecomment-20070",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_020071.json:
```json
{
    "body": "This looks good and should be applied.\n\nIn general I prefer single underscores to double -- strange things happen with double when inheritance comes in.  But in this situation, perhaps double is justified?\n\nIn the docstrings for the rational fixes, integer needs to be replaced by rational in a few places.",
    "created_at": "2008-04-14T06:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2914#issuecomment-20071",
    "user": "ncalexan"
}
```

This looks good and should be applied.

In general I prefer single underscores to double -- strange things happen with double when inheritance comes in.  But in this situation, perhaps double is justified?

In the docstrings for the rational fixes, integer needs to be replaced by rational in a few places.



---

archive/issue_comments_020072.json:
```json
{
    "body": "The fact that this is not touched *anywhere* else in the Sage codebase (or that there's a mistake) suggests this could just be deleted.  Why not just nuke the functionality, or make it only available from Cython?",
    "created_at": "2008-04-14T06:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2914#issuecomment-20072",
    "user": "ncalexan"
}
```

The fact that this is not touched *anywhere* else in the Sage codebase (or that there's a mistake) suggests this could just be deleted.  Why not just nuke the functionality, or make it only available from Cython?



---

archive/issue_comments_020073.json:
```json
{
    "body": "I've attached a new patch that just nukes the functionality, as Nick suggested. \nThis should be applied *instead* of the previously posted patch.\n\n -- William",
    "created_at": "2008-04-14T14:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2914#issuecomment-20073",
    "user": "was"
}
```

I've attached a new patch that just nukes the functionality, as Nick suggested. 
This should be applied *instead* of the previously posted patch.

 -- William



---

archive/issue_comments_020074.json:
```json
{
    "body": "apply this instead of previous version",
    "created_at": "2008-04-14T14:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2914#issuecomment-20074",
    "user": "was"
}
```

apply this instead of previous version



---

archive/issue_comments_020075.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-14T14:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2914#issuecomment-20075",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_020076.json:
```json
{
    "body": "I think this is better.",
    "created_at": "2008-04-14T15:37:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2914#issuecomment-20076",
    "user": "ncalexan"
}
```

I think this is better.



---

archive/issue_comments_020077.json:
```json
{
    "body": "Merged sage-2914_nuke_em.patch in Sage 3.0.alpha5",
    "created_at": "2008-04-14T17:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2914#issuecomment-20077",
    "user": "mabshoff"
}
```

Merged sage-2914_nuke_em.patch in Sage 3.0.alpha5



---

archive/issue_comments_020078.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-14T17:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2914#issuecomment-20078",
    "user": "mabshoff"
}
```

Resolution: fixed
