# Issue 5529: bring documentation of classical.py to 100%

archive/issues_005529.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: classical.py, doctest\n\nAs the subject says.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5529\n\n",
    "created_at": "2009-03-16T10:44:03Z",
    "labels": [
        "component: documentation",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "bring documentation of classical.py to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5529",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tba

Keywords: classical.py, doctest

As the subject says.

Issue created by migration from https://trac.sagemath.org/ticket/5529





---

archive/issue_comments_042916.json:
```json
{
    "body": "Attachment [trac_5529_doc.patch](tarball://root/attachments/some-uuid/ticket5529/trac_5529_doc.patch) by mvngu created at 2009-03-16 10:45:24",
    "created_at": "2009-03-16T10:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5529#issuecomment-42916",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_5529_doc.patch](tarball://root/attachments/some-uuid/ticket5529/trac_5529_doc.patch) by mvngu created at 2009-03-16 10:45:24



---

archive/issue_comments_042917.json:
```json
{
    "body": "The patch **trac_5529_doc.patch** should bring the documentation coverage of `sage.crypto.classical.py` to 100%... woo hoo...",
    "created_at": "2009-03-16T10:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5529#issuecomment-42917",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch **trac_5529_doc.patch** should bring the documentation coverage of `sage.crypto.classical.py` to 100%... woo hoo...



---

archive/issue_comments_042918.json:
```json
{
    "body": "Looks good, mostly.  I've made a few small changes and a few bigger ones.  The small changes: I changed \"EXAMPLE::\" to \"EXAMPLES::\" several times.  I changed \"\\mathbb{Z}\" to \"\\mathbf{Z}\" since this is the Sage style: try `latex(ZZ)`.  One line wasn't indented quite far enough, and I did a little minor rewording.\n\nThe more major changes: in the reference manual, methods which begin with an underscore don't appear.  For the most part, this doesn't bother me, but `__init__` methods often have important documentation, so for this file, I moved the docs for the `__init__` methods up a level to documentation for the class. This way it appears in the reference manual (as the first thing for the class) and also when you run sage and type `HillCryptosystem?`, for example.\n\nI give mvngu's part of this a positive review, so only my patch needs reviewing.",
    "created_at": "2009-03-23T02:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5529#issuecomment-42918",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good, mostly.  I've made a few small changes and a few bigger ones.  The small changes: I changed "EXAMPLE::" to "EXAMPLES::" several times.  I changed "\mathbb{Z}" to "\mathbf{Z}" since this is the Sage style: try `latex(ZZ)`.  One line wasn't indented quite far enough, and I did a little minor rewording.

The more major changes: in the reference manual, methods which begin with an underscore don't appear.  For the most part, this doesn't bother me, but `__init__` methods often have important documentation, so for this file, I moved the docs for the `__init__` methods up a level to documentation for the class. This way it appears in the reference manual (as the first thing for the class) and also when you run sage and type `HillCryptosystem?`, for example.

I give mvngu's part of this a positive review, so only my patch needs reviewing.



---

archive/issue_comments_042919.json:
```json
{
    "body": "Attachment [5529-new.patch](tarball://root/attachments/some-uuid/ticket5529/5529-new.patch) by @jhpalmieri created at 2009-03-23 02:46:46\n\napply this on top of the other patch",
    "created_at": "2009-03-23T02:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5529#issuecomment-42919",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [5529-new.patch](tarball://root/attachments/some-uuid/ticket5529/5529-new.patch) by @jhpalmieri created at 2009-03-23 02:46:46

apply this on top of the other patch



---

archive/issue_comments_042920.json:
```json
{
    "body": "The patch **5529-new.patch** applies fine against Sage 3.4, all doctests passed even with `-long` option. Rebuilding the HTML version of the reference manual, I see that documentation of many `_init__` methods are now visible. So positive review for jhpalmieri's part.",
    "created_at": "2009-03-23T05:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5529#issuecomment-42920",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch **5529-new.patch** applies fine against Sage 3.4, all doctests passed even with `-long` option. Rebuilding the HTML version of the reference manual, I see that documentation of many `_init__` methods are now visible. So positive review for jhpalmieri's part.



---

archive/issue_events_012959.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-23T21:02:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5529",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5529#event-12959"
}
```



---

archive/issue_comments_042921.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T21:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5529#issuecomment-42921",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042922.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T21:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5529#issuecomment-42922",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.4.1.alpha0.

Cheers,

Michael
