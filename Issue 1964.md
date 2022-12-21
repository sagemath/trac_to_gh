# Issue 1964: attaching multiple files should work but is broken (or never implemented?)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-29 02:38:26

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



---

Comment by was created at 2008-01-29 02:39:09

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

Comment by ncalexan created at 2008-02-10 06:53:57

Changing type from defect to enhancement.


---

Comment by ncalexan created at 2008-02-10 06:53:57

`1964-ncalexan-load-and-attach-multiple-files-1.hg` addresses this issue.  I refactored `interpreter.py` completely and added a NON-STANDARD test suite to convince myself that the code was working.  Apply with caution.


---

Comment by ncalexan created at 2008-02-10 06:53:57

Changing assignee from was to ncalexan.


---

Comment by mabshoff created at 2008-02-15 23:47:53

The patch looks very nice, add testing where there was none previous. But somebody else ought to take another look.

Cheers,

Michael


---

Comment by was created at 2008-02-19 05:55:51

Nick, please make a new bundle that is rebased against sage-2.10.2.alpha0 or alpha1.
I would love to review this.  I'll read over the code in a moment at least.


---

Comment by was created at 2008-02-19 06:28:51

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

Comment by mabshoff created at 2008-02-19 08:01:13

Nick: Please rebase against 2.10.2.alpha1. I assume you are asleep, so by the time you get up alpha1 ought to be out.

Cheers,

Michael


---

Comment by ncalexan created at 2008-02-20 23:44:07

Hopefully the patch attached applies to 2.10.alpha1.


---

Comment by mabshoff created at 2008-02-20 23:56:50

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

Comment by mabshoff created at 2008-02-21 00:16:41

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

Comment by mabshoff created at 2008-02-21 00:23:36

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

Attachment

`1964-ncalexan-against-2.10.2.patch` is a single patch against 2.10.2 that should merge cleanly.


---

Comment by mabshoff created at 2008-02-24 23:02:40

I can confirm that 1964-ncalexan-against-2.10.2.patch applies cleanly against my 2.10.3.a0 tree (which is still very close to 2.10.2). Let's hope William reviews this soon.

Cheers,

Michael


---

Comment by was created at 2008-02-26 04:40:59

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

Comment by mabshoff created at 2008-05-03 12:30:13

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-05-03 12:30:13

This should really, really be merged/cleaned up. Obviously Nick is not the person who would have to do it, but it would be nice ;)

Cheers,

Michael


---

Attachment


---

Comment by ncalexan created at 2008-05-18 18:22:54

The patch against 3.0 updates the previous patch and addresses the referee's comments.

It does *NOT* address the load/attach in files issue.  I am going to look at that now, but I don't know how to fix it.  This should be merged regardless with what happens with issue.


---

Attachment


---

Comment by ncalexan created at 2008-05-19 05:17:50

Apply `1964-ncalexan-against-3.0.patch` first.

Apply `1964-ncalexan-multiple-files-1.patch` second.

The second patch should allow attaching and loading multiple files from within .sage files.  It includes new tests for these scenarios.


---

Comment by ncalexan created at 2008-05-20 23:25:32

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

Comment by ncalexan created at 2008-05-22 04:18:24

The second patch has another small bug.  After fixing that bug, I have been using the patch for two days.  It does what it is intended to do... but I don't like what it does!  I think I'll solve the problem in a different way sometime soon.


---

Comment by craigcitro created at 2008-06-15 21:30:22

Changing priority from blocker to minor.


---

Comment by mpatel created at 2010-01-16 20:06:44

#7514 now allows, e.g.,

```
sage: attach('foo.py', 'bar.sage', 'hello.spyx')
```

Should we change or close this ticket?


---

Comment by was created at 2010-01-16 21:07:48

Yes, close this.  :-)


---

Comment by was created at 2010-01-16 21:07:48

Resolution: fixed
