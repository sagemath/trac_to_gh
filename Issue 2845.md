# Issue 2845: [with patch, needs review] PolyBoRi assertion errror

Issue created by migration from https://trac.sagemath.org/ticket/2845

Original creator: malb

Original creation time: 2008-04-07 16:14:50

Assignee: malb

Apparently, PolyBoRi doesn't like to call `lmDeg` on a zero polynomial. The attached patch catches this.


---

Attachment


---

Comment by mabshoff created at 2008-04-07 16:35:21

Patch looks good. Do we already have a doctest for this?

Cheers,

Michael


---

Comment by malb created at 2008-04-07 19:58:50

Actually, I noticed because we have a doctest. I compiled PolyBoRi with debugging support and this triggered the assertion error when running the doctests.


---

Comment by mabshoff created at 2008-04-07 20:05:36

Replying to [comment:2 malb]:
> Actually, I noticed because we have a doctest. I compiled PolyBoRi with debugging support and this triggered the assertion error when running the doctests.

Hi malb,

I figured this was actually the case after thinking about this a little later, so I am merging this. No objections, positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-07 20:06:51

Resolution: fixed


---

Comment by mabshoff created at 2008-04-07 20:06:51

Merged in Sage 3.0.alpha3
