# Issue 4359: [with patch, needs review] Huge number of small fixes to modular forms code

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-10-24 08:43:50

Assignee: craigcitro

This is just a big bundle of fixes to the modular forms code that I had piled up.


---

Attachment

Looks good.  I have some questions about `_ensure_is_compatible()` in modform/element.py

 1. I guess I don't quite know what the function is meant to be used for; the docstring says "compatible for arithmetic and comparison operations". I assume arithmetic here means addition or subtraction?

 2. With the patch, two forms of the same weight but different groups of the same level are deemed compatible.  For instance, if f is on Gamma0(11) and g is on Gamma1(11), or if f and g are on Gamma1(17) but with different Dirichlet characters.  Is this the desired behaviour?


---

Comment by craigcitro created at 2008-10-26 00:18:49

Changing status from new to assigned.


---

Attachment

Ah, good point. I added a patch that changes it to test that they have the same ambient space, which is what the docstring claims.


---

Comment by AlexGhitza created at 2008-10-26 00:22:21

OK, I'm happy.


---

Comment by mabshoff created at 2008-10-26 01:35:20

Resolution: fixed


---

Comment by mabshoff created at 2008-10-26 01:35:20

Merged both patches in Sage 3.2.alpha1
