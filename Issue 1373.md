# Issue 1373: 2.8.15.alpha2: quotient_module.py doctest failure

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-12-02 17:27:05

Assignee: was

On my laptop (32-bit x86 Linux, Debian testing) I get the following doctest failure in 2.8.15.alpha2:

```
sage -t  devel/sage-main/sage/modules/quotient_module.py    **********************************************************************
File "quotient_module.py", line 161:
    sage: cmp(Q1, 5)
Expected:
    1                  
Got:
    -1
**********************************************************************
```


The code compares type(Q1) and type(5); since type objects have no useful pre-defined comparison operation, this just compares the memory addresses of the type objects.

I think the doctest should just be removed.


---

Comment by was created at 2007-12-03 01:37:35


```
sage: cmp(Q1, 5) != 0
True
```



---

Comment by mabshoff created at 2007-12-03 01:52:47

Merged in 2.8.15.rc0.


---

Comment by mabshoff created at 2007-12-03 01:52:47

Resolution: fixed
