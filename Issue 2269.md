# Issue 2269: Many classes abuse has_coerce_map

Issue created by migration from https://trac.sagemath.org/ticket/2269

Original creator: gfurnish

Original creation time: 2008-02-22 22:30:31

Assignee: robertwb

Many classes pass has_coerce_map_from a self value that is not a Parent (when has_coerce_map_from is a member function of Parent), or pass it a value of self that does not have _has_coerce_map_from initialized (this is used for caching).  The initialization problem is almost certainly related to classes not correctly initializing Parent (as described in the TODO in init).  However the values of self that are not Parents are more mysterious.  The doctest failures caused by this can be easily recreated by adding a "return false" to the if statement described in enhancement 2268. 


---

Comment by robertwb created at 2008-10-30 08:31:34

I believe this can be marked as invalid given the new coercion model.


---

Comment by mabshoff created at 2008-10-30 08:37:04

Resolution: invalid


---

Comment by mabshoff created at 2008-10-30 08:37:04

Replying to [comment:2 robertwb]:
> I believe this can be marked as invalid given the new coercion model. 

RobertWB's wish is my command. Invalid.

Cheers,

Michael
