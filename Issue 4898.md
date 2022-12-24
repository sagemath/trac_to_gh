# Issue 4898: [with patch; needs review] Add style and labels to contour_plot()

archive/issues_004898.json:
```json
{
    "body": "Assignee: abergeron\n\nCC:  wcauchois @jasongrout\n\nThis patch add the option of styling lines, either individually or all at once, and adding contour level labels.\n\nAnother one is coming to support this in combination with #2770.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4898\n\n",
    "created_at": "2008-12-31T21:49:27Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "[with patch; needs review] Add style and labels to contour_plot()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4898",
    "user": "abergeron"
}
```
Assignee: abergeron

CC:  wcauchois @jasongrout

This patch add the option of styling lines, either individually or all at once, and adding contour level labels.

Another one is coming to support this in combination with #2770.

Issue created by migration from https://trac.sagemath.org/ticket/4898





---

archive/issue_comments_037143.json:
```json
{
    "body": "I think it would just be better to wait until #2770 and #4884 are merged since they conflict with this.  I'll post an updated patch then.",
    "created_at": "2008-12-31T22:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37143",
    "user": "abergeron"
}
```

I think it would just be better to wait until #2770 and #4884 are merged since they conflict with this.  I'll post an updated patch then.



---

archive/issue_comments_037144.json:
```json
{
    "body": "Attachment [trac_4898.patch](tarball://root/attachments/some-uuid/ticket4898/trac_4898.patch) by abergeron created at 2009-01-24 05:02:25\n\nUpdate patch is posted.  Start reviewing!",
    "created_at": "2009-01-24T05:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37144",
    "user": "abergeron"
}
```

