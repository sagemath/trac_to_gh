# Issue 3268: Fix GAP interface

Issue created by migration from https://trac.sagemath.org/ticket/3268

Original creator: rlm

Original creation time: 2008-05-21 16:43:12

Assignee: was

I might be wrong, but it looks like output isn't getting printed:


```
# From a pure GAP session:
GAP4, Version: 4.4.10 of 02-Oct-2007, i686-apple-darwin9.2.2-gcc
gap> g := Group((1,3,2),(2,4,3));
Group([ (1,3,2), (2,4,3) ])
gap> Stabilizer(g,4);
Group([ (1,3,2) ])
gap> 

# From a Sage session:
sage: %gap

  --> Switching to Gap <-- 

''
gap: g := Group((1,3,2),(2,4,3));

gap: Stabilizer(g,4);

gap: 
```



---

Comment by rlm created at 2008-05-25 06:25:24

This isn't just for Stabilizer(), since the group isn't printing either...


---

Attachment


---

Comment by mhansen created at 2009-01-23 09:31:05

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2009-01-23 09:31:05

Note that there is no good way to test this as you can't access the processed line as it's completely internal to the function.


---

Comment by mhansen created at 2009-01-23 09:31:05

Changing status from new to assigned.


---

Comment by robertwb created at 2009-01-23 22:11:49

Nice catch.


---

Comment by mabshoff created at 2009-01-24 23:00:41

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 23:00:41

Merged in Sage 3.3.alpha2.

Cheers,

Michael
