# Issue 1057: Order elements do not have Z as a (proper) basering

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-11-01 21:14:29

Assignee: was


```
sage: sage: K.<a> = NumberField(x^2 - 5)
sage: sage: B = K.maximal_order().basis();
sage: B[1].parent().base_ring() # this is bad
Rational Field
sage: B[1].parent().base()
Integer Ring
```


Also, _rmul_, etc needs to be re-implemented. 


---

Comment by robertwb created at 2007-11-01 21:14:35

Changing assignee from was to robertwb.


---

Attachment

Orders now have correct baserings. 

Whoever implemented the _base attribute might want to look at how it overrides the (cdef) ParentBase._base attribute, and the implications that might have. 

This patch makes patch #1044 obsolete.


---

Comment by mabshoff created at 2007-11-02 19:58:18

Changing assignee from robertwb to mabshoff.


---

Comment by mabshoff created at 2007-11-02 19:58:18

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-02 19:58:18

applied to 2.8.11.rc2 after reverting #1044.


---

Comment by was created at 2007-11-03 14:55:35

This is already fixed and in sage-2.8.11.


---

Comment by was created at 2007-11-03 14:55:59

Resolution: fixed
