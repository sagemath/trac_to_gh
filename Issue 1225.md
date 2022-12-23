# Issue 1225: OSX 10.4 PPC: slight numerical noise in rings/polynomial/polynomial_element.pyx

Issue created by migration from https://trac.sagemath.org/ticket/1225

Original creator: mabshoff

Original creation time: 2007-11-20 22:56:05

Assignee: mabshoff


```
michael-abshoffs-ibook-g4:~/Desktop/sage-2.8.13.rc0 mabshoff$ ./sage -
t  devel/sage-main/sage/rings/polynomial/polynomial_element.pyx
sage -t  devel/sage-main/sage/rings/polynomial/
polynomial_element.pyx**********************************************************************
File "polynomial_element.pyx", line 2314:
    sage: f.roots(ring=CC)
Expected:
    [(1.00000000000000, 1), (-0.500000000000000 + 0.866025403784438*I,
1), (-0.500000000000000 - 0.866025403784438*I, 1)]
Got:
    [(1.00000000000000, 1), (-0.500000000000000 + 0.866025403784439*I,
1), (-0.500000000000000 - 0.866025403784439*I, 1)]
**********************************************************************
File "polynomial_element.pyx", line 2749:
    sage: (x^3 - 1).complex_roots()
Expected:
    [1.00000000000000, -0.500000000000000 + 0.866025403784438*I,
-0.500000000000000 - 0.866025403784438*I]
Got:
    [1.00000000000000, -0.500000000000000 + 0.866025403784439*I,
-0.500000000000000 - 0.866025403784439*I]
**********************************************************************
2 items had failures:
   1 of  88 in __main__.example_55
   1 of  12 in __main__.example_57
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_polynomial_element.pyx
         [27.8 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-main/sage/rings/polynomial/
polynomial_element.pyx
Total time for all tests: 27.8 seconds
michael-abshoffs-ibook-g4:~/Desktop/sage-2.8.13.rc0 mabshoff$
```


I have a patch for this, so this issue should be resolved shortly.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-20 22:56:14

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-21 13:12:52

My patch doesn't work, i.e. the ".." trick:

```
    sage: f.roots(ring=CC)
Expected:
    [(1.00000000000000, 1), (-0.500000000000000 + 0.866025403784438*I, 1), (-0.500000000000000 - 0.8660254037844..*I, 1)]
Got:
    [(1.00000000000000, 1), (-0.500000000000000 + 0.866025403784438*I, 1), (-0.500000000000000 - 0.866025403784438*I, 1)
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-11-21 13:18:20


```
[14:11] <mabshoff> Is there a special trick on how to use "..." in such a list?
[14:14] <wstein2> Use ... rather than ..
[14:14] <wstein2> It's *three* dots.
```



---

Comment by mabshoff created at 2007-11-21 13:18:32

Resolution: fixed


---

Comment by mabshoff created at 2007-11-21 13:18:32

Merged in 2.8.13.rc2.
