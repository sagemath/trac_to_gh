# Issue 6557: fix bug in number field caching

Issue created by migration from https://trac.sagemath.org/ticket/6557

Original creator: was

Original creation time: 2009-07-18 22:07:13

Assignee: was


```
Here are two independent Sage 4.1 sessions which demonstrate that the
construction of NumberField's is context dependent:

       sage: K.<x> = CyclotomicField(5)[]
       sage: W.<a> = NumberField(x^2 + 1)
       sage: W
       Number Field in a with defining polynomial x^2 + 1 over its base field

       sage: W1 = NumberField(x^2+1,'a')
       sage: K.<x> = CyclotomicField(5)[]
       sage: W.<a> = NumberField(x^2 + 1)
       sage: W
       Number Field in a with defining polynomial x^2 + 1

In fact:

       sage: W1 is W0
       True
```



---

Attachment


---

Comment by cremona created at 2009-07-19 12:19:16

Changing keywords from "" to "Number fields".


---

Comment by cremona created at 2009-07-19 12:19:16

Positive review.  Applies to 4.1 and all tests in sage/rings/number_fields pass.


---

Comment by mvngu created at 2009-07-19 14:19:47

Resolution: fixed
