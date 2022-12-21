# Issue 4218: Extensions of Finite Fields don't work well

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2008-09-29 20:21:44

Assignee: tbd

The following sage snippets show (some of) the problems.  First, we set
the stage:

```
sage: F1.<a> = GF(2^7)
sage: P1.<x>=PolynomialRing(F1)
sage: f=x^2+x+F1(1)
sage: F2=F1.extension(f,'u')
sage: F2
Univariate Quotient Polynomial Ring in u over Finite Field in a of size 2^7 with modulus u^2 + u + 1
sage: a in F2
True
```


First problem:

```
sage: for i in xrange(100):
   ....:         r = F2.random_element()
   ....:     if r != F2(0) and r != F2(1):
   ....:             print "Yoicks! r=%s"%r
   ....: 
sage: 
```

No output means that 100 random elements of F2 are either
0 or 1, which seems somehow incorrect.

The next oddity is

```
sage: F1.order()
128
sage: F2.order()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/SandBox/Justin/sb/sage-3.1.1/<ipython console> in <module>()

/SandBox/Justin/sb/sage-3.1.1/ring.pyx in sage.rings.ring.Ring.order (sage/rings/ring.c:4108)()

NotImplementedError: 
```

Shouldn't .order() work for extensions as well as those directly defined?




---

Comment by mabshoff created at 2008-10-02 03:41:14

Justin,

please remember to assign a milestone to tickets you open :)

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-10-04 10:21:55

Changing assignee from tbd to AlexGhitza.


---

Comment by AlexGhitza created at 2008-10-04 10:22:05

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2008-12-20 18:20:04

The attached patch resolves the issues reported above, by implementing methods random_element() and order() for quotients of polynomial rings.


---

Attachment

Positive review.  Patch applies cleanly to 3.2.2 and doctests in sage/rings/polynomial pass.

I did notice while testing that this does not work:

```
sage: R.<x>=ZZ[]
sage: S=ZZ.extension(x^3-2,'a')
sage: S.order()
---------------------------------------------------------------------------
NotImplementedError    
```

and also that `S.random_element()` gives a random integer (I think).  Another ticket perhaps?


---

Comment by mabshoff created at 2008-12-21 22:39:46

Resolution: fixed


---

Comment by mabshoff created at 2008-12-21 22:39:46

Merged in Sage 3.2.3.alpha0
