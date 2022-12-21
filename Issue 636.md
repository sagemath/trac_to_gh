# Issue 636: cvxopt doesn't fully work yet in SAGE under Linux

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-10 21:51:52

Assignee: jkantor

If I build cvxopt on any *Linux* system, then it doesn't work, as follows:

```
sage: import cvxopt.base
---------------------------------------------------------------------------
<type 'exceptions.ImportError'>           Traceback (most recent call last)

/home2/sage/<ipython console> in <module>()

<type 'exceptions.ImportError'>: /home2/sage/s/local/lib/python2.5/site-packages/cvxopt/base.so: undefined symbol: _g95_ioparm
```


We need to:
  1. Figure out why this fails.

  2. Add doctests to SAGE core library to illustrate cvxopt and make sure it fully work, so the above sort of thing won't happen again.  Base these on the cvxopt tutorial, etc.  


---

Comment by mabshoff created at 2007-09-11 05:25:08

Changing component from algebraic geometry to packages.


---

Comment by mabshoff created at 2007-09-11 05:25:08

Yep, in retroperspective I am surprised that nobody caught the issue earlier. I never got cvxopt to compile on Solaris (it complains about a missing complex.h), but there were no specific doctest failures that I could attribute to the missing cvxopt.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-19 18:41:27

This ticket is related to #709 and #636. Once #709 goes in the other two tickets should be resolved.

Cheers,

Michael


---

Comment by was created at 2007-10-20 20:21:18

Resolution: fixed
