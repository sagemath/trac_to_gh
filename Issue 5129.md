# Issue 5129: numerical noise in roots calculus/calculus.py

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2009-01-29 19:55:22

Assignee: burcin


```
[jaap`@`peace sage-3.3.alpha0]$ ./sage -t "devel/sage/sage/calculus/calculus.py"
sage -t  "devel/sage/sage/calculus/calculus.py"
**********************************************************************
File "/home/jaap/Download/sage-3.3.alpha0/devel/sage/sage/calculus/calculus.py",
line 3206:
    sage: f.roots(ring=CC)
Expected:
    [(-0.0588115223184495, 1), (1.36050567903502 + 1.51880872209965*I,
1), (-1.33109991787579 + 1.52241655183732*I, 1), (1.36050567903502 -
1.51880872209965*I, 1), (-1.33109991787580 - 1.52241655183732*I, 1)]
Got:
    [(-0.0588115223184495, 1), (1.36050567903502 + 1.51880872209965*I,
1), (-1.33109991787580 + 1.52241655183732*I, 1), (1.36050567903502 -
1.51880872209965*I, 1), (-1.33109991787580 - 1.52241655183732*I, 1)]
**********************************************************************
File "/home/jaap/Download/sage-3.3.alpha0/devel/sage/sage/calculus/calculus.py",
line 3208:
    sage: (2.5*f).roots(ring=RR)
Expected:
    [(-0.0588115223184494, 1)]
Got:
    [(-0.0588115223184495, 1)]
**********************************************************************
File "/home/jaap/Download/sage-3.3.alpha0/devel/sage/sage/calculus/calculus.py",
line 3210:
    sage: f.roots(ring=CC, multiplicities=False)
Expected:
    [-0.0588115223184495, 1.36050567903502 + 1.51880872209965*I,
-1.33109991787579 + 1.52241655183732*I, 1.36050567903502 -
1.51880872209965*I, -1.33109991787580 - 1.52241655183732*I]
Got:
    [-0.0588115223184495, 1.36050567903502 + 1.51880872209965*I,
-1.33109991787580 + 1.52241655183732*I, 1.36050567903502 -
1.51880872209965*I, -1.33109991787580 - 1.52241655183732*I]
**********************************************************************
1 items had failures:
   3 of  29 in __main__.example_81
***Test Failed*** 3 failures.
For whitespace errors, see the file
/home/jaap/Download/sage-3.3.alpha0/tmp/.doctest_calculus.py
	 [243.9 s]
exit code: 1024

------------------------------

```


This is on Fedora 10, 32 bits.

Jaap


---

Comment by mabshoff created at 2009-02-03 17:37:06

This is a blocker!

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-03 17:37:06

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-03 17:37:06

Changing priority from major to blocker.


---

Comment by mabshoff created at 2009-02-03 17:37:06

Changing assignee from burcin to mabshoff.


---

Attachment


---

Comment by mabshoff created at 2009-02-03 18:25:30

Patch is up.

Cheers,

Michael


---

Comment by jsp created at 2009-02-03 18:36:30

On Fedora 9, 32 bits:


```
[jaap`@`paix sage-3.3.alpha3]$ ./sage -t "devel/sage/sage/calculus/calculus.py"
sage -t  "devel/sage/sage/calculus/calculus.py"             
	 [171.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 171.4 seconds

```


Looks good to me!

Jaap


---

Comment by mabshoff created at 2009-02-03 18:51:10

Merged in Sage 3.3.alpha5.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-03 18:51:10

Resolution: fixed
