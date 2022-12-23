# Issue 7146: MAKE and sqlite on Solaris: bomb!

archive/issues_007146.json:
```json
{
    "body": "Assignee: tbd\n\nI set MAKE to \"make -j10\" on solaris x86 (disk.math) and while building sqlite got quite a surprise:\n\n```\nwstein@disk:~$ ps -u wstein  |grep make|wc -l\n    5915\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7146\n\n",
    "created_at": "2009-10-07T15:33:27Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "title": "MAKE and sqlite on Solaris: bomb!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7146",
    "user": "was"
}
```
Assignee: tbd

I set MAKE to "make -j10" on solaris x86 (disk.math) and while building sqlite got quite a surprise:

```
wstein@disk:~$ ps -u wstein  |grep make|wc -l
    5915
```


Issue created by migration from https://trac.sagemath.org/ticket/7146





---

archive/issue_comments_059221.json:
```json
{
    "body": "I assume this refers to an old version of SQLite which is no longer relevant.",
    "created_at": "2013-05-23T14:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7146#issuecomment-59221",
    "user": "jdemeyer"
}
```

I assume this refers to an old version of SQLite which is no longer relevant.



---

archive/issue_comments_059222.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-23T14:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7146#issuecomment-59222",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059223.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-23T14:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7146#issuecomment-59223",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059224.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-05-27T11:24:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7146#issuecomment-59224",
    "user": "jdemeyer"
}
```

Resolution: invalid
