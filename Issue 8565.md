# Issue 8565: atan2(-pi,0) throws "divide by zero"

archive/issues_008565.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: pynac\n\nFrom sage-devel:\n\n```\nthe summary is:\n-------------------\natan2(3,0)   --> 1/2*pi\natan2(-3,0)  --> -1/2*pi\natan2(pi,0)  --> 1/2*pi\natan2(-pi,0) -->  RuntimeError: power::eval(): division by zero\n--------------------\n```\n\nsage-devel thread is here:\n\nhttp://groups.google.com/group/sage-devel/t/317e6bfe11fabb4\n\nalso reported on sage-support:\n\nhttp://groups.google.com/group/sage-support/t/02f3446e68381346\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8565\n\n",
    "created_at": "2010-03-20T10:33:22Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "atan2(-pi,0) throws \"divide by zero\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8565",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

Keywords: pynac

From sage-devel:

```
the summary is:
-------------------
atan2(3,0)   --> 1/2*pi
atan2(-3,0)  --> -1/2*pi
atan2(pi,0)  --> 1/2*pi
atan2(-pi,0) -->  RuntimeError: power::eval(): division by zero
--------------------
```

sage-devel thread is here:

http://groups.google.com/group/sage-devel/t/317e6bfe11fabb4

also reported on sage-support:

http://groups.google.com/group/sage-support/t/02f3446e68381346


Issue created by migration from https://trac.sagemath.org/ticket/8565





---

archive/issue_comments_077416.json:
```json
{
    "body": "add doctests",
    "created_at": "2010-04-02T14:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8565#issuecomment-77416",
    "user": "https://github.com/burcin"
}
```

add doctests



---

archive/issue_events_020663.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2010-04-02T14:52:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8565",
    "milestone": "sage-4.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8565#event-20663"
}
```



---

archive/issue_comments_077417.json:
```json
{
    "body": "Attachment [trac_8565-neg_pi.patch](tarball://root/attachments/some-uuid/ticket8565/trac_8565-neg_pi.patch) by @burcin created at 2010-04-02 14:52:12\n\nThe pynac package at #8644 includes the patches that were merged in `GiNaC` to fix this problem. attachment:trac_8565-neg_pi.patch adds doctests for the fix.\n\nThis ticket now depends on #8644.",
    "created_at": "2010-04-02T14:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8565#issuecomment-77417",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8565-neg_pi.patch](tarball://root/attachments/some-uuid/ticket8565/trac_8565-neg_pi.patch) by @burcin created at 2010-04-02 14:52:12

The pynac package at #8644 includes the patches that were merged in `GiNaC` to fix this problem. attachment:trac_8565-neg_pi.patch adds doctests for the fix.

This ticket now depends on #8644.



---

archive/issue_comments_077418.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-02T14:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8565#issuecomment-77418",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077419.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-09T11:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8565#issuecomment-77419",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077420.json:
```json
{
    "body": "Installs fine, all tests passed, works ad advertised. Positive review and thanks for fixing.",
    "created_at": "2010-04-09T11:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8565#issuecomment-77420",
    "user": "https://github.com/robert-marik"
}
```

Installs fine, all tests passed, works ad advertised. Positive review and thanks for fixing.



---

archive/issue_events_020664.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-04-29T04:13:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8565",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8565#event-20664"
}
```



---

archive/issue_comments_077421.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T04:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8565#issuecomment-77421",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
