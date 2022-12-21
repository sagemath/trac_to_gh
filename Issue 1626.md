# Issue 1626: update lcalc to 20070902

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-29 04:39:50

Assignee: mabshoff




---

Comment by mabshoff created at 2007-12-29 04:39:55

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-27 17:27:47

See also #932 and #449.

Cheers,

Michael


---

Comment by was created at 2008-01-27 17:32:34

Update it to NOW:

```
Dear Colleagues,

I've released a new version of lcalc.

This release fixes some bugs (so please update), has improvements to some of the key
routines, especially for higher degree L-functions (i.e. deg >=3, and also for Maass forms),
and better handling of output precision.

The code can be downloaded from:
http://pmmac03.math.uwaterloo.ca/~mrubinst/L_function_public/CODE/

Please email me any bugs you notice.

Thanks,
```



---

Comment by mabshoff created at 2008-03-26 00:08:27

The latest release is from Feb. 5th, 2008. I did fix some warnings, fixed a Solaris build issue and squashed about 500 lines of warnings. The changes have been send upstream and will hopefully be integrated soon.

Cheers,

Michael


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-04-14 02:51:35

The updated lcalc.spkg has some doctest failures:

```
sage -t -long devel/sage/sage/lfunctions/lcalc.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/tmp/lcalc.py", line 188:
    sage: E.lseries().values_along_line(0.5, 3, 5)
Expected:
    lcalc:  1.5 0 WARNING- we don't have enough Dirichlet coefficients.
    lcalc:  Will use the maximum possible, though the output will not necessarily be accurate.
    lcalc:  nan nan
    [(0, 0.209951303),
     (0.500000000, -...e-16),
     (1.00000000, 0.133768433),
     (2.00000000, 0.552975867)]
Got:
    [(0, 0.209951303), (0.500000000, -2.96501173e-16), (1.00000000, 0.133768433), (1.50000000, 0.360092864), (2.00000000, 0.552975867)]
```

I consider this good news and suggest fixing the doctest.

Cheers,

Michael


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-04-14 03:28:39

The updated spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha5/lcalc-20080205.spkg

fixes a number of issues:

 * update to to the latest release
 * fix Solaris build
 * add gcc 4.3 build support

This ticket also closes #449. For doctests to pass you need to apply trac_1626_lcalc_doctest_fix.patch.

The other three patches have been send upstream to Mike Rubinstein and will hopefully make it into the next upstream release.

Cheers,

Michael


---

Comment by was created at 2008-04-14 03:37:21

REPORT:

I have not tried the patch out, but I read everything carefully and it all looks *perfect* to me.


---

Comment by mabshoff created at 2008-04-14 03:56:48

Merged in Sage 3.0.alpha5


---

Comment by mabshoff created at 2008-04-14 03:56:48

Resolution: fixed
