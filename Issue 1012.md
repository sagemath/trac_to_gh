# Issue 1012: fix some doctests

Issue created by migration from https://trac.sagemath.org/ticket/1012

Original creator: was

Original creation time: 2007-10-27 15:40:43

Assignee: failure


```
I have the following doctest failures on BSD (Intel Mac).  See below.
All are easy to fix doctests that changed because of recent improvements
to Sage, I think.

        sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py
        sage -t  devel/sage-main/sage/interfaces/gp.py
        sage -t  devel/sage-main/sage/interfaces/maxima.py
Total time for all tests: 2982.5 seconds

sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py  **********************************************************************
File "cubegroup.py", line 1191:
    sage: C.plot3d()
Expected:
    <class 'sage.plot.plot3d.base.TransformGroup'>
Got:
    <class 'base.TransformGroup'>
************************************

******************************
File "gp.py", line 365:
    sage: ComplexField(10)(gp(11243.9812+15*I))
Expected:
     1.1e4 + 15*I
Got:
    1.1e4 + 15.*I
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_11


sage -t  devel/sage-main/sage/interfaces/maxima.py          **********************************************************************
File "maxima.py", line 1227:
    sage: ComplexField(10)(maxima('2342.23482943872+234*%i'))
Expected:
     2300 + 230*I
Got:
    2300. + 230.*I
**********************************************************************
1 items had failures:



I have the following doctest failures on sage.math:

        sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py
        sage -t  devel/sage-main/sage/interfaces/gp.py
        sage -t  devel/sage-main/sage/interfaces/maxima.py
        sage -t  devel/sage-main/sage/rings/finite_field_givaro.pyx
        sage -t  devel/sage-main/sage/rings/finite_field_ext_pari.py
Total time for all tests: 2332.1 seconds

The first givaro failure is:

File "finite_field_givaro.pyx", line 799:
    sage: hash(GF(3^4, 'a'))
Expected:
    -4281682415996964816
Got:
    695660592

The second finite field failure is:

sage -t  devel/sage-main/sage/rings/finite_field_ext_pari.py**********************************************************************
File "finite_field_ext_pari.py", line 593:
    sage: hash(GF(9,'a'))
Expected:
    -8785304532306495574
Got:
    205387690
**********************************************************************
File "finite_field_ext_pari.py", line 596:
    sage: hash(GF(9,'b'))
Expected:
    5852897890058287069
Got:
    -74532899
**********************************************************************
1 items had failures:
   2 of   4 in __main__.example_13


 William
```



---

Comment by was created at 2007-10-27 15:41:35

Changing priority from major to blocker.


---

Comment by cwitty created at 2007-10-27 16:10:34

Changing assignee from failure to cwitty.


---

Comment by cwitty created at 2007-10-27 16:10:34

Changing status from new to assigned.


---

Comment by cwitty created at 2007-10-27 21:10:51

Resolution: fixed
