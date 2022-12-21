# Issue 4901: bug in elliptic logarithm

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-01-01 16:28:39

Assignee: was

CC:  alexghitza

Keywords: elliptic logarithm

#4214 introduced something which causes this example to fail:

```
sage: EllipticCurve("4390c2").gens()[0].elliptic_logarithm()
---------------------------------------------------------------------------
MemoryError                               Traceback (most recent call last)

/home/john/sage-3.2.2.rc1/devel/sage-elllog/<ipython console> in <module>()

/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_point.py in elliptic_logarithm(self, embedding, precision, algorithm)
   1211             E_pari = ER.pari_curve(prec=precision)
   1212             pt_pari = [pari(emb(self[0])), pari(emb(self[1]))]
-> 1213             log_pari = E_pari.ellpointtoz(pt_pari, precision=precision)
   1214             while prec_words_to_bits(log_pari.precision()) < precision:
   1215                 working_prec = 2*precision

/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38603)()

/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.PariInstance.allocatemem (sage/libs/pari/gen.c:34732)()

/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.init_stack (sage/libs/pari/gen.c:37647)()

MemoryError: Unable to allocate 4096000000 bytes memory for PARI.
```

caused by an infinite loop.

The problem has been diagnosed by me and Alex and I'll post a patch shortly.



---

Attachment


---

Comment by cremona created at 2009-01-01 18:42:49

The infinite loop was fixed by Alex, who then said

```
We seem to have run into a different problem, though:

sage: E = EllipticCurve("4390c2")
sage: P = E.gens()[0]
sage: P.elliptic_logarithm(precision=64)
0.000256387258865202254
sage: P.elliptic_logarithm(precision=65)
0.0002563872588652022535 + 0.004614954316673684681*I
sage: P.elliptic_logarithm(precision=128)
0.00025638725886520225353198932528666427412 + 0.0046149543166736846806755335569568366865*I
sage: P.elliptic_logarithm(precision=129)
0.00025638725886520225353198932528666427412
sage: P.elliptic_logarithm(precision=256)
0.0002563872588652022535319893252866642741168388008346370015005142128009610936373
sage: P.elliptic_logarithm(precision=257)
0.00025638725886520225353198932528666427411683880083463700150051421280096109363730 + 0.0046149543166736846806755335569568366865361459796795879146958143680521472570409*I

This is quite upsetting.
```

to which John replied

```
The explanation is that  0.004614954316673684681*I is the imaginary
period.  the point P is on the identity component so its e-log should
be a real multiple of the real period, but is obviously only
determined up to addition of any period.  Clearly the pari code does
not bother about that.

Here's one fix:  if P.is_on_identity_component(emb) is True then we
know that the result should be real, so we can kill the imaginary
part, and also normalise by making sure that the real part divided by
the real period is in [0,1).  That's not hard.  And if P is not on the
id. component, do the same but set the imaginary part to equal exactly
half the imaginary period.
```


The attached patch does both.  Based on 3.2.2, tested on 32-bit and 64-bit.


---

Comment by AlexGhitza created at 2009-01-03 17:55:43

Looks good.


---

Comment by mabshoff created at 2009-01-12 01:04:33

Merged in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-12 01:04:33

Resolution: fixed
