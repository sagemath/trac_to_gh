# Issue 5458: Refactor set partitions with a single entry points in global name space for the various cartan types

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-03-08 21:03:46

Assignee: mhansen

CC:  sage-combinat

Refactor the set partitions code to have a single entry point in the global name space for the various types. I.e. from the user point of view, replace the various:

> > SetPartitions     SetPartitionsIk   SetPartitionsRk
> > SetPartitionsAk   SetPartitionsPRk  SetPartitionsSk
> > SetPartitionsBk   SetPartitionsPk   SetPartitionsTk

By something like:
 	SetPartitions(..., type=["A",3])

See also: http://groups.google.com/group/sage-devel/msg/a49f3288fca1b75c


---

Comment by mhansen created at 2013-07-23 14:30:55

Resolution: duplicate


---

Comment by mhansen created at 2013-07-23 14:30:55

I think we can close this as a duplicate of #14234 which actually has some work being done on it.


---

Comment by tscrim created at 2013-07-26 08:35:01

This is not a duplicate of #14234 since that does not remove these from the global namespace, deprecate them, nor correctly pass along the correct object. There is still work to be done here, so please reopen this ticket.
