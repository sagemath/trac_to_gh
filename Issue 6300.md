# Issue 6300: doctest fix related to singular upgrad; needed on 32-bit OS X intel, at least (maybe all 32-bit)

Issue created by migration from https://trac.sagemath.org/ticket/6300

Original creator: was

Original creation time: 2009-06-15 15:45:30

Assignee: tbd

> >> File
> >> "/Users/was/build/sage-4.0.2.rc0/devel/sage/sage/libs/singular/singular.
> >>pyx ", line 501:
> >>     sage: P(2^32-1)
> >> Expected:
> >>     -1
> >> Got:
> >>     4294967295
> >
> > Is that with my the fix at
> >
> >  http://trac.sagemath.org/sage_trac/attachment/ticket/6051/singular_exp_o
> >verflow.patch
> >
> > or without? It seems (since you are using a 32-bit system) all that needs
> > to be done is to fix the doctest.
>
> No, I had not applied your patch.  However, I just did, and the above
> issue remains.

Yes, the issue remains. One should change the doctest, i.e. the behaviour we
expect now is the wrong behaviour.


---

Attachment

Patch depends on hotfix at #6051.


---

Comment by malb created at 2009-06-15 16:23:35

With this patch and the hotfix from #6051 all doctests pass on sage.math FWIW.


---

Comment by was created at 2009-06-15 23:57:11

merged into 4.0.2.rc1


---

Comment by was created at 2009-06-15 23:57:11

Resolution: fixed
