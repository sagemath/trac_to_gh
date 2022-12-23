# Issue 4285: [with patch, needs review] update desolver interface

archive/issues_004285.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  mhansen\n\nThe current interface takes and returns raw maxima strings, and doesn't do any error handling. This gives the desolver a much more sage-like interface. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4285\n\n",
    "created_at": "2008-10-14T17:39:28Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] update desolver interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4285",
    "user": "robertwb"
}
```
Assignee: burcin

CC:  mhansen

The current interface takes and returns raw maxima strings, and doesn't do any error handling. This gives the desolver a much more sage-like interface. 

Issue created by migration from https://trac.sagemath.org/ticket/4285





---

archive/issue_comments_031354.json:
```json
{
    "body": "The last patch fixes some documentation.",
    "created_at": "2008-10-14T20:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31354",
    "user": "robertwb"
}
```

The last patch fixes some documentation.



---

archive/issue_comments_031355.json:
```json
{
    "body": "Using 3.1.3.alpha3, I got this:\n\n\n```\nsage: hg_sage.apply(\"/home/wdj/sagefiles/4285-desolver.2.patch\")\ncd \"/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage\" && hg import   \"/home/wdj/sagefiles/4285-desolver.2.patch\"\napplying /home/wdj/sagefiles/4285-desolver.2.patch\nsage: hg_sage.apply(\"/home/wdj/sagefiles/4285-desolver.3.patch\")\ncd \"/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage\" && hg import   \"/home/wdj/sagefiles/4285-desolver.3.patch\"\napplying /home/wdj/sagefiles/4285-desolver.3.patch\npatching file sage/calculus/desolvers.py\nHunk #1 FAILED at 20\nHunk #2 FAILED at 33\nHunk #3 FAILED at 151\nHunk #4 FAILED at 161\nHunk #5 FAILED at 172\n5 out of 5 hunks FAILED -- saving rejects to file sage/calculus/desolvers.py.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2008-10-14T20:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31355",
    "user": "wdj"
}
```

Using 3.1.3.alpha3, I got this:


```
sage: hg_sage.apply("/home/wdj/sagefiles/4285-desolver.2.patch")
cd "/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage" && hg import   "/home/wdj/sagefiles/4285-desolver.2.patch"
applying /home/wdj/sagefiles/4285-desolver.2.patch
sage: hg_sage.apply("/home/wdj/sagefiles/4285-desolver.3.patch")
cd "/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage" && hg import   "/home/wdj/sagefiles/4285-desolver.3.patch"
applying /home/wdj/sagefiles/4285-desolver.3.patch
patching file sage/calculus/desolvers.py
Hunk #1 FAILED at 20
Hunk #2 FAILED at 33
Hunk #3 FAILED at 151
Hunk #4 FAILED at 161
Hunk #5 FAILED at 172
5 out of 5 hunks FAILED -- saving rejects to file sage/calculus/desolvers.py.rej
abort: patch failed to apply
```




---

archive/issue_comments_031356.json:
```json
{
    "body": "Hm.... it's based on 3.1.3.rc0.",
    "created_at": "2008-10-14T21:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31356",
    "user": "robertwb"
}
```

Hm.... it's based on 3.1.3.rc0.



---

archive/issue_comments_031357.json:
```json
{
    "body": "Okay, I'll have to rebuild 3.1.3.rc0, which will take awhile.\nBut this:\n\n\n```\nsage: t = var('t')\nsage: x = function('x', t)\nsage: de = lambda y: diff(y,t) + y - 1\nsage: desolve(de(x(t)),[x,t])\ne^(-t)*(e^t + c)\nsage: f = desolve(diff(x,t) + x - 1, x, ics=[10,2]); f\ne^(-t)*(e^t + e^10)\nsage: plot(f)\n```\n\n\nis absolutely fantastic. So far, this is great! Thanks very much Robert. \n\nI'll do more testing in a few hours...",
    "created_at": "2008-10-14T21:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31357",
    "user": "wdj"
}
```

Okay, I'll have to rebuild 3.1.3.rc0, which will take awhile.
But this:


```
sage: t = var('t')
sage: x = function('x', t)
sage: de = lambda y: diff(y,t) + y - 1
sage: desolve(de(x(t)),[x,t])
e^(-t)*(e^t + c)
sage: f = desolve(diff(x,t) + x - 1, x, ics=[10,2]); f
e^(-t)*(e^t + e^10)
sage: plot(f)
```


is absolutely fantastic. So far, this is great! Thanks very much Robert. 

I'll do more testing in a few hours...



---

archive/issue_comments_031358.json:
```json
{
    "body": "This is a newly built clone of 3.1.3.rc0:\n\n\n```\nwdj@hera:~/sagefiles/sage-3.1.3.rc0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: desolve\nsage: hg_sage.apply(\"/home/wdj/sagefiles/4285-desolver.2.patch\")\ncd \"/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage\" && hg import   \"/home/wdj/sagefiles/4285-desolver.2.patch\"\napplying /home/wdj/sagefiles/4285-desolver.2.patch\nsage: hg_sage.apply(\"/home/wdj/sagefiles/4285-desolver.3.patch\")\ncd \"/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage\" && hg import   \"/home/wdj/sagefiles/4285-desolver.3.patch\"\napplying /home/wdj/sagefiles/4285-desolver.3.patch\npatching file sage/calculus/desolvers.py\nHunk #1 FAILED at 20\nHunk #2 FAILED at 33\nHunk #3 FAILED at 151\nHunk #4 FAILED at 161\nHunk #5 FAILED at 172\n5 out of 5 hunks FAILED -- saving rejects to file sage/calculus/desolvers.py.rej\nabort: patch failed to apply\n```\n\n| SAGE Version 3.1.3.rc0, Release Date: 2008-10-12                   |\n| Type notebook() for the GUI, and license() for information.        |\nJust to be clear, I am to apply patch 2 then patch 3?",
    "created_at": "2008-10-15T01:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31358",
    "user": "wdj"
}
```

This is a newly built clone of 3.1.3.rc0:


```
wdj@hera:~/sagefiles/sage-3.1.3.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: desolve
sage: hg_sage.apply("/home/wdj/sagefiles/4285-desolver.2.patch")
cd "/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage" && hg import   "/home/wdj/sagefiles/4285-desolver.2.patch"
applying /home/wdj/sagefiles/4285-desolver.2.patch
sage: hg_sage.apply("/home/wdj/sagefiles/4285-desolver.3.patch")
cd "/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage" && hg import   "/home/wdj/sagefiles/4285-desolver.3.patch"
applying /home/wdj/sagefiles/4285-desolver.3.patch
patching file sage/calculus/desolvers.py
Hunk #1 FAILED at 20
Hunk #2 FAILED at 33
Hunk #3 FAILED at 151
Hunk #4 FAILED at 161
Hunk #5 FAILED at 172
5 out of 5 hunks FAILED -- saving rejects to file sage/calculus/desolvers.py.rej
abort: patch failed to apply
```

| SAGE Version 3.1.3.rc0, Release Date: 2008-10-12                   |
| Type notebook() for the GUI, and license() for information.        |
Just to be clear, I am to apply patch 2 then patch 3?



---

archive/issue_comments_031359.json:
```json
{
    "body": "> Just to be clear, I am to apply patch 2 then patch 3?\n\nI guess no. The two patches are of the same size. Just apply one of them.",
    "created_at": "2008-10-15T07:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31359",
    "user": "zimmerma"
}
```

> Just to be clear, I am to apply patch 2 then patch 3?

I guess no. The two patches are of the same size. Just apply one of them.



---

archive/issue_comments_031360.json:
```json
{
    "body": "I made a review of this patch (tested against 3.1.2) and it is positive, here are my remarks:\n\nOne issue is that in the 2nd desolve example, one would prefer y(10) to be\nsubstituted by the initial condition y(10)=2 in the output, but this is still\nbetter than previously, and as Robert told me there is no point in investing\ntoo much in this if maxima is replaced by something else.\n\nics   -- (optional) the initial or boundary conditions (hereafter called x)\n-> shouldn't \"hereafter called x\" be removed?\n\nI see a few typos:\n(in)dependant -> (in)dependent?\ndiffereintial -> differential\nif there more -> if there is more (twice)\nvariabe -> variable",
    "created_at": "2008-10-15T07:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31360",
    "user": "zimmerma"
}
```

I made a review of this patch (tested against 3.1.2) and it is positive, here are my remarks:

One issue is that in the 2nd desolve example, one would prefer y(10) to be
substituted by the initial condition y(10)=2 in the output, but this is still
better than previously, and as Robert told me there is no point in investing
too much in this if maxima is replaced by something else.

ics   -- (optional) the initial or boundary conditions (hereafter called x)
-> shouldn't "hereafter called x" be removed?

I see a few typos:
(in)dependant -> (in)dependent?
differeintial -> differential
if there more -> if there is more (twice)
variabe -> variable



---

archive/issue_comments_031361.json:
```json
{
    "body": "Attachment\n\napply only this last patch",
    "created_at": "2008-10-15T10:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31361",
    "user": "robertwb"
}
```

Attachment

apply only this last patch



---

archive/issue_comments_031362.json:
```json
{
    "body": "Typos fixed. \n\nI imagine we'll be using maxima for differential equations for a while yet, but this interface will almost certainly be affected by the move to PyNaC all the same. \n\nwdj: there is no need to use a lambda function, you can directly write \n\n\n```\nsage: t = var('t')\nsage: x = function('x', t)\nsage: de = diff(x,t) + x - 1\nsage: desolve(de,[x,t])\ne^(-t)*(e^t + c)\nsage: f = desolve(diff(x,t) + x - 1, x, ics=[10,2]); f\ne^(-t)*(e^t + e^10)\nsage: plot(f)\n```\n",
    "created_at": "2008-10-15T10:11:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31362",
    "user": "robertwb"
}
```

Typos fixed. 

I imagine we'll be using maxima for differential equations for a while yet, but this interface will almost certainly be affected by the move to PyNaC all the same. 

wdj: there is no need to use a lambda function, you can directly write 


```
sage: t = var('t')
sage: x = function('x', t)
sage: de = diff(x,t) + x - 1
sage: desolve(de,[x,t])
e^(-t)*(e^t + c)
sage: f = desolve(diff(x,t) + x - 1, x, ics=[10,2]); f
e^(-t)*(e^t + e^10)
sage: plot(f)
```




---

archive/issue_comments_031363.json:
```json
{
    "body": "There is one more trivial fix required for tut.tex:\n\n```\nsage -t -long devel/doc/tut/tut.tex\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.alpha0/tmp/tut.py\", line 830:\n    : desolve(DE(x(t)), [x,t])\nExpected:\n    '%e^-t*(%e^t+%c)'\nGot:\n    e^(-t)*(e^t + c)\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T11:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31363",
    "user": "mabshoff"
}
```

There is one more trivial fix required for tut.tex:

```
sage -t -long devel/doc/tut/tut.tex
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha0/tmp/tut.py", line 830:
    : desolve(DE(x(t)), [x,t])
