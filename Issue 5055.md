# Issue 5055: Trivial but fatal typo in interact documentation

archive/issues_005055.json:
```json
{
    "body": "Assignee: @itolkov\n\nAbout halfway through the documentation of interact, there is this example:\n\n```\nsage: @interact\n... def _(title=[\"A Plot Demo\", \"Something silly\", \"something tricky\" , a=input_box(sin(x*sin(x*sin(x))), 'function'),\n...     clr = Color('red'), thickness=[1..30], zoom=(1,0.95,..,0.1), plot_points=(200..2000)):\n...     html('<h1 align=center>%s</h1>'%title)\n...     print plot_points\n...     show(plot(a, -zoom*pi,zoom*pi, color=clr, thickness=thickness, plot_points=plot_points))\n<html>...\n```\n\nThere should be a ] after the \" after the word tricky.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5055\n\n",
    "created_at": "2009-01-22T15:58:43Z",
    "labels": [
        "interact",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Trivial but fatal typo in interact documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5055",
    "user": "@kcrisman"
}
```
Assignee: @itolkov

About halfway through the documentation of interact, there is this example:

```
sage: @interact
... def _(title=["A Plot Demo", "Something silly", "something tricky" , a=input_box(sin(x*sin(x*sin(x))), 'function'),
...     clr = Color('red'), thickness=[1..30], zoom=(1,0.95,..,0.1), plot_points=(200..2000)):
...     html('<h1 align=center>%s</h1>'%title)
...     print plot_points
...     show(plot(a, -zoom*pi,zoom*pi, color=clr, thickness=thickness, plot_points=plot_points))
<html>...
```

There should be a ] after the " after the word tricky.

Issue created by migration from https://trac.sagemath.org/ticket/5055





---

archive/issue_comments_038510.json:
```json
{
    "body": "Changing assignee from @itolkov to @mwhansen.",
    "created_at": "2009-01-23T09:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5055#issuecomment-38510",
    "user": "@mwhansen"
}
```

Changing assignee from @itolkov to @mwhansen.



---

archive/issue_comments_038511.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T09:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5055#issuecomment-38511",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038512.json:
```json
{
    "body": "Where are you seeing this error?  I can't find it in any of the official Sage files.  I'd vote for marking this as invalid.",
    "created_at": "2009-01-23T09:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5055#issuecomment-38512",
    "user": "@mwhansen"
}
```

Where are you seeing this error?  I can't find it in any of the official Sage files.  I'd vote for marking this as invalid.



---

archive/issue_comments_038513.json:
```json
{
    "body": "Replying to [comment:1 mhansen]:\n> Where are you seeing this error?  I can't find it in any of the official Sage files.  I'd vote for marking this as invalid.\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: interact?\n```\n\n| Sage Version 3.3.alpha0, Release Date: 2009-01-19                  |\n| Type notebook() for the GUI, and license() for information.        |\nAnd then it comes.  Also, just above that, there is something about an interact \"campus\", which sounds odd to me... Anyway, this is pretty valid.  Though trivial.  \n\nAccording to search_src('tricky'), it is in server/notebook/interact.py",
    "created_at": "2009-01-23T18:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5055#issuecomment-38513",
    "user": "@kcrisman"
}
```

Replying to [comment:1 mhansen]:
> Where are you seeing this error?  I can't find it in any of the official Sage files.  I'd vote for marking this as invalid.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: interact?
```

| Sage Version 3.3.alpha0, Release Date: 2009-01-19                  |
| Type notebook() for the GUI, and license() for information.        |
And then it comes.  Also, just above that, there is something about an interact "campus", which sounds odd to me... Anyway, this is pretty valid.  Though trivial.  

According to search_src('tricky'), it is in server/notebook/interact.py



---

archive/issue_comments_038514.json:
```json
{
    "body": "Or, rather, it seems to be valid in a disturbing way...\n\n> According to search_src('tricky'), it is in server/notebook/interact.py\n\nWeirdly, when I actually look at that file, I see both [].  So now the question is why doesn't this appear when I type\n\n```\ninteract?\n```\n\nInstead, there is a space showing where the ] is in the actual file.  But that is probably not for a typo ticket, so if it's reproducible it should be a separate ticket.\n\nAttached is a patch fixing the word \"campus\" to \"canvas\", though, which **is** a trivial typo in the interact documentation.",
    "created_at": "2009-01-23T20:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5055#issuecomment-38514",
    "user": "@kcrisman"
}
```

Or, rather, it seems to be valid in a disturbing way...

> According to search_src('tricky'), it is in server/notebook/interact.py

Weirdly, when I actually look at that file, I see both [].  So now the question is why doesn't this appear when I type

```
interact?
```

Instead, there is a space showing where the ] is in the actual file.  But that is probably not for a typo ticket, so if it's reproducible it should be a separate ticket.

Attached is a patch fixing the word "campus" to "canvas", though, which **is** a trivial typo in the interact documentation.



---

archive/issue_comments_038515.json:
```json
{
    "body": "Based on 3.3.alpha0",
    "created_at": "2009-01-23T20:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5055#issuecomment-38515",
    "user": "@kcrisman"
}
```

Based on 3.3.alpha0



---

archive/issue_comments_038516.json:
```json
{
    "body": "Attachment [trac_5055.patch](tarball://root/attachments/some-uuid/ticket5055/trac_5055.patch) by @kcrisman created at 2009-01-24 02:49:57",
    "created_at": "2009-01-24T02:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5055#issuecomment-38516",
    "user": "@kcrisman"
}
```

Attachment [trac_5055.patch](tarball://root/attachments/some-uuid/ticket5055/trac_5055.patch) by @kcrisman created at 2009-01-24 02:49:57



---

archive/issue_comments_038517.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T14:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5055#issuecomment-38517",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_038518.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T14:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5055#issuecomment-38518",
    "user": "mabshoff"
}
```

Resolution: fixed
