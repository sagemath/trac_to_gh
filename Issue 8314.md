# Issue 8314: numerical noise in sage/misc/functional.py

archive/issues_008314.json:
```json
{
    "body": "Assignee: tbd\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/msg/ba90601a2c25291d):\n\n```\nOn 32-bit Suse I get this fuzz:\n\nFile \"/local/jec/sage-4.3.3.alpha1/devel/sage/sage/misc/functional.py\",\nline 705:\n    sage: h.n()\nExpected:\n    0.33944794097891573\nGot:\n    0.33944794097891567 \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8314\n\n",
    "created_at": "2010-02-20T16:26:06Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "numerical noise in sage/misc/functional.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8314",
    "user": "mvngu"
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

archive/issue_comments_073733.json:
```json
{
    "body": "based on Sage 4.3.3.alpha1",
    "created_at": "2010-02-20T16:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8314#issuecomment-73733",
    "user": "mvngu"
}
```

based on Sage 4.3.3.alpha1



---

archive/issue_comments_073734.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-20T16:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8314#issuecomment-73734",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073735.json:
```json
{
    "body": "Attachment [trac_8314-doctest.patch](tarball://root/attachments/some-uuid/ticket8314/trac_8314-doctest.patch) by mvngu created at 2010-02-20 16:28:28",
    "created_at": "2010-02-20T16:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8314#issuecomment-73735",
    "user": "mvngu"
}
```

Attachment [trac_8314-doctest.patch](tarball://root/attachments/some-uuid/ticket8314/trac_8314-doctest.patch) by mvngu created at 2010-02-20 16:28:28



---

archive/issue_comments_073736.json:
```json
{
    "body": "positive review -- the patch replaces two digits by ... so the tests pass.  It would have been nice to know why those digits are platform-dependent though...",
    "created_at": "2010-02-20T17:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8314#issuecomment-73736",
    "user": "cremona"
}
```

positive review -- the patch replaces two digits by ... so the tests pass.  It would have been nice to know why those digits are platform-dependent though...



---

archive/issue_comments_073737.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-20T17:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8314#issuecomment-73737",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073738.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-02-21T19:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8314#issuecomment-73738",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_073739.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-22T03:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8314#issuecomment-73739",
    "user": "mvngu"
}
```

Resolution: fixed
