# Issue 7625: include new version of sagenb (0.4.5)

archive/issues_007625.json:
```json
{
    "body": "Assignee: was\n\nIt's here:\n\n  http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.5.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/7625\n\n",
    "created_at": "2009-12-08T18:03:08Z",
    "labels": [
        "notebook",
        "blocker",
        "enhancement"
    ],
    "title": "include new version of sagenb (0.4.5)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7625",
    "user": "was"
}
```
Assignee: was

It's here:

  http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.5.spkg

Issue created by migration from https://trac.sagemath.org/ticket/7625





---

archive/issue_comments_065144.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-08T18:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65144",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065145.json:
```json
{
    "body": "\n```\n#7495: William Stein and Mitesh Patel: notebook: fix massive security vulnerability and get rid of all possible \"internal server errors\" when doing \"Data --> Upload or attach file [Reviewed by Mitesh Patel]\n#3619: William Stein: notebook -- record date & time each user logs in [Reviewed by Tim Dumol]\n#3849: William Stein and Mitesh Patel: notebook --get rid of internal server errors when uploading a worksheet [Reviewed by Tim Dumol]\n#7402: Tim Dumol: notebook -- Use `pkg_resources` to locate `DATA` directory [Reviwed by Mitesh Patel]\n#7428: Mitesh Patel: worksheets listed on published list only after they are republished, but not after initial publication [Reviewed by Tim Dumol]\n#7444: Mitesh Patel: Broken: searching published worksheets after publishing a worksheet for the first time [Reviewed by Tim Dumol]\n#7467: Tim Dumol: Make SageNB use `setuptools` instead of `distutils` [Reviewed by Mitesh Patel]\n#7390: Mitesh Patel: HTML notebook test report [Reviewed by Tim Dumol]\n#7470: Tim Dumol: SageNB -- Minor docstring fixes for `js.py` [Reviewed by Mitesh Patel]\n```\n",
    "created_at": "2009-12-08T18:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65145",
    "user": "was"
}
```


```
#7495: William Stein and Mitesh Patel: notebook: fix massive security vulnerability and get rid of all possible "internal server errors" when doing "Data --> Upload or attach file [Reviewed by Mitesh Patel]
#3619: William Stein: notebook -- record date & time each user logs in [Reviewed by Tim Dumol]
#3849: William Stein and Mitesh Patel: notebook --get rid of internal server errors when uploading a worksheet [Reviewed by Tim Dumol]
#7402: Tim Dumol: notebook -- Use `pkg_resources` to locate `DATA` directory [Reviwed by Mitesh Patel]
#7428: Mitesh Patel: worksheets listed on published list only after they are republished, but not after initial publication [Reviewed by Tim Dumol]
#7444: Mitesh Patel: Broken: searching published worksheets after publishing a worksheet for the first time [Reviewed by Tim Dumol]
#7467: Tim Dumol: Make SageNB use `setuptools` instead of `distutils` [Reviewed by Mitesh Patel]
#7390: Mitesh Patel: HTML notebook test report [Reviewed by Tim Dumol]
#7470: Tim Dumol: SageNB -- Minor docstring fixes for `js.py` [Reviewed by Mitesh Patel]
```




---

archive/issue_comments_065146.json:
```json
{
    "body": "I just posted the release notes for this above.",
    "created_at": "2009-12-08T18:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65146",
    "user": "was"
}
```

I just posted the release notes for this above.



---

archive/issue_comments_065147.json:
```json
{
    "body": "This looks good to me, apart from the comedy of errors that is the notebook settings page.  Also, 14 out of 15 Selenium tests still pass (cf. #7455).\n\nI think Dr. Palmieri reviewed #7470.\n\nPositive review, pending Tim's confirmation?",
    "created_at": "2009-12-08T21:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65147",
    "user": "mpatel"
}
```

This looks good to me, apart from the comedy of errors that is the notebook settings page.  Also, 14 out of 15 Selenium tests still pass (cf. #7455).

I think Dr. Palmieri reviewed #7470.

Positive review, pending Tim's confirmation?



---

archive/issue_comments_065148.json:
```json
{
    "body": "Hi, \n\nI merged in 9 more patches to make sagenb-0.4.6, which does fix the notebook settings page issues.  We should release sagenb-0.4.6 instead: \n\n   http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.5.spkg\n\n\n```\n#5100: Tim Dumol: worksheets: can't empty the trash (safari only?) [Reviewed by John Palmieri and William Stein]\n#3733: William Stein: document notebook.css; I also sphinxified the notebook? docstring [Reviewed by Tim Dumol]\n#7433: Tim Dumol: Changing title of worksheet changes title of corresponding published worksheet [Reviewed by William Stein]\n#7455: Tim Dumol: Searching on Log page does not work [Reviewed by William Stein]\n#4714: Mitesh Patel: use easy/load.js when loading jsmath in the notebook [Reviewed by William Stein]\n#7267: Mitesh Patel: Add a compact color picker to SageNB [Reviewed by William Stein and Tim Dumol]\n#7376: Mitesh Patel: searching published worksheets does not work to just search for username [Reviewed by William Stein]\n#7447: Mitesh Patel: SageNB version and install date / time [Reviewed by William Stein]\n#7611: Tim Dumol: Minor ReST improvements for the notebook object documentation [Reviewed by William Stein]\n```\n",
    "created_at": "2009-12-09T01:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65148",
    "user": "was"
}
```

Hi, 

I merged in 9 more patches to make sagenb-0.4.6, which does fix the notebook settings page issues.  We should release sagenb-0.4.6 instead: 

   http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.5.spkg


```
#5100: Tim Dumol: worksheets: can't empty the trash (safari only?) [Reviewed by John Palmieri and William Stein]
#3733: William Stein: document notebook.css; I also sphinxified the notebook? docstring [Reviewed by Tim Dumol]
#7433: Tim Dumol: Changing title of worksheet changes title of corresponding published worksheet [Reviewed by William Stein]
#7455: Tim Dumol: Searching on Log page does not work [Reviewed by William Stein]
#4714: Mitesh Patel: use easy/load.js when loading jsmath in the notebook [Reviewed by William Stein]
#7267: Mitesh Patel: Add a compact color picker to SageNB [Reviewed by William Stein and Tim Dumol]
#7376: Mitesh Patel: searching published worksheets does not work to just search for username [Reviewed by William Stein]
#7447: Mitesh Patel: SageNB version and install date / time [Reviewed by William Stein]
#7611: Tim Dumol: Minor ReST improvements for the notebook object documentation [Reviewed by William Stein]
```




---

archive/issue_comments_065149.json:
```json
{
    "body": "Here I meant  http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.6.spkg of course.",
    "created_at": "2009-12-09T01:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65149",
    "user": "was"
}
```

Here I meant  http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.6.spkg of course.



---

archive/issue_comments_065150.json:
```json
{
    "body": "All Se tests now pass.  But I'm a bit too tired right now to do further checking.\n\nPotential feature for the log page: A check box next to each cell, so the user can select a subset for a new worksheet?",
    "created_at": "2009-12-09T02:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65150",
    "user": "mpatel"
}
```

All Se tests now pass.  But I'm a bit too tired right now to do further checking.

Potential feature for the log page: A check box next to each cell, so the user can select a subset for a new worksheet?



---

archive/issue_comments_065151.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-09T11:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65151",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065152.json:
```json
{
    "body": "Se tests pass on my machine as well. Nothing broke in my worksheets either.\n\nSince Patel also agrees, I'll mark this with a positive review.",
    "created_at": "2009-12-09T11:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65152",
    "user": "timdumol"
}
```

Se tests pass on my machine as well. Nothing broke in my worksheets either.

Since Patel also agrees, I'll mark this with a positive review.



---

archive/issue_comments_065153.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-10T03:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65153",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_065154.json:
```json
{
    "body": "Correct me if I'm mistaken, but is #7467 actually included? I cannot find it in the merge log.",
    "created_at": "2009-12-10T14:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65154",
    "user": "timdumol"
}
```

Correct me if I'm mistaken, but is #7467 actually included? I cannot find it in the merge log.



---

archive/issue_comments_065155.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-12-10T19:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65155",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_065156.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2009-12-10T19:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65156",
    "user": "was"
}
```

