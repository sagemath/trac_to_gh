# Issue 6754: sage-4.1.1 -- numerical noise on OS X 10.5 PPC

Issue created by migration from https://trac.sagemath.org/ticket/6754

Original creator: was

Original creation time: 2009-08-15 16:36:55

Assignee: davidloeffler


```


**********************************************************************
File "/Users/wstein/build/sage-4.1.1/devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py", line 2881:
    sage: E.division_polynomial(3).roots(CC,multiplicities=False)
Expected:
    [-2.88288879135334,
    1.39292799513138,
    0.078313731444316... - 0.492840991709879*I,
    0.078313731444316... + 0.492840991709879*I]
Got:
    [-2.88288879135335, 1.39292799513138, 0.0783137314443168 - 0.492840991709879*I, 0.0783137314443168 + 0.492840991709879*I]
**********************************************************************
1 items had failures:
   1 of  22 in __main__.example_61
***Test Failed*** 1 failures.
```



---

Comment by cremona created at 2009-08-15 17:44:45

I don't see why this is not ok, give the "..." in the Expected text (assuming whitespace differences are also ok).


---

Comment by was created at 2009-10-02 16:16:52

Resolution: fixed
