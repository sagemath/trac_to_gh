# Issue 4413: '?' in docstring gets interpreted immediately by the parser

Issue created by migration from https://trac.sagemath.org/ticket/4413

Original creator: justin

Original creation time: 2008-10-31 21:05:37

Assignee: was

The following code, entered in the command-line interface to Sage, shows the effect:

```
sage: def foo(x):
   ....:     '''
   ....:     Eh?
Object `Eh` not found.
   ....:     '''
   ....:     return x
   ....: 
```

The parser appears to act on the '?' right away, rather than wait for the end of the thing being defined (or realizing that '?' in this case is not to be acted on).

The effect shows up with both single- and double- quotes, and with and without the "raw" qualifier (r!''').

This may be related to Trac#4405.




---

Comment by mhansen created at 2009-01-23 13:19:56

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-23 13:19:56

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2009-01-23 13:19:56

This is not related to #4405.  In fact, it is an IPython bug.  I've reported it here: http://lists.ipython.scipy.org/pipermail/ipython-dev/2009-January/004812.html


---

Comment by mhansen created at 2012-03-29 07:46:40

This is fixed in IPython 0.12.  We should close this when #12719 gets closed.


---

Comment by kini created at 2012-03-29 07:55:56

Changing status from new to needs_review.


---

Comment by kini created at 2012-03-29 07:56:06

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-01-25 09:47:59

Resolution: duplicate
