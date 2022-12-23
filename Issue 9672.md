# Issue 9672: Improve performance of Graph.genus

Issue created by migration from https://trac.sagemath.org/ticket/9672

Original creator: boothby

Original creation time: 2010-08-03 01:30:08

Assignee: jason, ncohen, rlm

CC:  rlm

Two easy improvements can be made to `Graph.genus`:

  * When computing local orbit structure of face map, don't compute the entire orbits.
  * Compute blocks and cut vertices, embed the individual blocks, and reconstruct them if the user wants the embedding.


---

Attachment


---

Comment by boothby created at 2010-08-05 14:45:52

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-08-23 03:37:48

Hmmm... I quite agree with the part of the patch distributing the genus computations over 2-connected components, but I know nothing about what happens in the `flip` method. I will try to have a closer look at that, but do you think reading some textbook may help me understand what it does ? I am totally ignorant  about graph embeddings `^^;`. If you have a title in mind, please tell me `:-)`

Nathann

P.S. : This shouldn't, of course, prevent any knowledgeable reviewer from reading this patch in the meantime.


---

Comment by boothby created at 2010-08-23 19:34:42

Nathann,

There's a forthcoming writeup about how this algorithm works.  Robert Miller understands how it works, though we haven't had a chance to chat about this patch yet.  Either I'll get Robert to review this, or finish the writeup.  I'm more tempted to have Robert review this, since I don't believe the algorithm is novel enough to publish.


---

Comment by ncohen created at 2010-08-24 10:26:02

Got it ! Waiting for Robert then `:-)`

I don't like to see tickets waiting for review in the Graph Theory section that are not mine `:-D`

Nathann


---

Comment by rlm created at 2010-11-11 12:33:28

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-11-11 12:33:28

Don't let this think you're getting out of writing up the algorithm!


---

Comment by rlm created at 2010-11-11 12:56:26

Or even, a sentence that makes sense!


---

Comment by jdemeyer created at 2010-11-11 16:46:07

Should this be merged in Sage 4.6.1? (if yes, please set the Milestone)


---

Comment by jdemeyer created at 2011-01-12 06:32:52

Resolution: fixed
