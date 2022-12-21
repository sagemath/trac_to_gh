# Issue 1309: [graphs] generate trees

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-11-28 19:58:44

Assignee: rlm

Keywords: graphs

From Chris Godsil's wishlist (with final reply by Robert Miller):


```
> 
>>> A database of trees, or a generator for trees. I think it would be
>>> reasonably
>>> straightforward to generate rooted trees, and hence get trees. The
>>> generators
>>> would be more useful than the database. It is not impossible that
>>> something
>>> in the nauty package generates trees.
> If you look into the code that graphs(7) calls, you will notice that
> you can pass it any vertex-hereditary property, including being a
> tree. So in some sense, this is already implemented. However, this
> could be its own constructor, and more importantly, I know of a way to
> optimize the generation of trees to go much faster than it would with
> what I described above. Create a ticket, and assign it to me.
> 
```




---

Comment by rlm created at 2007-12-02 04:52:18

Changing status from new to assigned.


---

Comment by rlm created at 2007-12-02 21:59:04

There are still significant bugs from the patch from

http://trac.sagemath.org/sage_trac/ticket/1361

that I am working on now. I discovered them while implementing this ticket, so the fixes will be in the patch for this.


---

Attachment


---

Comment by mabshoff created at 2007-12-03 02:07:11

Merged in 2.8.15.rc0.


---

Comment by mabshoff created at 2007-12-03 02:07:11

Resolution: fixed
