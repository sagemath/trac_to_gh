# Issue 3755: [with patch; needs review] finance -- improve implementation of hurst exponent

archive/issues_003755.json:
```json
{
    "body": "Assignee: was\n\nThis improves the examples, documentation, and implementation of the code in\nthe finance package for computing the Hurst exponent.  The main core improvement\nis that the algorithm is more sophisticated than the very naive one currently\nin Sage. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3755\n\n",
    "created_at": "2008-08-01T16:07:13Z",
    "labels": [
        "finance",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch; needs review] finance -- improve implementation of hurst exponent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3755",
    "user": "was"
}
```
Assignee: was

This improves the examples, documentation, and implementation of the code in
the finance package for computing the Hurst exponent.  The main core improvement
is that the algorithm is more sophisticated than the very naive one currently
in Sage. 

Issue created by migration from https://trac.sagemath.org/ticket/3755





---

archive/issue_comments_026676.json:
```json
{
    "body": "Attachment [sage-3755.patch](tarball://root/attachments/some-uuid/ticket3755/sage-3755.patch) by was created at 2008-08-01 16:07:44",
    "created_at": "2008-08-01T16:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3755#issuecomment-26676",
    "user": "was"
}
```

Attachment [sage-3755.patch](tarball://root/attachments/some-uuid/ticket3755/sage-3755.patch) by was created at 2008-08-01 16:07:44



---

archive/issue_comments_026677.json:
```json
{
    "body": "REFEREE REPORT\n\n* Patch installs and passes doctests.\n\n\n```\nsage -t --optional devel/sage-review-finance/sage/finance/time_series.pyx\n         [15.7 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 15.7 seconds\n```\n\n\n* I found no coding errors or bugs while testing the modified functions in the notebook.",
    "created_at": "2008-08-02T01:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3755#issuecomment-26677",
    "user": "brettnak"
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

archive/issue_comments_026678.json:
```json
{
    "body": "So is this a positive review? It looks to me like it is.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-03T08:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3755#issuecomment-26678",
    "user": "mabshoff"
}
```

So is this a positive review? It looks to me like it is.

Cheers,

Michael



---

archive/issue_comments_026679.json:
```json
{
    "body": "A positive review it is then.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-06T01:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3755#issuecomment-26679",
    "user": "mabshoff"
}
```

A positive review it is then.

Cheers,

Michael



---

archive/issue_comments_026680.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-06T01:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3755#issuecomment-26680",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha1



---

archive/issue_comments_026681.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-06T01:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3755#issuecomment-26681",
    "user": "mabshoff"
}
```

Resolution: fixed
