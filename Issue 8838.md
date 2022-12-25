# Issue 8838: make "arrow()" take 3d vectors

archive/issues_008838.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @kcrisman ryan\n\nA convention we have is that graphics commands do the right thing depending on if 2d or 3d input is passed.  We should make arrow() take 3-tuples to produce a 3d plot (by calling arrow3d).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8838\n\n",
    "created_at": "2010-05-01T19:25:58Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "make \"arrow()\" take 3d vectors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8838",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, was

CC:  @kcrisman ryan

A convention we have is that graphics commands do the right thing depending on if 2d or 3d input is passed.  We should make arrow() take 3-tuples to produce a 3d plot (by calling arrow3d).

Issue created by migration from https://trac.sagemath.org/ticket/8838





---

archive/issue_comments_081122.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-05-26T15:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8838#issuecomment-81122",
    "user": "https://github.com/jasongrout"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_081123.json:
```json
{
    "body": "In other words, this should work:\n\n\n```\nsage: arrow(vector([1,2,3]), vector([2,3,4]))\n```\n\n\nand should draw a 3d arrow.",
    "created_at": "2010-08-26T22:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8838#issuecomment-81123",
    "user": "https://github.com/jasongrout"
}
```

In other words, this should work:


```
sage: arrow(vector([1,2,3]), vector([2,3,4]))
```


and should draw a 3d arrow.



---

archive/issue_comments_081124.json:
```json
{
    "body": "Attachment [trac_8838_arrow2d_3d.patch](tarball://root/attachments/some-uuid/ticket8838/trac_8838_arrow2d_3d.patch) by ryan created at 2010-08-28 02:53:45\n\nmake arrow() behave more like line()",
    "created_at": "2010-08-28T02:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8838#issuecomment-81124",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_8838_arrow2d_3d.patch](tarball://root/attachments/some-uuid/ticket8838/trac_8838_arrow2d_3d.patch) by ryan created at 2010-08-28 02:53:45

make arrow() behave more like line()



---

archive/issue_comments_081125.json:
```json
{
    "body": "here is a patch that changes the behavior of arrow() to be more like line().  \n\nIf 2d coordinates are passed, arrow() returns an arrow2d() (the old arrow() function).  If 3d coordinates are passed, arrow() will now return an arrow3d().",
    "created_at": "2010-08-28T02:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8838#issuecomment-81125",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

here is a patch that changes the behavior of arrow() to be more like line().  

If 2d coordinates are passed, arrow() returns an arrow2d() (the old arrow() function).  If 3d coordinates are passed, arrow() will now return an arrow3d().



---

archive/issue_comments_081126.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-28T02:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8838#issuecomment-81126",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081127.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-29T02:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8838#issuecomment-81127",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081128.json:
```json
{
    "body": "This looks great.  However, for backwards compatibility, could you name the arguments to arrow() \"tailpoint\" and \"headpoint\".  Now, this command won't work, whereas before it would:\n\n\n```\narrow(tailpoint=(0,1), headpoint=(2,3))\n```\n\n\nWe should keep our API unless there is a very good reason to change it.",
    "created_at": "2010-08-29T02:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8838#issuecomment-81128",
    "user": "https://github.com/jasongrout"
}
```

This looks great.  However, for backwards compatibility, could you name the arguments to arrow() "tailpoint" and "headpoint".  Now, this command won't work, whereas before it would:


```
arrow(tailpoint=(0,1), headpoint=(2,3))
```


We should keep our API unless there is a very good reason to change it.



---

archive/issue_comments_081129.json:
```json
{
    "body": "Updated patch (with Sage 4.5.3)",
    "created_at": "2010-09-11T05:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8838#issuecomment-81129",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Updated patch (with Sage 4.5.3)



---

archive/issue_comments_081130.json:
```json
{
    "body": "Attachment [trac_8838_arrow2d_arrow3d.patch](tarball://root/attachments/some-uuid/ticket8838/trac_8838_arrow2d_arrow3d.patch) by ryan created at 2010-09-11 05:25:40",
    "created_at": "2010-09-11T05:25:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8838#issuecomment-81130",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_8838_arrow2d_arrow3d.patch](tarball://root/attachments/some-uuid/ticket8838/trac_8838_arrow2d_arrow3d.patch) by ryan created at 2010-09-11 05:25:40



---

archive/issue_comments_081131.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-11T05:25:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8838#issuecomment-81131",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081132.json:
```json
{
    "body": "Looks good! Thanks!\n\nApply only trac_8838_arrow2d_arrow3d.patch",
    "created_at": "2010-09-11T16:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8838#issuecomment-81132",
    "user": "https://github.com/jasongrout"
}
```

Looks good! Thanks!

Apply only trac_8838_arrow2d_arrow3d.patch



---

archive/issue_comments_081133.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-11T16:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8838#issuecomment-81133",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081134.json:
```json
{
    "body": "Note that this is Ryan's first contribution (along with #9199 and #7154)",
    "created_at": "2010-09-11T16:23:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8838#issuecomment-81134",
    "user": "https://github.com/jasongrout"
}
```

Note that this is Ryan's first contribution (along with #9199 and #7154)



---

archive/issue_events_009003.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-09-15T10:40:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8838#event-9003"
}
```



---

archive/issue_comments_081135.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8838#issuecomment-81135",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
