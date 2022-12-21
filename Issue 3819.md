# Issue 3819: Sage 3.1.alpha1> time_series.pyx numerical noise doctest failures

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-08-12 15:33:51

Assignee: mabshoff

CC:  cremona

Reported by John Cremona:

```
*******************
File "/home/john/sage-3.1.alpha1/tmp/time_series.py", line 1507:
    sage: finance.TimeSeries([z.hurst_exponent() for z in y]).mean()
Expected:
    0.57984822577934747
Got:
    0.57984822577934769
**********************************************************************
File "/home/john/sage-3.1.alpha1/tmp/time_series.py", line 1515:
    sage: finance.TimeSeries([z.hurst_exponent() for z in y]).mean()
Expected:
    0.2861023256237053
Got:
    0.28610232562370524
**********************************************************************
1 items had failures:
   2 of  16 in __main__.example_46
***Test Failed*** 2 failures.
For whitespace errors, see the file
/home/john/sage-3.1.alpha1/tmp/.doctest_time_series.py
         [9.8 s]
exit code: 1024
```



---

Comment by mabshoff created at 2008-08-12 17:13:54

John,

can you review this?

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-12 17:13:54

Changing status from new to assigned.


---

Attachment

Oops, adding John to the CC would help a lot when asking for his review :)

Cheers,

Michael


---

Comment by was created at 2008-08-13 00:18:48

I agree with this patch.


---

Comment by mabshoff created at 2008-08-13 00:20:25

Resolution: fixed


---

Comment by mabshoff created at 2008-08-13 00:20:25

Merged in Sage 3.1.alpha2