Changing status from closed to new.



---

archive/issue_comments_065157.json:
```json
{
    "body": "Replying to [comment:10 timdumol]:\n> Correct me if I'm mistaken, but is #7467 actually included? I cannot find it in the merge log.\n\nOh crap, you're right.  I don't know how I made that mistake.  Here's a sagenb-0.4.7 that includes that and one other patch I merged:\n\n  http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.7.spkg\n\n\n```\nSAGENB-0.4.7\n#7467: Tim Dumol: Make SageNB use `setuptools` instead of `distutils` [Reviewed by Mitesh Patel]\n#7628: Mitesh Patel: Error on account creation still creates (half of) an account [Reviewed by William Stein]\n```\n",
    "created_at": "2009-12-10T19:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65157",
    "user": "was"
}
```

Replying to [comment:10 timdumol]:
> Correct me if I'm mistaken, but is #7467 actually included? I cannot find it in the merge log.

Oh crap, you're right.  I don't know how I made that mistake.  Here's a sagenb-0.4.7 that includes that and one other patch I merged:

  http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.7.spkg


```
SAGENB-0.4.7
#7467: Tim Dumol: Make SageNB use `setuptools` instead of `distutils` [Reviewed by Mitesh Patel]
#7628: Mitesh Patel: Error on account creation still creates (half of) an account [Reviewed by William Stein]
```




---

archive/issue_comments_065158.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-10T19:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65158",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065159.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-12-11T02:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65159",
    "user": "mhansen"
}
```

Looks good.



---

archive/issue_comments_065160.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-11T02:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7625#issuecomment-65160",
    "user": "mhansen"
}
```

Resolution: fixed
