# Issue 1964: attaching multiple files should work but is broken (or never implemented?)

archive/issues_001964.json:
```json
{
    "body": "Assignee: was\n\nCC:  ncalexander@gmail.com\n\nThis illustrates attaching multiple files not working.  I don't know if this was ever implemented, but if so it's broken now.  If not, I think it will be fairly easy (the code is in misc/something). \n\n\n```\nteragon:tmp was$ touch a.sage b.sage\nteragon:tmp was$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10, Release Date: 2008-01-18                        |\n| Type notebook() for the GUI, and license() for information.        |\nsage: attach a.sage b.sage\n---------------------------------------------------------------------------\n<type 'exceptions.ImportError'>           Traceback (most recent call last)\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/misc/interpreter.py in sage_prefilter(self, block, continuation)\n    393         for i in range(len(B)):\n    394             L = B[i]\n--> 395             M = d\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1964\n\n",
    "created_at": "2008-01-29T02:38:26Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "attaching multiple files should work but is broken (or never implemented?)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1964",
    "user": "was"
}
```
Assignee: was

CC:  ncalexander@gmail.com

This illustrates attaching multiple files not working.  I don't know if this was ever implemented, but if so it's broken now.  If not, I think it will be fairly easy (the code is in misc/something). 


```
teragon:tmp was$ touch a.sage b.sage
teragon:tmp was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10, Release Date: 2008-01-18                        |
| Type notebook() for the GUI, and license() for information.        |
sage: attach a.sage b.sage
---------------------------------------------------------------------------
<type 'exceptions.ImportError'>           Traceback (most recent call last)

/Users/was/s/local/lib/python2.5/site-packages/sage/misc/interpreter.py in sage_prefilter(self, block, continuation)
    393         for i in range(len(B)):
    394             L = B[i]
--> 395             M = d
```


Issue created by migration from https://trac.sagemath.org/ticket/1964





---

archive/issue_comments_012707.json:
```json
{
    "body": "Loading multiple files also doesn't work.\n\n```\nsage: load a.sage b.sage\n---------------------------------------------------------------------------\n<type 'exceptions.ImportError'>           Traceback (most recent call last)\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/misc/interpreter.py in sage_prefilter(self, block, continuation)\n    393         for i in range(len(B)):\n    394             L = B[i]\n--> 395             M = do_prefilter_paste(L, continuation or (not first))\n    396             first = Fals\n```\n",
    "created_at": "2008-01-29T02:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12707",
    "user": "was"
}
```

Loading multiple files also doesn't work.

```
sage: load a.sage b.sage
---------------------------------------------------------------------------
<type 'exceptions.ImportError'>           Traceback (most recent call last)

/Users/was/s/local/lib/python2.5/site-packages/sage/misc/interpreter.py in sage_prefilter(self, block, continuation)
    393         for i in range(len(B)):
    394             L = B[i]
--> 395             M = do_prefilter_paste(L, continuation or (not first))
    396             first = Fals
