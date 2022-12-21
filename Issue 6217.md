# Issue 6217: [with patch, needs review] fix issues with sorting in formal_sum

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-06-05 00:22:10

Assignee: somebody


```
Ok, note that this is rc1 on Fedora 10, 32 bit:

The followin tests failed:


sage -t  "devel/sage/sage/structure/formal_sum.py"
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py", line 293:
    sage: for z in FormalSum([(1,2), (5, 'a'), (-3, 7)]): print z
Expected:
    (5, 'a')
    (1, 2)
    (-3, 7)
Got:
    (1, 2)
    (-3, 7)
    (5, 'a')
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py", line 304:
    sage: v = FormalSum([(1,2), (5, 'a'), (-3, 7)]); v
Expected:
    5*a + 2 - 3*7
Got:
    2 - 3*7 + 5*a
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py", line 306:
    sage: v[0]         # indirect doctest
Expected:
    (5, 'a')
Got:
    (1, 2)
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py", line 308:
    sage: v[1]
Expected:
    (1, 2)
Got:
    (-3, 7)
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py", line 310:
    sage: v[2]
Expected:
    (-3, 7)
Got:
    (5, 'a')
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py", line 312:
    sage: list(v)
Expected:
    [(5, 'a'), (1, 2), (-3, 7)]
Got:
    [(1, 2), (-3, 7), (5, 'a')]
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py", line 321:
    sage: v = FormalSum([(1,2), (5, 'a'), (-3, 7)]); v
Expected:
    5*a + 2 - 3*7
Got:
    2 - 3*7 + 5*a
**********************************************************************
3 items had failures:
   1 of   3 in __main__.example_12
   5 of   7 in __main__.example_13
   1 of   4 in __main__.example_14
***Test Failed*** 7 failures.
```



---

Attachment

I've made it so that the examples don't use the string 'a' as a bases since that was causing problems for the sorting.


---

Comment by was created at 2009-06-06 16:54:48

merged in 4.0.1.rc3


---

Comment by was created at 2009-06-06 16:54:48

Resolution: fixed
