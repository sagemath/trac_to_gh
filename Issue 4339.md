# Issue 4339: modular forms -- incorporate Nils Skoruppa's code for computing generators for the ring of modular forms of given level

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-22 17:49:42

Assignee: craigcitro

CC:  nilsskoruppa

Craig has an email from Nils with this code.


---

Comment by mabshoff created at 2008-10-31 21:42:10

I am adding Nils to the CC here so he is aware of the ticket. IIRC it was also a team effort to write that code, but I could be wrong. Some copy of Nil's code seems to be at

http://modular.math.washington.edu/home/ljpk/sage-add-ons/nils/

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-05 06:07:06

Craig, 

any news on this front? Maybe somebody else would be willing to start the review process if the code was posted?

Cheers,

Michael


---

Comment by craigcitro created at 2009-01-23 00:14:58

Changing type from defect to enhancement.


---

Comment by davidloeffler created at 2010-01-21 09:13:29

Can I suggest closing this ticket? I independently fixed the code for the ring of modular forms last year, and it got committed as part of #5727 (changeset 11961). I've since looked at Nils' code and it seems that he and I independently fixed the same bug in more or less the same way. Certainly find_generators.py now works, and has extensive doctests and passes them all.

I'm setting this to "needs review" (if you like, I'm asking for a review for the empty patch).

David


---

Comment by davidloeffler created at 2010-01-21 09:13:29

Changing status from new to needs_review.


---

Comment by was created at 2010-01-21 17:02:40

Looks good to me.  I can't see any bugs, and you didn't lower the coverage score.


---

Comment by was created at 2010-01-21 17:02:40

Changing status from needs_review to positive_review.


---

Comment by craigcitro created at 2010-01-21 18:20:16

Resolution: fixed


---

Comment by craigcitro created at 2010-01-21 18:20:16

I agree. I intended to close this ticket once you (David) fixed up that code, but apparently forgot.
