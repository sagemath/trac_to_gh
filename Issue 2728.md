# Issue 2728: doctest failures for maxima in Debian packaged sage 2.10.4

Issue created by migration from https://trac.sagemath.org/ticket/2728

Original creator: tabbott

Original creation time: 2008-03-29 23:43:26

Assignee: tabbott

I think these are problems with the maxima doctests below, unless there's a good reason why things should be printing without the "0." at the front or why small roundoff errors should matter.  None of them are materially different answers.

This is running with maxima 5.13.0 (the current in Debian lenny).

sage -t  devel/sage-main/sage/interfaces/maxima.py          **********************************************************************
File "maxima.py", line 795:
    sage: f(3.2)
Expected:
    -.05837414342758009
Got:
    -0.05837414342758
**********************************************************************
File "maxima.py", line 798:
    sage: f(2,3.5)
Expected:
    sin(2)-.9364566872907963
Got:
    sin(2)-0.9364566872908
**********************************************************************
File "maxima.py", line 816:
    sage: float(t(2))
Expected:
    0.90929742682568171
Got:
    0.90929742682568004
**********************************************************************
File "maxima.py", line 1543:
    sage: maxima('exp(-sqrt(x))').nintegral('x',0,1)
Expected:
    (.5284822353142306, 4.163314137883845E-11, 231, 0)
Got:
    (0.52848223531423, 4.1633141378838445E-11, 231, 0)
**********************************************************************
File "maxima.py", line 1588:
    sage: f.numer()         # I wonder how to get a real number (~1.463)??
Expected:
    -.8862269254527579*%i*erf(%i)
Got:
    -0.88622692545276*%i*erf(%i)
**********************************************************************
3 items had failures:
   3 of  14 in __main__.example_12
   1 of   4 in __main__.example_44
   1 of   8 in __main__.example_45
***Test Failed*** 5 failures.



---

Comment by mabshoff created at 2008-03-30 09:57:00

Resolution: wontfix


---

Comment by mabshoff created at 2008-03-30 09:57:00

This is not *Sage Specific*: It might be due to Debian packaging an older version of Maxima or alternatively be caused by using gcl instead of clisp. It is certainly borderline, but I don't think in this case it is on our end to fix this. 

Cheers,

Michael
