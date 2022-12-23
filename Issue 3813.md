# Issue 3813: Improve adaptive rendering in plot()

archive/issues_003813.json:
```json
{
    "body": "Assignee: was\n\nWilliam said at Sage Days 9 that he wanted better adaptive rendering.  So I did it.  \n\nIt actually looks much better by default.  Better enough that I don't think users will have to touch plot_points anymore.\n\nAnd it runs just as fast.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3813\n\n",
    "created_at": "2008-08-12T05:43:05Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "Improve adaptive rendering in plot()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3813",
    "user": "anakha"
}
```
Assignee: was

William said at Sage Days 9 that he wanted better adaptive rendering.  So I did it.  

It actually looks much better by default.  Better enough that I don't think users will have to touch plot_points anymore.

And it runs just as fast.

Issue created by migration from https://trac.sagemath.org/ticket/3813





---

archive/issue_comments_027106.json:
```json
{
    "body": "Attachment\n\nBetter adaptive rendering",
    "created_at": "2008-08-12T05:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27106",
    "user": "anakha"
}
```

Attachment

Better adaptive rendering



---

archive/issue_comments_027107.json:
```json
{
    "body": "reviewers changes",
    "created_at": "2008-08-13T01:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27107",
    "user": "saliola"
}
```

reviewers changes



---

archive/issue_comments_027108.json:
```json
{
    "body": "Attachment\n\nslabbe and I have some suggestions that we are submitting as trac_3813-review.patch. Most are documentation edits. Two noteworthy changes:\n\n1. Below data is a list of floats since that is the output of var_and_list_of_values:\n\n```\n3632\t\t        x, data = var_and_list_of_values(xrange, plot_points) \n3633\t- \t        data = list(data) \n```\n\n\n2. Lines 3683--3699: We moved the adaptive refinement algorithm into a standalone function and added documentation and doctests for it. It's an interesting enough function that a user might want to play with it.\n\n(sage-adaptive-plot.patch needs to be applied first.)",
    "created_at": "2008-08-13T01:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27108",
    "user": "saliola"
}
```

Attachment

slabbe and I have some suggestions that we are submitting as trac_3813-review.patch. Most are documentation edits. Two noteworthy changes:

1. Below data is a list of floats since that is the output of var_and_list_of_values:

```
3632		        x, data = var_and_list_of_values(xrange, plot_points) 
3633	- 	        data = list(data) 
```


2. Lines 3683--3699: We moved the adaptive refinement algorithm into a standalone function and added documentation and doctests for it. It's an interesting enough function that a user might want to play with it.

(sage-adaptive-plot.patch needs to be applied first.)



---