```




---

archive/issue_comments_012708.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-02-10T06:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12708",
    "user": "ncalexan"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_012709.json:
```json
{
    "body": "`1964-ncalexan-load-and-attach-multiple-files-1.hg` addresses this issue.  I refactored `interpreter.py` completely and added a NON-STANDARD test suite to convince myself that the code was working.  Apply with caution.",
    "created_at": "2008-02-10T06:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12709",
    "user": "ncalexan"
}
```

`1964-ncalexan-load-and-attach-multiple-files-1.hg` addresses this issue.  I refactored `interpreter.py` completely and added a NON-STANDARD test suite to convince myself that the code was working.  Apply with caution.



---

archive/issue_comments_012710.json:
```json
{
    "body": "Changing assignee from was to ncalexan.",
    "created_at": "2008-02-10T06:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12710",
    "user": "ncalexan"
}
```

Changing assignee from was to ncalexan.



---

archive/issue_comments_012711.json:
```json
{
    "body": "The patch looks very nice, add testing where there was none previous. But somebody else ought to take another look.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T23:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12711",
    "user": "mabshoff"
}
```

The patch looks very nice, add testing where there was none previous. But somebody else ought to take another look.

Cheers,

Michael



---

archive/issue_comments_012712.json:
```json
{
    "body": "Nick, please make a new bundle that is rebased against sage-2.10.2.alpha0 or alpha1.\nI would love to review this.  I'll read over the code in a moment at least.",
    "created_at": "2008-02-19T05:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12712",
    "user": "was"
}
```

Nick, please make a new bundle that is rebased against sage-2.10.2.alpha0 or alpha1.
I would love to review this.  I'll read over the code in a moment at least.



---

archive/issue_comments_012713.json:
```json
{
    "body": "REVIEW without trying the code:\n\n1. I just noticed this comment (by me) in the diffs (since you reformated it maybe): \" It does not convert indexes into 1-d arrays, since those have to be ints. \"\nI think we actually do now:\n\n```\nsage: preparse('v[7]')\n'v[Integer(7)]'\n```\n\n\n2. Wow, the doctests in interpreter.py are a disaster.  Thanks for fixing them in your patch!!!\n\n3. Your refactoring of the big function into little functions is superb.\n\nIf I could actually try the code and see it working, I would give it an enthusiastic positive review.   I did also just try applying the bundle to stock 2.10.1, and it also has lots of conflicts.",
    "created_at": "2008-02-19T06:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12713",
    "user": "was"
}
```

REVIEW without trying the code:

1. I just noticed this comment (by me) in the diffs (since you reformated it maybe): " It does not convert indexes into 1-d arrays, since those have to be ints. "
I think we actually do now:

```
sage: preparse('v[7]')
'v[Integer(7)]'
```


2. Wow, the doctests in interpreter.py are a disaster.  Thanks for fixing them in your patch!!!

3. Your refactoring of the big function into little functions is superb.

If I could actually try the code and see it working, I would give it an enthusiastic positive review.   I did also just try applying the bundle to stock 2.10.1, and it also has lots of conflicts.



---

archive/issue_comments_012714.json:
```json
{
    "body": "Nick: Please rebase against 2.10.2.alpha1. I assume you are asleep, so by the time you get up alpha1 ought to be out.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-19T08:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12714",
    "user": "mabshoff"
}
```

Nick: Please rebase against 2.10.2.alpha1. I assume you are asleep, so by the time you get up alpha1 ought to be out.

Cheers,

Michael



---

archive/issue_comments_012715.json:
```json
{
    "body": "Hopefully the patch attached applies to 2.10.alpha1.",
    "created_at": "2008-02-20T23:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12715",
    "user": "ncalexan"
}
```

Hopefully the patch attached applies to 2.10.alpha1.



---

archive/issue_comments_012716.json:
```json
{
    "body": "I get reject against 2.10.2.alpha1:\n\n```\nsage$ hg import ~/1964-ncalexan-load-and-attach-multiple-files-2.patch\n\napplying /home/mabshoff/1964-ncalexan-load-and-attach-multiple-files-2.patch\npatching file sage/misc/interpreter.py\nHunk #5 FAILED at 318\nHunk #6 FAILED at 358\nHunk #7 FAILED at 506\nHunk #8 FAILED at 520\nHunk #10 FAILED at 579\n5 out of 11 hunks FAILED -- saving rejects to file sage/misc/interpreter.py.rej\npatching file sage/misc/cython.py\nHunk #1 FAILED at 147\n1 out of 1 hunk FAILED -- saving rejects to file sage/misc/cython.py.rej\npatching file sage/misc/interpreter.py\nHunk #1 FAILED at 0\nHunk #2 FAILED at 17\nHunk #3 FAILED at 106\nHunk #4 FAILED at 140\nHunk #9 FAILED at 316\nHunk #10 FAILED at 348\nHunk #11 succeeded at 518 with fuzz 2 (offset 134 lines).\n6 out of 11 hunks FAILED -- saving rejects to file sage/misc/interpreter.py.rej\npatching file sage/misc/preparser.py\nHunk #1 FAILED at 197\nHunk #2 FAILED at 230\n2 out of 2 hunks FAILED -- saving rejects to file sage/misc/preparser.py.rej\nabort: patch failed to apply\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-02-20T23:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12716",
    "user": "mabshoff"
}
```

I get reject against 2.10.2.alpha1:

```
sage$ hg import ~/1964-ncalexan-load-and-attach-multiple-files-2.patch

