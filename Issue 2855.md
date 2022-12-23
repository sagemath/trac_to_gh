# Issue 2855: A correction to the weight of crystal elements for type A and a speedup for all types

Issue created by migration from https://trac.sagemath.org/ticket/2855

Original creator: bump

Original creation time: 2008-04-08 06:03:01

Assignee: mhansen

CC:  sage-combinat

For Cartan Types 'A' a problem with the weight function of crystals was described here:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/7cdfe075257ba963?hl=en

The method of correcting this problem was to hard-code the weight in the crystals of letters, 
and to have the crystals of tensors get the weight of a tensor element by summing the weights 
of its constituents. This alters the weight for Type A (correcting the defect) and returns the
same weight as the old algorithm for other Cartan types.

When the patch was implemented it was found to be 2-3 times faster than the old algorithm.


---

Comment by bump created at 2008-04-08 06:07:15

Resolution: duplicate