archive/issue_comments_027109.json:
```json
{
    "body": "REVIEW:\n\n* watch out -- sage-adaptive-plot.patch is not a mercurial patch, so no log message.  maybe copy in the message from the ticket. \n\n* The very first plot I tried (after applying both patches) is wrong: `plot(sin(1/x), (x,0,3), plot_points=5)`.  For me, it's missing the left-hand side of the plot.   I.e., for some reason inputting a small number of sample points results in only a small part of the plot being plotted.  This is not good.\n\n* It seems like it is no longer possible to make a plot that *doesn't* use adaptive refinement, since this now fails even though it used to work:\n\n```\ntime plot(sin(1/x), (x,-1,3),plot_points=10000, plot_division=0)\n```\n\nThus you've broken all code that uses plot_division.  You need to either support plot_division (why not??), or at the worst put in a deprecation warning.  If you do deprecation, see `rings/polynomial/polynomial_ring_constructor.py` for an example of how to do this using the warnings.warn function in the warnings module. \n\n* The default option for adaptive_tolerance is not giving in the docstring, but is 0.01.  It should be given here (which appears in two places in the file now):\n\n```\n        adaptive_tolerance -- how large a difference should be before the\n                              adaptive refinement code considers it significant.\n                              This depends on the interval you use by default.\n\n```\n\n\n* This line in adaptive_refinement has a bug:\n\n```\n    x = (p1[0] + p2[0])/2\n```\n\nIn particular, if you make p1[0] and p2[0] both Python int's then you can easily get a completely wrong answer.  You must coerce the entries of the pi's to floats first or replace 2 by 2.0.  For example:\n\n```\nfrom sage.plot.plot import adaptive_refinement\na = adaptive_refinement(sin, (int(0),1), (int(1),1), 0.01)\nb = adaptive_refinement(sin, (0,1), (1,1), 0.01)\na == b\n///\nFalse\n```\n\nSame comments about\n\n```\n    if abs((p1[1] + p2[1])/2 - y) > adaptive_tolerance:\n```\n",
    "created_at": "2008-08-13T03:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27109",
    "user": "was"
}
```

REVIEW:

* watch out -- sage-adaptive-plot.patch is not a mercurial patch, so no log message.  maybe copy in the message from the ticket. 

* The very first plot I tried (after applying both patches) is wrong: `plot(sin(1/x), (x,0,3), plot_points=5)`.  For me, it's missing the left-hand side of the plot.   I.e., for some reason inputting a small number of sample points results in only a small part of the plot being plotted.  This is not good.

* It seems like it is no longer possible to make a plot that *doesn't* use adaptive refinement, since this now fails even though it used to work:

```
time plot(sin(1/x), (x,-1,3),plot_points=10000, plot_division=0)
```

Thus you've broken all code that uses plot_division.  You need to either support plot_division (why not??), or at the worst put in a deprecation warning.  If you do deprecation, see `rings/polynomial/polynomial_ring_constructor.py` for an example of how to do this using the warnings.warn function in the warnings module. 

* The default option for adaptive_tolerance is not giving in the docstring, but is 0.01.  It should be given here (which appears in two places in the file now):

```
        adaptive_tolerance -- how large a difference should be before the
                              adaptive refinement code considers it significant.
                              This depends on the interval you use by default.

```


* This line in adaptive_refinement has a bug:

```
    x = (p1[0] + p2[0])/2
```

In particular, if you make p1[0] and p2[0] both Python int's then you can easily get a completely wrong answer.  You must coerce the entries of the pi's to floats first or replace 2 by 2.0.  For example:

```
from sage.plot.plot import adaptive_refinement
a = adaptive_refinement(sin, (int(0),1), (int(1),1), 0.01)
b = adaptive_refinement(sin, (0,1), (1,1), 0.01)
a == b
///
False
```

Same comments about

```
    if abs((p1[1] + p2[1])/2 - y) > adaptive_tolerance:
```




---

archive/issue_comments_027110.json:
```json
{
    "body": "IMPORTANT:\n\n I want to emphasize that I'm not claiming that some of the bugs mentioned today are a result of this patch!  If you don't want to fix them or don't know how, just let me know.   For example the first patch involving `plot(sin(1/x), (x,0,3), plot_points=5)` has been in Sage forever.",
    "created_at": "2008-08-13T03:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27110",
    "user": "was"
}
```

IMPORTANT:

 I want to emphasize that I'm not claiming that some of the bugs mentioned today are a result of this patch!  If you don't want to fix them or don't know how, just let me know.   For example the first patch involving `plot(sin(1/x), (x,0,3), plot_points=5)` has been in Sage forever.



---

archive/issue_comments_027111.json:
```json
{
    "body": "OH, I realized that I can make a plot that doesn't use adaptive refinement by using adaptive_recursion=0, and that this is clearly documented.",
    "created_at": "2008-08-13T03:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27111",
    "user": "was"
}
```

OH, I realized that I can make a plot that doesn't use adaptive refinement by using adaptive_recursion=0, and that this is clearly documented.



---

archive/issue_comments_027112.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-13T19:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27112",
    "user": "anakha"
}
```

Attachment



---

archive/issue_comments_027113.json:
```json
{
    "body": "Integrate all feedback and fix all reported issues.  This patch is cumulative, so you don't need the first two patches before.",
    "created_at": "2008-08-13T19:35:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27113",
    "user": "anakha"
}
```

Integrate all feedback and fix all reported issues.  This patch is cumulative, so you don't need the first two patches before.



---