applying /home/mabshoff/1964-ncalexan-load-and-attach-multiple-files-2.patch
patching file sage/misc/interpreter.py
Hunk #5 FAILED at 318
Hunk #6 FAILED at 358
Hunk #7 FAILED at 506
Hunk #8 FAILED at 520
Hunk #10 FAILED at 579
5 out of 11 hunks FAILED -- saving rejects to file sage/misc/interpreter.py.rej
patching file sage/misc/cython.py
Hunk #1 FAILED at 147
1 out of 1 hunk FAILED -- saving rejects to file sage/misc/cython.py.rej
patching file sage/misc/interpreter.py
Hunk #1 FAILED at 0
Hunk #2 FAILED at 17
Hunk #3 FAILED at 106
Hunk #4 FAILED at 140
Hunk #9 FAILED at 316
Hunk #10 FAILED at 348
Hunk #11 succeeded at 518 with fuzz 2 (offset 134 lines).
6 out of 11 hunks FAILED -- saving rejects to file sage/misc/interpreter.py.rej
patching file sage/misc/preparser.py
Hunk #1 FAILED at 197
Hunk #2 FAILED at 230
2 out of 2 hunks FAILED -- saving rejects to file sage/misc/preparser.py.rej
abort: patch failed to apply
```


Cheers,

Michael



---

archive/issue_comments_012717.json:
```json
{
    "body": "Ok, you need to apply only 1964-version-2-patch-3.patch via GNU patch. hg import won't work. The rejects are the following, and they seem harmless:\n\n```\n*************** def preparser(on=True):\n*** 447,471 ****\n          sage: 2/3\n          2/3\n          sage: preparser(False)\n-         sage: 2/3\n          0\n          sage: preparser(True)\n          sage: 2^3\n          8\n      \"\"\"\n      if embedded():\n-         print \"To turn off preparsing in the notebook, swith to Python mode.\"\n      if on:\n          InteractiveShell.prefilter = sage_prefilter\n      else:\n          InteractiveShell.prefilter = ipython_prefilter\n\n-\n  import sagedoc\n  import IPython.OInspect\n  IPython.OInspect.getdoc = sagedoc.my_getdoc\n  IPython.OInspect.getsource = sagedoc.my_getsource\n-\n\n  import __builtin__\n  _prompt = 'sage'\n--- 495,517 ----\n          sage: 2/3\n          2/3\n          sage: preparser(False)\n+         sage: 2/3 # known bug -- the preparser is always on in doctests\n          0\n          sage: preparser(True)\n          sage: 2^3\n          8\n      \"\"\"\n      if embedded():\n+         print \"To turn off preparsing in the notebook, switch to Python mode.\"\n      if on:\n          InteractiveShell.prefilter = sage_prefilter\n      else:\n          InteractiveShell.prefilter = ipython_prefilter\n\n  import sagedoc\n  import IPython.OInspect\n  IPython.OInspect.getdoc = sagedoc.my_getdoc\n  IPython.OInspect.getsource = sagedoc.my_getsource\n\n  import __builtin__\n  _prompt = 'sage'\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T00:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12717",
    "user": "mabshoff"
}
```

Ok, you need to apply only 1964-version-2-patch-3.patch via GNU patch. hg import won't work. The rejects are the following, and they seem harmless:

```
*************** def preparser(on=True):
*** 447,471 ****
          sage: 2/3
          2/3
          sage: preparser(False)
