# Issue 9333: the kash optional spkg doesn't work at all on OS X due to mistake in use of tar

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-25 03:08:21

Assignee: tbd




---

Attachment

for reference only; do not apply


---

Comment by jhpalmieri created at 2011-05-27 05:01:47

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2011-05-27 05:01:47

I've posted a link to a new spkg, along with the patch used to create it.  I have a feeling that it could use more work, but since it's an optional package for software which is 3 years old, I'm not sure if it's worth it.  I also have a feeling that it shouldn't be an optional package, but rather an experimental one: since it only installs on OS X and linux, that's not enough platforms for a good optional package.  But that change should be discussed elsewhere...


---

Comment by kcrisman created at 2011-06-08 20:17:41

It even works on PPC!

I did find an error in kash.py

```
sage: a = kash('(9 - 7) * (5 + 6)'); a              # optional -- kash

22
```

so I get "expected nothing" for that one test when I do `./sage -t -optional devel/sage/sage/interfaces/kash.py`.

Otherwise seems like this is reasonable.  Fix that and positive review, modulo my weak understanding of shell script - but the options are the right ones on Mac.  What the heck are those Linux options?

By the way, the development of KASH seems to have abruptly stopped.  Any chance it will resume?


---

Comment by kcrisman created at 2011-06-08 20:17:41

Changing status from needs_review to needs_work.


---

Attachment

patch for sage library


---

Comment by jhpalmieri created at 2011-06-08 21:45:22

Removing the blank line fixes the doctest for me.  (I have no idea what the linux options are, by the way.)


---

Comment by jhpalmieri created at 2011-06-08 21:45:22

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-06-08 22:15:56

Thumbs up.


---

Comment by kcrisman created at 2011-06-08 22:15:56

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-06-20 19:09:32

Sage patch merged in sage-4.7.1.alpha4 but the "optional packages" page needs to be updated manually.  John, can you take care of this?


---

Comment by jhpalmieri created at 2011-07-01 18:16:59

Replying to [comment:6 jdemeyer]:
> Sage patch merged in sage-4.7.1.alpha4 but the "optional packages" page needs to be updated manually.  John, can you take care of this?

Okay, done.


---

Comment by jdemeyer created at 2011-07-03 11:17:33

Resolution: fixed
