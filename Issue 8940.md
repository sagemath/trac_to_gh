# Issue 8940: doctest failures in sagedoc.py

archive/issues_008940.json:
```json
{
    "body": "Assignee: tbd\n\nHere's the failure on sage.math, when building Sage 4.4.2.alpha0 from source:\n\n```\nsage -t  -long devel/sage/sage/misc/sagedoc.py # 3 doctests failed\n```\n\nThe failure with sagedoc.py is due ticket #8468, whose patch was merged without also merging the relevant Sphinx configuration files.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8940\n\n",
    "created_at": "2010-05-10T01:09:57Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "doctest failures in sagedoc.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8940",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tbd

Here's the failure on sage.math, when building Sage 4.4.2.alpha0 from source:

```
sage -t  -long devel/sage/sage/misc/sagedoc.py # 3 doctests failed
```

The failure with sagedoc.py is due ticket #8468, whose patch was merged without also merging the relevant Sphinx configuration files.

Issue created by migration from https://trac.sagemath.org/ticket/8940





---

archive/issue_comments_082189.json:
```json
{
    "body": "This is invalid due to the report at this [sage-devel](http://groups.google.com/group/sage-devel/msg/13ea54c19e7fcb20) thread.",
    "created_at": "2010-05-10T10:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8940#issuecomment-82189",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This is invalid due to the report at this [sage-devel](http://groups.google.com/group/sage-devel/msg/13ea54c19e7fcb20) thread.



---

archive/issue_comments_082190.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-05-10T10:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8940#issuecomment-82190",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: invalid
