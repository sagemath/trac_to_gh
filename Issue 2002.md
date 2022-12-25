# Issue 2002: creating a fresh new notebook in sage-2.10.1.rc3 is broken

archive/issues_002002.json:
```json
{
    "body": "Assignee: boothby\n\n```\n[02:20am] william_stein: the notebook doesn't even work in rc3!!\n[02:21am] william_stein: sage: notebook(address=\"sage.math.washington.edu\", port=8389, directory=\"notebook\")\n[02:21am] william_stein: ...\n[02:21am] william_stein: <type 'exceptions.AttributeError'>: 'Notebook' object has no attribute 'set_prettyprint'\n[02:21am] william_stein: This is what happens when making a NEW NOTEBOOK not loading an existing one.\n[02:21am] william_stein: I'm glad I caught this!!\n[02:21am] william_stein: trac ticket coming up\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2002\n\n",
    "created_at": "2008-01-31T07:25:06Z",
    "labels": [
        "component: notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "creating a fresh new notebook in sage-2.10.1.rc3 is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2002",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

```
[02:20am] william_stein: the notebook doesn't even work in rc3!!
[02:21am] william_stein: sage: notebook(address="sage.math.washington.edu", port=8389, directory="notebook")
[02:21am] william_stein: ...
[02:21am] william_stein: <type 'exceptions.AttributeError'>: 'Notebook' object has no attribute 'set_prettyprint'
[02:21am] william_stein: This is what happens when making a NEW NOTEBOOK not loading an existing one.
[02:21am] william_stein: I'm glad I caught this!!
[02:21am] william_stein: trac ticket coming up
```



Issue created by migration from https://trac.sagemath.org/ticket/2002





---

archive/issue_comments_012922.json:
```json
{
    "body": "I think the attached fixes the issue, but I'm not sure how to create a new notebook, so I'm not sure how to test it.",
    "created_at": "2008-01-31T21:00:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2002#issuecomment-12922",
    "user": "https://github.com/jasongrout"
}
```

I think the attached fixes the issue, but I'm not sure how to create a new notebook, so I'm not sure how to test it.



---

archive/issue_comments_012923.json:
```json
{
    "body": "(which probably explains why this was never tested when submitting the original patch.  sorry!)",
    "created_at": "2008-01-31T21:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2002#issuecomment-12923",
    "user": "https://github.com/jasongrout"
}
```

(which probably explains why this was never tested when submitting the original patch.  sorry!)



---

archive/issue_comments_012924.json:
```json
{
    "body": "Attachment [pretty-print-notebook.patch](tarball://root/attachments/some-uuid/ticket2002/pretty-print-notebook.patch) by @jasongrout created at 2008-01-31 21:07:43",
    "created_at": "2008-01-31T21:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2002#issuecomment-12924",
    "user": "https://github.com/jasongrout"
}
```

Attachment [pretty-print-notebook.patch](tarball://root/attachments/some-uuid/ticket2002/pretty-print-notebook.patch) by @jasongrout created at 2008-01-31 21:07:43



---

archive/issue_comments_012925.json:
```json
{
    "body": "The attached patch also standardizes on \"pretty_print\" instead of \"prettyprint\".  The previous code had a mixture of the two spellings.",
    "created_at": "2008-01-31T21:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2002#issuecomment-12925",
    "user": "https://github.com/jasongrout"
}
```

The attached patch also standardizes on "pretty_print" instead of "prettyprint".  The previous code had a mixture of the two spellings.



---

archive/issue_comments_012926.json:
```json
{
    "body": "The issue has been solved, but I do believe that somebody else ought to double check this.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-01T05:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2002#issuecomment-12926",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue has been solved, but I do believe that somebody else ought to double check this.

Cheers,

Michael



---

archive/issue_comments_012927.json:
```json
{
    "body": "The issue appears to have been solved to me as well.",
    "created_at": "2008-02-01T06:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2002#issuecomment-12927",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

The issue appears to have been solved to me as well.



---

archive/issue_comments_012928.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc4",
    "created_at": "2008-02-01T06:02:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2002#issuecomment-12928",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc4



---

archive/issue_events_004831.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-01T06:02:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2002",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2002#event-4831"
}
```



---

archive/issue_comments_012929.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-01T06:02:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2002#issuecomment-12929",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
