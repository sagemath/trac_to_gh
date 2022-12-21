# Issue 4472: Sage 3.2.a3: more numerical noise in sage/calculus/wester.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-09 00:21:19

Assignee: mabshoff


```
sage -t  devel/sage/sage/calculus/wester.py                   
********************************************************************** 
File "/Users/tmp/sage-3.2.alpha3/tmp/wester.py", line 261: 
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
```



---

Comment by GeorgSWeber created at 2008-11-16 08:20:23

patch against Sage 3.2.rc1


---

Attachment


---

Comment by mabshoff created at 2008-11-16 08:56:40

Looks good to me. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-18 18:14:44

Resolution: fixed


---

Comment by mabshoff created at 2008-11-18 18:14:44

Merged in Sage 3.2.rc2
