# Issue 9661: pari(string) and gp(string) always returns a value, even when it should not

Issue created by migration from Trac.

Original creator: jdemeyer

Original creation time: 2010-08-01 16:47:28

Assignee: was

When executing a PARI or GP command from Sage, a value of 0 is returned when None would be expected.  For example, in a gp shell (started with sage -gp for example):


```
gp> kill(x)   /* No output */
```


But in Sage:

```
sage: gp('kill(x)')
0
sage: pari('kill(x)')
0
```


It should be possible to fix this by checking for `gnil` as return value.


---

Attachment


---

Comment by jdemeyer created at 2010-08-02 07:23:08

Changing assignee from was to jdemeyer.


---

Comment by jdemeyer created at 2010-08-02 07:23:37

Changing status from new to needs_review.


---

Comment by cremona created at 2010-08-03 01:43:03

I'm testing this now on 4.5.2.rc0.  Can you say why you included _sig_off ?  (I do not claim to understand how Sage/pari signal handling works.)  Without this patch there is a return with no _sig_off (unless the call to new_gen does that.)


---

Comment by cremona created at 2010-08-03 02:08:41

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-08-03 02:08:41

Tests all pass on 4.5.2.rc0 (64-bit ubuntu).


---

Comment by jdemeyer created at 2010-08-03 07:07:35

Replying to [comment:5 cremona]:
> I'm testing this now on 4.5.2.rc0.  Can you say why you included _sig_off ?  (I do not claim to understand how Sage/pari signal handling works.)  Without this patch there is a return with no _sig_off (unless the call to new_gen does that.)

It's exactly as you say, new_gen() calls _sig_off.


---

Comment by mpatel created at 2010-08-09 09:42:11

Resolution: fixed
