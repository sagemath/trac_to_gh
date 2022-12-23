# Issue 9674: Please revert sage/crypto/mq/sbox.py [11673:11b2f556827a:12294:d7533ae4895e]

Issue created by migration from https://trac.sagemath.org/ticket/9674

Original creator: nmouha

Original creation time: 2010-08-03 12:17:53

Assignee: mhansen

CC:  malb

Revision sage/crypto/mq/sbox.py [11673:11b2f556827a:12294:d7533ae4895e] (explacing log_b() by exact_log()) causes the following problems:

* difference_distribution_matrix() (in crypto/mq/sbox.py) crashes when an n-to-m bit S-box does not contain the element 2<sup>m-1</sup> (the wrong calculation of m results in an array index going out of bounds).

* the statement length != int(length) is never executed, because exact_log() always outputs an integer



---

Comment by ylchapuy created at 2010-08-07 13:01:46

Does ticket #9366 fix your problem?


---

Comment by nmouha created at 2010-08-07 23:16:41

Replying to [comment:1 ylchapuy]:
> Does ticket #9366 fix your problem?

Thank you for looking into this. You patch fixes the second bullet point. But the main problem is this line: "self.n = ZZ(max(S)+1).exact_log(2)".

Try this, and see what happens:
S = mq.SBox(5,6,0,3,4,2,1,2);
S.difference_distribution_matrix();


---

Comment by ylchapuy created at 2010-08-08 08:39:00

Changing status from new to needs_review.


---

Comment by ylchapuy created at 2010-08-08 08:39:00

You might review the following patch replacing `exact_log` with `nbits`.


---

Comment by nmouha created at 2010-08-08 11:08:39

Your proposed patch fixes the problem. I also think it's a cleaner solution than reversing the patch by mhansen. Thanks for your time.


---

Comment by ylchapuy created at 2010-08-09 18:33:23

If you are satisfied with the patch, and checked that all the doctests are still ok, then the procedure is to check the action "positive review" (bottom of the ticket page if you are logged in) and add yourself to the reviewers.
This allows the release manager to consider the merging of this ticket in the next release.


---

Comment by ylchapuy created at 2010-08-13 12:29:18

Maybe Martin will be interrested in reviewing this...


---

Comment by malb created at 2010-08-14 12:58:34

Patch looks good, doctests pass.


---

Comment by malb created at 2010-08-14 12:58:34

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-15 09:01:48

Please put the ticket number in the first line of the patch commit string.


---

Comment by mpatel created at 2010-08-15 09:01:48

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by ylchapuy created at 2010-08-15 11:23:31

Done, I put it back as positive review directly, I hope it's ok.


---

Comment by ylchapuy created at 2010-08-15 11:23:31

Changing status from needs_work to positive_review.


---

Comment by mpatel created at 2010-08-15 21:18:36

Sure.  Thanks!


---

Comment by mpatel created at 2010-09-15 11:13:27

Resolution: fixed
