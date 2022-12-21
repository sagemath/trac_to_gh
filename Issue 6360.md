# Issue 6360: [with spkg, needs review] Change -O2 to -O0 in singular spkg

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2009-06-19 04:37:01

Assignee: mabshoff

CC:  malb wstein

Currently, singular seems to segfault on some architecture/OS combinations, such as SuSE and ia64. (See #6240 for more details.) The spkg available at `/scratch/craigcitro/patches/singular-3-1-0-2-20090618.spkg` on `sage.math` changes `-O2` to `-O0` to fix this problem until we can get to the root of it (i.e. until we fix #6240). 


---

Comment by craigcitro created at 2009-06-19 06:51:35

Resolution: fixed


---

Comment by craigcitro created at 2009-06-19 06:51:35

Merged in final 4.0.2.


---

Comment by malb created at 2009-06-19 10:26:06

Sorry for jumping in so late. I guess what the ticket is supposed to do is to switch to `-O0` on Itanium *only*, right?


---

Comment by ncalexan created at 2009-06-19 16:06:52

Replying to [comment:4 malb]:
> Sorry for jumping in so late. I guess what the ticket is supposed to do is to switch to `-O0` on Itanium *only*, right?

Correct.
