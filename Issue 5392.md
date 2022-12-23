# Issue 5392: relative number field subfield method -- unclear documentation

Issue created by migration from https://trac.sagemath.org/ticket/5392

Original creator: dmharvey

Original creation time: 2009-02-27 16:03:04

Assignee: was

Consider


```
sage: R.<a> = NumberField(x^4 - 2*x^2 - 1)
sage: S.<i> = R.extension(x^2 + 1)
sage: S.subfield(a + i/a)
```


The S.subfield method documentation says that it constructs QQ(alpha), but this is false, I think it constructs R(alpha). In the above example, S.subfield(a + i/a) returns a number field of degree 8 over Q, whereas a + i/a has degree 4 over QQ (the minimal polynomial is `x^4 - 4x^2 + 8`).



---

Comment by davidloeffler created at 2009-07-20 20:32:19

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-20 20:32:19

Changing assignee from was to davidloeffler.


---

Comment by ArgaezG created at 2013-07-23 13:23:48

patch against sage 5.10


---

Attachment


---

Comment by ArgaezG created at 2013-07-23 13:24:34

Changing status from new to needs_review.


---

Comment by mkosters created at 2013-07-23 14:18:38

Changing keywords from "" to "sd51".


---

Comment by ArgaezG created at 2013-07-23 15:45:15

Changing status from needs_review to positive_review.


---

Comment by ArgaezG created at 2013-07-23 15:45:15

I happy with changes suggested by Michiel, and he is happy with mine.


---

Comment by mkosters created at 2013-07-23 18:01:49

Apply trac_5392_subfield_review.patch after trac_5392.patch​


---

Comment by jdemeyer created at 2013-07-24 07:31:31

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-07-24 07:31:31

The reviewer patch needs a proper commit message, use `hg qrefresh -e` for this.


---

Attachment

`@`jdemeyer: is it correct now?


---

Comment by mstreng created at 2013-07-24 08:45:00

Replying to [comment:8 mkosters]:
> `@`jdemeyer: is it correct now?

It has a proper commit message now. So assuming this is the same patch, I'll put this to positive review again.


---

Comment by mstreng created at 2013-07-24 08:45:00

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-07-31 12:53:02

Resolution: fixed
