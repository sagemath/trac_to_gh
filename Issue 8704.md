# Issue 8704: Improve the _repr_ of IntegerRange

Issue created by migration from https://trac.sagemath.org/ticket/8704

Original creator: hivert

Original creation time: 2010-04-17 09:53:05

Assignee: hivert

The actual printing in in discussion on [this thread](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/5ff945e9d813392c) of sage-combinat-devel. I'll implement it as soon as the decision is made.


---

Comment by hivert created at 2010-05-13 17:56:08

Changing status from new to needs_review.


---

Comment by hivert created at 2010-05-13 17:56:08

Changing keywords from "" to "integer range".


---

Comment by hivert created at 2010-05-13 17:56:08

Changing type from defect to enhancement.


---

Comment by hivert created at 2010-05-15 17:05:50

I fixed a doctest failure... All tests should pass now.


---

Comment by hivert created at 2010-05-31 21:51:17

I fixed the following issues raised by Nicolas on sage-combinat-devel

```
> >> The output of IntegerRange is much nicer now. I was about to put a
> >> positive review, when I had a last doubt about the consistency between:
> >>
> >>      sage: I = IntegerRange(2,100,5); I
> >>      {2, 7 .. 97}
> >>      sage: I = IntegerRange(54,Infinity,3); I
> >>      {54, 57, ..}
> >>
> >> Should there be a comma in both cases, in none, or is it good as is?
> >
> > I would say {2, 7 .. 97} should be replaced by {2, 7, .., 97} for
> > consistency.
```



---

Attachment


---

Comment by mhansen created at 2010-06-06 08:34:51

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 08:34:51

Looks good to me.


---

Comment by mhansen created at 2010-06-06 08:35:05

Resolution: fixed
