# Issue 2370: [with patch; with positve review] unable to coerce bool types to Sage integers

archive/issues_002370.json:
```json
{
    "body": "Assignee: @dfdeshom\n\n```\nsage: ZZ(True)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/tclemans/<ipython console> in <module>()\n\n/home/tclemans/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()\n\n<type 'exceptions.TypeError'>: unable to coerce element to an integer\nsage: ZZ(False)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/tclemans/<ipython console> in <module>()\n\n/home/tclemans/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()\n\n<type 'exceptions.TypeError'>: unable to coerce element to an integer\n\n--------------------------------------------\nAble to coerce bool types to Python integers\n--------------------------------------------\n\nsage: int(True)\n1\nsage: int(False)\n0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2370\n\n",
    "closed_at": "2008-03-05T06:27:36Z",
    "created_at": "2008-03-02T20:13:20Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch; with positve review] unable to coerce bool types to Sage integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2370",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: @dfdeshom

```
sage: ZZ(True)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/tclemans/<ipython console> in <module>()

/home/tclemans/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()

<type 'exceptions.TypeError'>: unable to coerce element to an integer
sage: ZZ(False)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/tclemans/<ipython console> in <module>()

/home/tclemans/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()

<type 'exceptions.TypeError'>: unable to coerce element to an integer

--------------------------------------------
Able to coerce bool types to Python integers
--------------------------------------------

sage: int(True)
1
sage: int(False)
0
```


Issue created by migration from https://trac.sagemath.org/ticket/2370





---

archive/issue_comments_015956.json:
```json
{
    "body": "Changing assignee from somebody to @dfdeshom.",
    "created_at": "2008-03-03T16:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2370#issuecomment-15956",
    "user": "https://github.com/dfdeshom"
}
```

Changing assignee from somebody to @dfdeshom.



---

archive/issue_comments_015957.json:
```json
{
    "body": "Added a small patch that check for bool types",
    "created_at": "2008-03-03T16:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2370#issuecomment-15957",
    "user": "https://github.com/dfdeshom"
}
```

Added a small patch that check for bool types



---

archive/issue_comments_015958.json:
```json
{
    "body": "The patch looks correct, but integer.pyx could certainly use some doctests. So somebody should at least add Timothy's trivial test case to the docstrings.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-05T06:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2370#issuecomment-15958",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch looks correct, but integer.pyx could certainly use some doctests. So somebody should at least add Timothy's trivial test case to the docstrings.

Cheers,

Michael



---

archive/issue_comments_015959.json:
```json
{
    "body": "Attachment [2370.patch](tarball://root/attachments/some-uuid/ticket2370/2370.patch) by @dfdeshom created at 2008-03-05 06:19:17\n\nReplying to [comment:2 mabshoff]:\n> The patch looks correct, but integer.pyx could certainly use some doctests.  \n\n\nDone.",
    "created_at": "2008-03-05T06:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2370#issuecomment-15959",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [2370.patch](tarball://root/attachments/some-uuid/ticket2370/2370.patch) by @dfdeshom created at 2008-03-05 06:19:17

Replying to [comment:2 mabshoff]:
> The patch looks correct, but integer.pyx could certainly use some doctests.  


Done.



---

archive/issue_comments_015960.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc2",
    "created_at": "2008-03-05T06:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2370#issuecomment-15960",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc2



---

archive/issue_events_005600.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-05T06:27:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2370",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2370#event-5600"
}
```



---

archive/issue_comments_015961.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-05T06:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2370#issuecomment-15961",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