-         sage: 2/3
          0
          sage: preparser(True)
          sage: 2^3
          8
      """
      if embedded():
-         print "To turn off preparsing in the notebook, swith to Python mode."
      if on:
          InteractiveShell.prefilter = sage_prefilter
      else:
          InteractiveShell.prefilter = ipython_prefilter

-
  import sagedoc
  import IPython.OInspect
  IPython.OInspect.getdoc = sagedoc.my_getdoc
  IPython.OInspect.getsource = sagedoc.my_getsource
-

  import __builtin__
  _prompt = 'sage'
--- 495,517 ----
          sage: 2/3
          2/3
          sage: preparser(False)
+         sage: 2/3 # known bug -- the preparser is always on in doctests
          0
          sage: preparser(True)
          sage: 2^3
          8
      """
      if embedded():
+         print "To turn off preparsing in the notebook, switch to Python mode."
      if on:
          InteractiveShell.prefilter = sage_prefilter
      else:
          InteractiveShell.prefilter = ipython_prefilter

  import sagedoc
  import IPython.OInspect
  IPython.OInspect.getdoc = sagedoc.my_getdoc
  IPython.OInspect.getsource = sagedoc.my_getsource

  import __builtin__
  _prompt = 'sage'
```


Cheers,

Michael



---

archive/issue_comments_012718.json:
```json
{
    "body": "Related to the reject the only doctest failure in misc that I get is:\n\n```\nsage -t  devel/sage-main/sage/misc/interpreter.py\n**********************************************************************\nFile \"interpreter.py\", line 499:\n    sage: 2/3\nExpected:\n    0\nGot:\n    2/3\n**********************************************************************\n```\n\nIt does look like the doctest failure above is somehow related to the reject.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T00:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12718",
    "user": "mabshoff"
}
```

Related to the reject the only doctest failure in misc that I get is:

```
sage -t  devel/sage-main/sage/misc/interpreter.py
**********************************************************************
File "interpreter.py", line 499:
    sage: 2/3
Expected:
    0
Got:
    2/3
