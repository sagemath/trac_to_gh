# Issue 5242: [with patch, needs review] generic_power can now handle semi-groups

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-02-12 13:20:31

Assignee: tbd

CC:  sage-combinat

Keywords: generic power

The former implementation of generic_power_c made two assumptions
 - `not a` is well defined for any element a
 - There is a one
These two assumptions do not always always hold. So I reorganized the initial code which handle particular cases so that:
 - it does not call "not a" when the exponent n is different from zero
 - it delegates to ~a the responsability of raising an error when the exponent n is negative and a is not invertible. This allows for monoids with partialy defined inversion (e.g. the multiplicative monoid of Z/12Z).

This modification revealed a problem in matrices: the empty matrix 0x0 modulo 2 was tested to be non invertible! I changed the test to the correct value. 

Investigating this revealled many other inconsistencies with matrices; those will
be taken care of in a subsequent patch.


---

Comment by hivert created at 2009-02-12 13:27:53

Proposal of patch for generic power


---

Attachment


---

Comment by hivert created at 2009-02-13 18:52:23

Changing assignee from tbd to hivert.


---

Comment by hivert created at 2009-02-13 18:52:23

Changing status from new to assigned.


---

Comment by cremona created at 2009-02-14 14:42:11

I would prefer not to have implicit casting of general types to booleans.  Can we not have "if n==0" or "if n.is_zero()" instead of "if not n", and similar?  Remember that Sage code is all visible to users, so we should avoid obscure programming idioms.


---

Comment by hivert created at 2009-02-14 15:39:05

Replying to [comment:5 cremona]:
Yes Sure. I more than agree with you. Remember that I didn't wrote this code, I just reorganize the order in which the tests are done. I'll soon propose another patch with a better idiom.


---

Comment by hivert created at 2009-02-14 15:59:44

Replying to [comment:5 cremona]:
Actually it seems that for n it is possible because we know its type. On the contrary it is not possible for a. Indeed a can be a plain Python int (wich forbid the use of `a.is_zero()`) of any type eg polynomial with forbid the use of `== 0` so I don't know what else to do (I'm far from being a cython expert) :

```
 sage -t  "devel/sage-combinat/sage/rings/polynomial/polydict.pyx"
**********************************************************************
File "/usr/local/sage/devel/sage-combinat/sage/rings/polynomial/polydict.pyx", line 695:
    sage: (f-f)**0
Expected:
    Traceback (most recent call last):
    ...
    ArithmeticError: 0^0 is undefined.
Got:
    PolyDict with representation {0: 1}
```


So if there is no better suggestion I'll stick with the current patch.


---

Comment by mabshoff created at 2009-02-14 16:19:18

I just tested my current 3.3.rc1 merge tree with this patch and

```
All tests passed!
```


Cheers,

Michael


---

Comment by malb created at 2009-02-14 17:15:08

Patch reads good, I suggest to open another ticket for the style issue.


---

Comment by mabshoff created at 2009-02-15 07:17:26

Merged in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-15 07:17:26

Resolution: fixed
