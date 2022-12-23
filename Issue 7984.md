# Issue 7984: QQbar doesn't use canonical coercion for comparison

Issue created by migration from https://trac.sagemath.org/ticket/7984

Original creator: robertwb

Original creation time: 2010-01-18 20:29:47

Assignee: AlexGhitza


```
sage: QQbar(2) == GF(7)(2)
BOOM
```


Should be False. 


---

Attachment


---

Comment by wjp created at 2010-01-18 21:11:59

Changing status from new to needs_work.


---

Comment by wjp created at 2010-01-18 21:11:59

This patch depends on #4621 but seems to break the doctest added by that patch.


---

Comment by robertwb created at 2010-01-20 08:20:30

This patch is correct, the one at #4621 is wrong.


---

Comment by robertwb created at 2010-01-20 08:20:30

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-02-21 16:04:24

This one looks good to me.  However, when testing #4621 I noticed that this:

```
F.<a>= NumberField(x^2-2)
RR(a)
```

causes an infinite recursion, which is not good, but not caused by this patch.

I am giving this a positive review, and letting #4621 be sorted out after, also the issue above.  Perhaps rwb would like to open a ticket for that unless it is already covered by one?


---

Comment by cremona created at 2010-02-21 16:04:24

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-02-21 16:04:24

Changing keywords from "" to "QQbar comparison".


---

Comment by mvngu created at 2010-03-02 21:06:13

Robert: I have merged [7984-qqbar-cmp.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7984/7984-qqbar-cmp.patch) in your name with a sensible commit message.


---

Comment by mvngu created at 2010-03-02 21:06:13

Resolution: fixed
