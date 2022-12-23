# Issue 8617: Add galrep by Drew Sutherland to Sage

Issue created by migration from https://trac.sagemath.org/ticket/8617

Original creator: was

Original creation time: 2010-03-27 23:25:24

Assignee: davidloeffler




---

Attachment


---

Attachment


---

Comment by was created at 2010-03-27 23:27:13

Changing status from new to needs_review.


---

Comment by ncalexan created at 2010-03-30 22:24:40

This looks malformed -- there is no galrep.c code included in the patch (that I can see).


---

Comment by rlm created at 2010-05-27 23:12:50

Changing status from needs_review to needs_work.


---

Attachment

I will review this ticket, as long as someone else makes the necessary changes to the extcode spkg to include the `galrep_*.dat` files in the appropriate manner.


---

Comment by rlm created at 2010-06-15 20:02:48

Changing status from needs_work to needs_review.


---

Attachment

PS - I don't think this is quite the right way to update extcode... I didn't realize I had done 'alpha0' --> 'alpha1'. I suppose the release manager would just add the "galrep" directory to the data/extcode directory, which would then be included in the new extcode spkg automatically by the dist script (Is this correct?)


---

Comment by rlm created at 2010-06-24 20:28:09

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-24 20:28:09

Since I'm doing release management for sage-4.5, I can just merge the files here the right way, and since I haven't actually contributed anything, I feel as if I can give it a positive review as is.


---

Comment by rlm created at 2010-07-06 03:27:37

Resolution: fixed


---

Comment by rlm created at 2010-07-13 16:35:21

I'm reverting this ticket, as it causes several weird problems: see #9445 and #9490.


---

Comment by rlm created at 2010-07-13 16:41:37

Resolution changed from fixed to 


---

Comment by rlm created at 2010-07-13 16:41:37

Changing status from closed to new.


---

Comment by rlm created at 2010-07-13 16:41:37

Removed `$SAGE_ROOT/data/extcode/galrep`, as well as the relevant lines from `module_list.py`, `sage/libs/all.py`, `setup.py` and deleted `sage/libs/galrep`.

:-(


---

Comment by rlm created at 2010-07-13 16:41:46

Changing status from new to needs_work.


---

Comment by was created at 2010-11-17 02:09:11

Note - I plan to include this in PSAGE: http://code.google.com/p/purplesage/issues/detail?id=10
