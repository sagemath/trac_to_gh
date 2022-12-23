# Issue 1482: xgcd suboptimal output

Issue created by migration from https://trac.sagemath.org/ticket/1482

Original creator: nbruin

Original creation time: 2007-12-12 20:36:50

Assignee: somebody

I was expecting xgcd(x,y) to produce u,v of minimal absolute value
such that u*x+v*y=gcd(x,y). However, presently it doesn't in the edge case where x divides y or vice versa (i.e., where (u,v)=(1,0) or (u,v)=(0,1) would be valid)

```
sage: xgcd(2,4)
(2, -1, 1)
sage: xgcd(4,2)
(2, 1, -1)
sage: xgcd(12,2)
(2, 1, -5)
```

This is not a bug in the strictest sense of the word, since the documentation does not promise u,v to be minimal, but for a lot of users minimal (u,v) would be the expected behaviour.

As far as I can see, this is directly the answer of mpz_gcdext.
Possible solutions:
 * fix mpz_gcdext
 * test in sage.rings.integer.Integer._xgcd if the gcd equals self.abs() or right.abs() and return (u,v)=(+-1,0) or (u,v)=(0,+-1) as appropriate (this is cython code
 * do this test in the python wrapper sage.rings.integer.Integer.xgcd instead.
Since xgcds are so crucial, I am hesitant to fix it myself. Can someone who knows the code well see what the appropriate solution is?



---

Comment by dmharvey created at 2007-12-22 15:35:52

I've started investigating. The issue is that since we included the fast gcd code of Niels Möller (see #424), the behaviour of `mpn_gcdext` has changed slightly, and the changes flows onto `mpz_gcdext`. Note that this is not a bug in the code, since neither the mpz nor mpn documentation claim any minimality condition on the cofactors.

Here is some mpn-level code which produces different answers under GMP 4.2.1 and the patched version:


```
   mp_limb_t s1p = 4;
   mp_limb_t s2p = 2;
   mp_limb_t r2p[2];
   mp_size_t r2n;
   mp_limb_t r1p[2];
   mp_size_t r1n;
   
   r1n = mpn_gcdext(r1p, r2p, &r2n, &s1p, 1, &s2p, 1);
   
   printf("first cofactor = %ld\n", (long)(r2p[0]) * ((r2n > 0) ? 1 : -1));
```


Vanilla GMP 4.2.1 prints -1, patched GMP prints 1.

I plan to fix this as follows. I think it would be good for Sage to guarantee minimality. I'm going to make the xgcd function call mpz_gcdext, then check for the "obvious" non-minimality issues and make corrections for those, and finally fall back on a (slower) but guaranteed algorithm if that doesn't work. Hopefully the latter should never actually be called, since it will need to divide by something somewhere.


---

Comment by dmharvey created at 2007-12-22 15:35:52

Changing assignee from somebody to dmharvey.


---

Comment by dmharvey created at 2007-12-22 15:35:52

Changing status from new to assigned.


---

Comment by was created at 2007-12-24 19:50:08

From Nils

```
I don't think anybody should care about the signs. Given the close
connection between continued fractions and Euclid's algorithm (which
does guarantee minimality), I guess you could try and see what signs
would be given back by a continued fractions approach.

It actually looks like they had a very good reason for departing from
returning minimal solutions in GMP's xgcd. It is nice to have an
option for minimality, but it should perhaps not be the default. The
way I ran into this problem was that I tested for one of the
parameters to be zero to detect if the gcd is equal to one of the
inputs. This example shows you're better off doing that by testing for
equality on the GCD and the inputs.

The "bug" should perhaps be the failure of the documentation to point
out that minimality is not guaranteed (people will naively expect
Euclid's algorithm)
```



---

Comment by dmharvey created at 2007-12-26 14:26:43

Earlier comments in the above thread:

http://groups.google.com/group/sage-devel/browse_thread/thread/26c80b8b90337a1a/90c60f2c0af4b105?lnk=gst&q=xgcd#90c60f2c0af4b105


---

Attachment


---

Comment by robertwb created at 2008-01-04 22:24:56

Interesting...

This looks good, and good documentation too.


---

Comment by mabshoff created at 2008-01-05 02:34:21

Resolution: fixed


---

Comment by mabshoff created at 2008-01-05 02:34:21

Merged in 2.9.2.rc1.
