# Issue 2831: plot taking a very, very long time

archive/issues_002831.json:
```json
{
    "body": "Assignee: @williamstein\n\nIn the notebook of sage-2.11:\n\ntime plot(1.0 - x * floor(1/x), (x,0.00001,1.0)\n\nCPU time: 143.77 s,  Wall time: 1660.39 s\n\nwith a correct image.\n\nMaple is almost immediate.\n\n\nEven worse:\n\ntime plot(1.0 - x * floor(1/x), (x, 0.0, 1.0), plot_points=1000)\n\n        \t\nCPU time: 244.71 s,  Wall time: 5155.23 s\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/2831\n\n",
    "created_at": "2008-04-06T16:40:19Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "plot taking a very, very long time",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2831",
    "user": "@jaapspies"
}
```
Assignee: @williamstein

In the notebook of sage-2.11:

time plot(1.0 - x * floor(1/x), (x,0.00001,1.0)

CPU time: 143.77 s,  Wall time: 1660.39 s

with a correct image.

Maple is almost immediate.


Even worse:

time plot(1.0 - x * floor(1/x), (x, 0.0, 1.0), plot_points=1000)

        	
CPU time: 244.71 s,  Wall time: 5155.23 s

Jaap

Issue created by migration from https://trac.sagemath.org/ticket/2831





---

archive/issue_comments_019428.json:
```json
{
    "body": "The problem is that \"floor(1/x)\" calls maxima. If you drop it the\nwhole thing takes about a second. \n\nCheers,\n\nMichael",
    "created_at": "2008-04-06T16:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2831#issuecomment-19428",
    "user": "mabshoff"
}
```

The problem is that "floor(1/x)" calls maxima. If you drop it the
whole thing takes about a second. 

Cheers,

Michael



---

archive/issue_comments_019429.json:
```json
{
    "body": "The problem is that there is a bug when deciding to use fast float, since the above\nplot takes 0.04 seconds to draw when one calls fast_float explicitly:\n\n```\nsage: time plot((1.0 - x * floor(1/x))._fast_float_(x), (x,0.00001,1.0))\nCPU times: user 0.03 s, sys: 0.01 s, total: 0.04 s\n```\n\n\n\n -- William",
    "created_at": "2008-04-06T19:08:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2831#issuecomment-19429",
    "user": "@williamstein"
}
```

The problem is that there is a bug when deciding to use fast float, since the above
plot takes 0.04 seconds to draw when one calls fast_float explicitly:

```
sage: time plot((1.0 - x * floor(1/x))._fast_float_(x), (x,0.00001,1.0))
CPU times: user 0.03 s, sys: 0.01 s, total: 0.04 s
```



 -- William



---

archive/issue_comments_019430.json:
```json
{
    "body": "Attachment [sage-2831.patch](tarball://root/attachments/some-uuid/ticket2831/sage-2831.patch) by @williamstein created at 2008-04-06 19:35:19",
    "created_at": "2008-04-06T19:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2831#issuecomment-19430",
    "user": "@williamstein"
}
```

Attachment [sage-2831.patch](tarball://root/attachments/some-uuid/ticket2831/sage-2831.patch) by @williamstein created at 2008-04-06 19:35:19



---

archive/issue_comments_019431.json:
```json
{
    "body": "This is an *absurdly* good speedup!\n\n          \t\n\nCPU time: 1.01 s,  Wall time: 3.75 s\n\ncompared with:\n\nCPU time: 244.71 s, Wall time: 5155.23 s",
    "created_at": "2008-04-06T19:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2831#issuecomment-19431",
    "user": "@jaapspies"
}
```

This is an *absurdly* good speedup!

          	

CPU time: 1.01 s,  Wall time: 3.75 s

compared with:

CPU time: 244.71 s, Wall time: 5155.23 s



---

archive/issue_comments_019432.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T20:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2831#issuecomment-19432",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2



---

archive/issue_comments_019433.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T20:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2831#issuecomment-19433",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019434.json:
```json
{
    "body": "Ok, somebody didn't doctest properly:\n\n```\nsage -t -long devel/sage/sage/functions/special.py          \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.alpha2/tmp/special.py\", line 905:\n    sage: P = plot(inverse_jacobi('sn', x, 0.5), 0, 1, plot_points=20)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_13[5]>\", line 1, in <module>\n        P = plot(inverse_jacobi('sn', x, RealNumber('0.5')), Integer(0), Integer(1), plot_points=Integer(20))###line 905:\n    sage: P = plot(inverse_jacobi('sn', x, 0.5), 0, 1, plot_points=20)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 3553, in __call__\n        G = funcs.plot(*args, **kwds)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 915, in plot\n        f = F._fast_float_(param)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 3814, in _fast_float_\n        raise NotImplementedError # return lambda x: float(self(x))\n    NotImplementedError\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_13\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.alpha2/tmp/.doctest_special.py\n         [4.7 s]\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-04-06T21:14:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2831#issuecomment-19434",
    "user": "mabshoff"
}
```

Ok, somebody didn't doctest properly:

```
sage -t -long devel/sage/sage/functions/special.py          
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/tmp/special.py", line 905:
    sage: P = plot(inverse_jacobi('sn', x, 0.5), 0, 1, plot_points=20)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[5]>", line 1, in <module>
        P = plot(inverse_jacobi('sn', x, RealNumber('0.5')), Integer(0), Integer(1), plot_points=Integer(20))###line 905:
    sage: P = plot(inverse_jacobi('sn', x, 0.5), 0, 1, plot_points=20)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 3553, in __call__
        G = funcs.plot(*args, **kwds)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 915, in plot
        f = F._fast_float_(param)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 3814, in _fast_float_
        raise NotImplementedError # return lambda x: float(self(x))
    NotImplementedError
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_13
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.alpha2/tmp/.doctest_special.py
         [4.7 s]
```


Cheers,

Michael



---

archive/issue_comments_019435.json:
```json
{
    "body": "Attachment [sage-2831_part2.patch](tarball://root/attachments/some-uuid/ticket2831/sage-2831_part2.patch) by @jaapspies created at 2008-04-06 21:31:14\n\nReplying to [comment:6 mabshoff]:\n> Ok, somebody didn't doctest properly:\n\nYou may call me names is you like :-)!\n\nJaap",
    "created_at": "2008-04-06T21:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2831#issuecomment-19435",
    "user": "@jaapspies"
}
```

Attachment [sage-2831_part2.patch](tarball://root/attachments/some-uuid/ticket2831/sage-2831_part2.patch) by @jaapspies created at 2008-04-06 21:31:14

Replying to [comment:6 mabshoff]:
> Ok, somebody didn't doctest properly:

You may call me names is you like :-)!

Jaap



---

archive/issue_comments_019436.json:
```json
{
    "body": "sage-2831_part2.patch add a fallback to lambda in case _fast_float fails. It also fixes the doctest issue. Positive review and merged in Sage 3.0.alpha2\n\nCheers,\n\nMichael",
    "created_at": "2008-04-06T21:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2831#issuecomment-19436",
    "user": "mabshoff"
}
```

sage-2831_part2.patch add a fallback to lambda in case _fast_float fails. It also fixes the doctest issue. Positive review and merged in Sage 3.0.alpha2

Cheers,

Michael



---

archive/issue_comments_019437.json:
```json
{
    "body": "Replying to [comment:7 jsp]:\n> Replying to [comment:6 mabshoff]:\n> > Ok, somebody didn't doctest properly:\n> \n> You may call me names is you like :-)!\n\nSure :)\n\nI would prefer if people stated what they actually doctested [i.e. which version of Sage with what patches applied on what platforms] so I would check myself in case somebody didn't do as much coverage as I would prefer. So you can always blame me too.\n\n> Jaap\n> \n\nCheers,\n\nMichael",
    "created_at": "2008-04-06T21:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2831#issuecomment-19437",
    "user": "mabshoff"
}
```

Replying to [comment:7 jsp]:
> Replying to [comment:6 mabshoff]:
> > Ok, somebody didn't doctest properly:
> 
> You may call me names is you like :-)!

Sure :)

I would prefer if people stated what they actually doctested [i.e. which version of Sage with what patches applied on what platforms] so I would check myself in case somebody didn't do as much coverage as I would prefer. So you can always blame me too.

> Jaap
> 

Cheers,

Michael
