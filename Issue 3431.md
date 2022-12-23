# Issue 3431: [with patch, needs review] QEPCAD interface

archive/issues_003431.json:
```json
{
    "body": "Assignee: was\n\nCC:  burcin\n\nKeywords: editor_cwitty\n\nThis provides an extensive Sage interface to QEPCAD.  (The patch was formerly posted on #772; we're moving it here to keep one issue per ticket.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3431\n\n",
    "created_at": "2008-06-15T21:46:21Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] QEPCAD interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3431",
    "user": "cwitty"
}
```
Assignee: was

CC:  burcin

Keywords: editor_cwitty

This provides an extensive Sage interface to QEPCAD.  (The patch was formerly posted on #772; we're moving it here to keep one issue per ticket.)

Issue created by migration from https://trac.sagemath.org/ticket/3431





---

archive/issue_comments_024185.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-15T22:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3431#issuecomment-24185",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_024186.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-06-15T22:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3431#issuecomment-24186",
    "user": "cwitty"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_024187.json:
```json
{
    "body": "This patch looks very nice and seems to behave as advertised.  There are some doctests that should be updated for qepcad 1.50 and also for the new interval printing notation in Sage 3.1.  Positive review pending fixing those things.",
    "created_at": "2008-08-16T21:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3431#issuecomment-24187",
    "user": "jason"
}
```

This patch looks very nice and seems to behave as advertised.  There are some doctests that should be updated for qepcad 1.50 and also for the new interval printing notation in Sage 3.1.  Positive review pending fixing those things.



---

archive/issue_comments_024188.json:
```json
{
    "body": "Attachment\n\nI've attached a patch to update the qepcad interface to deal with the newest interval printing, and to avoid locking the interface to one particular version of qepcad.\n\nNote that this patch depends on #3910 (without #3910, one doctest will fail).",
    "created_at": "2008-08-20T17:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3431#issuecomment-24188",
    "user": "cwitty"
}
```

Attachment

I've attached a patch to update the qepcad interface to deal with the newest interval printing, and to avoid locking the interface to one particular version of qepcad.

Note that this patch depends on #3910 (without #3910, one doctest will fail).



---

archive/issue_comments_024189.json:
```json
{
    "body": "With the newest qepcad spkg up at #772, all doctests in qepcad.py pass on sage 3.1.2alpha1.  It looks good to me.",
    "created_at": "2008-08-27T17:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3431#issuecomment-24189",
    "user": "jason"
}
```

With the newest qepcad spkg up at #772, all doctests in qepcad.py pass on sage 3.1.2alpha1.  It looks good to me.



---

archive/issue_comments_024190.json:
```json
{
    "body": "Merged both patches in Sage 3.1.2.alpha2",
    "created_at": "2008-08-28T02:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3431#issuecomment-24190",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.1.2.alpha2



---

archive/issue_comments_024191.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-28T02:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3431#issuecomment-24191",
    "user": "mabshoff"
}
```

Resolution: fixed
