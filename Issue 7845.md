# Issue 7845: Failed browse_sage_doc doctest

archive/issues_007845.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  jhpalmieri\n\nIn Sage 4.3.1.alpha0:\n\n```python\nsage -t  \"devel/sage/sage/misc/sagedoc.py\"\n**********************************************************************\nFile \"/home/jaap/downloads/sage-4.3/devel/sage/sage/misc/sagedoc.py\", line 897:\n     sage: browse_sage_doc(identity_matrix, 'html', False)[:59]\nExpected:\n     '<div class=\"docstring\">\\n    \\n  <p><strong>File:</strong> /v'\nGot:\n     '<div class=\"docstring\">\\n    \\n  <p><strong>File:</strong> /h'\n********************************************************************** \n```\n\n\n\nFirst reported by [Jaap Spies](http://groups.google.com/group/sage-devel/msg/960b6f10c9024d0f).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7845\n\n",
    "created_at": "2010-01-05T02:55:05Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Failed browse_sage_doc doctest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7845",
    "user": "mpatel"
}
```
Assignee: mvngu

CC:  jhpalmieri

In Sage 4.3.1.alpha0:

```python
sage -t  "devel/sage/sage/misc/sagedoc.py"
**********************************************************************
File "/home/jaap/downloads/sage-4.3/devel/sage/sage/misc/sagedoc.py", line 897:
     sage: browse_sage_doc(identity_matrix, 'html', False)[:59]
Expected:
     '<div class="docstring">\n    \n  <p><strong>File:</strong> /v'
Got:
     '<div class="docstring">\n    \n  <p><strong>File:</strong> /h'
********************************************************************** 
```



First reported by [Jaap Spies](http://groups.google.com/group/sage-devel/msg/960b6f10c9024d0f).

Issue created by migration from https://trac.sagemath.org/ticket/7845





---

archive/issue_comments_067952.json:
```json
{
    "body": "Tweak `browse_sage_doc` doctests.  sage repo.",
    "created_at": "2010-01-05T02:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7845#issuecomment-67952",
    "user": "mpatel"
}
```

Tweak `browse_sage_doc` doctests.  sage repo.



---

archive/issue_comments_067953.json:
```json
{
    "body": "Attachment [trac_7845-browse_sage_doctest.patch](tarball://root/attachments/some-uuid/ticket7845/trac_7845-browse_sage_doctest.patch) by mpatel created at 2010-01-05 02:58:26\n\nFeel free to tweak further!",
    "created_at": "2010-01-05T02:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7845#issuecomment-67953",
    "user": "mpatel"
}
```

Attachment [trac_7845-browse_sage_doctest.patch](tarball://root/attachments/some-uuid/ticket7845/trac_7845-browse_sage_doctest.patch) by mpatel created at 2010-01-05 02:58:26

Feel free to tweak further!



---

archive/issue_comments_067954.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-05T02:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7845#issuecomment-67954",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067955.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-05T04:31:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7845#issuecomment-67955",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067956.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-01-05T04:31:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7845#issuecomment-67956",
    "user": "jhpalmieri"
}
```

Looks good to me.



---

archive/issue_comments_067957.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T04:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7845#issuecomment-67957",
    "user": "rlm"
}
```

Resolution: fixed
