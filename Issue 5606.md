# Issue 5606: complex color plotting

archive/issues_005606.json:
```json
{
    "body": "Assignee: @williamstein\n\nIt's really a shame Sage can't produce graphics like http://commons.wikimedia.org/wiki/User:Jan_Homann/Mathematics yet. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5606\n\n",
    "created_at": "2009-03-25T03:50:59Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "complex color plotting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5606",
    "user": "@robertwb"
}
```
Assignee: @williamstein

It's really a shame Sage can't produce graphics like http://commons.wikimedia.org/wiki/User:Jan_Homann/Mathematics yet. 

Issue created by migration from https://trac.sagemath.org/ticket/5606





---

archive/issue_comments_043750.json:
```json
{
    "body": "Attachment [zeta.png](tarball://root/attachments/some-uuid/ticket5606/zeta.png) by @robertwb created at 2009-03-25 03:59:52",
    "created_at": "2009-03-25T03:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43750",
    "user": "@robertwb"
}
```

Attachment [zeta.png](tarball://root/attachments/some-uuid/ticket5606/zeta.png) by @robertwb created at 2009-03-25 03:59:52



---

archive/issue_comments_043751.json:
```json
{
    "body": "It's still a bit slow, #5093 should fix this.",
    "created_at": "2009-03-25T04:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43751",
    "user": "@robertwb"
}
```

It's still a bit slow, #5093 should fix this.



---

archive/issue_comments_043752.json:
```json
{
    "body": "REFEREE REPORT:\n\n* Coverage isn't 100%:\n\n\n```\nteragon:sage-3.4 wstein$ sage -coverage devel/sage/sage/plot/complex_plot.pyx \n----------------------------------------------------------------------\ndevel/sage/sage/plot/complex_plot.pyx\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE devel/sage/sage/plot/complex_plot.pyx: 85% (6 of 7)\n\nMissing doctests:\n\t * get_minmax_data(self):\n\n\nPossibly wrong (function name doesn't occur in doctests):\n\t * _render_on_subplot(self, subplot):\n\n```\n\n\n* I was puzzled why I couldn't change the aspect ratio (this is *not* a general problem with contour plots (say) in Sage):\n\n```\ntime complex_plot(zeta, (-5, 5), (-5, 5)).show(aspect_ratio=4)\n```\n\n\nOtherwise the code looks very *very* good.",
    "created_at": "2009-04-09T06:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43752",
    "user": "@williamstein"
}
```

REFEREE REPORT:

* Coverage isn't 100%:


```
teragon:sage-3.4 wstein$ sage -coverage devel/sage/sage/plot/complex_plot.pyx 
----------------------------------------------------------------------
devel/sage/sage/plot/complex_plot.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE devel/sage/sage/plot/complex_plot.pyx: 85% (6 of 7)

Missing doctests:
	 * get_minmax_data(self):


Possibly wrong (function name doesn't occur in doctests):
	 * _render_on_subplot(self, subplot):

```


* I was puzzled why I couldn't change the aspect ratio (this is *not* a general problem with contour plots (say) in Sage):

```
time complex_plot(zeta, (-5, 5), (-5, 5)).show(aspect_ratio=4)
```


Otherwise the code looks very *very* good.



---

archive/issue_comments_043753.json:
```json
{
    "body": "I added a doctest to get coverage up to 100%. \n\nAs for the aspect ratio issue, no idea. The same happens with density_plot: \n\n\n```\nsage: density_plot(sin(x) - sin(y), (-5,5), (-5,5)).show(aspect_ratio=4)\n```\n\n\nMaybe we could move that to a new ticket.",
    "created_at": "2009-04-09T07:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43753",
    "user": "@robertwb"
}
```

I added a doctest to get coverage up to 100%. 

As for the aspect ratio issue, no idea. The same happens with density_plot: 


```
sage: density_plot(sin(x) - sin(y), (-5,5), (-5,5)).show(aspect_ratio=4)
```


Maybe we could move that to a new ticket.



---

archive/issue_comments_043754.json:
```json
{
    "body": "The second and third hunk in 5606-complex-plot.patch are already in Sage via another patch, so I am attaching the version I merged (assuming doctests pass for me).\n\nCheers,\n\nMichael",
    "created_at": "2009-04-10T02:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43754",
    "user": "mabshoff"
}
```

The second and third hunk in 5606-complex-plot.patch are already in Sage via another patch, so I am attaching the version I merged (assuming doctests pass for me).

Cheers,

Michael



---

archive/issue_comments_043755.json:
```json
{
    "body": "Hmm, there are also the following two doctest failures:\n\n```\nsage -t -long devel/sage/sage/plot/complex_plot.pyx\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc2/devel/sage-main/sage/plot/complex_plot.pyx\", line 146:\n    sage: p = complex_plot(x^2-1, (-2, 2), (-2, 2))\nExpected nothing\nGot:\n    doctest:325: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)\n    doctest:5554: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)\n    doctest:5545: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc2/devel/sage-main/sage/plot/complex_plot.pyx\", line 162:\n    sage: p.get_minmax_data()\nExpected:\n    {'xmax': 2.0, 'xmin': -1.0, 'ymax': 4.0, 'ymin': -3.0}\nGot:\n    {'xmin': -1.0, 'ymin': -3.0, 'ymax': 4.0, 'xmax': 2.0}\n**********************************************************************\n```\n\n\nThe first one is trivial to fix by adding the variables to the plot ranges, the second one is caused by the dictionary being printing differently, so it might be a good idea to print the minmax_data as a list in a consistent format.\n\nI am bumping this ticket to 3.4.2 - if it is fixed it can still go into 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-10T02:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43755",
    "user": "mabshoff"
}
```

Hmm, there are also the following two doctest failures:

```
sage -t -long devel/sage/sage/plot/complex_plot.pyx
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage-main/sage/plot/complex_plot.pyx", line 146:
    sage: p = complex_plot(x^2-1, (-2, 2), (-2, 2))
Expected nothing
Got:
    doctest:325: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)
    doctest:5554: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)
    doctest:5545: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage-main/sage/plot/complex_plot.pyx", line 162:
    sage: p.get_minmax_data()
