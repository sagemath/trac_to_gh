# Issue 3601: Reimplementation of tensor products

Issue created by migration from Trac.

Original creator: aschilling

Original creation time: 2008-07-08 03:30:36

Assignee: Mike Hansen

CC:  sage-combinat-commits@googlegroups.com

Keywords: tensor products of crystals

I split TensorProductOfCrystals into TensorProductOfCrystalsWithGenerators and
FullTensorProductOfCrystals (with or without the option of being a classical crystal).
This makes it possible to have a more efficient way to access list, count, etc for 
tensor products that do not have module generators.

Also, the distinction between the specifications of module_generators and 
highest_weight_vectors is made more precise (which made it necessary to slightly 
change the implementation of Daniel Bump on characters).

This change is necessary for the upcoming implementation of affine crystals.


---

Attachment


---

Attachment

Hi Anne,

I added a few doctests and fixed some whitespace issues (there were tabs instead of spaces).  If you're fine with these changes, I'll go ahead and give it a positive review so it can get merged.

--Mike


---

Comment by aschilling created at 2008-07-09 21:18:17

Hi Mike,

Yes, your changes look fine to me (I wonder how the tabs instead of 
spaces happened to be wrong?).

Anne


---

Comment by mhansen created at 2008-07-09 21:20:18

I'm not sure.  Usually the editor picks that up just fine.


---

Comment by mabshoff created at 2008-07-10 01:41:01

Anne, Mike,

to be 100% clear: both patches should be applied in this case?

Cheers,

Michael


---

Comment by mhansen created at 2008-07-10 01:54:10

Yes, both patches.


---

Comment by mabshoff created at 2008-07-16 03:51:27

Merged in Sage 3.0.6.alpha0


---

Comment by mabshoff created at 2008-07-16 03:51:27

Resolution: fixed
