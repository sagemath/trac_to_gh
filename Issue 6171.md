# Issue 6171: [with patch, needs review] make 'prec' work with sqrt more of the time

archive/issues_006171.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nBefore this patch:\n\n```\nsage: sqrt(10.1, prec=100)\n...\nTypeError: sqrt() got an unexpected keyword argument 'prec'\n```\n\nThis is despite the fact that the docstring for sqrt lists as one of its inputs\n\n```\n            -  ``prec`` - integer (default: None): if None, returns\n               an exact square root; otherwise returns a numerical square root if\n               necessary, to the given bits of precision.\n```\n\nAfter this patch:\n\n```\nsage: sqrt(10.1, prec=100)\n3.1780497164141406804582045589\nsage: sqrt(10.1, prec=200)\n3.1780497164141406804582045589354800553656236461562686475080\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6171\n\n",
    "created_at": "2009-05-31T21:40:16Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, needs review] make 'prec' work with sqrt more of the time",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6171",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

Before this patch:

```
sage: sqrt(10.1, prec=100)
...
TypeError: sqrt() got an unexpected keyword argument 'prec'
```

This is despite the fact that the docstring for sqrt lists as one of its inputs

```
            -  ``prec`` - integer (default: None): if None, returns
               an exact square root; otherwise returns a numerical square root if
               necessary, to the given bits of precision.
```

After this patch:

```
sage: sqrt(10.1, prec=100)
3.1780497164141406804582045589
sage: sqrt(10.1, prec=200)
3.1780497164141406804582045589354800553656236461562686475080
```


Issue created by migration from https://trac.sagemath.org/ticket/6171





---

archive/issue_comments_049223.json:
```json
{
    "body": "Please add doctests to the patch illustrating that it fixes the bug.",
    "created_at": "2009-05-31T21:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6171#issuecomment-49223",
    "user": "was"
}
```

Please add doctests to the patch illustrating that it fixes the bug.



---

archive/issue_comments_049224.json:
```json
{
    "body": "> Please add doctests to the patch illustrating that it fixes the bug.\n\nYes, sorry about that.  I was just sitting down to produce a new patch when I saw this comment.  Here's a new patch.",
    "created_at": "2009-05-31T22:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6171#issuecomment-49224",
    "user": "jhpalmieri"
}
```

> Please add doctests to the patch illustrating that it fixes the bug.

Yes, sorry about that.  I was just sitting down to produce a new patch when I saw this comment.  Here's a new patch.



---

archive/issue_comments_049225.json:
```json
{
    "body": "Attachment [sqrt.patch](tarball://root/attachments/some-uuid/ticket6171/sqrt.patch) by jhpalmieri created at 2009-05-31 22:42:31",
    "created_at": "2009-05-31T22:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6171#issuecomment-49225",
    "user": "jhpalmieri"
}
```

Attachment [sqrt.patch](tarball://root/attachments/some-uuid/ticket6171/sqrt.patch) by jhpalmieri created at 2009-05-31 22:42:31



---

archive/issue_comments_049226.json:
```json
{
    "body": "Looks good to me.\n\nMerged in 4.0.1.alpha0.",
    "created_at": "2009-05-31T23:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6171#issuecomment-49226",
    "user": "mhansen"
}
```

Looks good to me.

Merged in 4.0.1.alpha0.



---

archive/issue_comments_049227.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-31T23:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6171#issuecomment-49227",
    "user": "mhansen"
}
```

Resolution: fixed
