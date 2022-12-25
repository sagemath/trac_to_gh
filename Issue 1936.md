# Issue 1936: r-2.6.1.p11: sage-check fails on OSX 10.5

archive/issues_001936.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn bsd the following happens:\n\n```\n     missing link(s):  methods methods\n  zScript                           text    html    latex   example\n  zpackages                         text    html    latex   example\n  zutils                            text    html    latex\n  Signals                           text    html    latex\nmake[5]: *** [test-Examples-Base] Error 2\nmake[4]: *** [test-Examples] Error 2\nmake[3]: *** [test-all-basics] Error 1\nmake[2]: *** [check] Error 2\n*************************************\nError testing package ** r-2.6.1.p11 **\n*************************************\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1936\n\n",
    "created_at": "2008-01-26T10:41:50Z",
    "labels": [
        "component: packages",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "r-2.6.1.p11: sage-check fails on OSX 10.5",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1936",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

On bsd the following happens:

```
     missing link(s):  methods methods
  zScript                           text    html    latex   example
  zpackages                         text    html    latex   example
  zutils                            text    html    latex
  Signals                           text    html    latex
make[5]: *** [test-Examples-Base] Error 2
make[4]: *** [test-Examples] Error 2
make[3]: *** [test-all-basics] Error 1
make[2]: *** [check] Error 2
*************************************
Error testing package ** r-2.6.1.p11 **
*************************************
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1936





---

archive/issue_comments_012251.json:
```json
{
    "body": "Changing component from packages to sage-check.",
    "created_at": "2008-01-26T10:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1936#issuecomment-12251",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from packages to sage-check.



---

archive/issue_comments_012252.json:
```json
{
    "body": "The exact same issue happens on sage.math.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-26T15:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1936#issuecomment-12252",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The exact same issue happens on sage.math.

Cheers,

Michael



---

archive/issue_events_002092.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-02T07:01:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1936",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1936#event-2092"
}
```



---

archive/issue_comments_012253.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-02-02T07:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1936#issuecomment-12253",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: wontfix



---

archive/issue_comments_012254.json:
```json
{
    "body": "As of Sage 4.3.2 (see #6532), the R spkg has been upgraded to version 2.10.1. I'm closing this ticket as wontfix. If the testsuite of R 2.10.1 fails, one needs to open a ticket for that.",
    "created_at": "2010-02-02T07:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1936#issuecomment-12254",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

As of Sage 4.3.2 (see #6532), the R spkg has been upgraded to version 2.10.1. I'm closing this ticket as wontfix. If the testsuite of R 2.10.1 fails, one needs to open a ticket for that.
