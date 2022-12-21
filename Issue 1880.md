# Issue 1880: Sage 2.10: qqbar numerical doctest failure

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-21 21:40:19

Assignee: mabshoff

Reported in http://groups.google.com/group/sage-devel/browse_thread/thread/ff3b035b8b42961f/f0dd2e8510b13853#f0dd2e8510b13853 by Francois: 


```
File "qqbar.py", line 3075:
    sage: cp.complex_roots(30, 1)
Expected:
    [[1.1892071150027208 .. 1.1892071150027213],
[-1.1892071150027213 .. -1.18920711500272...], [1.1892071150027208 ..
1.1892071150027213]*I, [-1.1892071150027213 .. -1.1892071150027208]*I]
Got:
    [[1.1892071150027208 .. 1.1892071150027213],
[-1.1892071150027213 .. -1.1892071150027210], [1.1892071150027210 ..
1.1892071150027213]*I, [-1.1892071150027213 .. -1.1892071150027208]*I] 
```



---

Attachment


---

Comment by mabshoff created at 2008-01-22 01:24:44

Resolution: fixed


---

Comment by mabshoff created at 2008-01-22 01:24:44

Merged in Sage 2.10.1.alpha1
