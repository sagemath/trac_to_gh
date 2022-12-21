# Issue 4889: deprecate matrix.list()

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-12-30 01:01:47

Assignee: was

list(M) and M.list() returning different lists is inconsistent. As discussed at http://groups.google.com/group/sage-support/browse_thread/thread/a7d8b439df769e7 we should have  M.entries() which replaces M.list() and deprecate the latter. 

The behavior of list(M) will remain the same, and consistency with M[i]. 


---

Comment by jason created at 2009-01-21 14:35:26

A reason to have m.list() return the entries is that m.dict() returns the entries, but in "sparse" dictionary format.


---

Comment by was created at 2009-01-30 07:13:46

I was coding, and I realized that I very strongly object to this ticket -- or at least the nebulousness of it -- I can't even write the code i want the way I want since I know that it will just break for sure as soon as somebody closes this ticket :-(.  For me it is an incredibly important design pattern when working with matrices to turn the entire matrix into a list of its entries -- do something with them -- then use the resulting list to make another matrix. 

This is exactly modeled on Magma's `Eltseq` command, which turns almost anything in Magma into a linear sequence, and almost anything in Magma can be reconstructed from that sequence.  

Anyway, the list method is not just one off thing that doesn't matter -- it's central to matrices.  So either wontfix this ticket or do it asap to get the pain over with.

I do worry that changing this is changing things for change sake, and I'm not convinced that is a good idea...


---

Comment by jason created at 2009-01-30 10:15:51

I have a partial patch for this.  I also worry that we are just changing things to change things, though I agree slightly that the new name (M.entries) is better than M.list in that it is more descriptive.

Your first paragraph seems to indicate that it would be much better for list(M) to return a list of entries, rather than a list of rows.  Is that correct?


---

Comment by jason created at 2009-01-30 10:18:20

For what it's worth, for a numpy array A, the iterator over all entries is given by A.flat


---

Comment by was created at 2010-01-17 14:14:58

See http://www.wstein.org/home/wstein/build/sage-4.3.1.rc0-boxen-x86_64-Linux/4889-part1.out for the output of doctests on part1.  Fixing all those (many) issues is all that is left.


---

Comment by was created at 2010-01-17 14:26:58

See also http://www.wstein.org/home/wstein/build/sage-4.3.1.rc0-boxen-x86_64-Linux/4889-part1-error_not_warn.out

Though I just spent a substantial amount of time on this ticket, I'm *seriously* considering arguing again that this change should *not* be made.  The reason is simply if literally hundreds of files in the Sage distro are so intensely impacted, then lots of external code will be too.  And this change simply isn't *that* important.  Better could be to just document the list method better, and point out the subtlety.


---

Attachment

part 1, which does what is needed in the matrix directory; another part will mop up.


---

Comment by was created at 2010-01-18 01:07:35

OK, after working on this for hours and hours, and changing a ridiculous amount of little stuff (see attached patch, still called -part1), I even more strongly believe this ".list()" usage is deeply entrenched throughout all of Sage.  I refuse to make this deprecation change, since it will certainly introduce subtle issues in SAge, and will likely break a lot of code that isn't in Sage.  Instead I'm posting a patch to document the subtlety clearly.


---

Comment by was created at 2010-01-18 01:07:59

apply this instead of the previous


---

Attachment


---

Comment by was created at 2010-01-18 01:08:24

Changing status from new to needs_review.


---

Comment by jason created at 2010-01-18 18:04:35

I'll post a patch which makes .entries an alias for list.  I think it's a better name, and better enough that it's worth having two names and encouraging people to use M.entries().


---

Comment by robertwb created at 2010-01-18 19:11:48

I agree with William that this is too big of a change to make, though +1 to encouraging an alias entries as it is more explicit.


---

Comment by was created at 2010-01-18 22:30:18

Yes, +1 to the alias.


---

Comment by ncalexan created at 2010-02-17 20:13:09

I don't really care if the alias goes in, but this looks fine to me.


---

Comment by ncalexan created at 2010-02-17 20:13:09

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-18 22:03:37

Resolution: fixed


---

Comment by mvngu created at 2010-02-18 22:03:37

Merged [trac_4889-document_instead_of_deprecate.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4889/trac_4889-document_instead_of_deprecate.patch).


---

Comment by jason created at 2010-02-19 16:29:50

Changing the title to reflect what was actually done.


---

Comment by jason created at 2010-02-19 16:31:29

I've made a new ticket to add the m.entries() alias: #8308.
