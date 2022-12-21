# Issue 2263: Sage 2.10.2.rc0: numerical noise doctest failure in calculus/calculus.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-02-22 19:15:32

Assignee: failure

Craig Citro reported:

```
**********************************************************************
File "calculus.py", line 
    sage: f.find_maximum_on_interval(0,5, tol=0.1, maxfun=10)
Expected:
    (0.56109032345808163, 0.857926501456)
Got:
    (0.56109032345808174, 0.857926501456)
********************************************************************** 
```



---

Comment by mabshoff created at 2008-02-22 19:15:44

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-22 19:15:44

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-02-22 19:15:44

Changing assignee from failure to mabshoff.


---

Comment by was created at 2008-02-22 21:06:19

Numerical noise makes sense here, since behind the scenes this is double arithmetic
done in FORTRAN in scipy.   So we should just change the expected output to 

(0.561090323458081..., 0.857926501456)


---

Attachment


---

Comment by mabshoff created at 2008-02-22 22:14:11

Resolution: fixed


---

Comment by mabshoff created at 2008-02-22 22:14:11

Merged in Sage 2.10.2.final
