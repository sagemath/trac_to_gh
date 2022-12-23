# Issue 5767: Bring coverage of plot3d/base.pyx up to 100%

archive/issues_005767.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  jason wcauchois\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5767\n\n",
    "created_at": "2009-04-12T00:00:11Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Bring coverage of plot3d/base.pyx up to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5767",
    "user": "robertwb"
}
```
Assignee: mabshoff

CC:  jason wcauchois



Issue created by migration from https://trac.sagemath.org/ticket/5767





---

archive/issue_comments_045102.json:
```json
{
    "body": "Bouncing to 3.4.2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T03:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45102",
    "user": "mabshoff"
}
```

Bouncing to 3.4.2.

Cheers,

Michael



---

archive/issue_comments_045103.json:
```json
{
    "body": "Before \n\n\n```\nSCORE sage/plot/plot3d/base.pyx: 5% (4 of 78)\n```\n\n\nAfter\n\n\n```\nSCORE sage/plot/plot3d/base.pyx: 87% (69 of 79)\n```\n\n\nI don't know when I'll have time to work on this again, so I think we should at least get these ones in.",
    "created_at": "2009-04-14T11:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45103",
    "user": "robertwb"
}
```

Before 


```
SCORE sage/plot/plot3d/base.pyx: 5% (4 of 78)
```


After


```
SCORE sage/plot/plot3d/base.pyx: 87% (69 of 79)
```


I don't know when I'll have time to work on this again, so I think we should at least get these ones in.



---

archive/issue_comments_045104.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-16T08:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45104",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_045105.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-04T05:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45105",
    "user": "wcauchois"
}
```

Attachment



---

archive/issue_comments_045106.json:
```json
{
    "body": "REFEREE REPORT\n\nExcellent work Robert! This patch applies to Sage 3.4.1 and the doctests are all valid. There were a number of misspellings which I corrected in 5767-referee.patch (I'm sorry I accidentally attached it twice; use either one). Besides that, I have a few concerns:\n\n* It looks like there are some typos due to copy-and-pasing:\n  * On line 446 the documentation for tachyon() says it returns \"an x3d input file\".\n  * On line 1202 the documentation for obj_repr() says it returns \"the x3d representation of a group\".\n  * On line 1230 the documentation for jmol_repr() says it returns \"the x3d representation of a group\".\n* The documentation for jmol_repr on line 657 is somewhat confusing for me, especially when you say that jmol uses the strings to \"construct self\". Could you replace that with something like \"construct a 3D mesh representing this object\"? The same concern applies to the documentation for tachyon_repr and obj_repr.\n* Do you think it would improve the readability of the documentation to replace \"self\" with \"!`self!`\" -- that is, to apply preformatting to it?\n* What's up with the trailing spaces on every line?\n* On line 730 you use the word \"preable\". Is this a typo?",
    "created_at": "2009-05-04T05:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45106",
    "user": "wcauchois"
}
```

REFEREE REPORT

