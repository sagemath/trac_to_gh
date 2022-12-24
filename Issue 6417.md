# Issue 6417: Unicode in LaTeX

archive/issues_006417.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: unicode LaTeX\n\nIn a %latex cell I couldn't use any accentuated letter. I had to write \\\"o to get \u00f6.\n\nUsing this patch I can write unicode characters directly. For example Hungarian chars:\n\n http://www.math.bme.hu/~morap/sage_unicode_latex.png\n\nThis feature is important because most of the world uses more than the first 128 characters of ANSII.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6417\n\n",
    "created_at": "2009-06-25T21:53:59Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Unicode in LaTeX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6417",
    "user": "mora"
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

archive/issue_comments_051533.json:
```json
{
    "body": "Attachment [12538.patch](tarball://root/attachments/some-uuid/ticket6417/12538.patch) by mora created at 2009-06-25 21:57:36",
    "created_at": "2009-06-25T21:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6417#issuecomment-51533",
    "user": "mora"
}
```

Attachment [12538.patch](tarball://root/attachments/some-uuid/ticket6417/12538.patch) by mora created at 2009-06-25 21:57:36



---

archive/issue_comments_051534.json:
```json
{
    "body": "Looks good to me except that it doesn't pass doctests.  Apply the patch at #6434 and you're good to go.\n\nSo this patch depends on #6434; modulo that, positive review.",
    "created_at": "2009-06-27T17:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6417#issuecomment-51534",
    "user": "jhpalmieri"
}
```

Looks good to me except that it doesn't pass doctests.  Apply the patch at #6434 and you're good to go.

So this patch depends on #6434; modulo that, positive review.



---

archive/issue_comments_051535.json:
```json
{
    "body": "`sage -t  \"devel/sage-main/sage/misc/latex.py\"` fails after applying this patch.",
    "created_at": "2009-07-03T18:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6417#issuecomment-51535",
    "user": "rlm"
}
```

`sage -t  "devel/sage-main/sage/misc/latex.py"` fails after applying this patch.



---

archive/issue_comments_051536.json:
```json
{
    "body": "> sage -t \"devel/sage-main/sage/misc/latex.py\" fails after applying this patch.\n\nAs my comment says, doctests don't pass until you apply the patch at #6434.  Once #6434 gets in, this one is ready to go.  Is there some way to label this besides \"positive review\" to indicate this?",
    "created_at": "2009-07-03T20:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6417#issuecomment-51536",
    "user": "jhpalmieri"
}
```

> sage -t "devel/sage-main/sage/misc/latex.py" fails after applying this patch.

As my comment says, doctests don't pass until you apply the patch at #6434.  Once #6434 gets in, this one is ready to go.  Is there some way to label this besides "positive review" to indicate this?



---

archive/issue_comments_051537.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n> > sage -t \"devel/sage-main/sage/misc/latex.py\" fails after applying this patch.\n> \n> As my comment says, doctests don't pass until you apply the patch at #6434.\n\nMy bad, wasn't paying enough attention.",
    "created_at": "2009-07-04T00:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6417#issuecomment-51537",
    "user": "rlm"
}
```

Replying to [comment:4 jhpalmieri]:
> > sage -t "devel/sage-main/sage/misc/latex.py" fails after applying this patch.
> 
> As my comment says, doctests don't pass until you apply the patch at #6434.

My bad, wasn't paying enough attention.



---

archive/issue_comments_051538.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-04T00:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6417#issuecomment-51538",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_051539.json:
```json
{
    "body": "See #6464 for a related issue. It concerns Unicode in Notebook worksheets.",
    "created_at": "2009-07-05T02:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6417#issuecomment-51539",
    "user": "mvngu"
}
```

See #6464 for a related issue. It concerns Unicode in Notebook worksheets.
