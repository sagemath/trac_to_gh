# Issue 9119: Cython variables used then later declared

archive/issues_009119.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  robertwb wcauchois\n\nThis patch takes care of a minor issue with variables being used, and then later declared.  This takes care of these warnings:\n\n\n```\nwarning: /Users/grout/sage-4.4.2/devel/sage-main/sage/plot/plot3d/parametric_surface.pyx:355:20: cdef variable 'u' declared after it is used\nwarning: /Users/grout/sage-4.4.2/devel/sage-main/sage/plot/plot3d/parametric_surface.pyx:355:23: cdef variable 'v' declared after it is used\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9119\n\n",
    "created_at": "2010-06-03T02:23:06Z",
    "labels": [
        "graphics",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Cython variables used then later declared",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9119",
    "user": "jason"
}
```
Assignee: jason, was

CC:  robertwb wcauchois

This patch takes care of a minor issue with variables being used, and then later declared.  This takes care of these warnings:


```
warning: /Users/grout/sage-4.4.2/devel/sage-main/sage/plot/plot3d/parametric_surface.pyx:355:20: cdef variable 'u' declared after it is used
warning: /Users/grout/sage-4.4.2/devel/sage-main/sage/plot/plot3d/parametric_surface.pyx:355:23: cdef variable 'v' declared after it is used
```



Issue created by migration from https://trac.sagemath.org/ticket/9119





---

archive/issue_comments_084811.json:
```json
{
    "body": "Attachment [trac-9119-declare-variables.patch](tarball://root/attachments/some-uuid/ticket9119/trac-9119-declare-variables.patch) by jason created at 2010-06-03 02:25:02\n\nThis ticket is a trivial one to review!",
    "created_at": "2010-06-03T02:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9119#issuecomment-84811",
    "user": "jason"
}
```

Attachment [trac-9119-declare-variables.patch](tarball://root/attachments/some-uuid/ticket9119/trac-9119-declare-variables.patch) by jason created at 2010-06-03 02:25:02

This ticket is a trivial one to review!



---

archive/issue_comments_084812.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-03T02:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9119#issuecomment-84812",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084813.json:
```json
{
    "body": "Yep.",
    "created_at": "2010-06-03T03:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9119#issuecomment-84813",
    "user": "robertwb"
}
```

Yep.



---

archive/issue_comments_084814.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-03T03:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9119#issuecomment-84814",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084815.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T00:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9119#issuecomment-84815",
    "user": "mhansen"
}
```

Resolution: fixed