Excellent work Robert! This patch applies to Sage 3.4.1 and the doctests are all valid. There were a number of misspellings which I corrected in 5767-referee.patch (I'm sorry I accidentally attached it twice; use either one). Besides that, I have a few concerns:

* It looks like there are some typos due to copy-and-pasing:
  * On line 446 the documentation for tachyon() says it returns "an x3d input file".
  * On line 1202 the documentation for obj_repr() says it returns "the x3d representation of a group".
  * On line 1230 the documentation for jmol_repr() says it returns "the x3d representation of a group".
* The documentation for jmol_repr on line 657 is somewhat confusing for me, especially when you say that jmol uses the strings to "construct self". Could you replace that with something like "construct a 3D mesh representing this object"? The same concern applies to the documentation for tachyon_repr and obj_repr.
* Do you think it would improve the readability of the documentation to replace "self" with "!`self!`" -- that is, to apply preformatting to it?
* What's up with the trailing spaces on every line?
* On line 730 you use the word "preable". Is this a typo?



---

archive/issue_comments_045107.json:
```json
{
    "body": "Replying to [comment:4 wcauchois]:\n> REFEREE REPORT\n> \n> Excellent work Robert! This patch applies to Sage 3.4.1 <SNIP>\n\nHi Bill, you should **really** always apply against the latest development release. 3.4.1->3.4.2.rc0 was not a large release, but in many other cases there is a rather large, i.e. non-zero chance the patch would either not apply any more or be broken by other changes. There is always a sage.math binary of the latest release development snapshot, so you can use that. Another alternative is to have a review version of Sage that you upgrade from development snapshot to development snapshot.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T06:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45107",
    "user": "mabshoff"
}
```

Replying to [comment:4 wcauchois]:
> REFEREE REPORT
> 
> Excellent work Robert! This patch applies to Sage 3.4.1 <SNIP>

Hi Bill, you should **really** always apply against the latest development release. 3.4.1->3.4.2.rc0 was not a large release, but in many other cases there is a rather large, i.e. non-zero chance the patch would either not apply any more or be broken by other changes. There is always a sage.math binary of the latest release development snapshot, so you can use that. Another alternative is to have a review version of Sage that you upgrade from development snapshot to development snapshot.

Cheers,

Michael



---

archive/issue_comments_045108.json:
```json
{
    "body": "OK, I will do that. I'm sorry for the inconvenience I've caused you! The thing is, I'm building 3.4.2.rc0 right now and its taking a while -- so I figured I'd do this review and then once we addressed the issues we could handle rebasing. But I understand the importance of ensuring compatibility with the latest release.",
    "created_at": "2009-05-04T07:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45108",
    "user": "wcauchois"
}
```

OK, I will do that. I'm sorry for the inconvenience I've caused you! The thing is, I'm building 3.4.2.rc0 right now and its taking a while -- so I figured I'd do this review and then once we addressed the issues we could handle rebasing. But I understand the importance of ensuring compatibility with the latest release.



---

archive/issue_comments_045109.json:
```json
{
    "body": "Replying to [comment:7 wcauchois]:\n> OK, I will do that. I'm sorry for the inconvenience I've caused you! \n\nI have no clue if this is actually a problem, I just wanted to point out how to avoid problems since this has been an issue with your reviews in the past ;)\n\n> The thing is, I'm building 3.4.2.rc0 right now and its taking a while -- so I figured I'd do this review and then once we addressed the issues we could handle rebasing. But I understand the importance of ensuring compatibility with the latest release.\n\nCool.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T07:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45109",
    "user": "mabshoff"
}
```

Replying to [comment:7 wcauchois]:
> OK, I will do that. I'm sorry for the inconvenience I've caused you! 

I have no clue if this is actually a problem, I just wanted to point out how to avoid problems since this has been an issue with your reviews in the past ;)

> The thing is, I'm building 3.4.2.rc0 right now and its taking a while -- so I figured I'd do this review and then once we addressed the issues we could handle rebasing. But I understand the importance of ensuring compatibility with the latest release.

Cool.

Cheers,

Michael



---

archive/issue_comments_045110.json:
```json
{
    "body": "Wow, looks like I wasn't able to spell that day... thanks for looking at this, I'll address the issues you mentioned and post a patch shortly.",
    "created_at": "2009-05-04T17:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45110",
    "user": "robertwb"
}
```

Wow, looks like I wasn't able to spell that day... thanks for looking at this, I'll address the issues you mentioned and post a patch shortly.



---

archive/issue_comments_045111.json:
```json
{
    "body": "apply after other two",
    "created_at": "2009-05-05T20:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45111",
    "user": "robertwb"
}
```

apply after other two



---

archive/issue_comments_045112.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-05T20:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45112",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_045113.json:
```json
{
    "body": "Thanks for looking into this. \n\nReplying to [comment:4 wcauchois]:\n> REFEREE REPORT\n> \n> Excellent work Robert! This patch applies to Sage 3.4.1 and the doctests are all valid. There were a number of misspellings which I corrected in 5767-referee.patch (I'm sorry I accidentally attached it twice; use either one). Besides that, I have a few concerns:\n> \n>  * It looks like there are some typos due to copy-and-pasing:\n>    * On line 446 the documentation for tachyon() says it returns \"an x3d input file\".\n>    * On line 1202 the documentation for obj_repr() says it returns \"the x3d representation of a group\".\n>    * On line 1230 the documentation for jmol_repr() says it returns \"the x3d representation of a group\".\n\nFixed. \n\n>  * The documentation for jmol_repr on line 657 is somewhat confusing for me, especially when you say that jmol uses the strings to \"construct self\". Could you replace that with something like \"construct a 3D mesh representing this object\"? The same concern applies to the documentation for tachyon_repr and obj_repr.\n\nI clarified it.\n\n>  * Do you think it would improve the readability of the documentation to replace \"self\" with \"!`self!`\" -- that is, to apply preformatting to it?\n\nI'm not sure it's worth it. \n\n>  * What's up with the trailing spaces on every line?\n\nSorry, I attached another patch that removes this (but I'm not sure if it'll apply cleanly, if not it's probably not worth it). \n\n>  * On line 730 you use the word \"preable\". Is this a typo?\n\nYep, I meant preamble. Fixed.",
    "created_at": "2009-05-05T20:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45113",
    "user": "robertwb"
}
```

