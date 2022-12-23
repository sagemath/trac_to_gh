# Issue 7976: Extends __classcall__ to control inheritance

Issue created by migration from https://trac.sagemath.org/ticket/7976

Original creator: hivert

Original creation time: 2010-01-18 13:03:46

Assignee: hivert

CC:  sage-combinat

Keywords: ClassCall inheritance

This patch extends `ClasscallMetaclass` so that one can control the call of a class trough two different static methods:

 - `__classcall__` which behave as usual and is inherited
 - `__classcall__no_inherits` which is not called by derived classes

If both exists the latter is used.


---

Comment by hivert created at 2010-01-18 15:08:42

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-01-18 22:06:36

Thanks Florent, and thanks for using this occasion to cleanup my code!

Can you fix the copyright dates? Mine should be 2009, and yours 2010

I like the idea of using Python's standard convention for private attributes; on the other hand, I am a bit worried about emulating Python's mechanism. In particular, we could eventually get in trouble with the class name hacking we do for pickling:

```
   sage: Sets.ParentMethods.__name__
   'Sets.ParentMethods'
```

I haven't found a way to *use* Python mechanism. So instead, what about using ``__classcall_private__``, and doing the test with '__classcall_private__' in cls.__dict__?

(I also prefer ``private`` to ``no_inherit``).

Cheers,


---

Comment by nthiery created at 2010-01-18 22:06:36

Changing keywords from "ClassCall inheritance" to "ClassCall, inheritance".


---

Comment by nthiery created at 2010-01-18 22:06:36

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2010-01-19 05:11:40

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-01-19 05:11:40

Replying to [comment:2 nthiery]:
> Thanks Florent, and thanks for using this occasion to cleanup my code!
> 
> Can you fix the copyright dates? Mine should be 2009, and yours 2010
> 
> [...]
> So instead, what about using ``__classcall_private__``, and doing the test with '__classcall_private__' in cls.__dict__?
> 
> (I also prefer ``private`` to ``no_inherit``).

I just uploaded a new patch which addresses all these remarks... Please re-review.


---

Attachment


---

Comment by nthiery created at 2010-01-19 09:07:55

Please double check the quick review patch, and add '#7976:' in front of the patch description, and it's good to go!


---

Comment by hivert created at 2010-01-19 11:50:38

Changing status from needs_review to positive_review.


---

Attachment

Replying to [comment:4 nthiery]:
> Please double check the quick review patch, and add '#7976:' in front of the patch description, and it's good to go!

I added '#7976:' and re-uploaded the patch. Thanks for the improvement of the doc. Your review patch is ok => positive review.


---

Comment by mvngu created at 2010-01-22 23:27:17

Merged in this order:

 1. [trac_7976-classcall_no_inherits-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7976/trac_7976-classcall_no_inherits-fh.patch)
 1. [trac_7976-classcall_no_inherits-review-nt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7976/trac_7976-classcall_no_inherits-review-nt.patch)


---

Comment by mvngu created at 2010-01-22 23:27:17

Resolution: fixed
