# Issue 11: doctest failure in functions/special.py

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 18:09:08

Assignee: somebody

sage -t -optional devel/sage-darcs/sage/functions/special.py*******************************************************\
***************
File "special.py", line 756:
    sage: inverse_jacobi("sn",0.47,1/2)
Exception raised:
    Traceback (most recent call last):
      File "/home/was/sage/local/lib/python2.4/doctest.py", line 1243, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example13[1]>", line 1, in ?
        inverse_jacobi("sn",RealNumber('0.47'),Integer(1)/Integer(2))###line 756:
    sage: inverse_jacobi("sn",0.47,1/2)
      File "/home/was/sage/local/lib/python2.4/site-packages/sage/functions/special.py", line 785, in inverse_jacob\
i
        return eval(maxima.eval("inverse_jacobi_sn(%s,%s)"%(RR(x),RR(m))))
      File "<string>", line 1
         ^[[
         ^
     SyntaxError: invalid syntax
**********************************************************************
File "special.py", line 758:
    sage: inverse_jacobi("sn",0.4707504,1/2)
Exception raised:


---

Comment by was created at 2006-10-15 18:10:16

Resolution: fixed


---

Comment by was created at 2006-10-15 18:10:16

Fixed:

The main trick was to use float conversions instead of RR before
calling into maxima.
