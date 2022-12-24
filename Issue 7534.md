# Issue 7534: Add a deprecation message at the top of most sage.server.* files

archive/issues_007534.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  timdumol was\n\nTo avoid confusion, we should add a message to the top of each **old** Sage notebook .py file stating that one should work on [SageNB](http://nb.sagemath.org/) instead.\n\nThis should be a patch to the core Sage library.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7534\n\n",
    "created_at": "2009-11-26T07:20:52Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Add a deprecation message at the top of most sage.server.* files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7534",
    "user": "mpatel"
}
```
Assignee: boothby

CC:  timdumol was

To avoid confusion, we should add a message to the top of each **old** Sage notebook .py file stating that one should work on [SageNB](http://nb.sagemath.org/) instead.

This should be a patch to the core Sage library.


Issue created by migration from https://trac.sagemath.org/ticket/7534





---

archive/issue_comments_063890.json:
```json
{
    "body": "How about\n\n```\nThis file is part of the OLD Sage notebook and is NOT actively developed,\nmaintained, or supported.  As of Sage v4.1.2, all notebook development has\nmoved to the separate Sage Notebook project:\n\nhttp://nb.sagemath.org/\n\nThe new notebook is installed in Sage as a spkg (e.g., sagenb-0.3.spkg).\n\nPlease visit the project's home page for more information, including directions on\nobtaining the latest source code.  For notebook-related development and support,\nplease consult the sage-notebook discussion group:\n\nhttp://groups.google.com/group/sage-notebook\n```\n\n?",
    "created_at": "2009-11-26T07:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63890",
    "user": "mpatel"
}
```

How about

```
This file is part of the OLD Sage notebook and is NOT actively developed,
maintained, or supported.  As of Sage v4.1.2, all notebook development has
moved to the separate Sage Notebook project:

http://nb.sagemath.org/

The new notebook is installed in Sage as a spkg (e.g., sagenb-0.3.spkg).

Please visit the project's home page for more information, including directions on
obtaining the latest source code.  For notebook-related development and support,
please consult the sage-notebook discussion group:

http://groups.google.com/group/sage-notebook
```

?



---

archive/issue_comments_063891.json:
```json
{
    "body": "See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/be3318a5770bf8f4).",
    "created_at": "2009-11-26T22:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63891",
    "user": "mpatel"
}
```

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/be3318a5770bf8f4).



---

archive/issue_comments_063892.json:
```json
{
    "body": "Adds the recommended deprecation message (with typo correction)",
    "created_at": "2009-11-30T06:26:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63892",
    "user": "timdumol"
}
```

Adds the recommended deprecation message (with typo correction)



---

archive/issue_comments_063893.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-30T06:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63893",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063894.json:
```json
{
    "body": "Attachment [trac_7534-deprecation-message](tarball://root/attachments/some-uuid/ticket7534/trac_7534-deprecation-message) by timdumol created at 2009-11-30 06:26:20\n\nThis should do the job.",
    "created_at": "2009-11-30T06:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63894",
    "user": "timdumol"
}
```

Attachment [trac_7534-deprecation-message](tarball://root/attachments/some-uuid/ticket7534/trac_7534-deprecation-message) by timdumol created at 2009-11-30 06:26:20

This should do the job.



---

archive/issue_comments_063895.json:
```json
{
    "body": "This causes some failures in tests in sage/server/",
    "created_at": "2009-12-02T19:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63895",
    "user": "mhansen"
}
```

This causes some failures in tests in sage/server/



---

archive/issue_comments_063896.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-02T19:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63896",
    "user": "mhansen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063897.json:
```json
{
    "body": "\n```\n        sage -t  devel/sage-main/sage/server/notebook/notebook_object.py # 4 doctests failed\n```\n",
    "created_at": "2009-12-02T19:23:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63897",
    "user": "mhansen"
}
```


```
        sage -t  devel/sage-main/sage/server/notebook/notebook_object.py # 4 doctests failed
```




---

archive/issue_comments_063898.json:
```json
{
    "body": "Replying to [comment:5 mhansen]:\n> {{{        sage -t  devel/sage-main/sage/server/notebook/notebook_object.py # 4 doctests failed\n> }}}\n\nSince the code isn't being run and is officially \"deprecated\", one option is to put a nodoctest.py file in the directory (or #nodoctest at the top of the file) so that the code isn't tested.",
    "created_at": "2009-12-10T01:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63898",
    "user": "was"
}
```

Replying to [comment:5 mhansen]:
> {{{        sage -t  devel/sage-main/sage/server/notebook/notebook_object.py # 4 doctests failed
> }}}

Since the code isn't being run and is officially "deprecated", one option is to put a nodoctest.py file in the directory (or #nodoctest at the top of the file) so that the code isn't tested.



---

archive/issue_comments_063899.json:
```json
{
    "body": "Adds `nodoctest.py` files.  Replacement patch.",
    "created_at": "2009-12-10T12:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63899",
    "user": "mpatel"
}
```

Adds `nodoctest.py` files.  Replacement patch.



---

archive/issue_comments_063900.json:
```json
{
    "body": "Attachment [trac_7534-deprecation-message_v2.patch](tarball://root/attachments/some-uuid/ticket7534/trac_7534-deprecation-message_v2.patch) by mpatel created at 2009-12-10 12:17:29\n\nV2 suppresses doctesting for the \"deprecated\" files.",
    "created_at": "2009-12-10T12:17:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63900",
    "user": "mpatel"
}
```

Attachment [trac_7534-deprecation-message_v2.patch](tarball://root/attachments/some-uuid/ticket7534/trac_7534-deprecation-message_v2.patch) by mpatel created at 2009-12-10 12:17:29

V2 suppresses doctesting for the "deprecated" files.



---

archive/issue_comments_063901.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-10T12:17:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63901",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063902.json:
```json
{
    "body": "Looks good to me now.",
    "created_at": "2009-12-10T18:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63902",
    "user": "was"
}
```

Looks good to me now.



---

archive/issue_comments_063903.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-10T18:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63903",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063904.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-14T16:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7534#issuecomment-63904",
    "user": "mhansen"
}
```

Resolution: fixed
