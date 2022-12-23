# Issue 9506: include libSingular error messages in exceptions

Issue created by migration from https://trac.sagemath.org/ticket/9506

Original creator: malb

Original creation time: 2010-07-15 12:49:08

Assignee: AlexGhitza

Like this:




```
sage: P.<e,d,c,b,a> = PolynomialRing(QQ,5,order='lex')
sage: I = sage.rings.ideal.Cyclic(P)

sage: triangL = sage.libs.singular.ff.triang__lib.triangL
sage: _ = triangL(I)
Traceback (most recent call last):
...
RuntimeError: Error in Singular function call 'triangL':
 The input is no groebner basis.
 leaving triang.lib::triangL
```



---

Comment by malb created at 2010-07-15 12:50:22

Changing status from new to needs_work.


---

Comment by malb created at 2010-07-15 12:50:22

The attached patch requires #4499 and a patch to Singular available at http://www.singular.uni-kl.de:8002/trac/ticket/244 which will be available in the next Singular release.


---

Comment by malb created at 2010-07-15 12:51:05

Argh, that's  #9499 and not#4499.


---

Attachment

This patch depends on #8059.


---

Comment by malb created at 2010-07-20 09:08:55

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-07-20 09:27:27

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-07-20 09:27:27

Looks good.  And I reviewed this informally before when I stress tested it for my application and found it didn't work (for several iterations).  But I think this is good.


---

Comment by mpatel created at 2010-08-15 08:02:52

Resolution: fixed
