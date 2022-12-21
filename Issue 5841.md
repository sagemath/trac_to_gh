# Issue 5841: reenable interface/lisp.py doctests

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-21 06:26:48

Assignee: mabshoff

CC:  mvngu mhansen jdemeyer

#5662 introduced a problem when using old clisp builds which we need to use on RHEL5/Itanium since any more current clisp is hopelessly broken there. But since Gonzalo's patch fixes a real issue in the clisp interface I don't want to change any of that patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-21 06:29:46

Changing status from new to assigned.


---

Comment by was created at 2009-06-15 23:26:30

Changing priority from blocker to critical.


---

Comment by was created at 2009-06-15 23:26:30

If we've released for 2 months without fixing this, it doesn't make sense to keep it as a blocker. Note that the lisp interface is in fact 100% completely broken right now.


---

Comment by kcrisman created at 2010-05-26 21:05:25

As far as I can tell, this is all no longer true.

```
./sage -t devel/sage/sage/interfaces/lisp.py
sage -t  "devel/sage/sage/interfaces/lisp.py"               
	 [5.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.7 seconds
```

Random tests that seem to be working fine:

```
sage:  lisp._equality_symbol()
---------------------------------------------------------------------------
<snip>
NotImplementedError: We should never reach here in the Lisp interface. Please report this as a bug.
sage: lisp.function_call('sin', ['2'])
0.90929741
sage: lisp.sin(2)
0.90929741
```

I figure this should be closed...


---

Comment by kcrisman created at 2011-01-19 21:11:13

To release manager: I believe this should be closed. It's not even clear what doctests were ever disabled unless you look around a bit.  

In fact, #6294 seems to have cleared this up.  I suggest it be closed.


---

Comment by kcrisman created at 2011-01-19 21:11:13

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-03-12 03:45:15

I really don't think this is 'positive review', but if this gets the release manager's attention to close the ticket, I guess I'll do it ;-)


---

Comment by kcrisman created at 2011-03-12 03:45:15

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-03-17 09:47:12

Resolution: invalid
