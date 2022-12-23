# Issue 1144: mpfr to RQDF coercion

Issue created by migration from https://trac.sagemath.org/ticket/1144

Original creator: zimmerma

Original creation time: 2007-11-11 13:09:12

Assignee: somebody

I do not understand the following in RQDF??:

        The rings that canonically coerce to the real quad double field are:
             * the mpfr real field, if its precision is at least 212 bits
                                                        <sup>^</sup><sup>^</sup><sup>^</sup><sup>^</sup><sup>^</sup>^^

On the contrary, RealField(p) should coerce to RQDF **exactly** for p <= 212 (in fact this
should be 215 = 53 + 1 + 53 + 1 + 53 + 1 + 53 since if you round to nearest, then the remainder
is smaller than 1/2 ulp of the most significant part).

Thus coercion from RealField() to RQDF should always work.





---

Comment by mabshoff created at 2007-11-11 14:14:19

Changing priority from minor to major.


---

Comment by mabshoff created at 2007-11-11 14:14:19

Changing assignee from somebody to cwitty.


---

Comment by cwitty created at 2007-11-15 02:46:38

This is the "canonical coercion", which is a somewhat different concept than coercion (the terminology is bad, and may change).

Canonical coercions are the coercions that Sage applies automatically, for instance when doing arithmetic.  If you try to add (or multiply, etc.) an element of A and an element of B, sage will look for a canonical coercion from A to B and a canonical coercion from B to A.  (Only one of these should exist.)  It will apply this coercion, and then do the arithmetic.

In general, the Sage policy is to prefer to throw away information, rather than make up information; so the product of an RR and an RQDF is an RR.

Explicit coercions are more general; for instance, both RR(RQDF(1)) and RQDF(RR(1)) work.

So the fact that the canonical coercions seem "backward" is by design.  However, the use of 212 instead of 215 does seem to be a bug.


---

Comment by robertwb created at 2007-12-04 08:07:15

Even if one can represent 215 bit numbers exactly with RDQF, the arithmetic it seems is only done to 212 bits of precision according to the documentation, so this would seem to be the correct bound. 

http://www.cs.berkeley.edu/~yozo/


---

Comment by mhansen created at 2007-12-06 21:01:28

Should this be marked as invalid then?


---

Comment by mhansen created at 2008-11-14 08:34:05

Since we are removing RQDF, I'm going to mark this as invalid.


---

Comment by mhansen created at 2008-11-14 08:34:05

Resolution: invalid
