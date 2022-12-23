# Issue 4835: pari starts up without inititializing enough primes?

Issue created by migration from https://trac.sagemath.org/ticket/4835

Original creator: cremona

Original creation time: 2008-12-20 12:05:51

Assignee: tbd

In 3.2.2, this looks ok:

```
sage: pari.default("primelimit")
500000
```

but nevertheless,

```
sage: K.<zeta>=CyclotomicField(23)
sage: K.ideal(2).factor()
...
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)
...
PariError: not enough precomputed primes, need primelimit ~  (35)
```




---

Comment by cremona created at 2008-12-20 12:52:24

I have narrowed it down to here:

```
sage: K.<z> = CyclotomicField(23)
sage: pK = K.pari_bnf(certify=False, units=True)
sage: pK.bnfcertify()

  ***   Warning: large Minkowski bound: certification will be VERY long.
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/home/john/sage-3.2.2.rc1/<ipython console> in <module>()

/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38663)()

PariError: not enough precomputed primes, need primelimit ~  (35)

sage: pari.default("primelimit")
500000
```

I uncommented line 6903 in sage/libs/pari/gen.pyx so I know that pari_init() was called with maxprime=500000 (the default) exactly once on startup and not again.  So the question in the ticket description seems to have a negative answer.

However in a gp session ("pari -gp", so the same version) I get:

```
? bnfcertify(bnfinit(polcyclo(23),1))
  *** bnfcertify: Warning: large Minkowski bound: certification will be VERY long.
  *** bnfcertify: not enough precomputed primes, need primelimit ~ 9324407.
```

so perhaps pari really cannot certify this field with having all primes up to 9.3 million, and the problem is that the error message report the wrong value for some reason when called from within Sage.  This is confirmed by continuing the above Sage session like this:

```
sage: pari.init_primes(10^7)
sage: pK.bnfcertify()
  ***   Warning: large Minkowski bound: certification will be VERY long.
```

followed by a long wait but no error message.


---

Comment by cremona created at 2008-12-20 16:35:30


```
sage: pari.init_primes(10^7)
sage: pK.bnfcertify()
  ***   Warning: large Minkowski bound: certification will be VERY long.
```

> followed by a long wait(*) but no error message.

3h 20m later:

```
1
```



---

Comment by AlexGhitza created at 2009-07-11 11:15:15

Changing component from algebra to interfaces.


---

Comment by AlexGhitza created at 2009-07-11 11:15:15

Changing assignee from tbd to was.


---

Comment by jdemeyer created at 2010-08-02 07:38:03

This issue does not appear anymore after upgrading PARI (ticket #9343), so I'm marking this invalid/duplicate/wontfix.


---

Comment by jdemeyer created at 2010-09-08 08:17:27

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-09-10 10:50:13

Resolution: duplicate
