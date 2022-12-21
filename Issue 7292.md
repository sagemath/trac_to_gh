# Issue 7292: Max Vertex/Edge disjoint st-paths

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-10-25 09:23:47

Assignee: rlm

With the functions from #6680, functions returning a maximal number of Vertex/Edge disjoint st-path should be defined. The will obviously use the flow functions, but in many applications the user is just interested in these paths, and so there should be an easy way to find them in Sage.


---

Comment by ncohen created at 2009-12-15 14:45:10

Changing status from new to needs_review.


---

Comment by rlm created at 2009-12-15 18:00:37

`vertex_disjoint_paths` loops forever...


---

Comment by rlm created at 2009-12-15 18:00:37

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2009-12-16 00:49:35

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-12-16 00:49:35

not anymore :-)


---

Comment by rlm created at 2009-12-16 02:56:13

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by mhansen created at 2009-12-19 23:57:44

Changing status from positive_review to needs_work.


---

Comment by mhansen created at 2009-12-19 23:57:44

I get the following failure:


```
**********************************************************************
File "/scratch/mhansen/release/4.3/rc1/sage-4.3.rc1/devel/sage-main/sage/graphs/graph.py", line 3581:
    sage: g.vertex_cover(value_only=True)
Expected:
    9
Got nothing
**********************************************************************
```



---

Comment by ncohen created at 2009-12-20 16:45:37

This is because of an odd thing : when this patch is applied over #7600, the body of vertex_cover totally disappears : only the docstring remains, and the function returns nothing. I will send an updated version of the patch "after" #7600 has been applied :-)


---

Comment by ncohen created at 2009-12-20 16:54:39

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-12-20 16:54:39

Here it is !!

Please check, when appying it, that nothing disappears "above" and "after" the added sections ! If this version is not easier to apply, I think the best way would be to create a patch based upon the version you are working on and the patch you already applied (this should not be long though, this patch just adds two consecutive functions)

Sorry for the trouble ! :-)

Nathann


---

Comment by rlm created at 2010-01-06 16:22:24

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-01-10 08:02:31

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-01-10 08:02:31

Rebased !

Nathann


---

Comment by rlm created at 2010-01-13 11:39:11

Resolution: fixed


---

Attachment

positive review
