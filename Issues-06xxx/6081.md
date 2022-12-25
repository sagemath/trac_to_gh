# Issue 6081: [with patch, positive review] make abelian categories abelian

archive/issues_006081.json:
```json
{
    "body": "Assignee: tbd\n\nAs reported [on sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/ea99b379e5b1b8ab): \n\n```\nsage: RingModules(ZZ).is_abelian() \nFalse \nsage: AbelianGroups().is_abelian()\nFalse\n```\nThe attached patch should fix this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6081\n\n",
    "closed_at": "2009-06-04T18:29:43Z",
    "created_at": "2009-05-19T03:53:34Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, positive review] make abelian categories abelian",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6081",
    "user": "https://github.com/jhpalmieri"
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

archive/issue_comments_048308.json:
```json
{
    "body": "Attachment [abelian.patch](tarball://root/attachments/some-uuid/ticket6081/abelian.patch) by @jhpalmieri created at 2009-05-19 03:53:54",
    "created_at": "2009-05-19T03:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6081#issuecomment-48308",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [abelian.patch](tarball://root/attachments/some-uuid/ticket6081/abelian.patch) by @jhpalmieri created at 2009-05-19 03:53:54



---

archive/issue_comments_048309.json:
```json
{
    "body": "This applies cleanly to 4.0.rc2 and passes doctests.  It looks good to me, but someone with a better overview should decide whether to merge it or just wait for the new category code to be merged.",
    "created_at": "2009-05-30T08:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6081#issuecomment-48309",
    "user": "https://github.com/aghitza"
}
```

This applies cleanly to 4.0.rc2 and passes doctests.  It looks good to me, but someone with a better overview should decide whether to merge it or just wait for the new category code to be merged.



---

archive/issue_comments_048310.json:
```json
{
    "body": "Merged in 4.0.1.rc1.",
    "created_at": "2009-06-04T18:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6081#issuecomment-48310",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.1.rc1.



---

archive/issue_events_014281.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-04T18:29:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6081#event-14281"
}
```



---

archive/issue_comments_048311.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T18:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6081#issuecomment-48311",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_048312.json:
```json
{
    "body": "LARGE GRUMBLE.\n\nWas it really that urgent to integrate this in????? \n\nI said I was going to handle it.\n\nNow I again need to rebase the category code + work around the compatibility in the sage-combinat patches.",
    "created_at": "2009-06-09T22:28:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6081#issuecomment-48312",
    "user": "https://github.com/nthiery"
}
```

LARGE GRUMBLE.

Was it really that urgent to integrate this in????? 

I said I was going to handle it.

Now I again need to rebase the category code + work around the compatibility in the sage-combinat patches.



---

archive/issue_comments_048313.json:
```json
{
    "body": "There wasn't any comment on the ticket saying that it shouldn't be merged.  It had a positive review and fixed a bug that someone actually encountered.  I guess I'm just so used to rebasing things that I don't think anything of it.  Sorry about that.",
    "created_at": "2009-06-09T22:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6081#issuecomment-48313",
    "user": "https://github.com/mwhansen"
}
```

There wasn't any comment on the ticket saying that it shouldn't be merged.  It had a positive review and fixed a bug that someone actually encountered.  I guess I'm just so used to rebasing things that I don't think anything of it.  Sorry about that.



---

archive/issue_comments_048314.json:
```json
{
    "body": "Alex had asked explicitly whether this should wait for the category code to be merged.\n\nOh well.\n\nBtw: other than that, I truly appreciated the hard work you did put into making this release happen!",
    "created_at": "2009-06-09T23:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6081#issuecomment-48314",
    "user": "https://github.com/nthiery"
}
```

Alex had asked explicitly whether this should wait for the category code to be merged.

Oh well.

Btw: other than that, I truly appreciated the hard work you did put into making this release happen!
