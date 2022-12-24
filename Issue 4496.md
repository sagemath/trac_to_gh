# Issue 4496: Plot doesn't allow variable outside tuple after lambda

archive/issues_004496.json:
```json
{
    "body": "Assignee: @williamstein\n\nAll of the following work fine in 3.2.alpha0:\n\n```\nsage: plot(lambda x: x,(x,-1,1))\nsage: plot(lambda x: x,-1,1)\nsage: plot(x,x,-1,1)\nsage: plot(x,-1,1)\n```\n\nBut this doesn't:\n\n```\nsage: plot(lambda x: x,x,-1,1)\nverbose 0 (3400: plot.py, plot) there were 3 extra arguments (besides <function <lambda> at 0x11a22f70>)\n---------------------------------------------------------------------------\nUnboundLocalError                         Traceback (most recent call last)\n<snip>\n.../sage-3.2.alpha0/local/lib/python2.5/site-packages/sage/plot/plot.pyc in plot(funcs, *args, **kwds)\n   3601     if do_show:\n   3602         G.show()\n-> 3603     return G\n   3604 \n   3605 def _plot(funcs, xrange, parametric=False,\n\nUnboundLocalError: local variable 'G' referenced before assignment\n```\n\nUpon further examination, it seems that the culprit is that SymbolicVariable has a plot method, but lambda functions do not.  This is easy to fix, by changing plot() in plot.py to handle this, for the n==3 args case.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4496\n\n",
    "created_at": "2008-11-11T22:38:43Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Plot doesn't allow variable outside tuple after lambda",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4496",
    "user": "@kcrisman"
}
```
Assignee: @williamstein

All of the following work fine in 3.2.alpha0:

```
sage: plot(lambda x: x,(x,-1,1))
sage: plot(lambda x: x,-1,1)
sage: plot(x,x,-1,1)
sage: plot(x,-1,1)
```

But this doesn't:

```
sage: plot(lambda x: x,x,-1,1)
verbose 0 (3400: plot.py, plot) there were 3 extra arguments (besides <function <lambda> at 0x11a22f70>)
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
<snip>
.../sage-3.2.alpha0/local/lib/python2.5/site-packages/sage/plot/plot.pyc in plot(funcs, *args, **kwds)
   3601     if do_show:
   3602         G.show()
-> 3603     return G
   3604 
   3605 def _plot(funcs, xrange, parametric=False,

UnboundLocalError: local variable 'G' referenced before assignment
```

Upon further examination, it seems that the culprit is that SymbolicVariable has a plot method, but lambda functions do not.  This is easy to fix, by changing plot() in plot.py to handle this, for the n==3 args case.

Issue created by migration from https://trac.sagemath.org/ticket/4496





---

archive/issue_comments_033251.json:
```json
{
    "body": "Attachment [trac_4496.patch](tarball://root/attachments/some-uuid/ticket4496/trac_4496.patch) by @kcrisman created at 2008-11-11 22:59:42\n\nBased on 3.2.alpha0",
    "created_at": "2008-11-11T22:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4496#issuecomment-33251",
    "user": "@kcrisman"
}
```

Attachment [trac_4496.patch](tarball://root/attachments/some-uuid/ticket4496/trac_4496.patch) by @kcrisman created at 2008-11-11 22:59:42

Based on 3.2.alpha0



---

archive/issue_comments_033252.json:
```json
{
    "body": "Changing assignee from @williamstein to @kcrisman.",
    "created_at": "2008-11-11T23:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4496#issuecomment-33252",
    "user": "@kcrisman"
}
```

Changing assignee from @williamstein to @kcrisman.



---

archive/issue_comments_033253.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-11T23:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4496#issuecomment-33253",
    "user": "@kcrisman"
}
```

Changing status from new to assigned.



---

archive/issue_comments_033254.json:
```json
{
    "body": "Could you add a doctest for this?",
    "created_at": "2008-11-21T17:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4496#issuecomment-33254",
    "user": "@mwhansen"
}
```

Could you add a doctest for this?



---

archive/issue_comments_033255.json:
```json
{
    "body": "Based on 3.2",
    "created_at": "2008-12-02T17:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4496#issuecomment-33255",
    "user": "@kcrisman"
}
```

Based on 3.2



---

archive/issue_comments_033256.json:
```json
{
    "body": "Attachment [trac_4496_with_doctests.patch](tarball://root/attachments/some-uuid/ticket4496/trac_4496_with_doctests.patch) by @kcrisman created at 2008-12-02 17:45:26\n\nThanks for waiting - doctests are here.  A separate ticket will be opened for the fact that \n\n```\nsage: p = plot(lambda x: f,x,-1,1)\n```\n\nwon't work, which is because \"evaluating\" the lambda function in this case returns a SymbolicCallableExpression which itself needs to be called again.",
    "created_at": "2008-12-02T17:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4496#issuecomment-33256",
    "user": "@kcrisman"
}
```

Attachment [trac_4496_with_doctests.patch](tarball://root/attachments/some-uuid/ticket4496/trac_4496_with_doctests.patch) by @kcrisman created at 2008-12-02 17:45:26

Thanks for waiting - doctests are here.  A separate ticket will be opened for the fact that 

```
sage: p = plot(lambda x: f,x,-1,1)
```

won't work, which is because "evaluating" the lambda function in this case returns a SymbolicCallableExpression which itself needs to be called again.



---

archive/issue_comments_033257.json:
```json
{
    "body": "This seems to install but with an odd message (see below). It also \npassed sage -testall on a intel mac os10.4 running sage 3.2.1.\n\nPatch and docstrings look good too. Modulo the odd message below, I give this\na positive review.\n\nLoading Sage library. Current Mercurial branch is: plot-lambda\nsage: hg_sage.apply(\"/Volumes/G-DRIVE-MINI/sagestuff/trac_4496320-linear-codes5.patch\")\n/Volumes/G-DRIVE-MINI/sagestuff/trac_4496.patch\n/Volumes/G-DRIVE-MINI/sagestuff/trac_4496_with_doctests.patch\nsage: hg_sage.apply(\"/Volumes/G-DRIVE-MINI/sagestuff/trac_4496_with_doctests.patch\")\ncd \"/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.alpha0/devel/sage\" && hg status\ncd \"/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.alpha0/devel/sage\" && hg status\ncd \"/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.alpha0/devel/sage\" && hg import   \"/Volumes/G-DRIVE-MINI/sagestuff/trac_4496_with_doctests.patch\"\napplying /Volumes/G-DRIVE-MINI/sagestuff/trac_4496_with_doctests.patch\npatching file sage/plot/plot.py\nHunk #1 succeeded at 1474 with fuzz 1 (offset -2100 lines).\nsage:",
    "created_at": "2008-12-03T00:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4496#issuecomment-33257",
    "user": "@wdjoyner"
}
```

This seems to install but with an odd message (see below). It also 
passed sage -testall on a intel mac os10.4 running sage 3.2.1.

Patch and docstrings look good too. Modulo the odd message below, I give this
a positive review.

Loading Sage library. Current Mercurial branch is: plot-lambda
sage: hg_sage.apply("/Volumes/G-DRIVE-MINI/sagestuff/trac_4496320-linear-codes5.patch")
/Volumes/G-DRIVE-MINI/sagestuff/trac_4496.patch
/Volumes/G-DRIVE-MINI/sagestuff/trac_4496_with_doctests.patch
sage: hg_sage.apply("/Volumes/G-DRIVE-MINI/sagestuff/trac_4496_with_doctests.patch")
cd "/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.alpha0/devel/sage" && hg status
cd "/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.alpha0/devel/sage" && hg status
cd "/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.alpha0/devel/sage" && hg import   "/Volumes/G-DRIVE-MINI/sagestuff/trac_4496_with_doctests.patch"
applying /Volumes/G-DRIVE-MINI/sagestuff/trac_4496_with_doctests.patch
patching file sage/plot/plot.py
Hunk #1 succeeded at 1474 with fuzz 1 (offset -2100 lines).
sage:



---

archive/issue_comments_033258.json:
```json
{
    "body": "Hi David,\n\nThis:\n\n```\nHunk #1 succeeded at 1474 with fuzz 1 (offset -2100 lines)\n```\n\nis harmless in this case since you applied the patch against a version of Sage that doe not have the plotting refactoring patch applied. I would highly recommend you update to 3.2.1 or 3.2.2.alpha0 once it is out since some rather invasive patches related to coercion will be merged in 3.2.2.a0.\n\nIn general a fuzz of thousands of lines always indicates something bad going on unless you get hit by missing refactoring patches like in this case.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-03T00:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4496#issuecomment-33258",
    "user": "mabshoff"
}
```

Hi David,

This:

```
Hunk #1 succeeded at 1474 with fuzz 1 (offset -2100 lines)
```

is harmless in this case since you applied the patch against a version of Sage that doe not have the plotting refactoring patch applied. I would highly recommend you update to 3.2.1 or 3.2.2.alpha0 once it is out since some rather invasive patches related to coercion will be merged in 3.2.2.a0.

In general a fuzz of thousands of lines always indicates something bad going on unless you get hit by missing refactoring patches like in this case.

Cheers,

Michael



---

archive/issue_comments_033259.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-04T16:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4496#issuecomment-33259",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_033260.json:
```json
{
    "body": "Merged trac_4496_with_doctests.patch in Sage 3.2.2.alpha0",
    "created_at": "2008-12-04T16:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4496#issuecomment-33260",
    "user": "mabshoff"
}
```

Merged trac_4496_with_doctests.patch in Sage 3.2.2.alpha0
