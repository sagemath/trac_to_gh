# Issue 6349: graphs -- bug in DiGraph constructor

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-17 22:27:52

Assignee: rlm


```
sage: DiGraph(matrix(2,[0,0,-1,1]), format="incidence_matrix")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/wstein/.sage/sage_notebook/worksheets/admin/187/code/29.py", line 7, in <module>
    DiGraph(matrix(_sage_const_2 ,[_sage_const_0 ,_sage_const_0 ,-_sage_const_1 ,_sage_const_1 ]), format="incidence_matrix")
  File "/Users/wstein/s/local/lib/python2.5/site-packages/Jinja-1.2-py2.5-macosx-10.3-i386.egg/", line 1, in <module>
    
  File "/Users/wstein/s/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 9894, in __init__
    raise ValueError(msg + msg2)
TypeError: cannot concatenate 'str' and 'exceptions.AssertionError' objects
```




---

Attachment


---

Comment by rlm created at 2009-06-17 22:53:57

Changing status from new to assigned.


---

Comment by rlm created at 2009-06-24 10:11:53

Resolution: fixed
