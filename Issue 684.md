# Issue 684: NTL integers do not coerce to SAGE integers

archive/issues_000684.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: x = ntl.ZZ(5)\nsage: x\n5\nsage: type(x)\n<type 'sage.libs.ntl.ntl.ntl_ZZ'>\nsage: Integer(x)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/dmharvey/<ipython console> in <module>()\n\n/home/dmharvey/integer.pyx in integer.Integer.__init__()\n\n<type 'exceptions.TypeError'>: unable to coerce element to an integer\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/684\n\n",
    "created_at": "2007-09-18T00:49:08Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "NTL integers do not coerce to SAGE integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/684",
    "user": "dmharvey"
}
```
Assignee: was


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

archive/issue_comments_003547.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-09-18T00:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/684#issuecomment-3547",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_003548.json:
```json
{
    "body": "This isn't a bug, it's a lack of something that would be nice being implemented (because we never got to it).\n\nIt's easy to do this:\n\n\n```\nsage: Integer(repr(ntl.ZZ_random(1000)))\n937\n```\n\n\nHowever, that uses base 10 strings.   It would be much better to get at the underlying\nNTL pointer to some GMP data.  I have no clue how to do that. \n\nWilliam",
    "created_at": "2007-09-18T00:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/684#issuecomment-3548",
    "user": "was"
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

archive/issue_comments_003549.json:
```json
{
    "body": "Changing assignee from was to dmharvey.",
    "created_at": "2007-09-28T04:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/684#issuecomment-3549",
    "user": "dmharvey"
}
```

Changing assignee from was to dmharvey.



---

archive/issue_comments_003550.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-28T04:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/684#issuecomment-3550",
    "user": "dmharvey"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003551.json:
```json
{
    "body": "This seems to work now:\n\n```\nmabshoff@sage:~$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.7, Release Date: 2007-10-15                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: x = ntl.ZZ(5)\nsage: x\n5\nsage: type(x)\n<type 'sage.libs.ntl.ntl_ZZ.ntl_ZZ'>\nsage: Integer(x)\n5\n```\n\nShould it be closed?\n\nCheers,\n\nMichael",
    "created_at": "2007-10-18T10:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/684#issuecomment-3551",
    "user": "mabshoff"
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

archive/issue_comments_003552.json:
```json
{
    "body": "Yep, this fully works now, and is implemented in ntl_wrap.cpp.  Nice.",
    "created_at": "2007-10-19T01:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/684#issuecomment-3552",
    "user": "was"
}
```

Yep, this fully works now, and is implemented in ntl_wrap.cpp.  Nice.



---

archive/issue_comments_003553.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-19T01:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/684#issuecomment-3553",
    "user": "was"
}
```

Resolution: fixed
