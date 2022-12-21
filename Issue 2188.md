# Issue 2188: mathematically senseless bit-shift operations in integer_mod.pyx

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-02-17 05:45:40

Assignee: cwitty

The current bit-shift operations are straight wrappers for the C bit-shift operators, which means that they are architecture-specific and mathematically very strange.  For instance, currently, on 32-bit x86 with a smallish modulus, `mod(a,n)<<s` evaluates to `mod((a<<(s%32))%2^32%n, n)`.

William, Robert Bradshaw, and I decided on IRC that the best we can do for bit-shift is this:
if 0<=a<n, then mod(a,n)<<s == mod(a<<s,n); and similarly for right-shift.


---

Comment by spancratz created at 2010-01-16 08:06:21

Resolution: invalid


---

Comment by spancratz created at 2010-01-16 08:06:21

The bit-shift method uses the GMP function ``mpz_mul_2exp``, thus this ticket is no longer valid.
