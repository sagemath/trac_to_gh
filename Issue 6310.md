# Issue 6310: optional doctest failure

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 14:39:31

Assignee: tbd


```
sage -t -long --optional devel/sage/sage/schemes/elliptic_curves/ell_egros.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/elliptic_curves/ell_egros.py", line 63:
    sage: [e.label() for e in EllipticCurves_with_good_reduction_outside_S([11])]
Expected:
    Failed to find S-integral points on  [0, 0, 0, 0, -25299648]
    Failed to find S-integral points on  [0, 0, 0, 0, -278296128]
    ['11a1',
    '11a2',
    '11a3',
    '121a1',
    '121a2',
    '121b1',
    '121b2',
    '121c1',
    '121c2',
    '121d1',
    '121d2',
    '121d3']
Got:
    ['11a1', '11a2', '11a3', '121a1', '121a2', '121b1', '121b2', '121c1', '121c2', '121d1', '121d2', '121d3']
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_ell_egros.py
	 [29.5 s]
```



---

Comment by cremona created at 2009-06-16 14:45:06

Was that with the large database installed?  that would make sense -- it needs the MW basis of the two curves whose conductors are 13068 and 52272, which it cannot find unless the optional package is installed.

I don't think I know how to tag that test to expect two warnings lines iff that package is not installed.  Would it work to put an initial "..." in front of the output?


---

Comment by cremona created at 2009-06-16 16:43:23

applies to 4.0.2.rc2


---

Attachment

I have fixed it by running that example with "proof=False" and explaining in the accompanying text that this is only needed to avoid warnings when the optional database is not installed.

Tested both with and without the database installed!


---

Comment by mvngu created at 2009-07-23 03:24:34

Resolution: fixed
