# Issue 5790: Updating some quirks in partition.py

Issue created by migration from Trac.

Original creator: andrew.mathas

Original creation time: 2009-04-15 06:41:27

Assignee: andrew.mathas

CC:  sage-combinat jbandlow saliola

Keywords: partitions, cores, quotients

Dear All,

I have just pushed a patch to the combinat server which:
    * deprecates _r_core_, _r_quotient_ (and _k_core_) in favour of _core_ and _quotient_, respectively. I also made _core_ return a partition rather than a list.
    * rewrite the Partition() calling function to use keywords rather than named arguments. In the process I deprecated the 'core_and_quotient' argument.
    * deprecated _partition_sign_ in favour of _sign_ and replaced the previous call to gap with plus or minus one as required.

Almost all of the changes are to partition.py, however, the  patch affects the following four files as they all called _r_core_ or _r_quotient_::
    sage/combinat/ktableau.py
    sage/combinat/partition.py
    sage/combinat/ribbon_tableau.py
    sage/combinat/skew_partition.py

Not all of the doc tests pass, however, the problems seem to be caused elsewhere.

Andrew


---

Comment by andrew.mathas created at 2009-04-15 06:47:10

Changing component from algebra to combinatorics.


---

Comment by andrew.mathas created at 2009-04-15 06:47:46

Changing type from defect to task.


---

Comment by saliola created at 2009-04-15 15:39:16

The patch looks good. A couple of small comments.

 * The documentation for core still uses the terminology "r-core". Perhaps you can replace this with 'core' and add a note along the lines: 'sometimes called r-core and k-core in the literature'.

 * Same comment applies to the documentation for "r-quotient".


---

Comment by andrew.mathas created at 2009-04-15 23:11:22

I've fixed the documentation problems...and also deprecated partition_associated, from_core_and_quotient and from_exp moving them all into Partition_class. All doc tests now pass.


---

Attachment


---

Attachment


---

Attachment

I noticed that from_core_and_quotient returned a list rather than a partition, so changed this as well...


---

Attachment

I've rebased this to apply to 4.0.1; all doctests pass.  I give a positive review to all of Andrew's changes, but I've left the status as 'needs review' so someone has a chance approve my changes.  Let's get this in quickly before we need to rebase again!  :)


---

Comment by ddrake created at 2009-06-16 01:49:06

I'm changing this from "task" to "enhancement" to make sure it shows up in the right queries and searches. Tasks somehow seem to get lost too easily.


---

Comment by ddrake created at 2009-06-16 01:49:06

Changing type from task to enhancement.


---

Attachment

Apply only 5790.2.patch and this patch (in this order)


---

Comment by saliola created at 2009-06-21 19:43:36

Andrew's changes made `from_exp` and `from_core_and_quotient`
methods of a partition, but they shouldn't be since they don't depend on
the partition at all. It's strange, to me, to have the constructor work
this way:


```
sage: p = Partition([])
sage: p.from_exp([3,2,1])
[3, 2, 2, 1, 1, 1]

sage: q = Partition([3,2,2,1,1,1])
sage: q.from_exp([3,2,1])
[3, 2, 2, 1, 1, 1]
```


I've reverted those changes in my review patch, otherwise it looks good. 

To be clear: I do not object to gathering all the code for constructing
partitions into one class. Perhaps a new `PartitionConstructor` class
would be better? Either way, this is not the point of this ticket.

Someone needs to look over my changes, of course.

Apply only 5790.2.patch and trac_5790-review.patch.


---

Comment by nthiery created at 2009-07-17 17:53:01

I am looking at it. Should be done tonight.


---

Comment by nthiery created at 2009-07-17 21:29:06

I rechecked the patches, merged them all together, did a couple minor doc fixes, renamed key_word into keyowrd, and merged in my patch on sage-combinat adding a doctest to the deprecation things for r_core and r_quotient (and fixed them, since they actually were broken) + updating of the llt code. The patch applies cleanly on 4.1. All tests pass. I consider it as good to go.

For the record. I am also about to attach a diff of my changes, should someone want to double checks.


---

Comment by nthiery created at 2009-07-17 21:29:52

Apply only this one


---

Attachment

For the record. Don't apply.


---

Attachment

I give a positive review to Nicolas's changes.


---

Comment by mvngu created at 2009-07-18 15:44:46

Resolution: fixed


---

Comment by mvngu created at 2009-07-18 15:44:46

Merged `trac_5790-partition.patch`.
