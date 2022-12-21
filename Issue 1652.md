# Issue 1652: length of DAGs with loops calculation runs infinite

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2008-01-01 19:23:44

Assignee: rlm

G4 has a loop: 2->4 and 4->2



```
G4 = DiGraph({1:[2,2,3,5], 2:[3,4], 3:[4], 4:[2,5,7], 5:[6]}, multiedges=True)
G4_path.count()

RuntimeError: maximum recursion depth exceeded
```



There are related issues calulating _incoming_paths_ and possibly more in _sage.combinat.graph_path_!


---

Comment by schilly created at 2008-01-01 19:25:55

ah, solution is very simple: just check if *G4.is_directed_acyclic()* is true ;)


---

Comment by rlm created at 2008-01-01 23:17:23

Could you be more specific? I have no idea what G4_path is. Also, could you post a full traceback?


---

Comment by mhansen created at 2008-01-19 19:29:19

Changing status from new to assigned.


---

Comment by mhansen created at 2008-01-19 19:29:19

Changing assignee from rlm to mhansen.


---

Attachment


---

Comment by ncalexan created at 2008-01-20 03:40:25

Code looks good, docstrings and tests seem appropriate.


---

Comment by mabshoff created at 2008-01-21 05:50:01

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 05:50:01

Resolution: fixed
