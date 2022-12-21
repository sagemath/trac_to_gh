# Issue 9666: Implement __hash__ for NumberFieldIdeal

Issue created by migration from Trac.

Original creator: jdemeyer

Original creation time: 2010-08-01 21:41:36

Assignee: davidloeffler

I propose to use a HNF Z-basis of number field ideals to compute the hash of an ideal.


---

Attachment


---

Comment by jdemeyer created at 2010-08-02 11:55:38

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-08-02 22:02:39

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-08-02 23:16:06

You need to add a doctest that illustrates use of the hash function, on both 32 and 64-bit computers.


---

Comment by was created at 2010-08-03 02:01:41

When I ran the test suite there were a bunch of failures in

   devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py

e.g.,

```
File "/mnt/usb1/scratch/wstein/build/sage-4.5.2.rc0/devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py", line 1141:
    sage: D.selmer_group([K.ideal(2, -a+1), K.ideal(3, a+1), K.ideal(a)], 3)
Expected:
    [2, -a - 1, -a]
Got:
    [2, -a - 1, a]
```



---

Comment by jdemeyer created at 2010-08-03 07:10:05

Apologies.  I did not expect the hash to have influence on this, I should have tested better.

I will postpone this to the release after the PARI upgrade, i.e. sage-4.6.1 or something.


---

Comment by was created at 2010-08-14 00:55:46

Resolution: duplicate


---

Comment by was created at 2010-08-14 00:55:46

The same is fixed correctly in #9400.  So I'm closing this as a dupe of that.
