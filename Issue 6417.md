# Issue 6417: Unicode in LaTeX

archive/issues_006417.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: unicode LaTeX\n\nIn a %latex cell I couldn't use any accentuated letter. I had to write \\\"o to get \u00f6.\n\nUsing this patch I can write unicode characters directly. For example Hungarian chars:\n\n http://www.math.bme.hu/~morap/sage_unicode_latex.png\n\nThis feature is important because most of the world uses more than the first 128 characters of ANSII.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6417\n\n",
    "created_at": "2009-06-25T21:53:59Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Unicode in LaTeX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6417",
    "user": "https://trac.sagemath.org/admin/accounts/users/mora"
}
```
Assignee: cwitty

Keywords: unicode LaTeX

In a %latex cell I couldn't use any accentuated letter. I had to write \"o to get ö.

Using this patch I can write unicode characters directly. For example Hungarian chars:

 http://www.math.bme.hu/~morap/sage_unicode_latex.png

This feature is important because most of the world uses more than the first 128 characters of ANSII.

Issue created by migration from https://trac.sagemath.org/ticket/6417





---

archive/issue_comments_051436.json:
```json
{
    "body": "Attachment [12538.patch](tarball://root/attachments/some-uuid/ticket6417/12538.patch) by mora created at 2009-06-25 21:57:36",
    "created_at": "2009-06-25T21:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6417#issuecomment-51436",
    "user": "https://trac.sagemath.org/admin/accounts/users/mora"
}
```

Attachment [12538.patch](tarball://root/attachments/some-uuid/ticket6417/12538.patch) by mora created at 2009-06-25 21:57:36



---

archive/issue_comments_051437.json:
```json
{
    "body": "Looks good to me except that it doesn't pass doctests.  Apply the patch at #6434 and you're good to go.\n\nSo this patch depends on #6434; modulo that, positive review.",
    "created_at": "2009-06-27T17:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6417#issuecomment-51437",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me except that it doesn't pass doctests.  Apply the patch at #6434 and you're good to go.

So this patch depends on #6434; modulo that, positive review.



---

archive/issue_comments_051438.json:
```json
{
    "body": "`sage -t  \"devel/sage-main/sage/misc/latex.py\"` fails after applying this patch.",
    "created_at": "2009-07-03T18:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6417#issuecomment-51438",
    "user": "https://github.com/rlmill"
}
```

`sage -t  "devel/sage-main/sage/misc/latex.py"` fails after applying this patch.



---

archive/issue_comments_051439.json:
```json
{
    "body": "> sage -t \"devel/sage-main/sage/misc/latex.py\" fails after applying this patch.\n\nAs my comment says, doctests don't pass until you apply the patch at #6434.  Once #6434 gets in, this one is ready to go.  Is there some way to label this besides \"positive review\" to indicate this?",
    "created_at": "2009-07-03T20:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6417#issuecomment-51439",
    "user": "https://github.com/jhpalmieri"
}
```

> sage -t "devel/sage-main/sage/misc/latex.py" fails after applying this patch.

As my comment says, doctests don't pass until you apply the patch at #6434.  Once #6434 gets in, this one is ready to go.  Is there some way to label this besides "positive review" to indicate this?



---

archive/issue_comments_051440.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n> > sage -t \"devel/sage-main/sage/misc/latex.py\" fails after applying this patch.\n> \n> As my comment says, doctests don't pass until you apply the patch at #6434.\n\nMy bad, wasn't paying enough attention.",
    "created_at": "2009-07-04T00:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6417#issuecomment-51440",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:4 jhpalmieri]:
> > sage -t "devel/sage-main/sage/misc/latex.py" fails after applying this patch.
> 
> As my comment says, doctests don't pass until you apply the patch at #6434.

My bad, wasn't paying enough attention.



---

archive/issue_events_015133.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-07-04T00:58:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6417#event-15133"
}
```



---

archive/issue_comments_051441.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-04T00:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6417#issuecomment-51441",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_051442.json:
```json
{
    "body": "See #6464 for a related issue. It concerns Unicode in Notebook worksheets.",
    "created_at": "2009-07-05T02:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6417#issuecomment-51442",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See #6464 for a related issue. It concerns Unicode in Notebook worksheets.
