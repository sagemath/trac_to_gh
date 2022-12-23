# Issue 7341: major tab completion issue in notebook (?)

Issue created by migration from https://trac.sagemath.org/ticket/7341

Original creator: was

Original creation time: 2009-10-28 22:17:40

Assignee: boothby

Try this in the notebook:

```
K.<a> = QuadraticField(-7)
b = K.pari_bnf()
b.<tab>
```


Then compare to the command line.  For some reason the last thing, "b.bnfunit" is missing in the notebook.


---

Comment by was created at 2009-10-29 01:35:52

Changing priority from major to blocker.


---

Attachment


---

Comment by was created at 2009-10-29 06:42:46

Changing status from new to needs_review.


---

Comment by timdumol created at 2009-10-29 12:08:19

Bug confirmed, and patch works. I've also added a new test in #7343 to confirm that the patch does the fix. Perhaps we should require any patch to SageNB to add a Selenium test?


---

Comment by timdumol created at 2009-10-29 12:08:19

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-11-09 17:17:55

Resolution: fixed
