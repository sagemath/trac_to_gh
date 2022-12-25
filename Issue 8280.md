# Issue 8280: cygwin: zn_poly shared library named incorrectly on cygwin

archive/issues_008280.json:
```json
{
    "body": "Assignee: tbd\n\nWhen trying to build sage on cygwin, I had to do this:\n\n\n```\nwstein@winxp ~/build/sage-4.3.3.alpha0/local/lib\n$ ln -s libzn_poly.so libzn_poly.dll\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8280\n\n",
    "created_at": "2010-02-16T02:08:16Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "cygwin: zn_poly shared library named incorrectly on cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8280",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

When trying to build sage on cygwin, I had to do this:


```
wstein@winxp ~/build/sage-4.3.3.alpha0/local/lib
$ ln -s libzn_poly.so libzn_poly.dll
```


Issue created by migration from https://trac.sagemath.org/ticket/8280





---

archive/issue_comments_073196.json:
```json
{
    "body": "I've posted an spkg which fixes this at http://sage.math.washington.edu/home/mhansen/cygwin_port/zn_poly-0.9.p2.spkg",
    "created_at": "2010-02-16T04:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8280#issuecomment-73196",
    "user": "https://github.com/mwhansen"
}
```

I've posted an spkg which fixes this at http://sage.math.washington.edu/home/mhansen/cygwin_port/zn_poly-0.9.p2.spkg



---

archive/issue_comments_073197.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-16T04:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8280#issuecomment-73197",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073198.json:
```json
{
    "body": "What is the purpose of this change?\n\n```\n-#!/usr/bin/env bash\n+B#!/usr/bin/env bash\n```\n",
    "created_at": "2010-02-16T07:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8280#issuecomment-73198",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

What is the purpose of this change?

```
-#!/usr/bin/env bash
+B#!/usr/bin/env bash
```




---

archive/issue_comments_073199.json:
```json
{
    "body": "Oops -- just a typo.  I've fixed it now.",
    "created_at": "2010-02-16T07:40:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8280#issuecomment-73199",
    "user": "https://github.com/mwhansen"
}
```

Oops -- just a typo.  I've fixed it now.



---

archive/issue_comments_073200.json:
```json
{
    "body": "The changes looks OK to me. Sage 4.3.3.alpha0 compiled OK with this updated spkg. All doctests pass. The Cygwin build went pass the compilation process of zn_poly.",
    "created_at": "2010-02-17T00:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8280#issuecomment-73200",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The changes looks OK to me. Sage 4.3.3.alpha0 compiled OK with this updated spkg. All doctests pass. The Cygwin build went pass the compilation process of zn_poly.



---

archive/issue_comments_073201.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-17T00:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8280#issuecomment-73201",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008479.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-17T00:29:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8280",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8280#event-8479"
}
```



---

archive/issue_comments_073202.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-17T00:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8280#issuecomment-73202",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
