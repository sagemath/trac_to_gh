# Issue 7844: notebook.address AttributeError

archive/issues_007844.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  was ddrake\n\nOn publishing a new worksheet:\n\n```python\n          File \"/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/twist.py\", line 1316, in render\n            addr += notebook.address\n        exceptions.AttributeError: 'Notebook' object has no attribute 'address'\n```\n\n\nI think this is a follow-up to #7639.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7844\n\n",
    "created_at": "2010-01-05T02:24:47Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "notebook.address AttributeError",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7844",
    "user": "mpatel"
}
```
Assignee: AlexGhitza

CC:  was ddrake

On publishing a new worksheet:

```python
          File "/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/twist.py", line 1316, in render
            addr += notebook.address
        exceptions.AttributeError: 'Notebook' object has no attribute 'address'
```


I think this is a follow-up to #7639.

Issue created by migration from https://trac.sagemath.org/ticket/7844





---

archive/issue_comments_067945.json:
```json
{
    "body": "`notebook.address` --> `notebook.interface`.  sagenb repo.",
    "created_at": "2010-01-05T02:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7844#issuecomment-67945",
    "user": "mpatel"
}
```

`notebook.address` --> `notebook.interface`.  sagenb repo.



---

archive/issue_comments_067946.json:
```json
{
    "body": "Attachment [trac_7844-notebook_address.patch](tarball://root/attachments/some-uuid/ticket7844/trac_7844-notebook_address.patch) by mpatel created at 2010-01-05 02:29:11\n\nHave I found them all?",
    "created_at": "2010-01-05T02:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7844#issuecomment-67946",
    "user": "mpatel"
}
```

Attachment [trac_7844-notebook_address.patch](tarball://root/attachments/some-uuid/ticket7844/trac_7844-notebook_address.patch) by mpatel created at 2010-01-05 02:29:11

Have I found them all?



---

archive/issue_comments_067947.json:
```json
{
    "body": "Changing component from algebra to notebook.",
    "created_at": "2010-01-05T02:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7844#issuecomment-67947",
    "user": "mpatel"
}
```

Changing component from algebra to notebook.



---

archive/issue_comments_067948.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-05T02:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7844#issuecomment-67948",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067949.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-05T04:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7844#issuecomment-67949",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067950.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-05T04:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7844#issuecomment-67950",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_067951.json:
```json
{
    "body": "merged into sagenb-0.5.",
    "created_at": "2010-01-05T04:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7844#issuecomment-67951",
    "user": "was"
}
```

merged into sagenb-0.5.
