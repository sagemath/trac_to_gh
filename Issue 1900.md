# Issue 1900: [with patch, needs review] Clean up adjacency matrix functions for graphs

Issue created by migration from https://trac.sagemath.org/ticket/1900

Original creator: rlm

Original creation time: 2008-01-24 00:25:27

Assignee: rlm

There were several options available to graphs but not digraphs, so I factored the code out to generic graphs, and made sure all functionality was available there.


---

Attachment


---

Comment by jason created at 2008-01-24 05:46:54

I further cleaned up the code a bit and hopefully made it a tad faster as well in graph_am-updated.patch, which should be applied instead of graph_am.patch.

Also, pending the outcome of the discussion on sage-devel, graph_am-over_integers.patch should be applied after graph_am-updated.patch in order to delete the over_integers parameter.

Reviews of my modifications would be appreciated.


---

Comment by jason created at 2008-01-24 06:14:01

Updated patch fixes doctests and calls to adjacency_matrix


---

Comment by jason created at 2008-01-24 06:22:49

Changing priority from minor to major.


---

Attachment


---

Comment by jason created at 2008-01-24 06:24:27

Priority changed since the default of returning an adjacency matrix over GF(2) made the characteristic polynomial function completely *wrong*.


---

Comment by jason created at 2008-01-24 18:58:10

Robert, where did your original patch go?  I don't want to take all the credit---you did the initial work here.  I'm not sure how to change the patch to include both of us as authors...


---

Comment by rlm created at 2008-01-24 20:18:19

I deleted it to avoid merge conflict. Don't worry about it.


---

Comment by mabshoff created at 2008-01-24 21:17:39

Resolution: fixed


---

Comment by mabshoff created at 2008-01-24 21:17:39

Both patches merged in Sage 2.10.1.alpha2
