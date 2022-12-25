# Issue 684: NTL integers do not coerce to SAGE integers

archive/issues_000684.json:
```json
{
    "body": "Assignee: dmharvey\n\n```\nsage: x = ntl.ZZ(5)\nsage: x\n5\nsage: type(x)\n<type 'sage.libs.ntl.ntl.ntl_ZZ'>\nsage: Integer(x)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/dmharvey/<ipython console> in <module>()\n\n/home/dmharvey/integer.pyx in integer.Integer.__init__()\n\n<type 'exceptions.TypeError'>: unable to coerce element to an integer\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/684\n\n",
    "closed_at": "2007-10-19T01:10:20Z",
    "created_at": "2007-09-18T00:49:08Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "NTL integers do not coerce to SAGE integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/684",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: dmharvey

```
sage: x = ntl.ZZ(5)
sage: x
5
sage: type(x)
<type 'sage.libs.ntl.ntl.ntl_ZZ'>
sage: Integer(x)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/dmharvey/<ipython console> in <module>()

/home/dmharvey/integer.pyx in integer.Integer.__init__()

<type 'exceptions.TypeError'>: unable to coerce element to an integer
```


Issue created by migration from https://trac.sagemath.org/ticket/684





---

archive/issue_comments_003534.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-09-18T00:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/684#issuecomment-3534",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_003535.json:
```json
{
    "body": "This isn't a bug, it's a lack of something that would be nice being implemented (because we never got to it).\n\nIt's easy to do this:\n\n```\nsage: Integer(repr(ntl.ZZ_random(1000)))\n937\n```\n\nHowever, that uses base 10 strings.   It would be much better to get at the underlying\nNTL pointer to some GMP data.  I have no clue how to do that. \n\nWilliam",
    "created_at": "2007-09-18T00:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/684#issuecomment-3535",
    "user": "https://github.com/williamstein"
}
```

This isn't a bug, it's a lack of something that would be nice being implemented (because we never got to it).

It's easy to do this:

```
sage: Integer(repr(ntl.ZZ_random(1000)))
937
```

However, that uses base 10 strings.   It would be much better to get at the underlying
NTL pointer to some GMP data.  I have no clue how to do that. 

William



---

archive/issue_comments_003536.json:
```json
{
    "body": "Changing assignee from @williamstein to dmharvey.",
    "created_at": "2007-09-28T04:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/684#issuecomment-3536",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing assignee from @williamstein to dmharvey.



---

archive/issue_comments_003537.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-28T04:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/684#issuecomment-3537",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003538.json:
```json
{
    "body": "This seems to work now:\n\n```\nmabshoff@sage:~$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.7, Release Date: 2007-10-15                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: x = ntl.ZZ(5)\nsage: x\n5\nsage: type(x)\n<type 'sage.libs.ntl.ntl_ZZ.ntl_ZZ'>\nsage: Integer(x)\n5\n```\nShould it be closed?\n\nCheers,\n\nMichael",
    "created_at": "2007-10-18T10:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/684#issuecomment-3538",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This seems to work now:

```
mabshoff@sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.7, Release Date: 2007-10-15                       |
| Type notebook() for the GUI, and license() for information.        |
sage: x = ntl.ZZ(5)
sage: x
5
sage: type(x)
<type 'sage.libs.ntl.ntl_ZZ.ntl_ZZ'>
sage: Integer(x)
5
```
Should it be closed?

Cheers,

Michael



---

archive/issue_events_001819.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-18T10:03:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/684#event-1819"
}
```



---

archive/issue_comments_003539.json:
```json
{
    "body": "Yep, this fully works now, and is implemented in ntl_wrap.cpp.  Nice.",
    "created_at": "2007-10-19T01:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/684#issuecomment-3539",
    "user": "https://github.com/williamstein"
}
```

Yep, this fully works now, and is implemented in ntl_wrap.cpp.  Nice.



---

archive/issue_events_001820.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-19T01:10:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/684#event-1820"
}
```



---

archive/issue_comments_003540.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-19T01:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/684#issuecomment-3540",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
