# Issue 4340: Speed up Victor Miller basis code

Issue created by migration from https://trac.sagemath.org/ticket/4340

Original creator: craigcitro

Original creation time: 2008-10-22 18:16:47

Assignee: craigcitro

The current Victor Miller basis code in Sage is painfully slow. 

I've already written much faster code, which I'll submit shortly.


---

Comment by craigcitro created at 2008-10-30 20:00:09

This code is a *massive* speedup over the old code, and is still not as fast as I'm planning on making it. Even in examples as small as `victor_miller_basis(300,100)`, this gives a factor of 900 speedup. It's also now faster than Magma.

I'm pretty sure I've got all the corner cases covered, too, but one can never be sure about these things ...


---

Comment by craigcitro created at 2008-10-30 20:00:09

Changing status from new to assigned.


---

Comment by robertwb created at 2008-10-30 20:56:45

Looks good to me--I had to add a "var" argument to modform/eis_series.py though, does this depend on a patch somewhere. But after that it seems to work fine (and fast). 

Also, "F62" threw me for a bit, perhaps "F6sqare" or something like that would be better?


---

Comment by craigcitro created at 2008-10-30 21:30:20

This extra argument to `eisenstein_series_qexp` was in #4359 ... 

Yeah, I picked `F62` because it was `F_6^2` when I was writing it on paper ... should I add a comment in the code, or actually change the name?


---

Comment by robertwb created at 2008-10-30 21:36:31

OK, looks like #4359 got in, so that's good. 

I'd actually change the name of F62.


---

Attachment

New patch with the name changed.


---

Comment by robertwb created at 2008-10-30 21:46:19

Positive review. Very nice work :).


---

Comment by mabshoff created at 2008-10-31 01:03:16

Sorry, but

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.alpha1, Release Date: 2008-10-26                  |
| Type notebook() for the GUI, and license() for information.        |
sage: f = ModularForms(1,4).0
sage: time L = f.modform_lseries()
WARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field
WARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field
WARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field
WARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field
WARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field
WARNING: possible bug in q_expansion_basis for modular forms space Modular Forms space of dimension 1 for Congruence Subgroup Gamma0(1) of weight 4 over Rational Field
<SNIP potentially infinite repetition - I killed the process after 20 minutes CPU time>
```

This is on sage.math with my 3.2.alph2 merge tree. Other than the above problem all doctests passed.

Cheers,

Michael


---

Attachment


---

Comment by craigcitro created at 2008-10-31 03:24:14

Yep, I stupidly just ignored the `cusp_only` argument in the case where the space was one-dimensional. Attached patch fixes it.


---

Comment by mabshoff created at 2008-10-31 03:51:03

The second patch fixes the doctest issue. Positive review, but I would be happy if an expert took another look.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-31 03:53:43

Merged both patches in Sage 3.2.alpha2


---

Comment by mabshoff created at 2008-10-31 03:53:43

Resolution: fixed