archive/issue_comments_027114.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-13T21:33:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27114",
    "user": "ncalexan"
}
```

Attachment



---

archive/issue_comments_027115.json:
```json
{
    "body": "I made some documentation changes and changed the meaning of adaptive_tolerance slightly.  `3813-diff.patch` is a relative patch showing those changes.\n\nApply only `3813-anakha-adaptive-plot-v3.patch`.\n\nI think this is ready to be applied even if my changes are not appreciated.",
    "created_at": "2008-08-13T21:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27115",
    "user": "ncalexan"
}
```

I made some documentation changes and changed the meaning of adaptive_tolerance slightly.  `3813-diff.patch` is a relative patch showing those changes.

Apply only `3813-anakha-adaptive-plot-v3.patch`.

I think this is ready to be applied even if my changes are not appreciated.



---

archive/issue_comments_027116.json:
```json
{
    "body": "I kind of agree with these changes.  The only one I have some issues is the adaptive_tolerance change.\n\nI had a personal debate on whether making it work like I did and what you did.  I decided on my way, so as to have a reasonable default in case nothing was specified and leave full control to the user otherwise.\n\nIn the end I don't really care either way.",
    "created_at": "2008-08-13T21:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27116",
    "user": "anakha"
}
```

I kind of agree with these changes.  The only one I have some issues is the adaptive_tolerance change.

I had a personal debate on whether making it work like I did and what you did.  I decided on my way, so as to have a reasonable default in case nothing was specified and leave full control to the user otherwise.

In the end I don't really care either way.



---

archive/issue_comments_027117.json:
```json
{
    "body": "This sounds like a positive review.  Thanks for this fantastic improvement to the sage plotting library!",
    "created_at": "2008-08-13T22:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27117",
    "user": "ncalexan"
}
```

This sounds like a positive review.  Thanks for this fantastic improvement to the sage plotting library!



---

archive/issue_comments_027118.json:
```json
{
    "body": "This patch has some slight reject issues:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.rc0/devel/sage$ patch -p1 < trac_3813-anakha-adaptive-plot-v3.patch \npatching file sage/plot/plot.py\nHunk #1 succeeded at 3449 (offset 35 lines).\nHunk #2 succeeded at 3504 (offset 35 lines).\nHunk #3 succeeded at 3531 (offset 35 lines).\nHunk #4 succeeded at 3599 (offset 35 lines).\nHunk #5 succeeded at 3679 (offset 46 lines).\nHunk #6 FAILED at 3704.\nHunk #7 FAILED at 4536.\n2 out of 7 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\n```\n\nPlease rebase it against 3.1.rc0 once it is out.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-15T06:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27118",
    "user": "mabshoff"
}
```

This patch has some slight reject issues:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.rc0/devel/sage$ patch -p1 < trac_3813-anakha-adaptive-plot-v3.patch 
patching file sage/plot/plot.py
Hunk #1 succeeded at 3449 (offset 35 lines).
Hunk #2 succeeded at 3504 (offset 35 lines).
Hunk #3 succeeded at 3531 (offset 35 lines).
Hunk #4 succeeded at 3599 (offset 35 lines).
Hunk #5 succeeded at 3679 (offset 46 lines).
Hunk #6 FAILED at 3704.
Hunk #7 FAILED at 4536.
2 out of 7 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
```

Please rebase it against 3.1.rc0 once it is out.

Cheers,

Michael



---

archive/issue_comments_027119.json:
```json
{
    "body": "Attachment\n\nRebase of the patch against 3.1.1.  Includes all prior patches.",
    "created_at": "2008-08-20T07:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27119",
    "user": "anakha"
}
```

Attachment

Rebase of the patch against 3.1.1.  Includes all prior patches.



---

archive/issue_comments_027120.json:
```json
{
    "body": "Rebase done.  Sorry for the delay.",
    "created_at": "2008-08-20T07:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27120",
    "user": "anakha"
}
```

Rebase done.  Sorry for the delay.



---

archive/issue_comments_027121.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-21T22:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27121",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027122.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha0",
    "created_at": "2008-08-21T22:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27122",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha0



---