Expected:
    {'xmax': 2.0, 'xmin': -1.0, 'ymax': 4.0, 'ymin': -3.0}
Got:
    {'xmin': -1.0, 'ymin': -3.0, 'ymax': 4.0, 'xmax': 2.0}
**********************************************************************
```


The first one is trivial to fix by adding the variables to the plot ranges, the second one is caused by the dictionary being printing differently, so it might be a good idea to print the minmax_data as a list in a consistent format.

I am bumping this ticket to 3.4.2 - if it is fixed it can still go into 3.4.1.

Cheers,

Michael



---

archive/issue_comments_043756.json:
```json
{
    "body": "Attachment [5606-complex-plot.patch](tarball://root/attachments/some-uuid/ticket5606/5606-complex-plot.patch) by @robertwb created at 2009-04-10 06:41:42",
    "created_at": "2009-04-10T06:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43756",
    "user": "@robertwb"
}
```

Attachment [5606-complex-plot.patch](tarball://root/attachments/some-uuid/ticket5606/5606-complex-plot.patch) by @robertwb created at 2009-04-10 06:41:42



---

archive/issue_comments_043757.json:
```json
{
    "body": "I've updated the patch, should pass doctests now.",
    "created_at": "2009-04-10T06:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43757",
    "user": "@robertwb"
}
```

I've updated the patch, should pass doctests now.



---

archive/issue_comments_043758.json:
```json
{
    "body": "> I've updated the patch, should pass doctests now. \n\nAs a reviewer I am finding this very annoying.  It means I have to somehow revert the patch in my own tree before I can safely apply yours *and* it makes it very very hard for me to see what you actually changed.  I would *much* rather have a part 2 patch that applies on top of the first one. \n\nOn a clean 3.4.1.rc1 build (which I think never had #5606 applied, so far as I can tell) I get:\n\n```\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/5606/5606-complex-plot.patch'\n)\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5606/5606-complex-plot.patch\nLoading: [..]\ncd \"/scratch/wstein/build/sage-3.4.1.rc1/devel/sage\" && hg status\ncd \"/scratch/wstein/build/sage-3.4.1.rc1/devel/sage\" && hg status\ncd \"/scratch/wstein/build/sage-3.4.1.rc1/devel/sage\" && hg import   \"/scratch/wstein/sage/temp/sage.math.washington.edu/1031/tmp_2.patch\"\napplying /scratch/wstein/sage/temp/sage.math.washington.edu/1031/tmp_2.patch\npatching file sage/misc/log.py\nHunk #1 FAILED at 64\n1 out of 1 hunks FAILED -- saving rejects to file sage/misc/log.py.rej\npatching file sage/misc/mathml.py\nHunk #1 FAILED at 26\n1 out of 1 hunks FAILED -- saving rejects to file sage/misc/mathml.py.rej\nfile sage/plot/complex_plot.pyx already exists\n1 out of 1 hunks FAILED -- saving rejects to file sage/plot/complex_plot.pyx.rej\nabort: patch failed to apply\n\nsage: hg_sage.log()\nchangeset:   11933:470a0a0e9a2c\ntag:         tip\nuser:        mabshoff@sage.math.washington.edu\ndate:        Sun Apr 05 23:49:53 2009 -0700\nsummary:     3.4.1.rc1\n\n...\n```\n",
    "created_at": "2009-04-10T14:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43758",
    "user": "@williamstein"
}
```

> I've updated the patch, should pass doctests now. 

As a reviewer I am finding this very annoying.  It means I have to somehow revert the patch in my own tree before I can safely apply yours *and* it makes it very very hard for me to see what you actually changed.  I would *much* rather have a part 2 patch that applies on top of the first one. 

On a clean 3.4.1.rc1 build (which I think never had #5606 applied, so far as I can tell) I get:

```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/5606/5606-complex-plot.patch'
)
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5606/5606-complex-plot.patch
Loading: [..]
cd "/scratch/wstein/build/sage-3.4.1.rc1/devel/sage" && hg status
cd "/scratch/wstein/build/sage-3.4.1.rc1/devel/sage" && hg status
cd "/scratch/wstein/build/sage-3.4.1.rc1/devel/sage" && hg import   "/scratch/wstein/sage/temp/sage.math.washington.edu/1031/tmp_2.patch"
applying /scratch/wstein/sage/temp/sage.math.washington.edu/1031/tmp_2.patch
patching file sage/misc/log.py
Hunk #1 FAILED at 64
1 out of 1 hunks FAILED -- saving rejects to file sage/misc/log.py.rej
patching file sage/misc/mathml.py
Hunk #1 FAILED at 26
1 out of 1 hunks FAILED -- saving rejects to file sage/misc/mathml.py.rej
file sage/plot/complex_plot.pyx already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/plot/complex_plot.pyx.rej
abort: patch failed to apply

