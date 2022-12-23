# Issue 7888: Do not pass comment lines to Macaulay2

Issue created by migration from https://trac.sagemath.org/ticket/7888

Original creator: novoselt

Original creation time: 2010-01-10 01:53:39

Assignee: was

Currently passing "pure comments" to Macaulay2 locks the interface since Macaulay2 does not print a new input prompts. Evaluating whitespace lines locks it as well and while there is some stripping code in Expect, it does not work if whitespace lines appear in the middle of a block.

The attached patch replaces all such lines with empty ones before passing to Macaulay2. This may break string constants occupying several lines, however, as far as I understand, they have no chance of working without substantial modification of Expect.eval, which currently executes code line by line. (In particular, they hang up now.)


---

Comment by novoselt created at 2010-01-10 01:54:38

Changing status from new to needs_review.


---

Attachment


---

Comment by novoselt created at 2010-01-11 20:59:39

Ticket #7897 fixes this in a better way.


---

Comment by novoselt created at 2010-01-11 20:59:39

Resolution: duplicate
