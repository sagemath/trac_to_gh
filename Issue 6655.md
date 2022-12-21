# Issue 6655: Clean up and new feature in partition

Issue created by migration from Trac.

Original creator: numata

Original creation time: 2009-07-29 14:25:13

Assignee: mhansen

CC:  sage-combinat

Keywords: Parition

I add a following new feature in partition:
a method returns a list of boxes in the arm.
and so more.


---

Attachment


---

Comment by numata created at 2009-07-29 15:57:19

Changing assignee from mhansen to numata.


---

Comment by numata created at 2009-07-29 15:57:19

Changing status from new to assigned.


---

Comment by hivert created at 2010-04-22 19:03:40

Changing keywords from "Parition" to "Partition cells arm legs".


---

Comment by hivert created at 2010-04-22 19:03:40

Changing assignee from numata to hivert.


---

Comment by hivert created at 2010-04-22 19:56:09

Should be ready for review ! Apply only [trac_6655_partition_corner_cells-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6655/trac_6655_partition_corner_cells-fh.patch)


---

Comment by hivert created at 2010-04-22 19:56:09

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-04-27 17:05:01

I slightly improved the doc and re-uploaded the patch...


---

Comment by hivert created at 2010-05-01 13:50:09

I just discovered some failing docttests. Everything should now be ok. Please review


---

Comment by aschilling created at 2010-05-01 16:46:30

Hi Florent,

Thank you for this patch. Here are a couple of comments:

* Please use consistently "in English convention" instead of "in english notations",
see line 840, 963, 924.

* Would it be possible to lift the methods arm_length, leg_length, hook_length, arm_cells, etc also to SkewPartitions? I recently needed those and it would be convenient to have them directly in Sage.

Cheers,

Anne


---

Attachment


---

Comment by hivert created at 2010-05-04 23:22:39

> * Please use consistently "in English convention" instead of "in english notations",
> see line 840, 963, 924.

Fixed...

> * Would it be possible to lift the methods arm_length, leg_length, hook_length, arm_cells, etc also to SkewPartitions? I recently needed those and it would be convenient to have them directly in Sage.

Except for `cells` which I just added, they are all accessible through `l.outer().arm_length`... So I'm not sure we wan't to link all of those.


---

Attachment

I reviewed the patch. It cleans up several features in partitions. In addition it fixes the slide method in skew_tableaux and adds the cell method to skew_partitions as requested. All tests pass. Positive review!

Release manager, please apply only
trac_6655_partition_corner_cells-fh.patch and 
trac_6655_partition_corner_cells-review-as.patch (in this order).


---

Comment by aschilling created at 2010-05-05 23:34:17

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-08 21:39:34

Merged in this order:

 1. [trac_6655_partition_corner_cells-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6655/trac_6655_partition_corner_cells-fh.patch)
 1. [trac_6655_partition_corner_cells-review-as.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6655/trac_6655_partition_corner_cells-review-as.patch)


---

Comment by mvngu created at 2010-05-08 21:39:34

Resolution: fixed
