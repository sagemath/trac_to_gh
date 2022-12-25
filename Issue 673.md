# Issue 673: Solaris 10: rings/complex_double.pyx doctests failure: inf vs. Infinity

archive/issues_000673.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: Solaris 10, doctest, real double\n\n\n```\nsage -t  rings/real_double.pyx                              **********************************************************************\nFile \"real_double.pyx\", line 952:\n    sage: RDF(0).log()\nExpected:\n    -inf\nGot:\n    -Infinity\n**********************************************************************\nFile \"real_double.pyx\", line 954:\n    sage: RDF(-1).log()\nExpected:\n    nan\nGot:\n    -NaN\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/673\n\n",
    "created_at": "2007-09-17T00:34:27Z",
    "labels": [
        "component: packages",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Solaris 10: rings/complex_double.pyx doctests failure: inf vs. Infinity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/673",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

Keywords: Solaris 10, doctest, real double


```
sage -t  rings/real_double.pyx                              **********************************************************************
File "real_double.pyx", line 952:
    sage: RDF(0).log()
Expected:
    -inf
Got:
    -Infinity
**********************************************************************
File "real_double.pyx", line 954:
    sage: RDF(-1).log()
Expected:
    nan
Got:
    -NaN
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/673





---

archive/issue_comments_003471.json:
```json
{
    "body": "Changing assignee from @williamstein to failure.",
    "created_at": "2007-09-17T01:24:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/673#issuecomment-3471",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to failure.



---

archive/issue_comments_003472.json:
```json
{
    "body": "Changing component from packages to doctest.",
    "created_at": "2007-09-17T01:24:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/673#issuecomment-3472",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from packages to doctest.



---

archive/issue_comments_003473.json:
```json
{
    "body": "Some of this might have been fixed by #848.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-15T00:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/673#issuecomment-3473",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Some of this might have been fixed by #848.

Cheers,

Michael



---

archive/issue_events_001793.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-04-09T05:07:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/673",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/673#event-1793"
}
```



---

archive/issue_comments_003474.json:
```json
{
    "body": "Attachment [trac_673.patch](tarball://root/attachments/some-uuid/ticket673/trac_673.patch) by @williamstein created at 2009-04-09 05:29:10",
    "created_at": "2009-04-09T05:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/673#issuecomment-3474",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_673.patch](tarball://root/attachments/some-uuid/ticket673/trac_673.patch) by @williamstein created at 2009-04-09 05:29:10



---

archive/issue_comments_003475.json:
```json
{
    "body": "Attachment [trac_673_part2.patch](tarball://root/attachments/some-uuid/ticket673/trac_673_part2.patch) by mabshoff created at 2009-04-09 07:09:14\n\nPositive review for both patches. This also makes the printing of NaN and Infinity consistent with CC. At the same time it fixes three more doctesting issues on Solaris where the libc caused different printouts.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T07:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/673#issuecomment-3475",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_673_part2.patch](tarball://root/attachments/some-uuid/ticket673/trac_673_part2.patch) by mabshoff created at 2009-04-09 07:09:14

Positive review for both patches. This also makes the printing of NaN and Infinity consistent with CC. At the same time it fixes three more doctesting issues on Solaris where the libc caused different printouts.

Cheers,

Michael



---

archive/issue_events_001794.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-09T07:10:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/673",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/673#event-1794"
}
```



---

archive/issue_comments_003476.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T07:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/673#issuecomment-3476",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.4.1.rc2.

Cheers,

Michael



---

archive/issue_comments_003477.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-09T07:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/673#issuecomment-3477",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
