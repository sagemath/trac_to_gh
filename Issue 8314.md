# Issue 8314: numerical noise in sage/misc/functional.py

archive/issues_008314.json:
```json
{
    "body": "Assignee: tbd\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/msg/ba90601a2c25291d):\n\n```\nOn 32-bit Suse I get this fuzz:\n\nFile \"/local/jec/sage-4.3.3.alpha1/devel/sage/sage/misc/functional.py\",\nline 705:\n    sage: h.n()\nExpected:\n    0.33944794097891573\nGot:\n    0.33944794097891567 \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8314\n\n",
    "created_at": "2010-02-20T16:26:06Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "numerical noise in sage/misc/functional.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8314",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tbd

From [sage-devel](http://groups.google.com/group/sage-devel/msg/ba90601a2c25291d):

```
On 32-bit Suse I get this fuzz:

File "/local/jec/sage-4.3.3.alpha1/devel/sage/sage/misc/functional.py",
line 705:
    sage: h.n()
Expected:
    0.33944794097891573
Got:
    0.33944794097891567 
```


Issue created by migration from https://trac.sagemath.org/ticket/8314





---

archive/issue_comments_073610.json:
```json
{
    "body": "based on Sage 4.3.3.alpha1",
    "created_at": "2010-02-20T16:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8314#issuecomment-73610",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on Sage 4.3.3.alpha1



---

archive/issue_comments_073611.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-20T16:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8314#issuecomment-73611",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073612.json:
```json
{
    "body": "Attachment [trac_8314-doctest.patch](tarball://root/attachments/some-uuid/ticket8314/trac_8314-doctest.patch) by mvngu created at 2010-02-20 16:28:28",
    "created_at": "2010-02-20T16:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8314#issuecomment-73612",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8314-doctest.patch](tarball://root/attachments/some-uuid/ticket8314/trac_8314-doctest.patch) by mvngu created at 2010-02-20 16:28:28



---

archive/issue_comments_073613.json:
```json
{
    "body": "positive review -- the patch replaces two digits by ... so the tests pass.  It would have been nice to know why those digits are platform-dependent though...",
    "created_at": "2010-02-20T17:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8314#issuecomment-73613",
    "user": "https://github.com/JohnCremona"
}
```

positive review -- the patch replaces two digits by ... so the tests pass.  It would have been nice to know why those digits are platform-dependent though...



---

archive/issue_comments_073614.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-20T17:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8314#issuecomment-73614",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073615.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-02-21T19:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8314#issuecomment-73615",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_073616.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-22T03:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8314#issuecomment-73616",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_019890.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-22T03:57:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8314#event-19890"
}
```
