# Issue 7792: Improved docs and added Width and Height at /interfaces/povray.py

archive/issues_007792.json:
```json
{
    "body": "Assignee: was\n\nKeywords: povray\n\nTo improve docs of Povray.\nTo have width and height parameters in Povray.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7792\n\n",
    "created_at": "2009-12-29T23:01:38Z",
    "labels": [
        "interfaces",
        "trivial",
        "bug"
    ],
    "title": "Improved docs and added Width and Height at /interfaces/povray.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7792",
    "user": "slosoi"
}
```
Assignee: was

Keywords: povray

To improve docs of Povray.
To have width and height parameters in Povray.

Issue created by migration from https://trac.sagemath.org/ticket/7792





---

archive/issue_comments_067250.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2009-12-29T23:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7792#issuecomment-67250",
    "user": "slosoi"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_067251.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-12-29T23:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7792#issuecomment-67251",
    "user": "slosoi"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_067252.json:
```json
{
    "body": "There are some bugs apparently in the width and height parameters in the changed code. \nThe parameters F and P work differently as I expected.",
    "created_at": "2009-12-30T03:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7792#issuecomment-67252",
    "user": "slosoi"
}
```

There are some bugs apparently in the width and height parameters in the changed code. 
The parameters F and P work differently as I expected.



---

archive/issue_comments_067253.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-30T04:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7792#issuecomment-67253",
    "user": "slosoi"
}
```

Attachment



---

archive/issue_comments_067254.json:
```json
{
    "body": "Replying to [comment:3 slosoi]:\n> There are some bugs apparently in the width and height parameters in the changed code. \n> The parameters F and P work differently as I expected.\n\nThe patch -file is old one. I will submit a new one after the compilation of Sage.",
    "created_at": "2009-12-30T04:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7792#issuecomment-67254",
    "user": "slosoi"
}
```

Replying to [comment:3 slosoi]:
> There are some bugs apparently in the width and height parameters in the changed code. 
> The parameters F and P work differently as I expected.

The patch -file is old one. I will submit a new one after the compilation of Sage.



---

archive/issue_comments_067255.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-30T19:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7792#issuecomment-67255",
    "user": "slosoi"
}
```

Attachment



---

archive/issue_comments_067256.json:
```json
{
    "body": "Attachment\n\nWhy are you removing the docstring from the class definition?",
    "created_at": "2010-02-07T23:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7792#issuecomment-67256",
    "user": "mhampton"
}
```

Attachment

Why are you removing the docstring from the class definition?



---

archive/issue_comments_067257.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-23T16:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7792#issuecomment-67257",
    "user": "boothby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067258.json:
```json
{
    "body": "Somethings up with these patches.  Both povray_doc.patch and povray_doc.2.patch are identical and won't apply on top of povray.py.  Also, the file is missing class-level documentation and doctests, (as mhampton noted, you should move the file-level doc back) and nothing is doctested in the methods.",
    "created_at": "2010-06-23T16:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7792#issuecomment-67258",
    "user": "boothby"
}
```

Somethings up with these patches.  Both povray_doc.patch and povray_doc.2.patch are identical and won't apply on top of povray.py.  Also, the file is missing class-level documentation and doctests, (as mhampton noted, you should move the file-level doc back) and nothing is doctested in the methods.
