# Issue 5920: Implements view(object, format='pdf')

archive/issues_005920.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat\n\nKeywords: latex view\n\nThis patch allows for:\n\n```\nsage: view(object, format = \"pdf\")\n```\n\n\nTypical use cases:\n- you prefer your pdf browser\n- view latex snippets which are not displayed in dvi viewers (e.g. tikzpicture)\n\nShould this use 'output=' rather than 'format='\n\nPotential extensions: `view(object, format='png')`, `view(object, format='html')`\n\nIssue created by migration from https://trac.sagemath.org/ticket/5920\n\n",
    "created_at": "2009-04-28T19:35:58Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "title": "Implements view(object, format='pdf')",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5920",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat

Keywords: latex view

This patch allows for:

```
sage: view(object, format = "pdf")
```


Typical use cases:
- you prefer your pdf browser
- view latex snippets which are not displayed in dvi viewers (e.g. tikzpicture)

Should this use 'output=' rather than 'format='

Potential extensions: `view(object, format='png')`, `view(object, format='html')`

Issue created by migration from https://trac.sagemath.org/ticket/5920





---

archive/issue_comments_046788.json:
```json
{
    "body": "Changing keywords from \"latex view\" to \"view, latex, dvi, pdf\".",
    "created_at": "2009-04-28T19:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46788",
    "user": "nthiery"
}
```

Changing keywords from "latex view" to "view, latex, dvi, pdf".



---

archive/issue_comments_046789.json:
```json
{
    "body": "It should be \n\n```\nsage: view(object, viewer='pdf')\n```\n\nfor consistency with all the 3d plotting code, which has viewer='tachyon' and viewer='jmol' options.",
    "created_at": "2009-04-28T22:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46789",
    "user": "was"
}
```

It should be 

```
sage: view(object, viewer='pdf')
```

for consistency with all the 3d plotting code, which has viewer='tachyon' and viewer='jmol' options.



---

archive/issue_comments_046790.json:
```json
{
    "body": "Replying to [comment:4 was]:\n> It should be \n> {{{\n> sage: view(object, viewer='pdf')\n> }}}\n> for consistency with all the 3d plotting code, which has viewer='tachyon' and viewer='jmol' options.\n\nHmm, how can you give this a positive review in light of this comment? I would much rather have the trivial rename in the original patch before merging it.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-28T23:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46790",
    "user": "mabshoff"
}
```

Replying to [comment:4 was]:
> It should be 
> {{{
> sage: view(object, viewer='pdf')
> }}}
> for consistency with all the 3d plotting code, which has viewer='tachyon' and viewer='jmol' options.

Hmm, how can you give this a positive review in light of this comment? I would much rather have the trivial rename in the original patch before merging it.

Cheers,

Michael



---

archive/issue_comments_046791.json:
```json
{
    "body": "Done in the new update patch. I switched back to needs review, though a quick glance from any of the two of you should do.",
    "created_at": "2009-04-28T23:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46791",
    "user": "nthiery"
}
```

Done in the new update patch. I switched back to needs review, though a quick glance from any of the two of you should do.



---

