# Issue 3013: bug in integrate (found during a talk!)

Issue created by migration from https://trac.sagemath.org/ticket/3013

Original creator: was

Original creation time: 2008-04-23 23:50:42

Assignee: was


```
sage: integrate(sin(x)*cos(10*x)*log(x))
Traceback (most recent call last):
...
TypeError: Error executing code in Maxima
CODE:
	sage22 : integrate(sage21,sage3)$
Maxima ERROR:
	

Too many contexts.
sage: show(integrate(sin(x^2)
```



---

Comment by was created at 2008-04-23 23:51:39

This is also a Maxima bug:

```
Last login: Wed Apr 23 16:43:25 on ttys014
teragon-2:~ was$ sage -maxima
Maxima 5.13.0 http://maxima.sourceforge.net
Using Lisp CLISP 2.41 (2006-10-13)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) integrate(sin(x)*cos(10*x)*log(x),x);

Too many contexts.
 -- an error.  To debug this try debugmode(true);
(%i2) 
```



---

Comment by mabshoff created at 2008-06-15 16:51:08

This is fixed in Maxima 5.15.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-22 21:46:47

This now works:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.1, Release Date: 2008-08-17                       |
| Type notebook() for the GUI, and license() for information.        |
sage: integrate(sin(x)*cos(10*x)*log(x))
(9*integrate(cos(11*x)/x, x) - 11*integrate(cos(9*x)/x, x) - 9*log(x)*cos(11*x) + 11*log(x)*cos(9*x))/198
```

So once we add a doctest we can close this ticket.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-08-22 22:05:17

Maxima returns a solution that is partially unevaluated, so merging this might or might not be a good idea.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-23 00:05:58

Resolution: fixed


---

Comment by mabshoff created at 2008-08-23 00:05:58

Merged in Sage 3.1.2.alpha0
