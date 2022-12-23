# Issue 9778: Grotzsch graph and Mycielski graphs

Issue created by migration from https://trac.sagemath.org/ticket/9779

Original creator: edward.scheinerman

Original creation time: 2010-08-22 00:48:00

Assignee: jason, ncohen, rlm

Added methods to create the Grotzsch graph and the Mycielski graphs. The Mycielski graphs are a sequence of triangle-free graphs with arbitrarily high chromatic number. The Grotzsch graph is (isomorphic to) the fourth graph in this series; it it triangle-free and has chromatic number equal to 4.


---

Comment by ncohen created at 2010-09-03 20:18:47

Changing status from new to needs_review.


---

Attachment

Hello !!!

Nice patch ! Nothing to complain about, and they bring nice additions to Sage `:-)`

I uploaded a (very short) patch with very small modifications. As usual, I give a positive review to your patch, and you can change the status of this ticket if you like mine `:-)`

(btw, don't forget to set your tickets as "needing review" when you have uploaded your patch !)

Nathann


---

Comment by edward.scheinerman created at 2010-09-03 20:34:55

Nathann: The edits you made are fine. Thanks. I set this to "positive review". What's next? -Ed


---

Comment by edward.scheinerman created at 2010-09-03 20:34:55

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-09-03 21:05:44

> Nathann: The edits you made are fine. Thanks. I set this to "positive review". What's next? -Ed
Peacefully waiting for the release managers to find it ? `:-)`

Nathann


---

Comment by mpatel created at 2010-09-05 03:47:41

Could someone prepend the ticket number to the commit string for [attachment:trac_9779.patch] (and restore the status to "positive review")?


---

Comment by mpatel created at 2010-09-05 03:47:41

Changing status from positive_review to needs_work.


---

Attachment


---

Attachment


---

Comment by edward.scheinerman created at 2010-09-06 00:39:17

Changing status from needs_work to positive_review.


---

Comment by edward.scheinerman created at 2010-09-06 00:39:17

Patch commit string edited as requested. (Please ignore trac_9779.2.patch ... it's identical to trac_9779.patch.)


---

Comment by mpatel created at 2010-09-18 07:42:26

Could someone rebase the patch(es) here against 4.6.alpha1 when it's released (soon) and restore the positive review?


---

Comment by mpatel created at 2010-09-18 07:42:26

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by edward.scheinerman created at 2010-09-20 18:45:42

Changing status from needs_work to positive_review.


---

Comment by edward.scheinerman created at 2010-09-20 18:45:42

I rebased the patch (I hope I did this correctly!).  -Ed


---

Attachment

Rebased for a working 4.6.alpha2.  Apply only this patch.


---

Comment by mpatel created at 2010-09-29 09:33:33

I've attached a patch rebased against a working 4.6.alpha2.  This fixes a reject in `sage/graphs/graph_generators.py.rej`:

```diff
--- graph_generators.py
+++ graph_generators.py
@@ -196,6 +199,8 @@
 - Harald Schilly and Yann Laigle-Chapuy (2010-03-24): added Fibonacci Tree
 
 - Jason Grout (2010-06-04): cospectral_graphs
+
+- Ed Scheinerman (2010-08-21): added Grotzsch graph and Mycielski graphs 
 """
 
 ###########################################################################
```



---

Comment by mpatel created at 2010-09-29 10:48:17

Resolution: fixed


---

Comment by ncohen created at 2010-09-29 11:54:52

Thank you !

Nathann
