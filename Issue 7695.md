# Issue 7695: naming of the variable in subfields of cyclotomic fields

Issue created by migration from https://trac.sagemath.org/ticket/7695

Original creator: wuthrich

Original creation time: 2009-12-16 00:33:08

Assignee: davidloeffler

Keywords: cyclotomic fields, subfields


```
sage: F = CyclotomicField(7)
sage: K = F.subfields(3)[0][0]
sage: K
Number Field in zeta70 with defining polynomial x^3 + x^2 - 2*x - 1
```


I think this convention of adding a 0 to the variable name, as nice and practicle as it is in general, is not good in this case. The resulting algebraic element is not a 70th root of unity as the name would suggest.


---

Comment by wuthrich created at 2010-07-30 17:22:26

exported against 4.5.2.alpha1; but must be applied after #9407


---

Comment by wuthrich created at 2010-07-30 17:24:15

Changing status from new to needs_review.


---

Attachment

This is ready for review but depends on #9407.

Of course, this is not the only solution, but it eliminates the cases that bother me.


---

Comment by wuthrich created at 2013-12-30 12:13:35

I rebased it and removed the useless dependency. This is really a trivial change.


---

Comment by wuthrich created at 2013-12-30 12:15:59

New commits:


---

Comment by jdemeyer created at 2013-12-30 12:34:58

I think it would be better to add the underscore in all cases where the generator ends with a digit.


---

Comment by jdemeyer created at 2013-12-30 12:34:58

Changing status from needs_review to needs_work.


---

Comment by wuthrich created at 2013-12-30 16:29:31

I agree. Here is the change. I am running the tests now to see if there are any other corrections in the documentation to make.


---

Comment by git created at 2013-12-30 16:29:45

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by wuthrich created at 2013-12-30 16:32:11

a little bit annoying that the push resets the dependency again. what did i do wrong ?


---

Comment by wuthrich created at 2013-12-30 19:01:34

Changing status from needs_work to needs_review.


---

Comment by pbruin created at 2013-12-30 21:54:02

Replying to [comment:13 wuthrich]:
> a little bit annoying that the push resets the dependency again. what did i do wrong ?
`sage --dev` has its own local version of the dependencies.  I think that when the local and remote dependencies are different, it is supposed to ask if you want to upload or download the dependency list or to leave the two lists different.


---

Comment by jdemeyer created at 2013-12-31 10:13:10

Patch looks good, running doctests now...


---

Comment by jdemeyer created at 2013-12-31 11:14:16

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-01-05 00:32:17

Resolution: fixed
