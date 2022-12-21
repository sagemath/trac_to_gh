# Issue 4990: [with code, needs work] Add code to compute Hilber class polynomials

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-17 08:47:24

Assignee: was

The attached Sage code has been written by

 * Eduardo Ocampo Alvarez
 * Andrey Timofeev

from the University of Essen in Germany. It needs some integration, but other than that it should be ready to be merged.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-17 08:47:51

This is the third verion of the code


---

Attachment

One thing that needs to be done is to convert everything to four spaces.


---

Comment by AlexGhitza created at 2009-01-23 07:07:31

Changing type from defect to enhancement.


---

Comment by AlexGhitza created at 2009-04-03 10:13:16

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2009-04-03 10:13:16

Changing keywords from "" to "hilbert class polynomial".


---

Comment by AlexGhitza created at 2009-04-03 10:13:16

Changing status from new to assigned.


---

Attachment

The attached patch adds the method `hilbert_class_polynomial()` to `NumberField_quadratic` and cleans the code up a little bit.

I cannot perform comparative timings since I don't have access to Magma at the moment.  Doing `%prun` with large discriminants indicates that the large majority of the time is spent in the Pari library computing the j-invariants of the representative tau's.  So I don't think rewriting the method in Cython will have a significant effect.

See also the discussion at

http://groups.google.com/group/sage-devel/browse_thread/thread/6c9aedf63106cc2d


---

Comment by cremona created at 2009-04-04 15:18:29

Alex, is your patch to be applied by itself, ignoring  the .txt file which it seems to be based on?  I assume so.  Is this intended to work on 3.4.1(.alpha0, say)?

John


---

Comment by AlexGhitza created at 2009-04-04 21:56:56

Yes: apply only the patch, to 3.4.1.alpha0.


---

Comment by ncalexan created at 2009-04-05 03:50:32

Looks good to me.  I tested it with the following script, and found a lot of curves with the correct endomorphism rings :)


```
K.<a> = QuadraticField(-34)
f = K.hilbert_class_polynomial()
assert K.class_number() == f.degree()

for P in K.primes_of_degree_one_list(20):
    p = P.norm()
    k = GF(p)
    rts = f.roots(k, multiplicities=False)
    for jj in rts:
        assert P.is_principal()
        E = EllipticCurve(jj)
        print E
        assert E.frobenius_order().number_field().is_isomorphic(K)
    if not rts:
        print "XXX", p
        assert not P.is_principal()
```



---

Comment by mabshoff created at 2009-04-05 23:16:17

Resolution: fixed


---

Comment by mabshoff created at 2009-04-05 23:16:17

Merged in Sage 3.4.1.rc1.

Cheers,

Michael


---

Comment by cremona created at 2009-04-20 12:44:33

Posted to sage-nt 2009-04-20:

Ticket #4990 implemented a hilbert_class_polynomial() method for
imaginary quadratic fields.  It is actually a function of the field's
discriminant, i.e. of a fundamental (negative) discriminant.  It was
written by      Eduardo Ocampo Alvarez and  Andrey Timofeev  from
Essen and is in sage/rings/number_field/number_field.py.

We also have a function in sage/schemes/elliptic_curves/cm.py called
hilbert_class_polynomial(D), which uses Magma to find more general
H.C.polys (D is any negative integer congruent to 0,1 mod 4).

For fundamental discriminants D, these give the same answer, i.e.
QuadraticField(D,'a').hilbert_class_polynomial() ==
hilbert_class_polynomial(D).

Question 1: does the code at #4990 (now merged actually work for
non-fundamental discriminants?  Someone might know;  testing it would
need a bit of coding, and I haven't done so.

Assuming that the answer is "yes",

Question 2: should we re-write the stand-alone function which takes as
its argument any negative discriminant (not necessarily fundamental)
and returns the appropriate H.C.poly, using the code now in
number_field.py instead of calling Magma;  and then change the current
method in number_field.py to just call that?  If so, where should the
stand-alone function go:  (a) where it now is, in
sage/schemes/elliptic_curves/cm.py, (b) in
sage/rings/number_field/somewhere, (c) somewhere else ?  We could then
also make the H.C.poly a function of (possibly non-maximal) orders in
(imaginary quadratic) number fields.

John

PS I found this out while converting cm.py to ReST for inclusion in
the manual.  Isn't it amazing what you find!