Attachment [trac_4898.patch](tarball://root/attachments/some-uuid/ticket4898/trac_4898.patch) by abergeron created at 2009-01-24 05:02:25

Update patch is posted.  Start reviewing!



---

archive/issue_comments_037145.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-24T05:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37145",
    "user": "abergeron"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037146.json:
```json
{
    "body": "What was this updated to?  I get conflicts applying it to 3.3alpha3.",
    "created_at": "2009-02-11T05:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37146",
    "user": "@jasongrout"
}
```

What was this updated to?  I get conflicts applying it to 3.3alpha3.



---

archive/issue_comments_037147.json:
```json
{
    "body": "I tried applying it to 3.3rc0:\n\n\n```\njason@sage:~$ patch contour_plot.py < trac_4898.patch \npatching file contour_plot.py\nHunk #2 FAILED at 53.\nHunk #3 FAILED at 75.\nHunk #4 FAILED at 136.\nHunk #5 succeeded at 167 (offset -1 lines).\nHunk #6 succeeded at 180 (offset -1 lines).\nHunk #7 FAILED at 226.\nHunk #8 succeeded at 272 (offset -2 lines).\nHunk #9 succeeded at 293 (offset -2 lines).\nHunk #10 succeeded at 308 (offset -2 lines).\nHunk #11 succeeded at 317 (offset -2 lines).\nHunk #12 succeeded at 345 (offset -2 lines).\n4 out of 12 hunks FAILED -- saving rejects to file contour_plot.py.rej\n```\n",
    "created_at": "2009-02-11T06:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37147",
    "user": "@jasongrout"
}
```

I tried applying it to 3.3rc0:


```
jason@sage:~$ patch contour_plot.py < trac_4898.patch 
patching file contour_plot.py
Hunk #2 FAILED at 53.
Hunk #3 FAILED at 75.
Hunk #4 FAILED at 136.
Hunk #5 succeeded at 167 (offset -1 lines).
Hunk #6 succeeded at 180 (offset -1 lines).
Hunk #7 FAILED at 226.
Hunk #8 succeeded at 272 (offset -2 lines).
Hunk #9 succeeded at 293 (offset -2 lines).
Hunk #10 succeeded at 308 (offset -2 lines).
Hunk #11 succeeded at 317 (offset -2 lines).
Hunk #12 succeeded at 345 (offset -2 lines).
4 out of 12 hunks FAILED -- saving rejects to file contour_plot.py.rej
```




---

archive/issue_comments_037148.json:
```json
{
    "body": "abergeron: what is the status of your work on this patch (and how can we help?)  It looks like it is very useful.  Thanks for doing this!",
    "created_at": "2009-05-30T08:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37148",
    "user": "@jasongrout"
}
```

abergeron: what is the status of your work on this patch (and how can we help?)  It looks like it is very useful.  Thanks for doing this!



---

archive/issue_comments_037149.json:
```json
{
    "body": "It is on my TODO list (which is rather long) and which I started attacking since the end of my finals.\n\nI don't have a recent version of Sage on my machine right now so it'll be a couple of days before I can rebase it.\n\nIf somebody else wants to do it in the meantime, that could help.",
    "created_at": "2009-05-31T02:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37149",
    "user": "abergeron"
}
```

It is on my TODO list (which is rather long) and which I started attacking since the end of my finals.

I don't have a recent version of Sage on my machine right now so it'll be a couple of days before I can rebase it.

If somebody else wants to do it in the meantime, that could help.



---

archive/issue_comments_037150.json:
```json
{
    "body": "Here is a somewhat significant rebase based on 4.1.2.alpha2, also more or less ReSTified.  There have been some definite changes in this file and matplotlib since then, so a few things now behave slightly differently from the original patch; however, I think they are just different, not wrong (especially when it comes to axes).   In particular I hope I got the option popping in the right spots.\n\nGreat thanks to Arnaud's work here - especially labeling contours is a great thing to have now!",
    "created_at": "2009-10-05T20:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37150",
    "user": "@kcrisman"
}
```

Here is a somewhat significant rebase based on 4.1.2.alpha2, also more or less ReSTified.  There have been some definite changes in this file and matplotlib since then, so a few things now behave slightly differently from the original patch; however, I think they are just different, not wrong (especially when it comes to axes).   In particular I hope I got the option popping in the right spots.

Great thanks to Arnaud's work here - especially labeling contours is a great thing to have now!



---

archive/issue_comments_037151.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-06T20:52:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37151",
    "user": "@jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_037152.json:
```json
{
    "body": "Unfortunately, it still needs more rebasing.  Here is the result of applying it to 4.1.2.rc0:\n\n\n```\njason@sage:~/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/devel/sage/sage$ hg qpush\napplying trac_4898-contour-labels-rebase.patch\npatching file sage/plot/contour_plot.py\nHunk #11 succeeded at 517 with fuzz 1 (offset 3 lines).\nHunk #12 FAILED at 549\n1 out of 12 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nErrors during apply, please fix and refresh trac_4898-contour-labels-rebase.patch\n```\n\n\nI'm excited for this to get in!",
    "created_at": "2009-10-06T20:52:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37152",
    "user": "@jasongrout"
}
```

Unfortunately, it still needs more rebasing.  Here is the result of applying it to 4.1.2.rc0:


```
jason@sage:~/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/devel/sage/sage$ hg qpush
applying trac_4898-contour-labels-rebase.patch
patching file sage/plot/contour_plot.py
Hunk #11 succeeded at 517 with fuzz 1 (offset 3 lines).
Hunk #12 FAILED at 549
1 out of 12 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_4898-contour-labels-rebase.patch
```


I'm excited for this to get in!



---

archive/issue_comments_037153.json:
```json
{
    "body": "Attachment [trac_4898-contour-labels-rebase.2.patch](tarball://root/attachments/some-uuid/ticket4898/trac_4898-contour-labels-rebase.2.patch) by @kcrisman created at 2009-10-08 02:39:07\n\nBased on 4.1.2.rc1.alpha3",
    "created_at": "2009-10-08T02:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37153",
    "user": "@kcrisman"
}
```

Attachment [trac_4898-contour-labels-rebase.2.patch](tarball://root/attachments/some-uuid/ticket4898/trac_4898-contour-labels-rebase.2.patch) by @kcrisman created at 2009-10-08 02:39:07

Based on 4.1.2.rc1.alpha3



---

archive/issue_comments_037154.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-08T02:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37154",
    "user": "@kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_037155.json:
```json
{
    "body": "Hmm, I had intended to delete the previous version...\n\nAnyway, there was a one-character (in fact, one space) thing that prevented it from applying.  So silly.  It should actually apply to rc0 as well, I suspect, but you never know... anyway, can you check that if the only issue is a space, that you fix it manually to at least see if doctests pass?",
    "created_at": "2009-10-08T02:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37155",
    "user": "@kcrisman"
}
```

Hmm, I had intended to delete the previous version...

Anyway, there was a one-character (in fact, one space) thing that prevented it from applying.  So silly.  It should actually apply to rc0 as well, I suspect, but you never know... anyway, can you check that if the only issue is a space, that you fix it manually to at least see if doctests pass?



---

archive/issue_comments_037156.json:
```json
{
    "body": "Attachment [trac_4898-contour-labels-rebase.patch](tarball://root/attachments/some-uuid/ticket4898/trac_4898-contour-labels-rebase.patch) by @kcrisman created at 2009-11-05 19:55:56\n\nBased on 4.2 - apply only this!",
    "created_at": "2009-11-05T19:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37156",
    "user": "@kcrisman"
}
```

Attachment [trac_4898-contour-labels-rebase.patch](tarball://root/attachments/some-uuid/ticket4898/trac_4898-contour-labels-rebase.patch) by @kcrisman created at 2009-11-05 19:55:56

Based on 4.2 - apply only this!



---

archive/issue_comments_037157.json:
```json
{
    "body": "I tweaked two of the defaults and add a bit more documentation.  This is great; I'm excited to see this go in!",
    "created_at": "2009-11-10T16:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37157",
    "user": "@jasongrout"
}
```

I tweaked two of the defaults and add a bit more documentation.  This is great; I'm excited to see this go in!



---

archive/issue_comments_037158.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-10T16:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37158",
    "user": "@jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_037159.json:
```json
{
    "body": "Attachment [trac-4898-reviewer.patch](tarball://root/attachments/some-uuid/ticket4898/trac-4898-reviewer.patch) by @jasongrout created at 2009-11-10 17:16:00\n\napply on top of previous patch",
    "created_at": "2009-11-10T17:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37159",
    "user": "@jasongrout"
}
```

Attachment [trac-4898-reviewer.patch](tarball://root/attachments/some-uuid/ticket4898/trac-4898-reviewer.patch) by @jasongrout created at 2009-11-10 17:16:00

apply on top of previous patch



---

archive/issue_comments_037160.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T06:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4898#issuecomment-37160",
    "user": "@mwhansen"
}
```

Resolution: fixed
