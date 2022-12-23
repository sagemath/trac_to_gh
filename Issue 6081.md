# Issue 6081: [with patch, needs review] make abelian categories abelian

archive/issues_006081.json:
```json
{
    "body": "Assignee: tbd\n\nAs reported [on sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/ea99b379e5b1b8ab): \n\n```\nsage: RingModules(ZZ).is_abelian() \nFalse \nsage: AbelianGroups().is_abelian()\nFalse\n```\n\nThe attached patch should fix this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6081\n\n",
    "created_at": "2009-05-19T03:53:34Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] make abelian categories abelian",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6081",
    "user": "jhpalmieri"
}
```
Assignee: tbd

As reported [on sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/ea99b379e5b1b8ab): 

```
sage: RingModules(ZZ).is_abelian() 
False 
sage: AbelianGroups().is_abelian()
False
```

The attached patch should fix this.

Issue created by migration from https://trac.sagemath.org/ticket/6081





---

archive/issue_comments_048400.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-19T03:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6081#issuecomment-48400",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_048401.json:
```json
{
    "body": "This applies cleanly to 4.0.rc2 and passes doctests.  It looks good to me, but someone with a better overview should decide whether to merge it or just wait for the new category code to be merged.",
    "created_at": "2009-05-30T08:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6081#issuecomment-48401",
    "user": "AlexGhitza"
}
```

This applies cleanly to 4.0.rc2 and passes doctests.  It looks good to me, but someone with a better overview should decide whether to merge it or just wait for the new category code to be merged.



---

archive/issue_comments_048402.json:
```json
{
    "body": "Merged in 4.0.1.rc1.",
    "created_at": "2009-06-04T18:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6081#issuecomment-48402",
    "user": "mhansen"
}
```

Merged in 4.0.1.rc1.



---

archive/issue_comments_048403.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T18:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6081#issuecomment-48403",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_048404.json:
```json
{
    "body": "LARGE GRUMBLE.\n\nWas it really that urgent to integrate this in????? \n\nI said I was going to handle it.\n\nNow I again need to rebase the category code + work around the compatibility in the sage-combinat patches.",
    "created_at": "2009-06-09T22:28:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6081#issuecomment-48404",
    "user": "nthiery"
}
```

LARGE GRUMBLE.

Was it really that urgent to integrate this in????? 

I said I was going to handle it.

Now I again need to rebase the category code + work around the compatibility in the sage-combinat patches.



---

archive/issue_comments_048405.json:
```json
{
    "body": "There wasn't any comment on the ticket saying that it shouldn't be merged.  It had a positive review and fixed a bug that someone actually encountered.  I guess I'm just so used to rebasing things that I don't think anything of it.  Sorry about that.",
    "created_at": "2009-06-09T22:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6081#issuecomment-48405",
    "user": "mhansen"
}
```

There wasn't any comment on the ticket saying that it shouldn't be merged.  It had a positive review and fixed a bug that someone actually encountered.  I guess I'm just so used to rebasing things that I don't think anything of it.  Sorry about that.



---

archive/issue_comments_048406.json:
```json
{
    "body": "Alex had asked explicitly whether this should wait for the category code to be merged.\n\nOh well.\n\nBtw: other than that, I truly appreciated the hard work you did put into making this release happen!",
    "created_at": "2009-06-09T23:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6081#issuecomment-48406",
    "user": "nthiery"
}
```

Alex had asked explicitly whether this should wait for the category code to be merged.

Oh well.

Btw: other than that, I truly appreciated the hard work you did put into making this release happen!
