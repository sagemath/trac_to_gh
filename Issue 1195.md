# Issue 1195: The "len" function for lists and sequences

Issue created by migration from https://trac.sagemath.org/ticket/1195

Original creator: ljpk

Original creation time: 2007-11-17 23:01:18

Assignee: cwitty

Currently, the method to obtain the length of a list or sequence is:

{{my_list=Sequence([1,2,3,4])
len(my_list)}}

This is not consistent with either MAGMA or PARI, and there is no method attached to the sequence or list which gives the length.

I would like to suggest that a method be added so that

{{my_list.length()}}

would give the answer ``4''.


---

Comment by mhansen created at 2007-11-18 05:53:43

On the other hand, len() is the standard Python way of doing things.


---

Comment by ncalexan created at 2007-11-24 21:25:51

This is not quite true -- there is a `.__len__()` function that `len()` calls.

Perhaps this should be at the level of `SageObject`: `.length()` calls `.__len__()?`  This is irritating but not idiomatic python, so I vote to keep it as is.


---

Comment by malb created at 2008-02-27 00:05:31

I vote against the proposal in this ticket, `len(Foo)` is the Python way.


---

Comment by was created at 2008-02-27 12:19:20

Resolution: wontfix


---

Comment by was created at 2008-02-27 12:19:20

> Perhaps this should be at the level of SageObject: .length() calls .__len__()? 
> This is irritating but not idiomatic python, so I vote to keep it as is.

I think this would be annoying.  It also adds to the clutter when one does X.[tab]
on a sage object X.  And everybody learns about len(...) in Python pretty soon.