archive/issue_comments_046792.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-04-29T00:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46792",
    "user": "AlexGhitza"
}
```

Looks good.



---

archive/issue_comments_046793.json:
```json
{
    "body": "Replying to [comment:10 was]:\nWhich work does it still need?",
    "created_at": "2009-04-29T06:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46793",
    "user": "nthiery"
}
```

Replying to [comment:10 was]:
Which work does it still need?



---

archive/issue_comments_046794.json:
```json
{
    "body": "Replying to [comment:11 nthiery]:\n> Replying to [comment:10 was]:\n> Which work does it still need?\n\nThis had a positive review by Alex since you addressed William's concern. Why did you change that?\n\nReinstating positive review.\n\nCheers,\n\nMichaell",
    "created_at": "2009-04-29T11:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46794",
    "user": "mabshoff"
}
```

Replying to [comment:11 nthiery]:
> Replying to [comment:10 was]:
> Which work does it still need?

This had a positive review by Alex since you addressed William's concern. Why did you change that?

Reinstating positive review.

Cheers,

Michaell



---

archive/issue_comments_046795.json:
```json
{
    "body": "Replying to [comment:12 mabshoff]:\n> This had a positive review by Alex since you addressed William's concern. Why did you change that?\n\nWilliam changed that, and that's precisely what I was puzzled about.\n\n> Reinstating positive review.\n\nThanks.",
    "created_at": "2009-04-29T21:34:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46795",
    "user": "nthiery"
}
```

Replying to [comment:12 mabshoff]:
> This had a positive review by Alex since you addressed William's concern. Why did you change that?

William changed that, and that's precisely what I was puzzled about.

> Reinstating positive review.

Thanks.



---

archive/issue_comments_046796.json:
```json
{
    "body": "This one needs a rebase post 3.4.2:\n\n```\nsage-3.4.2.rc0/devel/sage$ hg import trac_5920_view_as_pdf-5920-nt.patch \napplying trac_5920_view_as_pdf-5920-nt.patch\npatching file sage/misc/latex.py\nHunk #1 succeeded at 894 with fuzz 2 (offset 369 lines).\nHunk #4 FAILED at 575\n1 out of 6 hunks FAILED -- saving rejects to file sage/misc/latex.py.rej\nabort: patch failed to apply\n```\n\nOnce the rebase has been done the positive review can be reinstated [assuming doctests pass obviously ;)].\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T07:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46796",
    "user": "mabshoff"
}
```

This one needs a rebase post 3.4.2:

```
sage-3.4.2.rc0/devel/sage$ hg import trac_5920_view_as_pdf-5920-nt.patch 
applying trac_5920_view_as_pdf-5920-nt.patch
patching file sage/misc/latex.py
Hunk #1 succeeded at 894 with fuzz 2 (offset 369 lines).
Hunk #4 FAILED at 575
1 out of 6 hunks FAILED -- saving rejects to file sage/misc/latex.py.rej
abort: patch failed to apply
```

Once the rebase has been done the positive review can be reinstated [assuming doctests pass obviously ;)].

Cheers,

Michael



---

archive/issue_comments_046797.json:
```json
{
    "body": "Replying to [comment:14 mabshoff]:\n> This one needs a rebase post 3.4.2:\n\nDone\n\nPfiew. The workflow overhead has been large on this patch ...",
    "created_at": "2009-04-30T17:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46797",
    "user": "nthiery"
}
```

Replying to [comment:14 mabshoff]:
> This one needs a rebase post 3.4.2:

Done

Pfiew. The workflow overhead has been large on this patch ...



---

archive/issue_comments_046798.json:
```json
{
    "body": "Oops, please ignore the updated patch for a second",
    "created_at": "2009-04-30T17:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46798",
    "user": "nthiery"
}
```

Oops, please ignore the updated patch for a second



---

archive/issue_comments_046799.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-30T17:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46799",
    "user": "nthiery"
}
```

Attachment



---

archive/issue_comments_046800.json:
```json
{
    "body": "Replying to [comment:16 nthiery]:\n> Oops, please ignore the updated patch for a second\n\nFinally good to go!",
    "created_at": "2009-04-30T17:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46800",
    "user": "nthiery"
}
```

Replying to [comment:16 nthiery]:
> Oops, please ignore the updated patch for a second

Finally good to go!



---

archive/issue_comments_046801.json:
```json
{
    "body": "Marked as needing review again, i.e. that it applies and passes doctests.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T22:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46801",
    "user": "mabshoff"
}
```

Marked as needing review again, i.e. that it applies and passes doctests.

Cheers,

Michael



---

archive/issue_comments_046802.json:
```json
{
    "body": "It applies cleanly to 3.4.2.rc0, passes doctests, and does what it should when I try it out.",
    "created_at": "2009-05-01T00:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46802",
    "user": "AlexGhitza"
}
```

It applies cleanly to 3.4.2.rc0, passes doctests, and does what it should when I try it out.



---

archive/issue_comments_046803.json:
```json
{
    "body": "Replying to [comment:15 nthiery]:\n\n> Pfiew. The workflow overhead has been large on this patch ...\n\nYeah, given the amount of code this didn't go as smoothly as it should have :)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-01T04:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46803",
    "user": "mabshoff"
}
```

Replying to [comment:15 nthiery]:

> Pfiew. The workflow overhead has been large on this patch ...

Yeah, given the amount of code this didn't go as smoothly as it should have :)

Cheers,

Michael



---

archive/issue_comments_046804.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-07T07:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46804",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_046805.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-07T07:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5920#issuecomment-46805",
    "user": "mabshoff"
}
```

Resolution: fixed
