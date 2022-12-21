# Issue 3952: make plot() and parametric_plot() use fast_float on their functions

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-08-25 21:58:09

Assignee: was

Currently we have an error when calling these functions with constants.  Using fast_float will take care of this and presumably make the functions *way* faster to boot.


---

Comment by jason created at 2008-08-25 21:58:21

See #2410 for an example of the error.


---

Comment by mhansen created at 2008-08-26 02:01:11

This fixes #2409 and cuts the doctest time for plot.py in half.


---

Comment by mhansen created at 2008-08-26 02:09:53

Note that this depends on #2410 and #3853.


---

Comment by cwitty created at 2008-08-26 04:00:46

I've read through this patch, and it looks good to me.  Positive review, assuming the doctests pass (I didn't run the doctests).


---

Comment by mabshoff created at 2008-08-26 04:19:44

With the patch applied I am seeing one doctest failure:

```
sage -t -long devel/sage/sage/calculus/desolvers.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/tmp/desolvers.py", line 194:
    sage: P2 = parametric_plot((solnx,solny),0,1)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[17]>", line 1, in <module>
        P2 = parametric_plot((solnx,solny),Integer(0),Integer(1))###line 194:
    sage: P2 = parametric_plot((solnx,solny),0,1)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/site-packages/sage/plot/plot.py", line 3735, in parametric_plot
        raise ValueError, "there must be exactly one free variable in funcs"
    ValueError: there must be exactly one free variable in funcs 
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-08-26 06:48:47

Until the doctest is fixed this needs some work :(

Cheers,

Michael


---

Attachment

I've attached a new patch which fixes the issue.


---

Comment by mabshoff created at 2008-08-26 21:48:32

Positive review on the patch. The affected doctest now passes and Mike did explain to me in IRC what was fixed:

```
[2:41pm] mabshoff: mhansen: #3592 - what is changed?
[2:41pm] mabshoff: Did you fix the doctest or did you do more?
[2:42pm] mhansen: Oh, I changed a "!= 1" to a " > 1" in the new code (which is what is should have been).
[2:42pm] mabshoff: ok
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-08-26 22:16:42

Merged in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-26 22:16:42

Resolution: fixed