**********************************************************************
```

It does look like the doctest failure above is somehow related to the reject.

Cheers,

Michael



---

archive/issue_comments_012719.json:
```json
{
    "body": "Attachment\n\n`1964-ncalexan-against-2.10.2.patch` is a single patch against 2.10.2 that should merge cleanly.",
    "created_at": "2008-02-24T22:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12719",
    "user": "ncalexan"
}
```

Attachment

`1964-ncalexan-against-2.10.2.patch` is a single patch against 2.10.2 that should merge cleanly.



---

archive/issue_comments_012720.json:
```json
{
    "body": "I can confirm that 1964-ncalexan-against-2.10.2.patch applies cleanly against my 2.10.3.a0 tree (which is still very close to 2.10.2). Let's hope William reviews this soon.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-24T23:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12720",
    "user": "mabshoff"
}
```

I can confirm that 1964-ncalexan-against-2.10.2.patch applies cleanly against my 2.10.3.a0 tree (which is still very close to 2.10.2). Let's hope William reviews this soon.

Cheers,

Michael



---

archive/issue_comments_012721.json:
```json
{
    "body": "REFEREE REPORT:\n\n* I found a bug when testing this patch.  To replicate, create files a.sage and b.sage and put in a.sage\n\n```\nattach b.sage\n```\n\nin it.  This fails, but {{{attach \"b.sage\"} works.  This was a problem before this patch, so it is NOT the fault of this patch.   It's now trac #2310, which I've fixed. \n\n* I found a second bug when testing this patch.  Make a file a.sage, b.sage, and c.sage and put in a.sage\n\n```\nattach b.sage c.sage\n```\n\n\nThen attach a.sage.  Boom!  Attaching multiple files from within a file doesn't work.  This is in fact the main point of this ticket -- the user who showed me the bug was showing me it in that particular situation.  This point needs to be addressed.\nFrom the command line attaching multiple files does work fine. \n\n* This patch reformats this comment in interpreter.py: \"It does not convert indexes into 1-d arrays, since those have to be ints.\"  That comment is completely wrong.  Indexes *do* get converted to Sage ints.  I think I made this comment already somewhere above a few days ago.\n\n* This reformatted comment in interpreter.py is also wrong: \"Whenever you enter a blank line in the SAGE interpreter, *all* attached files that have changed are automatically reloaded.\"  It is NO LONGER necessary to enter a blank line to update attached files.  It used to be necessary, say 3 years ago.\n\n* I think these two lines in interpreter.py that are added by this patch should be removed:\n\n```\n \t165\t            #raise ImportError, \"Loading of '%s' not implemented (load .py, .pyx, and .sage files)\"%name \n \t166\t            #line = '' \n```\n\n\n* Regarding \n\n```\n \t186\t    \\Sage does NOT guarantee that files are reloaded in the order that they \n \t187\t    are attached!\n```\n\nI think it's dumb that we don't.  It wouldn't be hard to do.  If you agree, please open a separate trac ticket for that. If you disagree, please explain why, since then I disagree with you.\n\n* This statement in the docs is wrong since attached is a dict instead of a list:\n\n```\n \t191\t    Internally, an attached file name is put in the list \\code{attached}\n```\n\nThis isn't your fault -- I'm the one that made attached a dict...  But your patch would be a good place to fix this.\n\n\n-\n\nNick, please address each of the above points.  In some cases the appropriate response should just be to make another trac ticket. \n\n -- William",
    "created_at": "2008-02-26T04:40:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12721",
    "user": "was"
}
```

REFEREE REPORT:

* I found a bug when testing this patch.  To replicate, create files a.sage and b.sage and put in a.sage

```
attach b.sage
```

in it.  This fails, but {{{attach "b.sage"} works.  This was a problem before this patch, so it is NOT the fault of this patch.   It's now trac #2310, which I've fixed. 

* I found a second bug when testing this patch.  Make a file a.sage, b.sage, and c.sage and put in a.sage

```
attach b.sage c.sage
```


Then attach a.sage.  Boom!  Attaching multiple files from within a file doesn't work.  This is in fact the main point of this ticket -- the user who showed me the bug was showing me it in that particular situation.  This point needs to be addressed.
From the command line attaching multiple files does work fine. 

* This patch reformats this comment in interpreter.py: "It does not convert indexes into 1-d arrays, since those have to be ints."  That comment is completely wrong.  Indexes *do* get converted to Sage ints.  I think I made this comment already somewhere above a few days ago.

* This reformatted comment in interpreter.py is also wrong: "Whenever you enter a blank line in the SAGE interpreter, *all* attached files that have changed are automatically reloaded."  It is NO LONGER necessary to enter a blank line to update attached files.  It used to be necessary, say 3 years ago.

* I think these two lines in interpreter.py that are added by this patch should be removed:

```
 	165	            #raise ImportError, "Loading of '%s' not implemented (load .py, .pyx, and .sage files)"%name 
 	166	            #line = '' 
```


* Regarding 

```
 	186	    \Sage does NOT guarantee that files are reloaded in the order that they 
 	187	    are attached!
```

I think it's dumb that we don't.  It wouldn't be hard to do.  If you agree, please open a separate trac ticket for that. If you disagree, please explain why, since then I disagree with you.

* This statement in the docs is wrong since attached is a dict instead of a list:

```
 	191	    Internally, an attached file name is put in the list \code{attached}
```

This isn't your fault -- I'm the one that made attached a dict...  But your patch would be a good place to fix this.


-

Nick, please address each of the above points.  In some cases the appropriate response should just be to make another trac ticket. 

 -- William



---

archive/issue_comments_012722.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-05-03T12:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12722",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_012723.json:
```json
{
    "body": "This should really, really be merged/cleaned up. Obviously Nick is not the person who would have to do it, but it would be nice ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-05-03T12:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12723",
    "user": "mabshoff"
}
```

This should really, really be merged/cleaned up. Obviously Nick is not the person who would have to do it, but it would be nice ;)

Cheers,

Michael



---

archive/issue_comments_012724.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-18T18:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12724",
    "user": "ncalexan"
}
```

