# Issue 2084: default 20/40 in padics factory hard coded everywhere

archive/issues_002084.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @roed314\n\nThis should probably be factored out. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2084\n\n",
    "created_at": "2008-02-07T10:40:41Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "default 20/40 in padics factory hard coded everywhere",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2084",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

CC:  @roed314

This should probably be factored out. 

Issue created by migration from https://trac.sagemath.org/ticket/2084





---

archive/issue_comments_013456.json:
```json
{
    "body": "Changing component from algebraic geometry to number theory.",
    "created_at": "2008-02-07T10:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2084#issuecomment-13456",
    "user": "https://github.com/robertwb"
}
```

Changing component from algebraic geometry to number theory.



---

archive/issue_events_004993.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-07T18:11:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2084",
    "milestone": "sage-2.10.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2084#event-4993"
}
```



---

archive/issue_comments_013457.json:
```json
{
    "body": "In sage/rings/padics/factory.py, there is a twenty= and forty= at the top of the file.\n\nIt looks like we can close this ticket.  Robert, David, thoughts?",
    "created_at": "2009-06-04T21:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2084#issuecomment-13457",
    "user": "https://github.com/mwhansen"
}
```

In sage/rings/padics/factory.py, there is a twenty= and forty= at the top of the file.

It looks like we can close this ticket.  Robert, David, thoughts?



---

archive/issue_comments_013458.json:
```json
{
    "body": "Changing assignee from @williamstein to @roed314.",
    "created_at": "2009-06-07T13:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2084#issuecomment-13458",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @roed314.



---

archive/issue_comments_013459.json:
```json
{
    "body": "Changing component from number theory to padics.",
    "created_at": "2009-06-07T13:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2084#issuecomment-13459",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to padics.



---

archive/issue_comments_013460.json:
```json
{
    "body": "Attachment [trac_2084.patch](tarball://root/attachments/some-uuid/ticket2084/trac_2084.patch) by @mwhansen created at 2010-01-17 07:42:49",
    "created_at": "2010-01-17T07:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2084#issuecomment-13460",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_2084.patch](tarball://root/attachments/some-uuid/ticket2084/trac_2084.patch) by @mwhansen created at 2010-01-17 07:42:49



---

archive/issue_comments_013461.json:
```json
{
    "body": "I've changed the names.",
    "created_at": "2010-01-17T07:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2084#issuecomment-13461",
    "user": "https://github.com/mwhansen"
}
```

I've changed the names.



---

archive/issue_comments_013462.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T07:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2084#issuecomment-13462",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_013463.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-01-19T20:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2084#issuecomment-13463",
    "user": "https://github.com/roed314"
}
```

Changing priority from major to minor.



---

archive/issue_comments_013464.json:
```json
{
    "body": "Looks good.  All doctests in sage.rings.padics pass, as I would expect from the fact that this patch shouldn't change any functionality.",
    "created_at": "2010-01-19T20:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2084#issuecomment-13464",
    "user": "https://github.com/roed314"
}
```

Looks good.  All doctests in sage.rings.padics pass, as I would expect from the fact that this patch shouldn't change any functionality.



---

archive/issue_comments_013465.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T20:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2084#issuecomment-13465",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_004994.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-24T12:45:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2084",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2084#event-4994"
}
```



---

archive/issue_comments_013466.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-24T12:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2084#issuecomment-13466",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
