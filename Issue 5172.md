# Issue 5172: Sage 3.3.a5: more numerical noise in sage/calculus/calculus.py

Issue created by migration from https://trac.sagemath.org/ticket/5172

Original creator: mabshoff

Original creation time: 2009-02-04 14:09:25

Assignee: mabshoff

See on cicero:

```
sage -t -long "devel/sage/sage/calculus/calculus.py"        
**********************************************************************
File "/home/mabshoff/build-3.3.alpha5/sage-3.3.alpha5-cicero/devel/sage/sage/calculus/calculus.py", line 3206:
    sage: f.roots(ring=CC)
Expected:
    [(-0.0588115223184495, 1), (-1.331099917875... - 1.52241655183732*I, 1), (-1.33109991787579 + 1.52241655183732*I, 1), (1.36050567903502 - 1.51880872209965*I, 1), (1.36050567903502 + 1.51880872209965*I, 1)]
Got:
    [(-0.0588115223184495, 1), (-1.33109991787580 - 1.52241655183732*I, 1), (-1.33109991787580 + 1.52241655183732*I, 1), (1.36050567903502 - 1.51880872209965*I, 1), (1.36050567903502 + 1.51880872209965*I, 1)]
**********************************************************************
File "/home/mabshoff/build-3.3.alpha5/sage-3.3.alpha5-cicero/devel/sage/sage/calculus/calculus.py", line 3210:
    sage: f.roots(ring=CC, multiplicities=False)
Expected:
    [-0.0588115223184495, -1.331099917875... - 1.52241655183732*I, -1.33109991787579 + 1.52241655183732*I, 1.36050567903502 - 1.51880872209965*I, 1.36050567903502 + 1.51880872209965*I]
Got:
    [-0.0588115223184495, -1.33109991787580 - 1.52241655183732*I, -1.33109991787580 + 1.52241655183732*I, 1.36050567903502 - 1.51880872209965*I, 1.36050567903502 + 1.51880872209965*I]
**********************************************************************
```



---

Attachment


---

Comment by mabshoff created at 2009-02-05 13:24:23

Changing status from new to assigned.


---

Comment by jsp created at 2009-02-05 15:01:22

After applying the patch:


```
sage -t  "devel/sage/sage/calculus/calculus.py"             
	 [276.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 276.2 seconds
[jaap@paix sage-3.3.alpha4]$ 

```


Works for me on Fedora 9, 32 bits

Jaap


---

Comment by mabshoff created at 2009-02-05 23:40:50

Merged in Sage 3.3.alpha6.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-05 23:40:50

Resolution: fixed
