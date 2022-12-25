# Issue 3431: [with patch, positive review] QEPCAD interface

archive/issues_003431.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @burcin\n\nKeywords: editor_cwitty\n\nThis provides an extensive Sage interface to QEPCAD.  (The patch was formerly posted on #772; we're moving it here to keep one issue per ticket.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3431\n\n",
    "closed_at": "2008-08-28T02:54:29Z",
    "created_at": "2008-06-15T21:46:21Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, positive review] QEPCAD interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3431",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

CC:  @burcin

Keywords: editor_cwitty

This provides an extensive Sage interface to QEPCAD.  (The patch was formerly posted on #772; we're moving it here to keep one issue per ticket.)

Issue created by migration from https://trac.sagemath.org/ticket/3431





---

archive/issue_comments_024136.json:
```json
{
    "body": "Attachment [trac772-qepcad-interface.patch](tarball://root/attachments/some-uuid/ticket3431/trac772-qepcad-interface.patch) by cwitty created at 2008-06-15 22:17:33",
    "created_at": "2008-06-15T22:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3431#issuecomment-24136",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac772-qepcad-interface.patch](tarball://root/attachments/some-uuid/ticket3431/trac772-qepcad-interface.patch) by cwitty created at 2008-06-15 22:17:33



---

archive/issue_comments_024137.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-06-15T22:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3431#issuecomment-24137",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing type from defect to enhancement.



---

archive/issue_events_007750.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-06-15T22:32:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3431#event-7750"
}
```



---

archive/issue_comments_024138.json:
```json
{
    "body": "This patch looks very nice and seems to behave as advertised.  There are some doctests that should be updated for qepcad 1.50 and also for the new interval printing notation in Sage 3.1.  Positive review pending fixing those things.",
    "created_at": "2008-08-16T21:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3431#issuecomment-24138",
    "user": "https://github.com/jasongrout"
}
```

This patch looks very nice and seems to behave as advertised.  There are some doctests that should be updated for qepcad 1.50 and also for the new interval printing notation in Sage 3.1.  Positive review pending fixing those things.



---

archive/issue_comments_024139.json:
```json
{
    "body": "Attachment [trac3431-qepcad-interface-part2.patch](tarball://root/attachments/some-uuid/ticket3431/trac3431-qepcad-interface-part2.patch) by cwitty created at 2008-08-20 17:03:34\n\nI've attached a patch to update the qepcad interface to deal with the newest interval printing, and to avoid locking the interface to one particular version of qepcad.\n\nNote that this patch depends on #3910 (without #3910, one doctest will fail).",
    "created_at": "2008-08-20T17:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3431#issuecomment-24139",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac3431-qepcad-interface-part2.patch](tarball://root/attachments/some-uuid/ticket3431/trac3431-qepcad-interface-part2.patch) by cwitty created at 2008-08-20 17:03:34

I've attached a patch to update the qepcad interface to deal with the newest interval printing, and to avoid locking the interface to one particular version of qepcad.

Note that this patch depends on #3910 (without #3910, one doctest will fail).



---

archive/issue_comments_024140.json:
```json
{
    "body": "With the newest qepcad spkg up at #772, all doctests in qepcad.py pass on sage 3.1.2alpha1.  It looks good to me.",
    "created_at": "2008-08-27T17:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3431#issuecomment-24140",
    "user": "https://github.com/jasongrout"
}
```

With the newest qepcad spkg up at #772, all doctests in qepcad.py pass on sage 3.1.2alpha1.  It looks good to me.



---

archive/issue_comments_024141.json:
```json
{
    "body": "Merged both patches in Sage 3.1.2.alpha2",
    "created_at": "2008-08-28T02:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3431#issuecomment-24141",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.1.2.alpha2



---

archive/issue_events_007751.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-28T02:54:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3431#event-7751"
}
```



---

archive/issue_comments_024142.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-28T02:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3431#issuecomment-24142",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
