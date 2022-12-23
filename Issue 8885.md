# Issue 8885: deprecated_functions_alias and sphinx

Issue created by migration from https://trac.sagemath.org/ticket/8885

Original creator: hivert

Original creation time: 2010-05-05 11:06:53

Assignee: hivert

Keywords: Depreacation alias documentation

Currently if a function is a deprecated alias, the doc of the aliased function appears un the reference manual. Nothing shows that the function is deprecated. See for example the doc of
`sage.combinat.partition.associated`


---

Comment by hivert created at 2011-04-04 16:44:15

Changing status from new to needs_review.


---

Comment by hivert created at 2011-04-04 16:44:15

Should be ready for review


---

Comment by mariah created at 2011-06-16 14:14:14

Changing status from needs_review to needs_info.


---

Comment by mariah created at 2011-06-16 14:14:14

I applied the patch to sage-4.7.1.alpha1, did 'sage -b', and rebuilt the documentation.  Yet when I look at the doc of `sage.combinat.partition.associated`, I do not see anything saying that the function is deprecated.  Am I missing something?


---

Comment by hivert created at 2011-06-18 21:27:57

Hi Mariah,

Replying to [comment:3 mariah]:
> I applied the patch to sage-4.7.1.alpha1, did 'sage -b', and rebuilt the
> documentation.  Yet when I look at the doc of
`sage.combinat.partition.associated`,
> I do not see anything saying that the function is deprecated.  Am I missing something?

This is what I got under the command line

```
sage: P.associated?
Type:           DeprecatedFunctionAlias
Base Class:     <class 'sage.misc.misc.DeprecatedFunctionAlias'>
String Form:    <sage.misc.misc.DeprecatedFunctionAlias object at 0x30c6210>
Namespace:      Interactive
File:           /home/florent/src/Sage/sage/local/lib/python2.6/site-packages/sage/misc/misc.py
Definition:     P.associated(self, *args, **kwds)
Docstring:
    Deprecated since version Sage: Version 4.4. Use ``conjugate()``
    instead.
[...]
```

It also work under the notebook and the html built doc.

How did you rebuild the documentation ? If you just did {{{sage -docbuild
reference html}}} then without touching `partitions.py` Sphinx consider it
upto date and doesn't rebuild the documentation. Is that what you did ?

Florent


---

Comment by mariah created at 2011-06-21 18:50:38

Changing status from needs_info to needs_review.


---

Comment by mariah created at 2011-06-21 18:50:38

Oops!  That is exactly what I did!


---

Comment by mariah created at 2011-06-21 18:51:23

So this time I applied the patch, did 'sage -b', 'touch devel/sage/sage/combinat/partitions.py', then did 'sage -docbuild reference html'.  Now I see that the function is deprecated.  I also did 'make testlong' and all tests passed.  Positive review!


---

Comment by mariah created at 2011-06-21 18:51:23

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2011-06-21 18:58:17

Replying to [comment:6 mariah]:
> So this time I applied the patch, did 'sage -b', 'touch devel/sage/sage/combinat/partitions.py', then did 'sage -docbuild reference html'.  Now I see that the function is deprecated.  I also did 'make testlong' and all tests passed.  Positive review!

Excellent ! Thanks for the review.

Florent


---

Comment by jdemeyer created at 2011-06-24 14:57:48

This should be rebased to sage-4.7.1.alpha3.


---

Comment by jdemeyer created at 2011-06-24 14:57:48

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by hivert created at 2011-06-28 15:08:12

Changing status from needs_work to positive_review.


---

Comment by hivert created at 2011-06-28 15:08:12

Replying to [comment:8 jdemeyer]:
> This should be rebased to sage-4.7.1.alpha3.

Done ! I is only rebase therefore I revert back to positive review. I'm not sure I'm allowed to do that.


---

Comment by jdemeyer created at 2011-06-28 20:38:04

If you made only a pure rebase with no other changes, putting the ticket back to positive_review is the right thing to do.


---

Comment by jdemeyer created at 2011-06-28 20:38:04

Changing keywords from "Depreacation alias documentation" to "deprecation alias documentation".


---

Comment by jdemeyer created at 2011-07-04 12:02:06

Resolution: fixed


---

Comment by hivert created at 2011-07-04 21:07:14

For the record I added a dependency to #11320.
