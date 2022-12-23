# Issue 4456: sage-3.2.alpha3 -- numerical noise on osx 32-bit intel

Issue created by migration from https://trac.sagemath.org/ticket/4456

Original creator: was

Original creation time: 2008-11-06 21:28:19

Assignee: mabshoff


```
sage -t  devel/sage/sage/calculus/wester.py
**********************************************************************
File "/Users/was/build/sage-3.2.alpha3/tmp/wester.py", line 261:
   : [float(f(i/10)) for i in range(1,5)]
Expected:
   <BLANKLINE>
   [-0.00033670040754082975,
    -0.0027778004096620235,
    -0.00989099409140...,
    -0.025411145508414...]
Got:
   [-0.00033670040754081587, -0.0027778004096621622,
-0.0098909940914039818, -0.025411145508414779]
**********************************************************************
1 items had failures:
  1 of 193 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file
/Users/was/build/sage-3.2.alpha3/tmp/.doctest_wester.py
        [11.4 s]
```



---

Comment by mabshoff created at 2008-11-09 00:29:00

Resolution: duplicate


---

Comment by mabshoff created at 2008-11-09 00:29:00

Oops, I opened a dupe of this at #4472, but since I will post a patch there I am closing this ticket :)

Cheers,

Michael
