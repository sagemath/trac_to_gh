# Issue 2733: PARI in Debian has the mathnf bug

archive/issues_002733.json:
```json
{
    "body": "Assignee: @timabbott\n\nIs this bug important enough to bother Bill Allombert (the maintainer of PARI in Debian) to upgrade PARI in Debian?\n\nsage -t  devel/sage-main/sage/matrix/tests.py               **********************************************************************\nFile \"tests.py\", line 55:\n    sage: a.mathnf(1)[1][1,] == gp('[4, 2, 1, 0, 3, 1, 1, 0, 1, 1, 2, 2, 3, 3, 0, 0, 1, 3]')\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2733\n\n",
    "created_at": "2008-03-30T05:14:16Z",
    "labels": [
        "component: debian-package",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "PARI in Debian has the mathnf bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2733",
    "user": "https://github.com/timabbott"
}
```
Assignee: @timabbott

Is this bug important enough to bother Bill Allombert (the maintainer of PARI in Debian) to upgrade PARI in Debian?

sage -t  devel/sage-main/sage/matrix/tests.py               **********************************************************************
File "tests.py", line 55:
    sage: a.mathnf(1)[1][1,] == gp('[4, 2, 1, 0, 3, 1, 1, 0, 1, 1, 2, 2, 3, 3, 0, 0, 1, 3]')
Expected:
    True
Got:
    False
**********************************************************************


Issue created by migration from https://trac.sagemath.org/ticket/2733





---

archive/issue_events_002921.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-30T09:50:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2733",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2733#event-2921"
}
```



---

archive/issue_comments_018769.json:
```json
{
    "body": "This is not \"Sage Specific\": This is a packaging bug in Debian's pari.deb and should be filed as a bug report at the Debian bug tracker. See http://wiki.sagemath.org/TracGuidelines for the rules that up to now weren't written down.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-30T09:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2733#issuecomment-18769",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is not "Sage Specific": This is a packaging bug in Debian's pari.deb and should be filed as a bug report at the Debian bug tracker. See http://wiki.sagemath.org/TracGuidelines for the rules that up to now weren't written down.

Cheers,

Michael



---

archive/issue_comments_018770.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-03-30T09:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2733#issuecomment-18770",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix
