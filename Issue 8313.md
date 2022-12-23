# Issue 8313: Misplaced "`" in linear code construction documentation.

Issue created by migration from https://trac.sagemath.org/ticket/8313

Original creator: hivert

Original creation time: 2010-02-20 14:32:52

Assignee: wdj

While reading the doc I found the following trivial doc mistake:
At the begining of the file Linear Code construction, there is a `denotetheanswerby` which is typeset by LaTeX. I've no time to create the (trivial) patch right now. I'll if no one beats me. 


---

Comment by mvngu created at 2010-02-20 14:55:42

What is the exact path of the file(s) you are referring to? Which chapter/section in the Constructions document?


---

Comment by wdj created at 2010-02-20 15:03:07

Replying to [comment:1 mvngu]:
> What is the exact path of the file(s) you are referring to? Which chapter/section in the Constructions document?

It's about 10-15 lines from the top of 
http://www.sagemath.org/doc/reference/sage/coding/code_constructions.html


---

Attachment


---

Comment by hivert created at 2010-04-10 09:19:18

Changing status from new to needs_review.


---

Comment by hivert created at 2010-04-10 09:19:18

Changing keywords from "" to "Typo documentation".


---

Comment by hivert created at 2010-04-10 09:19:18

I had completely forgotten about this one... Trivial fix. Please review.


---

Comment by mvngu created at 2010-04-10 21:42:51

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 20:08:31

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 20:08:31

Merged in 4.4.alpha0:
 - trac_8313-typo_codeconstruction-fh.patch
