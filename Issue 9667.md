# Issue 9667: Use PARI's hash_GEN() for gen.__hash__

Issue created by migration from Trac.

Original creator: jdemeyer

Original creation time: 2010-08-02 09:47:20

Assignee: was

The latest version of PARI has a function `hash_GEN` which hashes a PARI `GEN`.  Since this is very likely faster than hashing the string representation of a `GEN`, we should use this for the `gen` class in sage/libs/pari/gen.pyx


---

Comment by jdemeyer created at 2010-08-02 12:22:58

Patch to be applied on top of #9343


---

Comment by jdemeyer created at 2010-09-15 17:12:33

Changing status from new to needs_review.


---

Attachment


---

Comment by jdemeyer created at 2010-09-15 17:13:13

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-09-15 17:13:13

Ignore this ticket, see #9764 instead.


---

Comment by mpatel created at 2010-09-28 11:15:03

Resolution: duplicate


---

Comment by was created at 2011-07-29 20:19:35

Hi,

For the record, this change introduced a major bug into Sage, because PARI's hash_GEN is itself buggy.  For example, by playing with ideals in Sage (code is complicated though...), I quickly got into this situation:

```
sage: n0
[11, 3; 0, 1]
sage: n1
[11, 3; 0, 1]
sage: hash(n0)
-7493989779944505307
sage: hash(n1)
-6341068275337658331
```



---

Comment by jdemeyer created at 2011-08-01 10:03:18

Replying to [comment:5 was]:
> For the record, this change introduced a major bug into Sage, because PARI's hash_GEN is itself buggy.
See #11611, I have not tracked it down precisely.


---

Comment by jdemeyer created at 2011-08-03 13:35:49

Replying to [comment:5 was]:
> Hi,
> 
> For the record, this change introduced a major bug into Sage, because PARI's hash_GEN is itself buggy.
Don't blaim PARI when the fault is the Sage->PARI interface. The issue is not `hash_GEN()`, it is a problem with how integers are converted from Sage to PARI.  I have a patch for this issue at #11611.
