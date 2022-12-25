# Issue 5101: [with patch, needs review] more types for sage_input: vectors, matrices, etc.

archive/issues_005101.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @jasongrout\n\nI'm attaching a patch to increase sage_input support.  Newly supported are floats, elements of RDF and CC, vectors, and matrices (sparse and dense).  I also added some new features to sage_input for handling these new types, and fixed a bug in matrix_modn_sparse that was exposed in the process (sorry, the bug fix really should have been a separate patch).\n\nThis patch depends on #2898 (and hence indirectly on #3938).\n\nIssue created by migration from https://trac.sagemath.org/ticket/5101\n\n",
    "created_at": "2009-01-25T20:32:52Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] more types for sage_input: vectors, matrices, etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5101",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

CC:  @jasongrout

I'm attaching a patch to increase sage_input support.  Newly supported are floats, elements of RDF and CC, vectors, and matrices (sparse and dense).  I also added some new features to sage_input for handling these new types, and fixed a bug in matrix_modn_sparse that was exposed in the process (sorry, the bug fix really should have been a separate patch).

This patch depends on #2898 (and hence indirectly on #3938).

Issue created by migration from https://trac.sagemath.org/ticket/5101





---

archive/issue_comments_038887.json:
```json
{
    "body": "Attachment [sage-input-sequel.patch](tarball://root/attachments/some-uuid/ticket5101/sage-input-sequel.patch) by @jasongrout created at 2009-02-06 07:55:39\n\nI've looked over the patch and it looks reasonable.  Doctests pass on 3.3alpha3 for all (nontrivially) touched files.  Positive review.\n\nThis does depend on someone reviewing 2898, though.",
    "created_at": "2009-02-06T07:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5101#issuecomment-38887",
    "user": "https://github.com/jasongrout"
}
```

Attachment [sage-input-sequel.patch](tarball://root/attachments/some-uuid/ticket5101/sage-input-sequel.patch) by @jasongrout created at 2009-02-06 07:55:39

I've looked over the patch and it looks reasonable.  Doctests pass on 3.3alpha3 for all (nontrivially) touched files.  Positive review.

This does depend on someone reviewing 2898, though.



---

archive/issue_comments_038888.json:
```json
{
    "body": "This fix depends on #2898 getting a positive review and getting merged.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T02:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5101#issuecomment-38888",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This fix depends on #2898 getting a positive review and getting merged.

Cheers,

Michael



---

archive/issue_events_005347.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-09T09:05:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5101",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5101#event-5347"
}
```



---

archive/issue_comments_038889.json:
```json
{
    "body": "Merged in Sage 3.3.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T09:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5101#issuecomment-38889",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc0.

Cheers,

Michael



---

archive/issue_comments_038890.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-09T09:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5101#issuecomment-38890",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
