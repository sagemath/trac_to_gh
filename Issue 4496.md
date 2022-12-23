# Issue 4496: Plot doesn't allow variable outside tuple after lambda

Issue created by migration from https://trac.sagemath.org/ticket/4496

Original creator: kcrisman

Original creation time: 2008-11-11 22:38:43

Assignee: was

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


---

Attachment

Based on 3.2.alpha0


---

Comment by kcrisman created at 2008-11-11 23:01:25

Changing assignee from was to kcrisman.


---

Comment by kcrisman created at 2008-11-11 23:01:25

Changing status from new to assigned.


---

Comment by mhansen created at 2008-11-21 17:01:43

Could you add a doctest for this?


---

Comment by kcrisman created at 2008-12-02 17:43:27

Based on 3.2


---

Attachment

Thanks for waiting - doctests are here.  A separate ticket will be opened for the fact that 

```
sage: p = plot(lambda x: f,x,-1,1)
```

won't work, which is because "evaluating" the lambda function in this case returns a SymbolicCallableExpression which itself needs to be called again.


---

Comment by wdj created at 2008-12-03 00:49:07

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

Comment by mabshoff created at 2008-12-03 00:52:38

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

Comment by mabshoff created at 2008-12-04 16:37:26

Resolution: fixed


---

Comment by mabshoff created at 2008-12-04 16:37:26

Merged trac_4496_with_doctests.patch in Sage 3.2.2.alpha0
