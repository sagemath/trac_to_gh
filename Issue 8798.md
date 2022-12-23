# Issue 8798: Duplicate version of feedback_arc_set and feedback_vertex_set

Issue created by migration from https://trac.sagemath.org/ticket/8798

Original creator: ncohen

Original creation time: 2010-04-28 08:08:21

Assignee: jason, ncohen, rlm

CC:  mvngu

Here is the problem :


```
~/sage/sage-doc/sage/graphs$ grep -e "def.*eedback" *
digraph.py:    def feedback_edge_set(self,value_only=False):
digraph.py:    def feedback_vertex_set(self,value_only=False):
generic_graph.py:    def feedback_edge_set(self,value_only=False):
generic_graph.py:    def feedback_vertex_set(self,value_only=False):
~/sage/sage-doc/sage/graphs$ 
```



---

Attachment


---

Comment by ncohen created at 2010-04-28 08:13:33

And here is the patch ! This code would not work for undirected graphs anyway :-)

Nathann


---

Comment by ncohen created at 2010-04-28 08:13:33

Changing status from new to needs_review.


---

Attachment

The patch [trac_8798.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8798/trac_8798.patch) is OK by me. However, it would likely conflict with #8786. So [trac_8798-rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8798/trac_8798-rebased.patch) is a rebase of [trac_8798.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8798/trac_8798.patch) on top of #8786. Someone other than myself needs to check the rebased patch. If it's OK, then the whole ticket is good to go.


---

Comment by ncohen created at 2010-04-29 16:56:17

Checked ! Thank you for your help ! :-)

Nathann


---

Comment by ncohen created at 2010-04-29 16:56:17

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-08 21:58:54

Resolution: fixed


---

Comment by mvngu created at 2010-05-08 21:58:54

Merged [trac_8798-rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8798/trac_8798-rebased.patch).
