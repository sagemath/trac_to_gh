# Issue 9403: preimage method in NumberFieldHomomorphism_im_gens

Issue created by migration from https://trac.sagemath.org/ticket/9403

Original creator: jeremywest

Original creation time: 2010-07-01 23:18:22

Assignee: AlexGhitza

CC:  ebeyerstedt fwclarke davidloeffler

Keywords: number field, embedding, homomorphism, preimage

I am adding a preimage method in the NumberFieldHomomorphism_im_gens class. There may be a better or more general place to put this, but we need it for the descend_to method in EllipticCurve so I am putting it there for now.




---

Comment by jeremywest created at 2010-07-01 23:32:36

Changing status from new to needs_work.


---

Comment by jeremywest created at 2010-07-02 00:17:48

A preimage method for NumberFieldHomomorphism


---

Comment by jeremywest created at 2010-07-02 00:18:23

Changing status from needs_work to needs_review.


---

Attachment

I have implemented the preimage method including documentation and tests. I just need a review now. Let me know if this should go somewhere better.


---

Comment by ebeyerstedt created at 2010-07-02 04:12:23

The new patch changes each usage of .vector_space to .absolute_vector_space.
Also added a doctest.


---

Comment by ebeyerstedt created at 2010-07-02 05:44:14

Replaces previous patch.


---

Attachment

Updated documentation.


---

Comment by aly.deines created at 2010-07-02 17:54:04

Changing status from needs_review to positive_review.


---

Comment by jeremywest created at 2010-07-02 19:16:40

I changed the error message that is returned when the input is not in the image of the homomorphism so that, rather than a message about solving a matrix equation, it gives a message about the input not being in the image.


---

Comment by davidloeffler created at 2010-07-02 19:43:26

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2010-07-02 19:43:26

If you really must upload new patches to an already positively reviewed ticket, you *must* put the status back to "needs review".


---

Comment by davidloeffler created at 2010-07-02 19:43:33

Changing status from needs_work to needs_review.


---

Attachment

Fixes error handling message, replaces all previous patches.


---

Comment by ddrake created at 2010-07-22 23:54:34

David -- can you review the newest patch? If this ticket can get a positive review, then it and #9384 can get into 4.5.2.


---

Comment by aly.deines created at 2010-07-26 21:58:13

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-27 00:50:45

Resolution: fixed


---

Comment by ddrake created at 2010-07-27 00:50:45

Please include the ticket number in your commit messages! Also, Jeremy, you might want to set your username in your .hgrc file -- your patch has a username of "jeremy`@`west-imac-8-2007.local".


---

Comment by mpatel created at 2010-07-27 04:36:30

I'm entering a guess for the Reviewer(s) field.  Please correct me if I'm wrong.
