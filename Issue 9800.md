# Issue 9800: Linear programming construction doc fixes

Issue created by migration from Trac.

Original creator: rhinton

Original creation time: 2010-08-25 13:48:21

Assignee: ncohen

Keywords: linear programming, constructions, doc

The linear programming page in the Sage Constructions document has a few errors. 

1.  In the vertex cover example, the objective should be to minimize, not maximize the sum.  Also, the example code is missing the objective function.

2.  The maximal matching example code is also missing the objective function.

3.  I couldn't run the examples even after having installed glpk according to the instructions.  Sage complained that no solver was installed.



---

Attachment


---

Comment by rhinton created at 2010-08-25 14:03:49

Changing status from new to needs_work.


---

Comment by rhinton created at 2010-08-25 14:03:49

Attached patch apparently fixes problem (1).  

It attempts to fix problem (2), but I get an exception

```
MIPSolverException: 'GLPK : Solution is undefined'
```


Regarding (3), glpk apparently installed just fine on another machine, so I will bring up the problem on sage-devel to get help on the failed install.


---

Comment by rhinton created at 2010-08-27 16:37:52

Resolution: wontfix


---

Comment by rhinton created at 2010-08-27 16:37:52

Nathann Cohen promised a rewrite of this documentation soon.  See 

http://groups.google.com/group/sage-devel/browse_thread/thread/330baaf798e51a01

for details.
