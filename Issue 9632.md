# Issue 9632: System-dependent term order for printed expressions

archive/issues_009632.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @burcin cwitty @dandrake @jhpalmieri @kcrisman\n\nThe order in which the terms in some symbolic expressions are printed depends on the platform/system.  For example, evaluating `cos(x) + zeta(x)` yields\n\n* `zeta(x) + cos(x)` on Linux\n* `cos(x) + zeta(x)` on OS X\n\nin Sage 4.4.4 and 4.5.2.alpha{0,1}, at least.\n\nPlease see #9582 for some details and discussion.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9632\n\n",
    "created_at": "2010-07-29T06:16:00Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.11",
    "title": "System-dependent term order for printed expressions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9632",
    "user": "https://github.com/qed777"
}
```
Assignee: @burcin

CC:  @burcin cwitty @dandrake @jhpalmieri @kcrisman

The order in which the terms in some symbolic expressions are printed depends on the platform/system.  For example, evaluating `cos(x) + zeta(x)` yields

* `zeta(x) + cos(x)` on Linux
* `cos(x) + zeta(x)` on OS X

in Sage 4.4.4 and 4.5.2.alpha{0,1}, at least.

Please see #9582 for some details and discussion.

Issue created by migration from https://trac.sagemath.org/ticket/9632





---

archive/issue_comments_093195.json:
```json
{
    "body": "#10282 is a duplicate of this issue.\n\nThe patches attached to #9880 fix this.",
    "created_at": "2010-11-18T15:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93195",
    "user": "https://github.com/burcin"
}
```

#10282 is a duplicate of this issue.

The patches attached to #9880 fix this.



---

archive/issue_comments_093196.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-11-18T15:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93196",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_093197.json:
```json
{
    "body": "#10282 almost certainly is the same thing.",
    "created_at": "2010-11-18T16:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93197",
    "user": "https://github.com/kcrisman"
}
```

#10282 almost certainly is the same thing.



---

archive/issue_comments_093198.json:
```json
{
    "body": "When this is closed (which would hopefully happen with #9880 integrated), let's be sure to write doctests for both this ticket and #10282, which would just be to say that \n\n```\nsage: psi(1,1/3)*log(3)\nlog(3)*psi(1, 1/3)\n```\n\nis the same on all systems, in addition to the `zeta(x)+cos(x)` example here.",
    "created_at": "2011-01-13T03:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93198",
    "user": "https://github.com/kcrisman"
}
```

When this is closed (which would hopefully happen with #9880 integrated), let's be sure to write doctests for both this ticket and #10282, which would just be to say that 

```
sage: psi(1,1/3)*log(3)
log(3)*psi(1, 1/3)
```

is the same on all systems, in addition to the `zeta(x)+cos(x)` example here.



---

archive/issue_comments_093199.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-07-01T00:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93199",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093200.json:
```json
{
    "body": "Attachment [trac_9632-doctests.patch](tarball://root/attachments/some-uuid/ticket9632/trac_9632-doctests.patch) by @burcin created at 2013-07-01 00:49:12\n\nThis was fixed by #9880. [attachment:trac_9632-doctests.patch] adds doctests.",
    "created_at": "2013-07-01T00:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93200",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9632-doctests.patch](tarball://root/attachments/some-uuid/ticket9632/trac_9632-doctests.patch) by @burcin created at 2013-07-01 00:49:12

This was fixed by #9880. [attachment:trac_9632-doctests.patch] adds doctests.



---

archive/issue_comments_093201.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-07-12T13:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93201",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009771.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-07-31T12:53:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9632#event-9771"
}
```



---

archive/issue_comments_093202.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-07-31T12:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93202",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