archive/issue_comments_027123.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-21T23:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27123",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_027124.json:
```json
{
    "body": "trac_3813_doctestfixes.patch fixes the following two doctest failures:\n\n```\nsage -t  devel/sage/sage/plot/plot.py                       \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha0/tmp/plot.py\", line 4762:\n    sage: n1 = len(adaptive_refinement(f, (0,0), (pi,0), adaptive_tolerance=0.01)); n1\nExpected:\n    79\nGot:\n    15\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha0/tmp/plot.py\", line 4766:\n    sage: n3 = len(adaptive_refinement(f, (0,0), (pi,0), adaptive_tolerance=0.005)); n3\nExpected:\n    88\nGot:\n    16\n**********************************************************************\n```\n\nIt also makes two doctests long.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-21T23:40:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27124",
    "user": "mabshoff"
}
```

trac_3813_doctestfixes.patch fixes the following two doctest failures:

```
sage -t  devel/sage/sage/plot/plot.py                       
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha0/tmp/plot.py", line 4762:
    sage: n1 = len(adaptive_refinement(f, (0,0), (pi,0), adaptive_tolerance=0.01)); n1
Expected:
    79
Got:
    15
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha0/tmp/plot.py", line 4766:
    sage: n3 = len(adaptive_refinement(f, (0,0), (pi,0), adaptive_tolerance=0.005)); n3
Expected:
    88
Got:
    16
**********************************************************************
```

It also makes two doctests long.

Cheers,

Michael



---

archive/issue_comments_027125.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-08-22T00:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27125",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_027126.json:
```json
{
    "body": "Arnaut, Franco, \n\nafter discussing this in IRC we thought it might be a good idea to sort out the problems with those two failed doctests before merging this patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-22T00:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27126",
    "user": "mabshoff"
}
```

Arnaut, Franco, 

after discussing this in IRC we thought it might be a good idea to sort out the problems with those two failed doctests before merging this patch.

Cheers,

Michael



---

archive/issue_comments_027127.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-08-22T00:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27127",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_027128.json:
```json
{
    "body": "I think this is because I changed the default value of adaptive_recursion in the adaptive_refinement() at the last moment.  It seems I forgot to rebuild when running the doctests.  \n\nSo just changing the value for what you get should be enough.  Or you can add an adaptive_recursion parameter set to 10 and you should get the same results as in the tests.  If you get differing results then something is wrong.",
    "created_at": "2008-08-22T04:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27128",
    "user": "anakha"
}
```

I think this is because I changed the default value of adaptive_recursion in the adaptive_refinement() at the last moment.  It seems I forgot to rebuild when running the doctests.  

So just changing the value for what you get should be enough.  Or you can add an adaptive_recursion parameter set to 10 and you should get the same results as in the tests.  If you get differing results then something is wrong.



---

archive/issue_comments_027129.json:
```json
{
    "body": "I just realized I forgot to change the summary after the argument I made.  \n\nAlso, just to make it clear, the two patches that are needed for anybody wanting to try this out are trac_3813_rebase.patch and trac_3813_doctestfixes.patch",
    "created_at": "2008-08-23T21:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27129",
    "user": "anakha"
}
```

I just realized I forgot to change the summary after the argument I made.  

Also, just to make it clear, the two patches that are needed for anybody wanting to try this out are trac_3813_rebase.patch and trac_3813_doctestfixes.patch



---

archive/issue_comments_027130.json:
```json
{
    "body": "Attachment\n\nThe latest trac_3813-final.patch should apply to the latest Sage.",
    "created_at": "2008-08-27T00:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27130",
    "user": "mhansen"
}
```

Attachment

The latest trac_3813-final.patch should apply to the latest Sage.



---

archive/issue_comments_027131.json:
```json
{
    "body": "Merged trac_3813-final.patch in Sage 3.1.2.alpha1",
    "created_at": "2008-08-27T00:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27131",
    "user": "mabshoff"
}
```

Merged trac_3813-final.patch in Sage 3.1.2.alpha1



---

archive/issue_comments_027132.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T00:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3813#issuecomment-27132",
    "user": "mabshoff"
}
```

Resolution: fixed
