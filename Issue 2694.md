# Issue 2694: Hecke algebra basis not implemented

Issue created by migration from Trac.

Original creator: syazdani

Original creation time: 2008-03-28 05:02:07

Assignee: craigcitro

Hecke algebra basis is not implemented.
here is how one can reproduce it:

```
sage: M=ModularSymbols(431,2,1)
sage: C=M.cuspidal_submodule()
sage: TT=C.hecke_algebra()
sage: TT.basis()
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/home/syazdani/sage-2.11.alpha1/<ipython console> in <module>()

/home/syazdani/sage/local/lib/python2.5/site-packages/sage/modular/hecke/algebra.py in basis(self)
    145
    146     def basis(self):
--> 147         raise NotImplementedError
    148
    149     def discriminant(self):

<type 'exceptions.NotImplementedError'>:
```




---

Comment by mabshoff created at 2008-07-31 03:33:49

Craig,

any progress here?

Cheers,

Michael


---

Comment by tscrim created at 2013-02-05 03:23:05

This works for me on `5.5.rc0`:

```
sage: M = ModularSymbols(431,2,1)
sage: C = M.cuspidal_submodule()
sage: TT = C.hecke_algebra()
sage: TT.basis()
[Hecke operator on Modular Symbols subspace of dimension 36 of Modular Symbols space of dimension 37 for Gamma_0(431) of weight 2 with sign 1 over Rational Field defined by:
...
36 x 36 dense matrix over Rational Field]
```



---

Comment by tscrim created at 2013-02-05 03:23:05

Changing status from new to needs_review.


---

Comment by cnassau created at 2013-02-12 09:27:00

It also works for me in 5.7.beta4 so I'm giving the `wontfix` a positive review.


---

Comment by cnassau created at 2013-02-12 09:27:00

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-02-17 20:08:12

Resolution: worksforme
