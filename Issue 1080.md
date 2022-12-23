# Issue 1080: inconsistent doctest failure in sage/misc/sage_eval.py

Issue created by migration from https://trac.sagemath.org/ticket/1080

Original creator: cwitty

Original creation time: 2007-11-03 17:14:28

Assignee: cwitty

On one of my machines (64-bit x86 Debian testing), doctesting sage/misc/sage_eval.py sometimes fails with:

```
**********************************************************************
File "sage_eval.py", line 92:
    sage: ff = gap.eval('x:=IndeterminatesOfPolynomialRing(R);; f:=x^2+1;'); ff
Expected:
    'x^2+1'
Got:
    '1'
**********************************************************************
File "sage_eval.py", line 94:
    sage: sage_eval(ff, locals={'x':x})
Expected:
    x^2 + 1
Got:
    1
**********************************************************************
File "sage_eval.py", line 96:
    sage: eval(ff)
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: Use ** for exponentiation, not '^', which means xor
    in Python, and has the wrong precedence.
Got:
    1
**********************************************************************
1 items had failures:
   3 of  27 in __main__.example_1
```


(This fails about half the times I run it.)

It looks like some sort of timing issue.


---

Attachment

Found it.  Gap sends garbage collection information that starts with an '`@`', followed by one of these characters '123456!"#$%&', and then terminated by a plus sign.  The code was sometimes grabbing too much data, including part of the real Gap output.


---

Comment by was created at 2007-11-03 18:46:41

Resolution: fixed
