# Issue 4438: Sage 3.2.a2: numerical noise in sage/calculus/functional.py and wester.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-04 13:55:36

Assignee: mabshoff


```
sage -t  devel/sage/sage/calculus/functional.py             
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/functional.py", line 248:
    sage: [float(h(i)) for i in range(5)]
Expected:
    <BLANKLINE>
    [0.0,
     -1.1102230246251565e-16,
     -5.5511151231257827e-17,
     -5.5511151231257827e-17,
     -6.9388939039072284e-17]
Got:
    [0.0, -1.1102230246251565e-16, 5.5511151231257827e-17, -5.5511151231257827e-17, -6.9388939039072284e-17]
**********************************************************************


sage -t  devel/sage/sage/calculus/wester.py                 
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/wester.py", line 261:
    : [float(f(i/10)) for i in range(1,5)]
Expected:
    <BLANKLINE>
    [-0.00033670040754082975,
     -0.0027778004096620235,
     -0.0098909940914040928,
     -0.025411145508414501]
Got:
    [-0.00033670040754082975, -0.0027778004096620235, -0.0098909940914039263, -0.02541114550841439]
**********************************************************************
```



---

Comment by GeorgSWeber created at 2008-11-04 22:11:25

Hi, these failures do not seem to be related.

In the "functional.py" case, the sign of the third entry flips (!); in the "wester.py" case, the last three digits of the third entry disagree.


---

Comment by mabshoff created at 2008-11-04 22:18:59

Replying to [comment:1 GeorgSWeber]:
> Hi, these failures do not seem to be related.

Yeah, I know. The point was that these are two small failures, so one ticket seem to cover it.

> In the "functional.py" case, the sign of the third entry flips (!); in the "wester.py" case, the last three digits of the third entry disagree.

Yep, I have patches that will be up shortly.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-11-05 22:28:25

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-11-05 22:31:12

Looks good.


---

Comment by mabshoff created at 2008-11-05 23:14:15

Resolution: fixed


---

Comment by mabshoff created at 2008-11-05 23:14:15

Merged in Sage 3.2.alpha3
