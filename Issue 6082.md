# Issue 6082: [with patch, needs review] realloc called too often for Integer construction/deconstruction

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-05-19 06:02:38

Assignee: somebody

When putting objects back into the pool, we realloc the `mpz_t` to a smaller size to be able to reclaim the memory for larger integers. Unfortunately, chopping them to one limb means that they will often need to grow again (even if subsequent arithmetic fits in a limb). 


---

Attachment

Now it only reclaims the memory if more than 10 limbs (80 bytes) are used.


---

Comment by mabshoff created at 2009-05-21 02:08:03

Resolution: fixed


---

Comment by mabshoff created at 2009-05-21 02:08:03

Merged in Sage 4.0.rc0.

Cheers,

Michael
