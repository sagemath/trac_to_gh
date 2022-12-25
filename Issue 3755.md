# Issue 3755: [with patch; positive review] finance -- improve implementation of hurst exponent

archive/issues_003755.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis improves the examples, documentation, and implementation of the code in\nthe finance package for computing the Hurst exponent.  The main core improvement\nis that the algorithm is more sophisticated than the very naive one currently\nin Sage. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3755\n\n",
    "closed_at": "2008-08-06T01:04:19Z",
    "created_at": "2008-08-01T16:07:13Z",
    "labels": [
        "component: finance"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch; positive review] finance -- improve implementation of hurst exponent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3755",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This improves the examples, documentation, and implementation of the code in
the finance package for computing the Hurst exponent.  The main core improvement
is that the algorithm is more sophisticated than the very naive one currently
in Sage. 

Issue created by migration from https://trac.sagemath.org/ticket/3755





---

archive/issue_comments_026619.json:
```json
{
    "body": "Attachment [sage-3755.patch](tarball://root/attachments/some-uuid/ticket3755/sage-3755.patch) by @williamstein created at 2008-08-01 16:07:44",
    "created_at": "2008-08-01T16:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3755#issuecomment-26619",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3755.patch](tarball://root/attachments/some-uuid/ticket3755/sage-3755.patch) by @williamstein created at 2008-08-01 16:07:44



---

archive/issue_comments_026620.json:
```json
{
    "body": "REFEREE REPORT\n\n* Patch installs and passes doctests.\n\n```\nsage -t --optional devel/sage-review-finance/sage/finance/time_series.pyx\n         [15.7 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 15.7 seconds\n```\n\n* I found no coding errors or bugs while testing the modified functions in the notebook.",
    "created_at": "2008-08-02T01:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3755#issuecomment-26620",
    "user": "https://trac.sagemath.org/admin/accounts/users/brettnak"
}
```

REFEREE REPORT

* Patch installs and passes doctests.

```
sage -t --optional devel/sage-review-finance/sage/finance/time_series.pyx
         [15.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 15.7 seconds
```

* I found no coding errors or bugs while testing the modified functions in the notebook.



---

archive/issue_comments_026621.json:
```json
{
    "body": "So is this a positive review? It looks to me like it is.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-03T08:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3755#issuecomment-26621",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

So is this a positive review? It looks to me like it is.

Cheers,

Michael



---

archive/issue_comments_026622.json:
```json
{
    "body": "A positive review it is then.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-06T01:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3755#issuecomment-26622",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

A positive review it is then.

Cheers,

Michael



---

archive/issue_comments_026623.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-06T01:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3755#issuecomment-26623",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.alpha1



---

archive/issue_comments_026624.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-06T01:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3755#issuecomment-26624",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008607.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-06T01:04:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3755",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3755#event-8607"
}
```
