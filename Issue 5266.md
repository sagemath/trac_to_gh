# Issue 5266: plot_vector_field does not plot the end of the range when given plot_points argument

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-02-14 10:22:25

Assignee: was


```
var('x,y')
plot_vector_field( (-1,y), (x, -1, 1), (y, -1, 1), plot_points=4)
```


picks the 4 points at x=-1, -0.5,0, and 0.5, but doesn't get x=1!  The points it should pick are x=-1, -1/3, 1/3, and 1 (so we hit the end of the x-range).  The same applies to y.



---

Comment by jason created at 2009-02-14 11:00:09

Changing assignee from was to jason.


---

Attachment


---

Comment by jason created at 2009-02-14 11:00:09

Changing status from new to assigned.


---

Comment by jason created at 2009-02-14 11:00:29

Changing priority from major to blocker.


---

Comment by jason created at 2009-02-14 11:00:29

mabshoff said to make this a blocker...


---

Comment by mabshoff created at 2009-02-14 13:46:48

All doctests pass with the patch applied, so now we need a formal review for this one.

Cheers,

Michael


---

Comment by mhansen created at 2009-02-14 14:13:20

Looks good to me.


---

Comment by mabshoff created at 2009-02-14 16:09:22

Resolution: fixed


---

Comment by mabshoff created at 2009-02-14 16:09:22

Merged in Sage 3.3.rc1.

Cheers,

Michael
