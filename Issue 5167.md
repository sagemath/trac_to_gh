# Issue 5167: Sage 3.3.a4 on OSX: doctest failure in sage/calculus/calculus.py due to changed order of roots

Issue created by migration from https://trac.sagemath.org/ticket/5167

Original creator: mabshoff

Original creation time: 2009-02-03 18:12:12

Assignee: mabshoff

Note that this problem is different from #5129, but has also been observed on other platforms:

```
sage -t -long "devel/sage/sage/calculus/calculus.py"        
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py", line 3206:
    sage: f.roots(ring=CC)
Expected:
    [(-0.0588115223184495, 1), (1.36050567903502 + 1.51880872209965*I, 1), (-1.33109991787579 + 1.52241655183732*I, 1), (1.360505
67903502 - 1.51880872209965*I, 1), (-1.33109991787580 - 1.52241655183732*I, 1)]
Got:
    [(-0.0588115223184495, 1), (-1.33109991787579 + 1.52241655183732*I, 1), (1.36050567903502 + 1.51880872209965*I, 1), (-1.33109
991787579 - 1.52241655183732*I, 1), (1.36050567903502 - 1.51880872209965*I, 1)]
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py", line 3210:
    sage: f.roots(ring=CC, multiplicities=False)
Expected:
    [-0.0588115223184495, 1.36050567903502 + 1.51880872209965*I, -1.33109991787579 + 1.52241655183732*I, 1.36050567903502 - 1.518
80872209965*I, -1.33109991787580 - 1.52241655183732*I]
Got:
    [-0.0588115223184495, -1.33109991787579 + 1.52241655183732*I, 1.36050567903502 + 1.51880872209965*I, -1.33109991787579 - 1.52
241655183732*I, 1.36050567903502 - 1.51880872209965*I]
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py", line 3214:
    sage: f.roots(ring=QQbar, multiplicities=False)
Expected:
    [-0.05881152231844944?, 1.360505679035020? + 1.518808722099650?*I, -1.331099917875796? + 1.522416551837318?*I, 1.360505679035
020? - 1.518808722099650?*I, -1.331099917875796? - 1.522416551837318?*I]
Got:
    [-0.05881152231844944?, -1.331099917875796? + 1.522416551837318?*I, 1.360505679035020? + 1.518808722099650?*I, -1.33109991787
5796? - 1.522416551837318?*I, 1.360505679035020? - 1.518808722099650?*I]
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-02-03 18:34:34

#4544 ought to resolve this issue.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-03 20:11:10

Fixed via merging the reviewer patch at #4544.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-03 20:11:10

Resolution: fixed
