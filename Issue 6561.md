# Issue 6561: Trivial bug with cartesian product of an empty list of iterators

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-07-19 18:11:06

Assignee: cwitty

CC:  was

The function cartesian_product_iterator (which takes a list of iterators as input) gets the wrong answer when given an empty list. It returns an empty list; but the cartesian product of an empty list of iterators should be *the list containing the empty tuple*. 

The current behaviour means as a consequence that listing the elements of the zero finitely-presented module returns an empty list, rather than [0] which is clearly the right answer.




---

Attachment


---

Comment by davidloeffler created at 2009-07-20 11:50:43

Here's a patch. This fixes the bug, and removes some special-case code in combinat/words and abelian_groups that was there to work around the previous wrong behaviour.

William: I think I mentioned this to you in Barcelona -- any chance you could review it, or suggest someone else who could?


---

Comment by AlexGhitza created at 2009-08-19 07:55:16

David, I am getting errors when I try to apply your patch to sage-4.1.1.  Can you try to rebase it?


---

Comment by davidloeffler created at 2009-08-19 10:21:39

rebased to 4.1.1


---

Attachment

Here is a new rebased patch; I have checked it passes doctests in 4.1.1.


---

Comment by AlexGhitza created at 2009-08-19 11:00:52

Looks good.


---

Comment by mvngu created at 2009-08-24 05:51:20

Resolution: fixed


---

Comment by mvngu created at 2009-08-24 05:51:57

Merged `trac_6561-empty_cartesian_product-rebased.patch`.
