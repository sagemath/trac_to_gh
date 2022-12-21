# Issue 3607: graph_isom.py: "Conditional jump or move depends on uninitialised value(s)"

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-07-08 11:51:25

Assignee: rlm


```
==19975== Conditional jump or move depends on uninitialised value(s)
==19975==    at 0x1F3E16DD: __pyx_pf_4sage_6graphs_10graph_isom_search_tree (graph_isom.c:12972)
==19975==    by 0x4F0F43: PyCFunction_Call (methodobject.c:77)
==19975==    by 0x41B0FA: PyObject_Call (abstract.c:1861)
==19975==    by 0x4952F3: do_call (ceval.c:3784)
==19975==    by 0x494BAA: call_function (ceval.c:3596)
==19975==    by 0x491174: PyEval_EvalFrameEx (ceval.c:2272)
==19975==    by 0x492E64: PyEval_EvalCodeEx (ceval.c:2836)
==19975==    by 0x48B385: PyEval_EvalCode (ceval.c:494)
==19975==    by 0x4965CA: exec_statement (ceval.c:4177)
==19975==    by 0x48EE67: PyEval_EvalFrameEx (ceval.c:1666)
==19975==    by 0x492E64: PyEval_EvalCodeEx (ceval.c:2836)
==19975==    by 0x494E7C: fast_function (ceval.c:3669)
```



---

Comment by rlm created at 2008-07-08 19:07:50

In state 6 and state 16, the two lines

```
if hb > nu.k: # update hb since we are backtracking (not in [1])
    hb = nu.k # recall hb is the longest common ancestor of rho and nu
```

need to be wrapped with an `if lab:` clause. Will post a patch once my build finishes.


---

Comment by rlm created at 2008-07-08 19:07:50

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-07-08 21:01:16

Nice job rlm, this nails the issue and valgrind now gives graph_isom.py a clean bill of health.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-09 07:35:38

For the record: This is before the patch on Itanium SLES 10:

```
sage -t  devel/sage/sage/graphs/graph_isom.pyx              **********************************************************************
File "/home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/graph_isom.py", line 1383:
    sage: Y0.is_isomorphic(Y1)
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/graph_isom.py", line 1385:
    sage: Y0.is_isomorphic(HS)
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
```

But with the patch applied it still fails:

```
mabshoff`@`iras:~/sage-3.0.4.alpha2-SLES10-4.3.1> ./sage -t -long devel/sage-main/sage/graphs/graph_isom.pyx
sage -t -long devel/sage-main/sage/graphs/graph_isom.pyx    **********************************************************************
File "/home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/graph_isom.py", line 1383:
    sage: Y0.is_isomorphic(Y1)
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/graph_isom.py", line 1385:
    sage: Y0.is_isomorphic(HS)
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   2 of 124 in __main__.example_24
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/.doctest_graph_isom.py
         [89.4 s]
exit code: 1024
```

So this is likely a gcc bug or something that exposes the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-09 07:36:10

The patch itself fixes a problem and should be applied obviously. I meant to mention that on the ticket.

Cheers,

Michael


---

Comment by was created at 2008-07-09 16:06:16

Resolution: fixed


---

Comment by mabshoff created at 2008-07-09 16:16:24

Merged in Sage 3.0.4.rc2
