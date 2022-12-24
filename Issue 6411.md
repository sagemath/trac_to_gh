# Issue 6411: sdist makes sage unable to run without building

archive/issues_006411.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @williamstein\n\nWilliam was complaining about being unable to reproduce this, so here's an easy way to reproduce it:\n\nTake sage-4.1.alpha1, do an sdist, and try running sage. Boom.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6411\n\n",
    "created_at": "2009-06-25T17:28:23Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "sdist makes sage unable to run without building",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6411",
    "user": "@rlmill"
}
```
Assignee: @craigcitro

CC:  @williamstein

William was complaining about being unable to reproduce this, so here's an easy way to reproduce it:

Take sage-4.1.alpha1, do an sdist, and try running sage. Boom.

Issue created by migration from https://trac.sagemath.org/ticket/6411





---

archive/issue_comments_051484.json:
```json
{
    "body": "I think if you run a \"sage -br\" afterward, it will work.  There are just a few things that get compiled when doing that.  Looking at those, it should be easy to trac down what changed.",
    "created_at": "2009-06-25T20:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6411#issuecomment-51484",
    "user": "@mwhansen"
}
```

I think if you run a "sage -br" afterward, it will work.  There are just a few things that get compiled when doing that.  Looking at those, it should be easy to trac down what changed.



---

archive/issue_comments_051485.json:
```json
{
    "body": "This is because in spkg-dist, we do the following:\n\n\n```\nrm -rf c_lib/*.so c_lib/*.os c_lib/*/*.os c_lib/*/*/*.os\n```\n\n\nThis causes libcsage to be built again.  What we should do instead is delete the files from the tmp directory that we copy things into.",
    "created_at": "2010-01-17T01:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6411#issuecomment-51485",
    "user": "@mwhansen"
}
```

This is because in spkg-dist, we do the following:


```
rm -rf c_lib/*.so c_lib/*.os c_lib/*/*.os c_lib/*/*/*.os
```


This causes libcsage to be built again.  What we should do instead is delete the files from the tmp directory that we copy things into.



---

archive/issue_comments_051486.json:
```json
{
    "body": "Attachment [trac_6411.patch](tarball://root/attachments/some-uuid/ticket6411/trac_6411.patch) by @mwhansen created at 2010-01-17 01:53:22",
    "created_at": "2010-01-17T01:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6411#issuecomment-51486",
    "user": "@mwhansen"
}
```

Attachment [trac_6411.patch](tarball://root/attachments/some-uuid/ticket6411/trac_6411.patch) by @mwhansen created at 2010-01-17 01:53:22



---

archive/issue_comments_051487.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T02:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6411#issuecomment-51487",
    "user": "@mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_051488.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T18:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6411#issuecomment-51488",
    "user": "@wjp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051489.json:
```json
{
    "body": "This looks good, and fixes the problem for me.",
    "created_at": "2010-01-17T18:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6411#issuecomment-51489",
    "user": "@wjp"
}
```

This looks good, and fixes the problem for me.



---

archive/issue_comments_051490.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-18T22:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6411#issuecomment-51490",
    "user": "@rlmill"
}
```

Resolution: fixed