Attachment



---

archive/issue_comments_012725.json:
```json
{
    "body": "The patch against 3.0 updates the previous patch and addresses the referee's comments.\n\nIt does *NOT* address the load/attach in files issue.  I am going to look at that now, but I don't know how to fix it.  This should be merged regardless with what happens with issue.",
    "created_at": "2008-05-18T18:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12725",
    "user": "ncalexan"
}
```

The patch against 3.0 updates the previous patch and addresses the referee's comments.

It does *NOT* address the load/attach in files issue.  I am going to look at that now, but I don't know how to fix it.  This should be merged regardless with what happens with issue.



---

archive/issue_comments_012726.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-19T05:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12726",
    "user": "ncalexan"
}
```

Attachment



---

archive/issue_comments_012727.json:
```json
{
    "body": "Apply `1964-ncalexan-against-3.0.patch` first.\n\nApply `1964-ncalexan-multiple-files-1.patch` second.\n\nThe second patch should allow attaching and loading multiple files from within .sage files.  It includes new tests for these scenarios.",
    "created_at": "2008-05-19T05:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12727",
    "user": "ncalexan"
}
```

Apply `1964-ncalexan-against-3.0.patch` first.

Apply `1964-ncalexan-multiple-files-1.patch` second.

The second patch should allow attaching and loading multiple files from within .sage files.  It includes new tests for these scenarios.



---

archive/issue_comments_012728.json:
```json
{
    "body": "There is an error as written.  Change the line\n\n\n```\n    return '\\n'.join(lines_done) % literal_dict\n```\n\nto\n\n```\n    return '\\n'.join(lines_done)\n```\n\n\nI will post a new patch with this fixed and doctested shortly.",
    "created_at": "2008-05-20T23:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12728",
    "user": "ncalexan"
}
```

There is an error as written.  Change the line


```
    return '\n'.join(lines_done) % literal_dict
```

to

```
    return '\n'.join(lines_done)
```


I will post a new patch with this fixed and doctested shortly.



---

archive/issue_comments_012729.json:
```json
{
    "body": "The second patch has another small bug.  After fixing that bug, I have been using the patch for two days.  It does what it is intended to do... but I don't like what it does!  I think I'll solve the problem in a different way sometime soon.",
    "created_at": "2008-05-22T04:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12729",
    "user": "ncalexan"
}
```

The second patch has another small bug.  After fixing that bug, I have been using the patch for two days.  It does what it is intended to do... but I don't like what it does!  I think I'll solve the problem in a different way sometime soon.



---

archive/issue_comments_012730.json:
```json
{
    "body": "Changing priority from blocker to minor.",
    "created_at": "2008-06-15T21:30:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12730",
    "user": "craigcitro"
}
```

Changing priority from blocker to minor.



---

archive/issue_comments_012731.json:
```json
{
    "body": "#7514 now allows, e.g.,\n\n```\nsage: attach('foo.py', 'bar.sage', 'hello.spyx')\n```\n\nShould we change or close this ticket?",
    "created_at": "2010-01-16T20:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12731",
    "user": "mpatel"
}
```

#7514 now allows, e.g.,

```
sage: attach('foo.py', 'bar.sage', 'hello.spyx')
```

Should we change or close this ticket?



---

archive/issue_comments_012732.json:
```json
{
    "body": "Yes, close this.  :-)",
    "created_at": "2010-01-16T21:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12732",
    "user": "was"
}
```

Yes, close this.  :-)



---

archive/issue_comments_012733.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-16T21:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1964#issuecomment-12733",
    "user": "was"
}
```

Resolution: fixed
