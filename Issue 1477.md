# Issue 1477: notebook -- make it unicode aware

archive/issues_001477.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n\n\nOn Dec 12, 2007 7:48 AM, greg2k4@mail.ru <greg2k4@mail.ru> wrote:\n> \n> Hi all,\n> \n> I need to use non-english characters (in comments) in Notebook\n> worksheet.\n> While working, they're shown w/o problem, but if I save (\"download to\n> file\") worksheet, then close\n> SAGE, then open again and load .sws file, sometimes (!) I see just\n> unicode codes (like %u4041)\n> instead of my chars.\n> Strange, but sometimes they're loaded correctly...\n> I'm using Sage v 2.8.13 (VMware) under winXP Pro.\n> \n> Am I missing something?\n\nNo, more likely I'm missing something in how that functionality\nwas implemened.  You're probably one of the first ever Russian uses of \nSage, and we have had very little testing of Unicode in Sage. \nHopefully fixing the above is for developers just a \nmatter of changing a few lines in \n\n  SAGE_ROOT/devel/sage/sage/server/noteboook\n\nthat relate to loading and saving the file worksheet.txt. \n   \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1477\n\n",
    "created_at": "2007-12-12T16:37:05Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- make it unicode aware",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1477",
    "user": "was"
}
```
Assignee: boothby


```


On Dec 12, 2007 7:48 AM, greg2k4@mail.ru <greg2k4@mail.ru> wrote:
> 
> Hi all,
> 
> I need to use non-english characters (in comments) in Notebook
> worksheet.
> While working, they're shown w/o problem, but if I save ("download to
> file") worksheet, then close
> SAGE, then open again and load .sws file, sometimes (!) I see just
> unicode codes (like %u4041)
> instead of my chars.
> Strange, but sometimes they're loaded correctly...
> I'm using Sage v 2.8.13 (VMware) under winXP Pro.
> 
> Am I missing something?

No, more likely I'm missing something in how that functionality
was implemened.  You're probably one of the first ever Russian uses of 
Sage, and we have had very little testing of Unicode in Sage. 
Hopefully fixing the above is for developers just a 
matter of changing a few lines in 

  SAGE_ROOT/devel/sage/sage/server/noteboook

that relate to loading and saving the file worksheet.txt. 
   
```


Issue created by migration from https://trac.sagemath.org/ticket/1477





---

archive/issue_comments_009503.json:
```json
{
    "body": "\n```\n> Could you summarize the situation with rendering problems?  Is it as follows:\n> (1) When you try to put them in input cells, they get corrupted on load/save.\n\nTo be correct, they're replaced by \"non-browser\"  unicode codes (like\n%u0440 instead of &#x0440; )\n\n> (2) Using edit mode, unicode not in ``'s gets saved just fine.\n\nYes, as they are NOT processed (as I understand) and get saved \"as\nis\".\n\n\n> Oh, by the way, when you're entering html in edit mode, you can just do,\n> e.g., consider $y^2 = x^3 + \\sqrt{x}$ and the formula will get typeset\n> using jsmath.\n\nThanks, can be helpful when writing my materials.\n```\n",
    "created_at": "2007-12-13T18:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1477#issuecomment-9503",
    "user": "was"
}
```


```
> Could you summarize the situation with rendering problems?  Is it as follows:
> (1) When you try to put them in input cells, they get corrupted on load/save.

To be correct, they're replaced by "non-browser"  unicode codes (like
%u0440 instead of &#x0440; )

> (2) Using edit mode, unicode not in ``'s gets saved just fine.

Yes, as they are NOT processed (as I understand) and get saved "as
is".


> Oh, by the way, when you're entering html in edit mode, you can just do,
> e.g., consider $y^2 = x^3 + \sqrt{x}$ and the formula will get typeset
> using jsmath.

Thanks, can be helpful when writing my materials.
```




---

archive/issue_comments_009504.json:
```json
{
    "body": "Hmm, didn't we fix this by adding UTF-8 support?\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T22:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1477#issuecomment-9504",
    "user": "mabshoff"
}
```

Hmm, didn't we fix this by adding UTF-8 support?

Cheers,

Michael



---

archive/issue_comments_009505.json:
```json
{
    "body": "This sounds very much like #2896. It is not fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T05:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1477#issuecomment-9505",
    "user": "mabshoff"
}
```

This sounds very much like #2896. It is not fixed.

Cheers,

Michael



---

archive/issue_comments_009506.json:
```json
{
    "body": "Sage's support for Unicode and UTF-8 in the notebook is _awful_.  It will take a bit of work to fix this.  For starters, we should be using encodeURIComponent in the Javascript instead of escape since escape fails miserably for non-ASCII characters.\n\nI'll look into this more once the templating is done.  There's too many strings floating as it is.",
    "created_at": "2009-01-19T13:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1477#issuecomment-9506",
    "user": "mhansen"
}
```

Sage's support for Unicode and UTF-8 in the notebook is _awful_.  It will take a bit of work to fix this.  For starters, we should be using encodeURIComponent in the Javascript instead of escape since escape fails miserably for non-ASCII characters.

I'll look into this more once the templating is done.  There's too many strings floating as it is.



---

archive/issue_comments_009507.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:49:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1477#issuecomment-9507",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_009508.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T21:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1477#issuecomment-9508",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009509.json:
```json
{
    "body": "Fixed via #4547 and #5211.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T21:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1477#issuecomment-9509",
    "user": "mabshoff"
}
```

Fixed via #4547 and #5211.

Cheers,

Michael
