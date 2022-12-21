# Issue 8114: doctest failure in `sage/libs/cremona/newforms.pyx` on 32-bit machines from #8042

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2010-01-28 22:28:32

Assignee: was

CC:  aghitza

I forgot to test my fix from #8042 on 32-bit platforms, and the fix causes doctest failures anywhere that `long` is smaller than 64 bits. I'm attaching a simple patch to fix this -- we just don't perform that test on 32-bit platforms.


---

Attachment


---

Comment by craigcitro created at 2010-01-28 22:32:31

Changing status from new to needs_review.


---

Comment by was created at 2010-01-28 23:07:55

With this patch applied, on 32-bit linux we have:


```
wstein`@`ubuntu32:/tmp/wstein/farm/sage-4.3.2.alpha0$         sage -t  -long "devel/sage/sage/libs/cremona/newforms.pyx"                                                                                        

sage -t -long "devel/sage/sage/libs/cremona/newforms.pyx"   

         [6.3 s]
                
```


Which is good.   However, I do not think the patch you posted explains very well what is going on.  It's not good for a user reading it.  I've posted an additional patch (apply after yours), which I think does a better job testing things and illustrating the issue.


---

Comment by was created at 2010-01-28 23:08:08

Changing priority from major to blocker.


---

Attachment


---

Comment by craigcitro created at 2010-01-28 23:13:06

Sure, that's fine. I was expecting that anyone who wanted to know what was going on would look at #8042, where there's an explanation -- but you're right, it wouldn't hurt to have at least some explanation in the code itself. (Basically, my rule of thumb is that anything in an `EXAMPLES` section needs a good explanation, but for things in the `TESTS` section, a pointer to a trac ticket is sufficient.)

Positive review -- apply both patches. (William, I'm listing us both as authors and reviewers, since we each reviewed the other person's contribution.)


---

Comment by craigcitro created at 2010-01-28 23:13:06

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-30 23:44:10

Merged in this order:

 1. [trac_8114.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8114/trac_8114.patch)
 1. [trac_8114-part2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8114/trac_8114-part2.patch)


---

Comment by mvngu created at 2010-01-30 23:44:10

Resolution: fixed
