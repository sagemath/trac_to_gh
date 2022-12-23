# Issue 9632: System-dependent term order for printed expressions

archive/issues_009632.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  burcin cwitty ddrake jhpalmieri kcrisman\n\nThe order in which the terms in some symbolic expressions are printed depends on the platform/system.  For example, evaluating `cos(x) + zeta(x)` yields\n\n* `zeta(x) + cos(x)` on Linux\n* `cos(x) + zeta(x)` on OS X\n\nin Sage 4.4.4 and 4.5.2.alpha{0,1}, at least.\n\nPlease see #9582 for some details and discussion.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9632\n\n",
    "created_at": "2010-07-29T06:16:00Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "System-dependent term order for printed expressions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9632",
    "user": "mpatel"
}
```
Assignee: burcin

CC:  burcin cwitty ddrake jhpalmieri kcrisman

The order in which the terms in some symbolic expressions are printed depends on the platform/system.  For example, evaluating `cos(x) + zeta(x)` yields

* `zeta(x) + cos(x)` on Linux
* `cos(x) + zeta(x)` on OS X

in Sage 4.4.4 and 4.5.2.alpha{0,1}, at least.

Please see #9582 for some details and discussion.

Issue created by migration from https://trac.sagemath.org/ticket/9632





---

archive/issue_comments_093351.json:
```json
{
    "body": "#10282 is a duplicate of this issue.\n\nThe patches attached to #9880 fix this.",
    "created_at": "2010-11-18T15:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93351",
    "user": "burcin"
}
```

#10282 is a duplicate of this issue.

The patches attached to #9880 fix this.



---

archive/issue_comments_093352.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-11-18T15:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93352",
    "user": "burcin"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_093353.json:
```json
{
    "body": "#10282 almost certainly is the same thing.",
    "created_at": "2010-11-18T16:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93353",
    "user": "kcrisman"
}
```

#10282 almost certainly is the same thing.



---

archive/issue_comments_093354.json:
```json
{
    "body": "When this is closed (which would hopefully happen with #9880 integrated), let's be sure to write doctests for both this ticket and #10282, which would just be to say that \n\n```\nsage: psi(1,1/3)*log(3)\nlog(3)*psi(1, 1/3)\n```\n\nis the same on all systems, in addition to the `zeta(x)+cos(x)` example here.",
    "created_at": "2011-01-13T03:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93354",
    "user": "kcrisman"
}
```

When this is closed (which would hopefully happen with #9880 integrated), let's be sure to write doctests for both this ticket and #10282, which would just be to say that 

```
sage: psi(1,1/3)*log(3)
log(3)*psi(1, 1/3)
```

is the same on all systems, in addition to the `zeta(x)+cos(x)` example here.



---

archive/issue_comments_093355.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-07-01T00:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93355",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093356.json:
```json
{
    "body": "Attachment\n\nThis was fixed by #9880. [attachment:trac_9632-doctests.patch] adds doctests.",
    "created_at": "2013-07-01T00:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93356",
    "user": "burcin"
}
```

Attachment

This was fixed by #9880. [attachment:trac_9632-doctests.patch] adds doctests.



---

archive/issue_comments_093357.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-07-12T13:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93357",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093358.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-07-31T12:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9632#issuecomment-93358",
    "user": "jdemeyer"
}
```

Resolution: fixed
