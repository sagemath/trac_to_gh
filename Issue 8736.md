# Issue 8736: Bug in computing radical of univariate polynomial

Issue created by migration from Trac.

Original creator: johanbosman

Original creation time: 2010-04-21 09:43:31

Assignee: AlexGhitza

From #sage-devel:
<wjp> sage: R.<x> = GF(2)[]
<wjp> sage: (x^2).radical()
<wjp> 1


---

Comment by johanbosman created at 2010-04-21 11:19:03

Changing status from new to needs_review.


---

Comment by leif created at 2010-04-21 20:10:31

I was told it is not bad to put the corresponding ticket number in the doctest and/or near the code that fixes an issue for later reference.


---

Attachment


---

Comment by johanbosman created at 2010-04-22 10:55:52

Like this? ;)


---

Comment by novoselt created at 2010-04-22 21:23:39

Probably like that, but now this patch file contains two patches and does not apply cleanly. I know that if you remove the existing patch before repeating the export command, everything should be fine and you will get a nice new patch. Maybe there are better ways which I am not aware of. Otherwise the patch seems fine to me and passes all doctests (I ran them on the previous working version).


---

Comment by novoselt created at 2010-04-22 21:23:39

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-04-22 22:31:57

Johan's patch with first hunk deleted


---

Attachment

It's easier to just edit the patch (i.e., delete the first hunk)...


---

Comment by leif created at 2010-04-22 22:33:07

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2010-04-23 03:08:34

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-29 04:58:22

Resolution: fixed
