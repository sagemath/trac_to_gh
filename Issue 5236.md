# Issue 5236: x^(-pm) in ramified extensions of Qp

Issue created by migration from https://trac.sagemath.org/ticket/5236

Original creator: roed

Original creation time: 2009-02-11 21:46:13

Assignee: roed

This is probably a problem with some of the shifting code in pow_computer_ext, since it only occurs when raising an element to a power that's a negative multiple of p.  pow_computer_ext needs cleaning up and doctesting anyway.

```
sage: W.<w> = Qp(5,6).ext(x^2+5)
sage: (5+w)^-4
w^-4 + 4*w^-3 + 3 + 2*w + 3*w^2 + 3*w^5 + w^6 + O(w^8)
sage: (5+w)^-5
RuntimeError: ZZ_p: division by non-invertible element
sage: W(5)^-5
4*w^-10 + w^-8 + O(w^2)
sage: w^-5
w^-5 + O(w^7)
sage: (1+w)^-5
RuntimeError: ZZ_p: division by non-invertible element
sage: (1+w)^5
1 + 4*w^3 + 3*w^4 + O(w^12)
sage: (1+w)^-7
1 + 3*w + 3*w^2 + 3*w^3 + 3*w^6 + 3*w^7 + 2*w^8 + w^9 + 3*w^10 + O(w^12)
sage: (1+w)^-10
RuntimeError: ZZ_p: division by non-invertible element
```



---

Comment by roed created at 2009-02-11 21:46:40

Changing keywords from "" to "padics, exponentiation".


---

Comment by roed created at 2009-02-13 05:18:28

The problem is just in the exponentiation code.  I need to use my own newton's method inverse (in ntl_wrap.cpp) rather than NTL's InvMod.  A bit annoying: I don't really know what the relative speeds are.  But it should produce the correct answer at least.


---

Comment by kedlaya created at 2009-03-17 03:21:58

Looks good, applies against 3.4, passes doctests, and withstands some additional poking. Positive review.


---

Comment by roed created at 2009-03-17 09:00:09

I found another case of this, for capped absolute extensions.


---

Comment by roed created at 2009-04-25 07:50:56

Rebased against 5778.


---

Attachment


---

Comment by mabshoff created at 2009-04-26 19:56:29

Changing component from basic arithmetic to padics.


---

Comment by roed created at 2009-05-11 09:26:28

Includes commit message, rebased against 3.4.2 and #5778.


---

Attachment

Applies against 4.0alpha0, passes all doctests, looks reasonable to me. Positive review.


---

Comment by mabshoff created at 2009-05-19 17:00:56

Resolution: fixed


---

Comment by mabshoff created at 2009-05-19 17:00:56

Merged trac5236.2.patch in Sage 4.0.rc0.

Cheers,

Michael
