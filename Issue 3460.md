# Issue 3460: [with patch, needs review] add power_basis() to number fields

Issue created by migration from https://trac.sagemath.org/ticket/3460

Original creator: ncalexan

Original creation time: 2008-06-18 03:40:55

Assignee: tbd

CC:  ccitro

Keywords: number field power basis

The patch describes it best.  Very useful.


---

Attachment

Mostly okay, couple of issues:

 * in the docstring, `t^d` should be `t^{d-1} `
 * shouldn't QQ get this method too? I suppose this is a more general problem, it's not just this method. Maybe that should be a different ticket.
 * the docstring is slightly ambiguous. "Return the power basis for this number field over its base field.": it's not "the" power basis, it's "a" power basis. Also, "and t is a root of f(x) in this field": it's not just any root, it's the root that's being used to represent the elements. Perhaps just merge these sentences.


---

Comment by mabshoff created at 2008-08-10 05:59:10

Merged in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-10 05:59:10

Resolution: fixed


---

Comment by mabshoff created at 2008-08-10 06:02:03

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-08-10 06:02:03

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-08-10 06:02:03

Oops, Nick will hopefully get the issues addressed before 3.1.alpha1, so that we can properly close this. 

Cheers,

Michael


---

Attachment

This addresses the comments about the docstring and adds the desired function to QQ.

It also addresses a bug in residue_field that I just noticed... sorry for the crosspost.


---

Attachment

Final patch fixes a one word type in the doctest :)

Hopefully it's good now.  All patches are "from scratch", i.e. apply only the last patch.


---

Comment by cremona created at 2008-08-10 19:18:30

Looks good to me.

Patch number 3 applies cleanly to 3.1.alpha0, and all tests in sage.rings pass.

I note that the implementation for QQ relies on its gen() being 1.  It might be safer to use self(1) instead.  But that's very minor.


---

Comment by mabshoff created at 2008-08-10 20:21:19

Merged 3460-ncalexan-nf-power-basis-3.patch in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-10 20:21:19

Resolution: fixed
