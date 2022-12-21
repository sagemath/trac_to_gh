# Issue 2051: [with doc patch, needs review] added documentation for parameters of groebner_basis method of boolean ideals

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-02-05 11:53:47

Assignee: malb

CC:  burcin

See patch.


---

Attachment

It might be a good idea not to document features that don't work. (I.e., as outlined in #2052, draw_matrices, invert, noro, preprocess_only) As a matter of fact, I am not sure if all the other options work as they should. Maybe we should include optional doctests for them.

BTW, last time I asked Michael Brickenstein, `PolyBoRi` did not include a usable noro implementation.


---

Attachment

The patch `pbori_gb_doc2.patch` addresses Burcin's comments above. It should be applied on top of the first patch.


---

Comment by burcin created at 2008-02-05 13:50:39

Looks good to me.


---

Comment by mabshoff created at 2008-02-07 05:18:54

Merged both patches in Sage 2.10.2.alpha0


---

Comment by mabshoff created at 2008-02-07 05:18:54

Resolution: fixed
