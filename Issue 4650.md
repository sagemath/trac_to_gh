# Issue 4650: matrix_modn_sparse needs cleanup

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2008-11-29 02:35:02

Assignee: boothby

Keywords: sparse

matrix_modn_sparse needs some housecleaning.  One gem, in particular:


```
    cdef Py_ssize_t i, j, k
    k = 0
    for i from 0 <= i < self._nrows:
        for j from 0 <= j < self.rows[i].num_nonzero:
            k+=1
    return QQ(k)/QQ(self.nrows()*self.ncols()) 
```


also, it could use some fast nonzero_positions, getitem, etc. methods


---

Comment by craigcitro created at 2009-01-15 23:08:14

Changing assignee from boothby to craigcitro.


---

Attachment

I agree, this file needs a lot of cleanup.

I fixed the one example Tom mentioned above ... lots more needs to be done, but I thought it would be good to close this and open a new series of specific tickets (most of which will probably get handled at SD12 in San Diego).


---

Comment by craigcitro created at 2009-01-15 23:08:14

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-18 04:50:29

Positive review. I change the summary to properly reflect what you fixed.

As you pointed out followup should happen via individual tickets.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-18 04:50:41

Merged in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-18 04:50:41

Resolution: fixed
