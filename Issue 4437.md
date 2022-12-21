# Issue 4437: Sage 3.2.a2: numerical noise in sage/graphs/graph.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-04 13:53:58

Assignee: mabshoff

On an x86:

```
sage -t  devel/sage/sage/graphs/graph.py                    **********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-cicero/tmp/graph.py", line 5802:
    sage: P.spectrum(laplacian=True)
Expected:
    [...e-16, 2.0, 2.0, 2.0, 2.0, 2.0, 5.0, 5.0, 5.0, 5.0]
Got:
    [4.89153937105e-17, 2.0, 2.0, 2.0, 2.0, 2.0, 5.0, 5.0, 5.0, 5.0]
**********************************************************************
```



---

Attachment


---

Comment by mhansen created at 2008-11-05 22:20:26

I'm okay with this.


---

Comment by mabshoff created at 2008-11-05 23:13:27

Resolution: fixed


---

Comment by mabshoff created at 2008-11-05 23:13:27

Merged in Sage 3.2.alpha3
