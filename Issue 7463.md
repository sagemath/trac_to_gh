# Issue 7463: document memory management for the magma interface

archive/issues_007463.json:
```json
{
    "body": "Assignee: @williamstein\n\nAdd documentation to magma.py explaining memory management for this interface. \n\nThe attached patch will -- if tested using \n\n```\ncd devel/sage/sage/interfaces/\nsage -t --only_optional=magma magma.py\n```\nhave doctest failures.  This isn't because of this patch.  See #7462. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7463\n\n",
    "created_at": "2009-11-14T18:55:29Z",
    "labels": [
        "component: interfaces",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "document memory management for the magma interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7463",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Add documentation to magma.py explaining memory management for this interface. 

The attached patch will -- if tested using 

```
cd devel/sage/sage/interfaces/
sage -t --only_optional=magma magma.py
```
have doctest failures.  This isn't because of this patch.  See #7462. 

Issue created by migration from https://trac.sagemath.org/ticket/7463





---

archive/issue_comments_062745.json:
```json
{
    "body": "Attachment [trac_7463.patch](tarball://root/attachments/some-uuid/ticket7463/trac_7463.patch) by @williamstein created at 2009-11-14 18:56:09",
    "created_at": "2009-11-14T18:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7463#issuecomment-62745",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7463.patch](tarball://root/attachments/some-uuid/ticket7463/trac_7463.patch) by @williamstein created at 2009-11-14 18:56:09



---

archive/issue_comments_062746.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-14T18:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7463#issuecomment-62746",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062747.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-14T20:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7463#issuecomment-62747",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062748.json:
```json
{
    "body": "I couldn't resist to review this right on the spot. What should I say? I even tested the html documentation, and everything seems to be just perfect.",
    "created_at": "2009-11-14T20:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7463#issuecomment-62748",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

I couldn't resist to review this right on the spot. What should I say? I even tested the html documentation, and everything seems to be just perfect.



---

archive/issue_events_017693.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-17T06:01:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7463",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7463#event-17693"
}
```



---

archive/issue_comments_062749.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T06:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7463#issuecomment-62749",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
