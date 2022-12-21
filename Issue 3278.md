# Issue 3278: [with patch, needs review] update the crystal iterator to use the new backtracking code

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-05-23 10:12:49

Assignee: mhansen

CC:  sage-combinat




---

Attachment


---

Comment by ddrake created at 2008-05-26 06:00:27

Positive review, with one caveat: I didn't actually apply the patch and run the tests, because my Sage tree is messed up at the moment. mhansen on IRC said the tests pass...however, "because he said so on IRC" is an insult to the whole idea of review, so I feel like I should offer that warning. :)


---

Comment by mabshoff created at 2008-05-26 06:19:22

I applied the patch to my merge tree and "-testall -long" passed. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-26 06:19:40

Merged in Sage 3.0.3.alpha0


---

Comment by mabshoff created at 2008-05-26 06:19:40

Resolution: fixed
