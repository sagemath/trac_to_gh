# Issue 8037: add sagetex to the french tutorial

Issue created by migration from https://trac.sagemath.org/ticket/8037

Original creator: jhpalmieri

Original creation time: 2010-01-22 06:18:10

Assignee: mvngu

CC:  ddrake

Make changes in the French tutorial corresponding to those in #7617 in the English version.


---

Attachment


---

Comment by mmezzarobba created at 2010-02-25 22:53:42

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2010-02-25 22:54:20

Changing assignee from mvngu to mmezzarobba.


---

Comment by ddrake created at 2010-02-26 02:03:36

Uh oh, there's a tiny reject with this patch in 4.3.3 -- a "[SA]" got turned into "[Sage]". I'll upload a new patch.


---

Comment by ddrake created at 2010-02-26 02:04:21

fix a small reject in introduction.rst


---

Attachment

By the way, the documentation builds fine and appears as it should. (I'm using 4.3.3.) I think this can be a positive review, although I would prefer to have a French speaker (or at least someone who knows more than I do!) look over the patch.


---

Comment by ddrake created at 2010-02-26 02:21:25

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-02 22:11:42

Merged [trac_8037_sagetex_french_tutorial.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8037/trac_8037_sagetex_french_tutorial.2.patch).



Marc, Dan: Avoid putting the following line at the top of your patch file:

```
exporting patch:
```

It can result in Mercurial ignoring your commit message, so that your commit message won't show up in the changelog.


---

Comment by mvngu created at 2010-03-02 22:11:42

Resolution: fixed
