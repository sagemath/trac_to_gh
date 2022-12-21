# Issue 2281: elliptic_curve_finite_field: order caching problem

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-02-23 20:57:05

Assignee: was

The problem, caused by the patches to #1130, are that the cached field `elliptic_curve_finite_field.__order` which is python-mangled to `elliptic_curve_finite_field._elliptic_curve_finite_field_order`, was being accessed (and even set) by elements of the `EllipticCurvePoint_finite_field` class.

Solution: rename the field `_order` (with a single underscore) to show that it is intended to be private but can still be accessed easily by "friendly" classes which know what they are doing.

Patch (based on 2.10.2) to follow will address some other issues with `elliptic_curve_finite_field`


---

Attachment

Patch 8681.patch fixes this.  Most of the changes are dealing with the double/single underscore problem.  In addition, less use is made of pari/gp scripts for prime fields since the native code here handles more cases (larger primes), as in a new doctest which shows that we are closer to reasonable behaviour in cases such as in #351.  [The example in the doctest is a little smaller, but the example from #351 works fine in <5s).

The referee is welcome to ask for more detailed info.


---

Comment by mhansen created at 2008-02-28 00:21:21

Applies to 2.10.3.alpha0 and passes tests for me.


---

Comment by mabshoff created at 2008-02-28 00:30:20

Merged in Sage 2.10.3.rc0


---

Comment by mabshoff created at 2008-02-28 00:30:20

Resolution: fixed