Expected:
    '%e^-t*(%e^t+%c)'
Got:
    e^(-t)*(e^t + c)
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_031364.json:
```json
{
    "body": "based on 3.1.4",
    "created_at": "2008-10-18T11:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31364",
    "user": "wdj"
}
```

based on 3.1.4



---

archive/issue_comments_031365.json:
```json
{
    "body": "Attachment\n\nI added a patch which literally changes exactly this one line in tut.tex. Hope this is what you wanted!",
    "created_at": "2008-10-18T11:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31365",
    "user": "wdj"
}
```

Attachment

I added a patch which literally changes exactly this one line in tut.tex. Hope this is what you wanted!



---

archive/issue_comments_031366.json:
```json
{
    "body": "Replying to [comment:10 wdj]:\n> I added a patch which literally changes exactly this one line in tut.tex. Hope this is what you wanted!\n\nPretty much, thanks for the patch and a positive review for the last one.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T12:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31366",
    "user": "mabshoff"
}
```

Replying to [comment:10 wdj]:
> I added a patch which literally changes exactly this one line in tut.tex. Hope this is what you wanted!

Pretty much, thanks for the patch and a positive review for the last one.

Cheers,

Michael



---

archive/issue_comments_031367.json:
```json
{
    "body": "Merged both patches in Sage 3.2.alpha0.\n\nMike: Note that the patch by David touches tut.tex",
    "created_at": "2008-10-18T12:06:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31367",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.alpha0.

Mike: Note that the patch by David touches tut.tex



---

archive/issue_comments_031368.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-18T12:06:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31368",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031369.json:
```json
{
    "body": "> Mike: Note that the patch by David touches tut.tex\n\nas a consequence, it should be ported back to the translations of the tutorial\n(in particular the french one, which is in progress, see the SD10 coding sprint page).",
    "created_at": "2008-10-18T12:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31369",
    "user": "zimmerma"
}
```

> Mike: Note that the patch by David touches tut.tex

as a consequence, it should be ported back to the translations of the tutorial
(in particular the french one, which is in progress, see the SD10 coding sprint page).



---

archive/issue_comments_031370.json:
```json
{
    "body": "Replying to [comment:13 zimmerma]:\n> > Mike: Note that the patch by David touches tut.tex\n> \n> as a consequence, it should be ported back to the translations of the tutorial\n> (in particular the french one, which is in progress, see the SD10 coding sprint page).\n\nI agree. The translation is already based on the ReST sources. One thing I just thought about was that all the documentation in the various languages ought to be doctested. This discussion should probably move to [sage-devel] so we can start designing a protocol how to deal with the new translation projects. Either way we will make the switch to the new ReST documentation for all bug the reference manual and depending on how things go we might even switch the reference manual for 3.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T12:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31370",
    "user": "mabshoff"
}
```

Replying to [comment:13 zimmerma]:
> > Mike: Note that the patch by David touches tut.tex
> 
> as a consequence, it should be ported back to the translations of the tutorial
> (in particular the french one, which is in progress, see the SD10 coding sprint page).

I agree. The translation is already based on the ReST sources. One thing I just thought about was that all the documentation in the various languages ought to be doctested. This discussion should probably move to [sage-devel] so we can start designing a protocol how to deal with the new translation projects. Either way we will make the switch to the new ReST documentation for all bug the reference manual and depending on how things go we might even switch the reference manual for 3.2.

Cheers,

Michael



---

archive/issue_comments_031371.json:
```json
{
    "body": "I made the change is the ReST documentation.",
    "created_at": "2008-10-18T15:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4285#issuecomment-31371",
    "user": "mhansen"
}
```

I made the change is the ReST documentation.
