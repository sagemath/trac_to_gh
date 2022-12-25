# Issue 7844: notebook.address AttributeError

archive/issues_007844.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @williamstein @dandrake\n\nOn publishing a new worksheet:\n\n```python\n          File \"/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/twist.py\", line 1316, in render\n            addr += notebook.address\n        exceptions.AttributeError: 'Notebook' object has no attribute 'address'\n```\n\n\nI think this is a follow-up to #7639.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7844\n\n",
    "created_at": "2010-01-05T02:24:47Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "notebook.address AttributeError",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7844",
    "user": "https://github.com/qed777"
}
```
Assignee: @aghitza

CC:  @williamstein @dandrake

On publishing a new worksheet:

```python
          File "/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/twist.py", line 1316, in render
            addr += notebook.address
        exceptions.AttributeError: 'Notebook' object has no attribute 'address'
```


I think this is a follow-up to #7639.

Issue created by migration from https://trac.sagemath.org/ticket/7844





---

archive/issue_comments_067828.json:
```json
{
    "body": "`notebook.address` --> `notebook.interface`.  sagenb repo.",
    "created_at": "2010-01-05T02:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7844#issuecomment-67828",
    "user": "https://github.com/qed777"
}
```

`notebook.address` --> `notebook.interface`.  sagenb repo.



---

archive/issue_comments_067829.json:
```json
{
    "body": "Attachment [trac_7844-notebook_address.patch](tarball://root/attachments/some-uuid/ticket7844/trac_7844-notebook_address.patch) by @qed777 created at 2010-01-05 02:29:11\n\nHave I found them all?",
    "created_at": "2010-01-05T02:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7844#issuecomment-67829",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7844-notebook_address.patch](tarball://root/attachments/some-uuid/ticket7844/trac_7844-notebook_address.patch) by @qed777 created at 2010-01-05 02:29:11

Have I found them all?



---

archive/issue_comments_067830.json:
```json
{
    "body": "Changing component from algebra to notebook.",
    "created_at": "2010-01-05T02:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7844#issuecomment-67830",
    "user": "https://github.com/qed777"
}
```

Changing component from algebra to notebook.



---

archive/issue_comments_067831.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-05T02:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7844#issuecomment-67831",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067832.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-05T04:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7844#issuecomment-67832",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067833.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-05T04:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7844#issuecomment-67833",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_067834.json:
```json
{
    "body": "merged into sagenb-0.5.",
    "created_at": "2010-01-05T04:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7844#issuecomment-67834",
    "user": "https://github.com/williamstein"
}
```

merged into sagenb-0.5.
