# Issue 8743: change_ring on a rational matrix may return self

archive/issues_008743.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @williamstein @rbeezer\n\nchange_ring on a rational matrix goes against the documentation for the generic change_ring function, which states that a copy is always returned.  This patch fixes this and adds a TestSuite test for it (the advantage of a testsuite test is that this will be run for *every* matrix class, not just the rational matrix class).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8743\n\n",
    "closed_at": "2010-06-06T01:33:11Z",
    "created_at": "2010-04-22T01:17:21Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "change_ring on a rational matrix may return self",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8743",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, was

CC:  @williamstein @rbeezer

change_ring on a rational matrix goes against the documentation for the generic change_ring function, which states that a copy is always returned.  This patch fixes this and adds a TestSuite test for it (the advantage of a testsuite test is that this will be run for *every* matrix class, not just the rational matrix class).

Issue created by migration from https://trac.sagemath.org/ticket/8743





---

archive/issue_comments_079861.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-22T01:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8743#issuecomment-79861",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079862.json:
```json
{
    "body": "Attachment [trac-8743-change_ring.patch](tarball://root/attachments/some-uuid/ticket8743/trac-8743-change_ring.patch) by @jasongrout created at 2010-04-22 01:41:00",
    "created_at": "2010-04-22T01:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8743#issuecomment-79862",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8743-change_ring.patch](tarball://root/attachments/some-uuid/ticket8743/trac-8743-change_ring.patch) by @jasongrout created at 2010-04-22 01:41:00



---

archive/issue_comments_079863.json:
```json
{
    "body": "Fixes bug, code seems to be OK, test is included, all tests pass. Positive review.",
    "created_at": "2010-05-19T14:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8743#issuecomment-79863",
    "user": "https://trac.sagemath.org/admin/accounts/users/jsyri"
}
```

Fixes bug, code seems to be OK, test is included, all tests pass. Positive review.



---

archive/issue_comments_079864.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-19T14:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8743#issuecomment-79864",
    "user": "https://trac.sagemath.org/admin/accounts/users/jsyri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_021247.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T01:33:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8743",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8743#event-21247"
}
```



---

archive/issue_comments_079865.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:33:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8743#issuecomment-79865",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_079866.json:
```json
{
    "body": "I understand the ticket is closed, but is there any rational for the current behavior? Seems very inefficient, and returning self should be totally safe for immutable matrices at least.",
    "created_at": "2010-06-06T06:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8743#issuecomment-79866",
    "user": "https://github.com/robertwb"
}
```

I understand the ticket is closed, but is there any rational for the current behavior? Seems very inefficient, and returning self should be totally safe for immutable matrices at least.



---

archive/issue_comments_079867.json:
```json
{
    "body": "The patch does return self for immutable matrices.",
    "created_at": "2010-06-06T06:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8743#issuecomment-79867",
    "user": "https://github.com/mwhansen"
}
```

The patch does return self for immutable matrices.
