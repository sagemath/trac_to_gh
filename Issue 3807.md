# Issue 3807: [with patch, needs review] Fix gcc 4.3 issues in David Harvey Bernoulli modp code

Issue created by migration from https://trac.sagemath.org/ticket/3807

Original creator: mabshoff

Original creation time: 2008-08-12 01:32:49

Assignee: mabshoff

There are two build issues in the Bernoulli mod p code with gcc 4.3 or higher. The attached patch fixes those.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-12 01:32:56

Changing status from new to assigned.


---

Attachment

Works fine on osx with gcc 4.0.1.

I say positive review unless something funny comes up in alpha2 testing.


---

Comment by mabshoff created at 2008-08-12 02:16:25

Resolution: fixed


---

Comment by mabshoff created at 2008-08-12 02:16:25

Merged in Sage 3.1.alpha2
