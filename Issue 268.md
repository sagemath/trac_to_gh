# Issue 268: IntegerMod sqrt() doesn't work for non-prime moduli

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-02-17 21:49:03

Assignee: somebody

This one's tricky; not sure the best way to proceed. The problem is that IntegerMod's `sqrt()` function uses PARI for the underlying functionality, but PARI doesn't work when the modulus is not a prime, even though you would hope it still works when the modulus is a _prime power_.

Relevant reading is the `sqrt` function at

http://www.skalatan.de/pariguide/doc/Transcendental_functions.html#sqrt

e.g. some weirdness:


```
sage: Mod(4, 5).sqrt()
 2

sage: Mod(4, 25).sqrt()
...
<type 'exceptions.ValueError'>: self must be a square.

sage: pari(Mod(4, 25)).sqrt()
...
<class 'gen.PariError'>:  (8)

sage: pari(Mod(4, 125)).sqrt()
...
<class 'gen.PariError'>: non quadratic residue in gsqrt (51)
```


It would be possible I guess to cast to a pari p-adic, but that would involve testing the modulus of the ring for being a prime power on every sqrt() invocation... seems horribly inefficient.



---

Comment by was created at 2007-08-18 18:11:55

It works now in age-2.8.1.


---

Comment by was created at 2007-08-18 18:11:55

Resolution: fixed
