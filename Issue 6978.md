# Issue 6978: [patch, needs review] fixes matplotlib to compile in cygwin

archive/issues_006978.json:
```json
{
    "body": "Assignee: tbd\n\nHere is a fixed package:\n\nhttp://femhub.googlecode.com/files/matplotlib-0.98.5.3rc0-svn6910.p5.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/6978\n\n",
    "created_at": "2009-09-21T16:41:33Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "[patch, needs review] fixes matplotlib to compile in cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6978",
    "user": "certik"
}
```
Assignee: tbd

Here is a fixed package:

http://femhub.googlecode.com/files/matplotlib-0.98.5.3rc0-svn6910.p5.spkg

Issue created by migration from https://trac.sagemath.org/ticket/6978





---

archive/issue_comments_057707.json:
```json
{
    "body": "The latest matplotlib we have in Sage is 0.99, though.  It's in 4.1.2 already.  See #5448 for the spkg.\n\nI was just going to update the spkg to have 0.99.1, which was just pre-announced on matplotlib-devel (barring any problems) as svn 7813.\n\nSo at bare minimum, the spkg above needs to use the spkg from #5448.  Ondrej, if you want to update to 0.99.1, that would be great too.  0.99.1 obsoletes several of the patches in the spkg, as they've been merged upstream.",
    "created_at": "2009-09-21T22:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6978#issuecomment-57707",
    "user": "jason"
}
```

The latest matplotlib we have in Sage is 0.99, though.  It's in 4.1.2 already.  See #5448 for the spkg.

I was just going to update the spkg to have 0.99.1, which was just pre-announced on matplotlib-devel (barring any problems) as svn 7813.

So at bare minimum, the spkg above needs to use the spkg from #5448.  Ondrej, if you want to update to 0.99.1, that would be great too.  0.99.1 obsoletes several of the patches in the spkg, as they've been merged upstream.



---

archive/issue_comments_057708.json:
```json
{
    "body": "I'll do so. I don't know why I used 0.98.5. I will first build femhub with this tonight and if all works, update matplotlib and see if I can fix that one too.",
    "created_at": "2009-09-21T22:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6978#issuecomment-57708",
    "user": "certik"
}
```

I'll do so. I don't know why I used 0.98.5. I will first build femhub with this tonight and if all works, update matplotlib and see if I can fix that one too.



---

archive/issue_comments_057709.json:
```json
{
    "body": "the new matplotlib already fixed this problem. so closed as invalid.",
    "created_at": "2009-09-22T09:10:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6978#issuecomment-57709",
    "user": "was"
}
```

the new matplotlib already fixed this problem. so closed as invalid.



---

archive/issue_comments_057710.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-22T09:10:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6978#issuecomment-57710",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_057711.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-09-22T16:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6978#issuecomment-57711",
    "user": "mvngu"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_057712.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-09-22T16:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6978#issuecomment-57712",
    "user": "mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_057713.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-09-22T16:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6978#issuecomment-57713",
    "user": "mvngu"
}
```

Resolution: invalid
