# Issue 2973: RDF doctest failures on arch linux (gcc 4.3)

Issue created by migration from https://trac.sagemath.org/ticket/2973

Original creator: was

Original creation time: 2008-04-20 21:03:23

Assignee: somebody


```
sage -t  devel/sage/sage/rings/real_double.pyx              **********************************************************************
File "/home/was/build/sage-3.0.rc0/tmp/real_double.py", line 544:
    sage: a = -RDF(1)/RDF(0); a.str()
Expected:
    '-inf'
Got:
    'inf'
**********************************************************************
File "/home/was/build/sage-3.0.rc0/tmp/real_double.py", line 979:
    sage: a.is_positive_infinity()
Expected:
    False
Got:
    True
**********************************************************************
File "/home/was/build/sage-3.0.rc0/tmp/real_double.py", line 991:
    sage: a.is_negative_infinity()
Expected:
    True
Got:
    False
**********************************************************************
3 items had failures:
   1 of   6 in __main__.example_35
   1 of   5 in __main__.example_67
   1 of   5 in __main__.example_68
***Test Failed*** 3 failures.

```



---

Comment by mabshoff created at 2008-04-20 22:53:45

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-20 22:53:45

I know how to fix this. Spkg coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-20 22:53:45

Changing assignee from somebody to mabshoff.


---

Comment by mabshoff created at 2008-04-21 04:00:17

The fix is to use GSL's isinf in all cases and not only on OSX. Hence the diff is minimal in spkg-install. The spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/rc1/gsl-1.10.p1.spkg

Cheers,

Michael


---

Comment by was created at 2008-04-21 04:40:59

works for me and the changes to the spkg look good.


---

Comment by mabshoff created at 2008-04-21 04:54:26

Resolution: fixed


---

Comment by mabshoff created at 2008-04-21 04:54:26

Merged in Sage 3.0.rc1
