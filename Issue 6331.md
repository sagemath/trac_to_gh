# Issue 6331: optional doctest failure -- magma interface slight problems

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 15:08:39

Assignee: tbd


```
sage -t -long --optional devel/sage/sage/interfaces/mathematica.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/mathematica.py", line 181:
    sage: n.FactorInteger()                  # optional - mathematica
Expected:
    {{2, 2}, {3, 2}, {5, 3}, {541, 1}}       # optional - mathematica
Got:
    {{2, 2}, {3, 2}, {5, 3}, {541, 1}}
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/mathematica.py", line 236:
    sage: math_bessel_K(2,I)                      # optional - mathematica
Expected:
    0.180489972066962*I - 2.592886175491197
Got:
    -2.592886175491196978 + 0.1804899720669620266*I
**********************************************************************
1 items had failures:
   2 of  62 in __main__.example_0
***Test Failed*** 2 failures.
```



---

Comment by flawrence created at 2009-09-14 07:17:41

Both these errors are addressed in #4948.  The first error (an extra "# optional - mathematica") is fixed properly.  The second error is probably due to 32/64 bit versions of mathematica, or maybe even just different versions of mathematica.  The patch in #4948 adds -2.592886175491196978 + 0.1804899720669620266*I as a legitimate solution.


---

Comment by flawrence created at 2009-09-23 04:20:54

I believe that this should be fixed in 4.1.2.alpha2 since #4948 was merged.


---

Comment by mhansen created at 2009-10-05 04:47:25

Seems good to me.  Fixed by #4948.


---

Comment by mhansen created at 2009-10-05 04:47:25

Resolution: duplicate
