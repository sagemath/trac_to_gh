# Issue 2250: sage 2.10.2.rc0: elliptic_curves/monsky_washnitzer.py doctest failure with -long

Issue created by migration from https://trac.sagemath.org/ticket/2250

Original creator: mabshoff

Original creation time: 2008-02-21 19:30:23

Assignee: was


```
sage -t -long devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py
**********************************************************************
File "monsky_washnitzer.py", line 1380:
    sage: A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.rc0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_32[64]>", line 1, in <module>
        A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time###line 1380:
    sage: A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1439, in matrix_of_frobenius
        F1_reduced = reduce_all(Q, p, F1_coeffs, offset)
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 913, in reduce_all
        exact_form = reduce_positive(Q, p, coeffs, offset, exact_form)
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 790, in reduce_positive
        a[0] = a[0] - Qa*a[2]/3   # subtract d(y^j + 3)
      File "element.pyx", line 1482, in sage.structure.element.RingElement.__div__
      File "coerce.pyx", line 247, in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c
      File "coerce.pyx", line 432, in sage.structure.coerce.CoercionModel_cache_maps.get_action_c
      File "coerce.pyx", line 550, in sage.structure.coerce.CoercionModel_cache_maps.discover_action_c
      File "action.pyx", line 93, in sage.categories.action.Action.__invert__
      File "action.pyx", line 156, in sage.categories.action.InverseAction.__init__
    TypeError: No inverse defined for Right scalar multiplication by Integer Ring on Power Series Ring in t over Ring of integers modulo 14641.
**********************************************************************
File "monsky_washnitzer.py", line 1382:
    sage: B                                                     # long time
Expected:
    [1144 + 264*t + 841*t^2 + 1025*t^3 + O(t^4)  176 + 1052*t + 216*t^2 + 523*t^3 + O(t^4)]
    [   847 + 668*t + 81*t^2 + 424*t^3 + O(t^4)   185 + 341*t + 171*t^2 + 642*t^3 + O(t^4)]
Got:
    [ 514  927]
    [ 702 1036]
**********************************************************************
File "monsky_washnitzer.py", line 1392:
    sage: B.det()                                               # long time
Expected:
    11 + 484*t^2 + 451*t^3 + O(t^4)
Got:
    209
**********************************************************************
1 items had failures:
   3 of  68 in __main__.example_32
***Test Failed*** 3 failures.
For whitespace errors, see the file .doctest_monsky_washnitzer.py
         [14.3 s]
exit code: 256
```



---

Comment by robertwb created at 2008-02-21 20:38:45

On 2.10.2.alpha0 + #2079 fixes, it passes fine. 


```
Robert-Bradshaws-Laptop:~/sage/current/devel/sage-bugs2 robert$ sage -t -long sage/schemes/elliptic_curves/monsky_washnitzer.py 
sage -t -long sage/schemes/elliptic_curves/monsky_washnitzer.py
Raising timeout to 1800 seconds due to '-long' option

         [28.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 28.5 seconds
```



---

Comment by robertwb created at 2008-02-21 20:49:06

I take that back, I was working in the wrong branch. I do get that error in 2.10.2.alpha0 + #2079 fixes.


---

Attachment

The above patch fixes this issue, returning None rather than raising an error in this corner case where there is no action (now that division by Z -> multiplication by Q).


---

Comment by was created at 2008-02-21 22:54:51

This works fine:


```
was@sage:~/build/sage-2.10.2.alpha2$ ./sage -t -long devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py
sage -t -long devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py
Raising timeout to 1800 seconds due to '-long' option

	 [14.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 14.4 seconds

```



---

Comment by mabshoff created at 2008-02-21 22:56:23

Merged in Sage 2.10.2.rc0


---

Comment by mabshoff created at 2008-02-21 22:56:23

Resolution: fixed