sage: hg_sage.log()
changeset:   11933:470a0a0e9a2c
tag:         tip
user:        mabshoff@sage.math.washington.edu
date:        Sun Apr 05 23:49:53 2009 -0700
summary:     3.4.1.rc1

...
```




---

archive/issue_comments_043759.json:
```json
{
    "body": "Just FYI: As mentioned above two hunk that delete and import of \"sage.plot.all\" in log.py and mathml.py need to be deleted since they are already gone in 3.4.1.rc1. Then the patch applies and passes doctests for me.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-10T17:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43759",
    "user": "mabshoff"
}
```

Just FYI: As mentioned above two hunk that delete and import of "sage.plot.all" in log.py and mathml.py need to be deleted since they are already gone in 3.4.1.rc1. Then the patch applies and passes doctests for me.

Cheers,

Michael



---

archive/issue_comments_043760.json:
```json
{
    "body": "Sorry, I will post a separate patch next time. Ironically, I've had people complain to me about that behavior too, but usually it's when the list of patches gets cumbersome.",
    "created_at": "2009-04-10T18:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43760",
    "user": "@robertwb"
}
```

Sorry, I will post a separate patch next time. Ironically, I've had people complain to me about that behavior too, but usually it's when the list of patches gets cumbersome.



---

archive/issue_comments_043761.json:
```json
{
    "body": "Attachment [trac_5606-complex-plot.patch](tarball://root/attachments/some-uuid/ticket5606/trac_5606-complex-plot.patch) by mabshoff created at 2009-04-10 20:38:52\n\nThis version of the patch removes the two hunk in Robert's patch that are already in 3.4.1.rc1",
    "created_at": "2009-04-10T20:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43761",
    "user": "mabshoff"
}
```

Attachment [trac_5606-complex-plot.patch](tarball://root/attachments/some-uuid/ticket5606/trac_5606-complex-plot.patch) by mabshoff created at 2009-04-10 20:38:52

This version of the patch removes the two hunk in Robert's patch that are already in 3.4.1.rc1



---

archive/issue_comments_043762.json:
```json
{
    "body": "trac_5606-complex-plot.patch does apply to my merge tree and pass long doctests.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-10T20:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43762",
    "user": "mabshoff"
}
```

trac_5606-complex-plot.patch does apply to my merge tree and pass long doctests.

Cheers,

Michael



---

archive/issue_comments_043763.json:
```json
{
    "body": "Merged rac_5606-complex-plot.patch in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-11T00:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43763",
    "user": "mabshoff"
}
```

Merged rac_5606-complex-plot.patch in Sage 3.4.1.rc2.

Cheers,

Michael



---

archive/issue_comments_043764.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-11T00:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5606#issuecomment-43764",
    "user": "mabshoff"
}
```

Resolution: fixed
