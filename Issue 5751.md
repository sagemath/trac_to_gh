# Issue 5751: cartan_type now a method rather than attribute in weyl_characters.py

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2009-04-11 15:47:37

Assignee: tbd

CC:  sage-combinat

In connection with #5729 this makes cartan_type a method rather than attribute in weyl_characters.py.

See cartan_type now a method rather than attribute in weyl_characters.py

But this patch has a minor conflict with #5721 which is the more important of the two
patches. So let us get #5721 merged first.


---

Comment by bump created at 2009-04-15 15:32:32

patch revised to apply after the 5721 patches


---

Comment by mabshoff created at 2009-04-15 19:25:43

Changing assignee from tbd to mhansen.


---

Comment by mabshoff created at 2009-04-15 19:25:43

Changing component from algebra to combinatorics.


---

Comment by aschilling created at 2009-04-17 07:28:05

line 316 in sage/combinat/crystal/crystals.py needs to be updated so that
the tests in this file will pass.

Anne


---

Comment by aschilling created at 2009-04-17 07:36:37

Except for my previous comment on the tests in crystals.py I give this patch a positive review.


---

Comment by mabshoff created at 2009-04-17 07:38:40

Well, it is does not pass doctests please do not give a patch positive review. You should write that pending the doctest fix this is a positive review.

Cheers,

Michael


---

Comment by bump created at 2009-04-17 12:34:25

I uploaded an additional tiny patch that addresses the problem Anne found. It
goes on top of the original patch.

This time I checked that passes `sage --testall`.


---

Comment by mabshoff created at 2009-04-17 12:44:32

Positive review for Dan's fix that Anne suggested. This makes it a positive review in total.

Cheers,

Michael


---

Attachment


---

Comment by bump created at 2009-04-20 14:04:28

Changing status from new to assigned.


---

Comment by bump created at 2009-04-20 14:04:28

Changing assignee from mhansen to bump.


---

Comment by bump created at 2009-04-20 14:04:28

I found that the patches didn't apply cleanly to sage-3.4.1.rc4, so I
rebased. The patch trac_5751-rebased-3.4.1.patch  supercedes the
previous two patches.


---

Comment by mabshoff created at 2009-04-23 05:42:01

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-23 05:42:01

Resolution: fixed
