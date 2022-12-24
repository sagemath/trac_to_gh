# Issue 7590: Create Bipartite Graph according to 2 degree sequences

archive/issues_007590.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  wdj\n\nGiven the sequence of degrees for set A and a sequence of degree for set B, create the corresponding bipartite graph if possible.\n\nUse #7301\n\nIssue created by migration from https://trac.sagemath.org/ticket/7590\n\n",
    "created_at": "2009-12-03T12:40:23Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Create Bipartite Graph according to 2 degree sequences",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7590",
    "user": "ncohen"
}
```
Assignee: rlm

CC:  wdj

Given the sequence of degrees for set A and a sequence of degree for set B, create the corresponding bipartite graph if possible.

Use #7301

Issue created by migration from https://trac.sagemath.org/ticket/7590





---

archive/issue_comments_064707.json:
```json
{
    "body": "Here it is !",
    "created_at": "2009-12-04T17:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64707",
    "user": "ncohen"
}
```

Here it is !



---

archive/issue_comments_064708.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-04T17:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64708",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064709.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-12-15T17:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64709",
    "user": "rlm"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_064710.json:
```json
{
    "body": "What is the status of #7301 and this patch? The comments on #7301 are a bit confusing, but at the end it seems as if perhaps this patch should depend on the other version instead of #7301?",
    "created_at": "2009-12-15T17:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64710",
    "user": "rlm"
}
```

What is the status of #7301 and this patch? The comments on #7301 are a bit confusing, but at the end it seems as if perhaps this patch should depend on the other version instead of #7301?



---

archive/issue_comments_064711.json:
```json
{
    "body": "Well, I'd say this patch is ready for review (as it is written and functional) even though #7301 is not :-)\n\nThe discussion in #7301 could lead to a gale_ryser function which does not use GLPK  ( and may be even more efficient ), which is good for everybody :-)\n\nAs this function is not so fundamental to Sage, I see no harm in making it wait until #7301 is ready :-)",
    "created_at": "2009-12-16T00:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64711",
    "user": "ncohen"
}
```

Well, I'd say this patch is ready for review (as it is written and functional) even though #7301 is not :-)

The discussion in #7301 could lead to a gale_ryser function which does not use GLPK  ( and may be even more efficient ), which is good for everybody :-)

As this function is not so fundamental to Sage, I see no harm in making it wait until #7301 is ready :-)



---

archive/issue_comments_064712.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-12-16T00:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64712",
    "user": "ncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_064713.json:
```json
{
    "body": "Attachment [trac_7590.patch](tarball://root/attachments/some-uuid/ticket7590/trac_7590.patch) by rlm created at 2009-12-16 03:01:01\n\nAdded # optional to some doctests.",
    "created_at": "2009-12-16T03:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64713",
    "user": "rlm"
}
```

Attachment [trac_7590.patch](tarball://root/attachments/some-uuid/ticket7590/trac_7590.patch) by rlm created at 2009-12-16 03:01:01

Added # optional to some doctests.



---

archive/issue_comments_064714.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-16T03:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64714",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064715.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-12-16T03:05:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64715",
    "user": "rlm"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_064716.json:
```json
{
    "body": "(This is fine by me once #7301 is ready...)",
    "created_at": "2009-12-16T03:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64716",
    "user": "rlm"
}
```

(This is fine by me once #7301 is ready...)



---

archive/issue_comments_064717.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-13T09:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64717",
    "user": "rlm"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064718.json:
```json
{
    "body": "positive review.",
    "created_at": "2010-01-13T09:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64718",
    "user": "rlm"
}
```

positive review.



---

archive/issue_comments_064719.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T09:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64719",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_064720.json:
```json
{
    "body": "Thanks !! :-)",
    "created_at": "2010-01-13T09:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64720",
    "user": "ncohen"
}
```

Thanks !! :-)
