# Issue 7502: lazy import module

archive/issues_007502.json:
```json
{
    "body": "Assignee: was\n\nThis is something I came up with when trying to reduce sage start up time. \n\n\n```\n2.033 sage.all (None)\n0.407 sage.server.all (sage.all)\n0.404 notebook.all (sage.server.all)\n0.365 sage.server.notebook.notebook (notebook.all)\n...\n```\n\n\nNow notebook() needs to be in the global namespace, but usually the entire notebook server does not need to be loaded. I'm sure there's other trimming we could do here as well. \n\nIt's unclear what level to put this in, but I would think sage.server.notebook.all would be a good place (e.g. we could lazily import interact.*, sage_email.*, and lazily import notebook and inotebook). That could cut down startup time by 25%. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7502\n\n",
    "created_at": "2009-11-20T09:20:53Z",
    "labels": [
        "user interface",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "lazy import module",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7502",
    "user": "robertwb"
}
```
Assignee: was

This is something I came up with when trying to reduce sage start up time. 


```
2.033 sage.all (None)
0.407 sage.server.all (sage.all)
0.404 notebook.all (sage.server.all)
0.365 sage.server.notebook.notebook (notebook.all)
...
```


Now notebook() needs to be in the global namespace, but usually the entire notebook server does not need to be loaded. I'm sure there's other trimming we could do here as well. 

It's unclear what level to put this in, but I would think sage.server.notebook.all would be a good place (e.g. we could lazily import interact.*, sage_email.*, and lazily import notebook and inotebook). That could cut down startup time by 25%. 

Issue created by migration from https://trac.sagemath.org/ticket/7502





---

archive/issue_comments_063420.json:
```json
{
    "body": "Attachment [7502-lazy-import.patch](tarball://root/attachments/some-uuid/ticket7502/7502-lazy-import.patch) by robertwb created at 2009-11-20 09:21:44",
    "created_at": "2009-11-20T09:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7502#issuecomment-63420",
    "user": "robertwb"
}
```

Attachment [7502-lazy-import.patch](tarball://root/attachments/some-uuid/ticket7502/7502-lazy-import.patch) by robertwb created at 2009-11-20 09:21:44



---

archive/issue_comments_063421.json:
```json
{
    "body": "Somewhat related: #8102 + #8107 reduce the startup time by cutting unnecessary imports.",
    "created_at": "2010-01-28T05:58:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7502#issuecomment-63421",
    "user": "mpatel"
}
```

Somewhat related: #8102 + #8107 reduce the startup time by cutting unnecessary imports.



---

archive/issue_comments_063422.json:
```json
{
    "body": "By the way, is this up for review?",
    "created_at": "2010-01-28T05:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7502#issuecomment-63422",
    "user": "mpatel"
}
```

By the way, is this up for review?



---

archive/issue_comments_063423.json:
```json
{
    "body": "Yes.",
    "created_at": "2010-01-28T19:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7502#issuecomment-63423",
    "user": "robertwb"
}
```

Yes.



---

archive/issue_comments_063424.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-28T19:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7502#issuecomment-63424",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063425.json:
```json
{
    "body": "Attachment [7502-lazy-import.2.patch](tarball://root/attachments/some-uuid/ticket7502/7502-lazy-import.2.patch) by mpatel created at 2010-01-30 03:34:11\n\nAlso map tab completion.  Add to reference manual. Rebased vs. 4.3.2.alpha0. Replaces previous.",
    "created_at": "2010-01-30T03:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7502#issuecomment-63425",
    "user": "mpatel"
}
```

Attachment [7502-lazy-import.2.patch](tarball://root/attachments/some-uuid/ticket7502/7502-lazy-import.2.patch) by mpatel created at 2010-01-30 03:34:11

Also map tab completion.  Add to reference manual. Rebased vs. 4.3.2.alpha0. Replaces previous.



---

archive/issue_comments_063426.json:
```json
{
    "body": "My review is positive, but someone should review the changes in v2.",
    "created_at": "2010-01-30T03:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7502#issuecomment-63426",
    "user": "mpatel"
}
```

My review is positive, but someone should review the changes in v2.



---

archive/issue_comments_063427.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-30T05:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7502#issuecomment-63427",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063428.json:
```json
{
    "body": "Thanks. Yes, your additions look good as well.",
    "created_at": "2010-01-30T05:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7502#issuecomment-63428",
    "user": "robertwb"
}
```

Thanks. Yes, your additions look good as well.



---

archive/issue_comments_063429.json:
```json
{
    "body": "Merged [7502-lazy-import.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7502/7502-lazy-import.2.patch).",
    "created_at": "2010-01-30T23:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7502#issuecomment-63429",
    "user": "mvngu"
}
```

Merged [7502-lazy-import.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7502/7502-lazy-import.2.patch).



---

archive/issue_comments_063430.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-30T23:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7502#issuecomment-63430",
    "user": "mvngu"
}
```

Resolution: fixed
