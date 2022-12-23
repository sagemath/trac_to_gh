# Issue 2139: set partitions iterator not working

Issue created by migration from https://trac.sagemath.org/ticket/2139

Original creator: mhansen

Original creation time: 2008-02-11 06:39:11

Assignee: mhansen

CC:  sage-combinat

Hello,

I'm doing some work with complete matchings, and I'm dealing with them
as set partitions. I just need to iterate over matchings, not make
lists, so it seems like I shouldn't run out of memory (I have 1.5 gigs
installed), but I am. I'm using Sage 2.10.1 on Linux.

If I do something like the following, memory usage climbs and climbs:

 n = 0
 for m in SetPartitions(range(16), [2, 2, 2, 2, 2, 2, 2, 2]):
   n += 1

This seems weird, since there's a set partitions iterator, and it
shouldn't take a lot of memory.

On the other hand, here's an iterator for complete matchings that I
wrote that works just fine:

 def matchings(n):
   for m in matchingsset(range(1, n+1)): yield m

 def matchingsset(L):
   if len(L) == 0:
     yield []
   else:
     for k in range(1,len(L)):
       for m in matchingsset(L[1:k] + L[k+1:]):
         yield m + [[L[0], L[k]]]
   return

Now running the same counting loop works, with no extra memory usage:

 n = 0
 for m in matchings(16):
   n += 1

Sage seems to have an iterator for set partitions; it is working? Do I
need to use something else to get a memory-efficient iterator?

Thanks for the help,

Dan


---

Attachment


---

Comment by mhansen created at 2008-02-11 06:57:35

Changing status from new to assigned.


---

Comment by ncalexan created at 2008-02-15 03:45:09

Again, I say apply.  Again, there are no doctests!


---

Comment by mhansen created at 2008-02-15 03:47:51

I don't know the best way to doctest memory usage, but this is a "reimplementation" of something that already has doctests.  So, it's already being doctested for correctness, just not memory consumption.


---

Comment by mabshoff created at 2008-02-15 04:57:19

Resolution: fixed


---

Comment by mabshoff created at 2008-02-15 04:57:19

Merged in Sage 2.10.2.alpha0
