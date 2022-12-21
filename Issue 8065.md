# Issue 8065: irreducible_characters() and word_problem() should sort their output

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2010-01-25 22:19:53

Assignee: joyner

These group functions use the GAP interface and return unsorted lists.  This makes them prone to doctest breakage when GAP is upgraded (and the order of things changes) or when GAP uses non-deterministic algorithms (and the order of things is ill-defined).

The patch fixes `irreducible_characters` and `word_problem`.  There might be more functions in `sage/groups` that require the same treatment, but that can go on a different ticket.



---

Attachment


---

Comment by AlexGhitza created at 2010-01-25 22:21:44

Changing status from new to needs_review.


---

Comment by dimpase created at 2010-01-26 09:46:06

Changing status from needs_review to needs_work.


---

Comment by dimpase created at 2010-01-26 09:46:06

see http://groups.google.com.sg/group/sage-devel/browse_thread/thread/98245adfb0c45e88/802a0ab633a0fb48#802a0ab633a0fb48
