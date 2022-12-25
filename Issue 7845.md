# Issue 7845: Failed browse_sage_doc doctest

archive/issues_007845.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @jhpalmieri\n\nIn Sage 4.3.1.alpha0:\n\n```python\nsage -t  \"devel/sage/sage/misc/sagedoc.py\"\n**********************************************************************\nFile \"/home/jaap/downloads/sage-4.3/devel/sage/sage/misc/sagedoc.py\", line 897:\n     sage: browse_sage_doc(identity_matrix, 'html', False)[:59]\nExpected:\n     '<div class=\"docstring\">\\n    \\n  <p><strong>File:</strong> /v'\nGot:\n     '<div class=\"docstring\">\\n    \\n  <p><strong>File:</strong> /h'\n********************************************************************** \n```\n\n\n\nFirst reported by [Jaap Spies](http://groups.google.com/group/sage-devel/msg/960b6f10c9024d0f).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7845\n\n",
    "created_at": "2010-01-05T02:55:05Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Failed browse_sage_doc doctest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7845",
    "user": "https://github.com/qed777"
}
```
Assignee: mvngu

CC:  @jhpalmieri

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

archive/issue_comments_067835.json:
```json
{
    "body": "Tweak `browse_sage_doc` doctests.  sage repo.",
    "created_at": "2010-01-05T02:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7845#issuecomment-67835",
    "user": "https://github.com/qed777"
}
```

Tweak `browse_sage_doc` doctests.  sage repo.



---

archive/issue_comments_067836.json:
```json
{
    "body": "Attachment [trac_7845-browse_sage_doctest.patch](tarball://root/attachments/some-uuid/ticket7845/trac_7845-browse_sage_doctest.patch) by @qed777 created at 2010-01-05 02:58:26\n\nFeel free to tweak further!",
    "created_at": "2010-01-05T02:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7845#issuecomment-67836",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7845-browse_sage_doctest.patch](tarball://root/attachments/some-uuid/ticket7845/trac_7845-browse_sage_doctest.patch) by @qed777 created at 2010-01-05 02:58:26

Feel free to tweak further!



---

archive/issue_comments_067837.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-05T02:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7845#issuecomment-67837",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067838.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-05T04:31:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7845#issuecomment-67838",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067839.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-01-05T04:31:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7845#issuecomment-67839",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me.



---

archive/issue_comments_067840.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T04:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7845#issuecomment-67840",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_008060.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-13T04:14:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7845",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7845#event-8060"
}
```
