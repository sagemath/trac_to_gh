# Issue 3556: [with patch, needs review] Bug in IntegerModRing(n) for very large n

Issue created by migration from https://trac.sagemath.org/ticket/3556

Original creator: craigcitro

Original creation time: 2008-07-06 01:20:25

Assignee: craigcitro

Notice the following:


```
sage: IntegerModRing(next_prime(10^30)).unit_gens()
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

/home/craigcitro/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/rings/integer_mod_ring.py in unit_gens(self)
    780             m = n/(p**r)
    781             for g in self.__unit_gens_primepowercase(p, r):
--> 782                 x = g.crt(integer_mod.Mod(1,m))
    783                 self.__unit_gens.append(x)
    784         return self.__unit_gens

/home/craigcitro/integer_mod.pyx in sage.rings.integer_mod.IntegerMod_abstract.crt (sage/rings/integer_mod.c:7044)()

/home/craigcitro/integer_mod.pyx in sage.rings.integer_mod.IntegerMod_gmp.__crt (sage/rings/integer_mod.c:8578)()

ZeroDivisionError: moduli must be coprime
sage: 
```


The issue is that `crt` doesn't play well when one of the moduli is 1. The attached patch fixes it, and adds a few doctests.


---

Attachment


---

Comment by mabshoff created at 2008-07-06 18:42:15

Merged in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-06 18:42:15

Resolution: fixed
