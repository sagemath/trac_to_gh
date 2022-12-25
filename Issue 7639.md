# Issue 7639: notebook -- change "address" option to "interface" in notebook(...) command

archive/issues_007639.json:
```json
{
    "body": "Assignee: @williamstein\n\nAddress refers to a network interface. So perhaps we can change address to interface, but continue accepting address for backwards compatibility? Something like this in the docstring:\n\n```\n            - ``interface``       -- (default: 'localhost'), address of network\n              interface to listen on; give '' to listen on all interfaces. You may \n              use ``address`` here for backwards compatibility, but this is deprecated\n              and will be removed in the future.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7639\n\n",
    "created_at": "2009-12-09T14:46:48Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "notebook -- change \"address\" option to \"interface\" in notebook(...) command",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7639",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Address refers to a network interface. So perhaps we can change address to interface, but continue accepting address for backwards compatibility? Something like this in the docstring:

```
            - ``interface``       -- (default: 'localhost'), address of network
              interface to listen on; give '' to listen on all interfaces. You may 
              use ``address`` here for backwards compatibility, but this is deprecated
              and will be removed in the future.
```

Issue created by migration from https://trac.sagemath.org/ticket/7639





---

archive/issue_comments_065169.json:
```json
{
    "body": "Attachment [sagenb-7639.patch](tarball://root/attachments/some-uuid/ticket7639/sagenb-7639.patch) by @williamstein created at 2009-12-09 15:12:51",
    "created_at": "2009-12-09T15:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7639#issuecomment-65169",
    "user": "https://github.com/williamstein"
}
```

Attachment [sagenb-7639.patch](tarball://root/attachments/some-uuid/ticket7639/sagenb-7639.patch) by @williamstein created at 2009-12-09 15:12:51



---

archive/issue_comments_065170.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-09T15:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7639#issuecomment-65170",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065171.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-10T02:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7639#issuecomment-65171",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065172.json:
```json
{
    "body": "Works as advertised. Positive review here.",
    "created_at": "2009-12-10T02:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7639#issuecomment-65172",
    "user": "https://github.com/dandrake"
}
```

Works as advertised. Positive review here.



---

archive/issue_comments_065173.json:
```json
{
    "body": "Merged into sagenb-0.4.8.",
    "created_at": "2010-01-04T06:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7639#issuecomment-65173",
    "user": "https://github.com/williamstein"
}
```

Merged into sagenb-0.4.8.



---

archive/issue_comments_065174.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T06:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7639#issuecomment-65174",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_018166.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-01-04T06:53:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7639",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7639#event-18166"
}
```
