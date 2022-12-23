# Issue 9509: graphs() should give you graphs

Issue created by migration from https://trac.sagemath.org/ticket/9509

Original creator: rlm

Original creation time: 2010-07-15 14:43:30

Assignee: jason, ncohen, rlm

CC:  boothby vdelecroix




---

Attachment


---

Comment by rlm created at 2010-07-15 14:46:43

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2010-07-15 17:32:40

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2010-07-15 17:32:40

Great, great, great!

Thank you for this very nice mini patch...


---

Comment by mpatel created at 2010-07-21 02:36:53

I'm about to attach V2, which is rebased for this queue:

```
[...other, non-graph theory patches to be merged into 4.5.2.alpha0...]
trac_9111.patch
trac_9111-doc-edits.patch
trac_9111-doc_addition.patch
trac_9373.patch
trac_9375-graph-doctests.patch
trac_9485-strongly_connected_componnents_digraph-fix-nt.patch
trac_8953.patch
trac_9532-graphs-randstate.patch
trac-9141-cospectral_graphs.2.patch
trac_9141-smallfixes.patch
trac_9509-graph_gen.2.patch
```

Please check and let me know if there are problems.


---

Attachment

Rebased for queue in comment 3.  Apply only this patch.


---

Comment by mpatel created at 2010-07-21 02:39:21

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-07-21 02:39:28

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-07-21 08:21:10

Looks good to me!


---

Comment by rlm created at 2010-07-21 08:21:10

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 10:27:28

Resolution: fixed
