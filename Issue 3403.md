# Issue 3403: [with patch; needs review] get doctest coverage for rational up to 100%

Issue created by migration from https://trac.sagemath.org/ticket/3403

Original creator: was

Original creation time: 2008-06-12 15:14:25

Assignee: somebody




---

Attachment


---

Comment by mabshoff created at 2008-06-26 03:27:14

Merged in Sage 3.0.4.alpha1


---

Comment by mabshoff created at 2008-06-26 03:27:14

Resolution: fixed


---

Comment by mabshoff created at 2008-06-26 04:10:31

We have one broken doctest:

```
sage -t  devel/sage/sage/misc/sageinspect.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha1/tmp/sageinspect.py", line 77:
    sage: sage_getdoc(sage.rings.rational.make_rational).lstrip()
Expected:
    ''
Got:
    "Make a rational number from s (a string in base 32)\n\n    INPUT:\n        s -- string in base 32\n    OUTPUT:\n        Rational\n        \n    EXAMPLES:\n        sage: (-7/15).str(32)\n        '-7/f'\n        sage: sage.rings.rational.make_rational('-7/f')\n        -7/15    \n    "
**********************************************************************
1 items had failures:
   1 of  26 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.4.alpha1/tmp/.doctest_sageinspect.py
	 [2.6 s]
exit code: 1024
```



---

Comment by mabshoff created at 2008-06-26 05:03:46

Fixed in Sage 3.0.4.alpha1 as discussed with William in person.

Cheers,

Michael