Thanks for looking into this. 

Replying to [comment:4 wcauchois]:
> REFEREE REPORT
> 
> Excellent work Robert! This patch applies to Sage 3.4.1 and the doctests are all valid. There were a number of misspellings which I corrected in 5767-referee.patch (I'm sorry I accidentally attached it twice; use either one). Besides that, I have a few concerns:
> 
>  * It looks like there are some typos due to copy-and-pasing:
>    * On line 446 the documentation for tachyon() says it returns "an x3d input file".
>    * On line 1202 the documentation for obj_repr() says it returns "the x3d representation of a group".
>    * On line 1230 the documentation for jmol_repr() says it returns "the x3d representation of a group".

Fixed. 

>  * The documentation for jmol_repr on line 657 is somewhat confusing for me, especially when you say that jmol uses the strings to "construct self". Could you replace that with something like "construct a 3D mesh representing this object"? The same concern applies to the documentation for tachyon_repr and obj_repr.

I clarified it.

>  * Do you think it would improve the readability of the documentation to replace "self" with "!`self!`" -- that is, to apply preformatting to it?

I'm not sure it's worth it. 

>  * What's up with the trailing spaces on every line?

Sorry, I attached another patch that removes this (but I'm not sure if it'll apply cleanly, if not it's probably not worth it). 

>  * On line 730 you use the word "preable". Is this a typo?

Yep, I meant preamble. Fixed.



---

archive/issue_comments_045114.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-06T06:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45114",
    "user": "wcauchois"
}
```

Attachment



---

archive/issue_comments_045115.json:
```json
{
    "body": "REFEREE REPORT:\n\nLooking over the code again, I noticed a few other instances where \"concatenate\" was spelled incorrectly. I fixed these in 5767-refree2.patch. With this and Robert's changes, positive review.\n\n(By the way Robert: Mercurial queues is awesome! I made 5767-all.patch with qfold :).)",
    "created_at": "2009-05-06T06:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45115",
    "user": "wcauchois"
}
```

REFEREE REPORT:

Looking over the code again, I noticed a few other instances where "concatenate" was spelled incorrectly. I fixed these in 5767-refree2.patch. With this and Robert's changes, positive review.

(By the way Robert: Mercurial queues is awesome! I made 5767-all.patch with qfold :).)



---

archive/issue_comments_045116.json:
```json
{
    "body": "Note that your 5767-all.patch lost all authorship information...",
    "created_at": "2009-05-06T06:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45116",
    "user": "robertwb"
}
```

Note that your 5767-all.patch lost all authorship information...



---

archive/issue_comments_045117.json:
```json
{
    "body": "Attachment\n\nthis patch incorporates ALL of the changes; apply to sage 3.4.2",
    "created_at": "2009-05-06T06:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45117",
    "user": "wcauchois"
}
```

Attachment

this patch incorporates ALL of the changes; apply to sage 3.4.2



---

archive/issue_comments_045118.json:
```json
{
    "body": "Replying to [comment:12 robertwb]:\n> Note that your 5767-all.patch lost all authorship information...\n\nOh shoot! OK, I fixed it manually and it works. I think that MQ unfortunately does not preserve the metadata usually associated with a changeset.",
    "created_at": "2009-05-06T07:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45118",
    "user": "wcauchois"
}
```

Replying to [comment:12 robertwb]:
> Note that your 5767-all.patch lost all authorship information...

Oh shoot! OK, I fixed it manually and it works. I think that MQ unfortunately does not preserve the metadata usually associated with a changeset.



---

archive/issue_comments_045119.json:
```json
{
    "body": "I'm pretty sure queues can be used to preserve metadata using qfold, but that's fine. Thanks for looking at this. \n\n- Robert",
    "created_at": "2009-05-06T07:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45119",
    "user": "robertwb"
}
```

I'm pretty sure queues can be used to preserve metadata using qfold, but that's fine. Thanks for looking at this. 

- Robert



---

archive/issue_comments_045120.json:
```json
{
    "body": "Merged 5767-all.patch in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-07T07:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45120",
    "user": "mabshoff"
}
```

Merged 5767-all.patch in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_045121.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-07T07:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5767#issuecomment-45121",
    "user": "mabshoff"
}
```

Resolution: fixed
