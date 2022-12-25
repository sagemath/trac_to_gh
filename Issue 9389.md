# Issue 9389: sage crashing when computing local_data() for an EC

archive/issues_009389.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @williamstein cturner ylchapuy\n\nKeywords: segfault crash local_data\n\nIn 4.4.4 the following crashes Sage:\n\n```\nsage: K.<b3> = NumberField(x^6 + 15*x^4 + 2*x^3 + 156*x^2 - 48*x + 701)\nsage: E = EllipticCurve(K, [0, 1116/38413*b3^5+54/38413*b3^4+20460/38413*b3^3+3222/38413*b3^2+88752/38413*b3-34404/38413, 0, 54/38413*b3^5+3720/38413*b3^4+990/38413*b3^3+29895/38413*b3^2+19164/38413*b3+485313/38413, 0])\nsage: E.local_data()\n```\n\nBoom!\n\nIssue created by migration from https://trac.sagemath.org/ticket/9389\n\n",
    "created_at": "2010-06-30T03:26:30Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage crashing when computing local_data() for an EC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9389",
    "user": "https://github.com/arminstraub"
}
```
Assignee: @aghitza

CC:  @williamstein cturner ylchapuy

Keywords: segfault crash local_data

In 4.4.4 the following crashes Sage:

```
sage: K.<b3> = NumberField(x^6 + 15*x^4 + 2*x^3 + 156*x^2 - 48*x + 701)
sage: E = EllipticCurve(K, [0, 1116/38413*b3^5+54/38413*b3^4+20460/38413*b3^3+3222/38413*b3^2+88752/38413*b3-34404/38413, 0, 54/38413*b3^5+3720/38413*b3^4+990/38413*b3^3+29895/38413*b3^2+19164/38413*b3+485313/38413, 0])
sage: E.local_data()
```

Boom!

Issue created by migration from https://trac.sagemath.org/ticket/9389





---

archive/issue_comments_089228.json:
```json
{
    "body": "Changing assignee from @aghitza to @JohnCremona.",
    "created_at": "2010-06-30T03:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89228",
    "user": "https://github.com/arminstraub"
}
```

Changing assignee from @aghitza to @JohnCremona.



---

archive/issue_comments_089229.json:
```json
{
    "body": "Changing component from algebra to elliptic curves.",
    "created_at": "2010-06-30T03:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89229",
    "user": "https://github.com/arminstraub"
}
```

Changing component from algebra to elliptic curves.



---

archive/issue_comments_089230.json:
```json
{
    "body": "Can you see if it still crashes after applying the patch at #9266?",
    "created_at": "2010-06-30T11:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89230",
    "user": "https://github.com/JohnCremona"
}
```

Can you see if it still crashes after applying the patch at #9266?



---

archive/issue_comments_089231.json:
```json
{
    "body": "> Can you see if it still crashes after applying the patch at #9266?\n\n\nIt still crashes on my machine after applying the patch.",
    "created_at": "2010-06-30T15:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89231",
    "user": "https://github.com/arminstraub"
}
```

> Can you see if it still crashes after applying the patch at #9266?


It still crashes on my machine after applying the patch.



---

archive/issue_comments_089232.json:
```json
{
    "body": "More precisely, the verbose for the second example gives :\n\n```\nverbose 1 (568: ell_local_data.py, _tate) Running Tate's algorithm with P = Fractional ideal (3, 1/24*a^3 - 1/4*a^2 - 7/12*a + 3)                                         \n[...]\nverbose 1 (568: ell_local_data.py, _tate) P is not principal, uniformizer pi = 1/24*a^3 - 1/4*a^2 - 7/12*a + 3 (time = 0.174974)\nverbose 1 (627: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3\nverbose 1 (628: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3\nverbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3\nverbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3\nverbose 2 (568: ell_local_data.py, _tate) After first transform [1/2*a^3 + 1/2*a^2 + 1, 0, 1/2*a^3 + 1/2*a^2 + 1]\n, [a1,a2,a3,a4,a6] = [0, 3/2*a^3 + 3/2*a^2 + 3, a^3 + a^2 + 3, 51*a^3 + 552*a^2 - 486*a - 8019, 1797*a^3 + 4964*a^2 - 32562*a - 91701]\n, valuations = [+Infinity, 1, 1, 5, 2] (time = 2.197665)\nverbose 2 (568: ell_local_data.py, _tate) After second transform [0, 0, a^3 + a^2 + 3]\n[a1, a2, a3, a4, a6] = [0, 3/2*a^3 + 3/2*a^2 + 3, 3*a^3 + 3*a^2 + 9, 51*a^3 + 552*a^2 - 486*a - 8019, 1657*a^3 + 3488*a^2 - 31266*a - 70335]\nValuations: [+Infinity, 1, 2, 5, 3] (time = 2.211662)\nverbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3\nverbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3\nverbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3\nverbose 1 (568: ell_local_data.py, _tate) Analyzing roots of cubic T^3 + 7/18*a^3 + 3/4*a^2 + 1/18*a + 1/2*T^2 + 0*T + 23/36*a^3 + a^2 + 1/18*a + 1, case 1 (time = 2.285651)\nverbose 1 (568: ell_local_data.py, _tate) Distinct roots (time = 2.285651)\n/usr/local/sage/local/bin/sage-sage: line 206:  6216 Aborted                 sage-ipython \"$@\" -i\n```",
    "created_at": "2010-07-02T17:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89232",
    "user": "https://github.com/categorie"
}
```

More precisely, the verbose for the second example gives :

```
verbose 1 (568: ell_local_data.py, _tate) Running Tate's algorithm with P = Fractional ideal (3, 1/24*a^3 - 1/4*a^2 - 7/12*a + 3)                                         
[...]
verbose 1 (568: ell_local_data.py, _tate) P is not principal, uniformizer pi = 1/24*a^3 - 1/4*a^2 - 7/12*a + 3 (time = 0.174974)
verbose 1 (627: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3
verbose 1 (628: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3
verbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3
verbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3
verbose 2 (568: ell_local_data.py, _tate) After first transform [1/2*a^3 + 1/2*a^2 + 1, 0, 1/2*a^3 + 1/2*a^2 + 1]
, [a1,a2,a3,a4,a6] = [0, 3/2*a^3 + 3/2*a^2 + 3, a^3 + a^2 + 3, 51*a^3 + 552*a^2 - 486*a - 8019, 1797*a^3 + 4964*a^2 - 32562*a - 91701]
, valuations = [+Infinity, 1, 1, 5, 2] (time = 2.197665)
verbose 2 (568: ell_local_data.py, _tate) After second transform [0, 0, a^3 + a^2 + 3]
[a1, a2, a3, a4, a6] = [0, 3/2*a^3 + 3/2*a^2 + 3, 3*a^3 + 3*a^2 + 9, 51*a^3 + 552*a^2 - 486*a - 8019, 1657*a^3 + 3488*a^2 - 31266*a - 70335]
Valuations: [+Infinity, 1, 2, 5, 3] (time = 2.211662)
verbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3
verbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3
verbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3
verbose 1 (568: ell_local_data.py, _tate) Analyzing roots of cubic T^3 + 7/18*a^3 + 3/4*a^2 + 1/18*a + 1/2*T^2 + 0*T + 23/36*a^3 + a^2 + 1/18*a + 1, case 1 (time = 2.285651)
verbose 1 (568: ell_local_data.py, _tate) Distinct roots (time = 2.285651)
/usr/local/sage/local/bin/sage-sage: line 206:  6216 Aborted                 sage-ipython "$@" -i
```



---

archive/issue_comments_089233.json:
```json
{
    "body": "I checked and this actually doesn't have anything to do with elliptic curves; it's exposing a bug in residue fields of number field ideals. Some playing around with the Sage debugger reveals that the second example fails when trying to do the following:\n\n```\nsage: K.<a> = NumberField(x^4-32*x^2+324)                                                \nsage: I = K.ideal(3, 1/24*a^3 - 1/4*a^2 - 7/12*a + 3)\nsage: R = PolynomialRing(I.residue_field(), 'x')\nsage: R([23/36*a^3 + a^2 + 1/18*a + 1, 0, 7/18*a^3 + 3/4*a^2 + 1/18*a + 1/2, 1]) # boom!\n/storage/masiao/sage-4.5.alpha1/local/bin/sage-sage: line 206: 14086 Aborted                 sage-ipython \"$@\" -i\n```",
    "created_at": "2010-07-02T22:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89233",
    "user": "https://github.com/loefflerd"
}
```

I checked and this actually doesn't have anything to do with elliptic curves; it's exposing a bug in residue fields of number field ideals. Some playing around with the Sage debugger reveals that the second example fails when trying to do the following:

```
sage: K.<a> = NumberField(x^4-32*x^2+324)                                                
sage: I = K.ideal(3, 1/24*a^3 - 1/4*a^2 - 7/12*a + 3)
sage: R = PolynomialRing(I.residue_field(), 'x')
sage: R([23/36*a^3 + a^2 + 1/18*a + 1, 0, 7/18*a^3 + 3/4*a^2 + 1/18*a + 1/2, 1]) # boom!
/storage/masiao/sage-4.5.alpha1/local/bin/sage-sage: line 206: 14086 Aborted                 sage-ipython "$@" -i
```



---

archive/issue_comments_089234.json:
```json
{
    "body": "Changing assignee from @JohnCremona to @loefflerd.",
    "created_at": "2010-07-02T22:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89234",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @JohnCremona to @loefflerd.



---

archive/issue_comments_089235.json:
```json
{
    "body": "Changing component from elliptic curves to number fields.",
    "created_at": "2010-07-02T22:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89235",
    "user": "https://github.com/loefflerd"
}
```

Changing component from elliptic curves to number fields.



---

archive/issue_comments_089236.json:
```json
{
    "body": "Is someone working on this? Here is a trivial example in 4.5.3:\n\n```\nsage: K.<a> = QuadraticField(5)\nsage: E = EllipticCurve(K,[1,2*a])\nsage: E.local_data(K.ideal(2))\n```\n\nBoom. Similarly:\n\n```\nsage: K.<a> = QuadraticField(5)\nsage: R = PolynomialRing(K.ring_of_integers().residue_field(K.ideal(2)), 'x')\nsage: R([1/2*a])\n```",
    "created_at": "2010-10-27T08:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89236",
    "user": "https://trac.sagemath.org/admin/accounts/users/jgaski"
}
```

Is someone working on this? Here is a trivial example in 4.5.3:

```
sage: K.<a> = QuadraticField(5)
sage: E = EllipticCurve(K,[1,2*a])
sage: E.local_data(K.ideal(2))
```

Boom. Similarly:

```
sage: K.<a> = QuadraticField(5)
sage: R = PolynomialRing(K.ring_of_integers().residue_field(K.ideal(2)), 'x')
sage: R([1/2*a])
```



---

archive/issue_comments_089237.json:
```json
{
    "body": "I thought this had been fixed by #9315 which was merged in 4.6.alpha1, but it is not:\n\n```\nsage: version()\n'Sage Version 4.6.rc0, Release Date: 2010-10-21'\nsage: K.<a> = QuadraticField(5)\nsage: R = PolynomialRing(K.ring_of_integers().residue_field(K.ideal(2)), 'x')\nsage: R\nUnivariate Polynomial Ring in x over Residue field in abar of Fractional ideal (2)\nsage: R([1/2*a])\n/home/jec/sage-current/local/bin/sage-sage: line 217: 15900 Aborted                 sage-ipython \"$@\" -i\n```\nNow of course a/2 cannot be pushed into the residue field, as this (perfectly correct) behaviour shows:\n\n```\nsage: R(a/2)    \n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n...\nZeroDivisionError: Cannot reduce field element 1/2*a modulo Fractional ideal (2): it has negative valuation\n```\n\n I tried tracing this through and the crash happens here:\n\n```\n> /home/jec/sage-current/local/lib/python2.6/site-packages/sage/misc/classcall_metaclass.py(258)__call__()\n    257         elif hasattr(cls, \"__classcall__\"):\n--> 258             return cls.__classcall__(cls, *args, **options)\n```\nafter doing lots of stuff which seemed to have little to do with constructing a polynomial (element of R) out of a list of coefficients.\n\nI am CC'ing ylchapuy since I think the code where problems start is in polynomial_zz_pex.pyx which he wrote and which was put into 4.5.3 with #7841 (of which I was one reviewer...)",
    "created_at": "2010-10-27T16:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89237",
    "user": "https://github.com/JohnCremona"
}
```

I thought this had been fixed by #9315 which was merged in 4.6.alpha1, but it is not:

```
sage: version()
'Sage Version 4.6.rc0, Release Date: 2010-10-21'
sage: K.<a> = QuadraticField(5)
sage: R = PolynomialRing(K.ring_of_integers().residue_field(K.ideal(2)), 'x')
sage: R
Univariate Polynomial Ring in x over Residue field in abar of Fractional ideal (2)
sage: R([1/2*a])
/home/jec/sage-current/local/bin/sage-sage: line 217: 15900 Aborted                 sage-ipython "$@" -i
```
Now of course a/2 cannot be pushed into the residue field, as this (perfectly correct) behaviour shows:

```
sage: R(a/2)    
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
...
ZeroDivisionError: Cannot reduce field element 1/2*a modulo Fractional ideal (2): it has negative valuation
```

 I tried tracing this through and the crash happens here:

```
> /home/jec/sage-current/local/lib/python2.6/site-packages/sage/misc/classcall_metaclass.py(258)__call__()
    257         elif hasattr(cls, "__classcall__"):
--> 258             return cls.__classcall__(cls, *args, **options)
```
after doing lots of stuff which seemed to have little to do with constructing a polynomial (element of R) out of a list of coefficients.

I am CC'ing ylchapuy since I think the code where problems start is in polynomial_zz_pex.pyx which he wrote and which was put into 4.5.3 with #7841 (of which I was one reviewer...)



---

archive/issue_comments_089238.json:
```json
{
    "body": "Changing keywords from \"segfault crash local_data\" to \"segfault polynomial finite field\".",
    "created_at": "2010-10-27T16:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89238",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "segfault crash local_data" to "segfault polynomial finite field".



---

archive/issue_comments_089239.json:
```json
{
    "body": "NOTE:\n\nJohn, you are *definitely* right that the problem in polynomial coercion is caused by #7841, since by simply switching to not using NTL polynomials the proper behavior is restored:\n\n```\nsage: K.<a> = QuadraticField(5)\nsage: R = PolynomialRing(K.ideal(2).residue_field(), 'x', implementation='generic')\nsage: R([1/2*a])\n...\nTypeError\n```\n\nIf ylchapuy doesn't fix this soon, we could revert his PolynomialRing implementation for the next Sage release, if necessary....\nBut probably the fix isn't too hard (for him -- it might be very hard for me).",
    "created_at": "2010-10-27T22:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89239",
    "user": "https://github.com/williamstein"
}
```

NOTE:

John, you are *definitely* right that the problem in polynomial coercion is caused by #7841, since by simply switching to not using NTL polynomials the proper behavior is restored:

```
sage: K.<a> = QuadraticField(5)
sage: R = PolynomialRing(K.ideal(2).residue_field(), 'x', implementation='generic')
sage: R([1/2*a])
...
TypeError
```

If ylchapuy doesn't fix this soon, we could revert his PolynomialRing implementation for the next Sage release, if necessary....
But probably the fix isn't too hard (for him -- it might be very hard for me).



---

archive/issue_comments_089240.json:
```json
{
    "body": "In fact, after disabling the buggy ylchapuy code as follows, the original elliptic curve example works.\n\n1. The patch:\n\n```\n\ndiff -r b5dab6864f35 sage/rings/polynomial/polynomial_ring.py\n--- a/sage/rings/polynomial/polynomial_ring.py  Sat Sep 04 21:40:16 2010 -0700\n+++ b/sage/rings/polynomial/polynomial_ring.py  Wed Oct 27 15:50:43 2010 -0700\n@@ -1222,7 +1222,8 @@\n         \"\"\"\n         if implementation is None: implementation=\"NTL\"\n         from sage.rings.finite_rings.finite_field_base import is_FiniteField\n-        if implementation == \"NTL\" and is_FiniteField(base_ring):\n+        # this is buggy as a florida swamp -- see trac 9389\n+        if False and (implementation == \"NTL\" and is_FiniteField(base_ring)):\n             p=base_ring.characteristic()\n             from sage.libs.ntl.ntl_ZZ_pEContext import ntl_ZZ_pEContext\n             from sage.libs.ntl.ntl_ZZ_pX import ntl_ZZ_pX\n```\n\n2. The result with this patch:\n\n```\nsage: K.<a> = QuadraticField(5)\nsage: E = EllipticCurve(K,[1,2*a])\nsage: E.local_data(K.ideal(2))\nLocal data at Fractional ideal (2):\nReduction type: bad additive\nLocal minimal model: Elliptic Curve defined by y^2 = x^3 + x + 2*a over Number Field in a with defining polynomial x^2 - 5\nMinimal discriminant valuation: 9\nConductor exponent: 5\nKodaira Symbol: I0*\nTamagawa Number: 1\nsage: E.conductor()\nFractional ideal (544)\nsage: E.tamagawa_numbers()\n[1, 1]\n```",
    "created_at": "2010-10-27T22:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89240",
    "user": "https://github.com/williamstein"
}
```

In fact, after disabling the buggy ylchapuy code as follows, the original elliptic curve example works.

1. The patch:

```

diff -r b5dab6864f35 sage/rings/polynomial/polynomial_ring.py
--- a/sage/rings/polynomial/polynomial_ring.py  Sat Sep 04 21:40:16 2010 -0700
+++ b/sage/rings/polynomial/polynomial_ring.py  Wed Oct 27 15:50:43 2010 -0700
@@ -1222,7 +1222,8 @@
         """
         if implementation is None: implementation="NTL"
         from sage.rings.finite_rings.finite_field_base import is_FiniteField
-        if implementation == "NTL" and is_FiniteField(base_ring):
+        # this is buggy as a florida swamp -- see trac 9389
+        if False and (implementation == "NTL" and is_FiniteField(base_ring)):
             p=base_ring.characteristic()
             from sage.libs.ntl.ntl_ZZ_pEContext import ntl_ZZ_pEContext
             from sage.libs.ntl.ntl_ZZ_pX import ntl_ZZ_pX
```

2. The result with this patch:

```
sage: K.<a> = QuadraticField(5)
sage: E = EllipticCurve(K,[1,2*a])
sage: E.local_data(K.ideal(2))
Local data at Fractional ideal (2):
Reduction type: bad additive
Local minimal model: Elliptic Curve defined by y^2 = x^3 + x + 2*a over Number Field in a with defining polynomial x^2 - 5
Minimal discriminant valuation: 9
Conductor exponent: 5
Kodaira Symbol: I0*
Tamagawa Number: 1
sage: E.conductor()
Fractional ideal (544)
sage: E.tamagawa_numbers()
[1, 1]
```



---

archive/issue_comments_089241.json:
```json
{
    "body": "Good work!  Let's hope ylchapuy provides a fix;  otherwise this can be used as a workaround.",
    "created_at": "2010-10-28T08:38:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89241",
    "user": "https://github.com/JohnCremona"
}
```

Good work!  Let's hope ylchapuy provides a fix;  otherwise this can be used as a workaround.



---

archive/issue_comments_089242.json:
```json
{
    "body": "polynomial_zz_pex should not be used here.\n\n```\nis_FiniteField(base_ring):\n```\n\nmight be the wrong test because\n\n```\nsage: K.ideal(2).residue_field().is_finite()\nyes\n```\n\nWe should change the line \n\n```\nif implementation == \"NTL\" and is_FiniteField(base_ring):\n```\nto something appropriate, it should only be used for `PolynomialRing(GF(q))` I guess\n\nYann",
    "created_at": "2010-10-28T13:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89242",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

polynomial_zz_pex should not be used here.

```
is_FiniteField(base_ring):
```

might be the wrong test because

```
sage: K.ideal(2).residue_field().is_finite()
yes
```

We should change the line 

```
if implementation == "NTL" and is_FiniteField(base_ring):
```
to something appropriate, it should only be used for `PolynomialRing(GF(q))` I guess

Yann



---

archive/issue_comments_089243.json:
```json
{
    "body": "In fact those tests should probably go in `polynomial_ring_constructor.py`, in the _single_variate function. The init function for PolynomialRing_Field would then be the generic case.",
    "created_at": "2010-10-28T13:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89243",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

In fact those tests should probably go in `polynomial_ring_constructor.py`, in the _single_variate function. The init function for PolynomialRing_Field would then be the generic case.



---

archive/issue_comments_089244.json:
```json
{
    "body": "as a simple workaround, this solves the problem:\n\n```\ndiff -r 1b5dc2667b48 sage/rings/polynomial/polynomial_ring.py\n--- a/sage/rings/polynomial/polynomial_ring.py  Sat Oct 23 15:07:20 2010 +0200\n+++ b/sage/rings/polynomial/polynomial_ring.py  Thu Oct 28 15:53:58 2010 +0200\n@@ -1222,7 +1222,7 @@\n         \"\"\"\n         if implementation is None: implementation=\"NTL\"\n         from sage.rings.finite_rings.finite_field_base import is_FiniteField\n-        if implementation == \"NTL\" and is_FiniteField(base_ring):\n+        if implementation == \"NTL\" and is_FiniteField(base_ring) and not isinstance(base_ring, sage.rings.residue_field.ResidueField_generic):\n             p=base_ring.characteristic()\n             from sage.libs.ntl.ntl_ZZ_pEContext import ntl_ZZ_pEContext\n             from sage.libs.ntl.ntl_ZZ_pX import ntl_ZZ_pX\n```\n\nThough I must admit I don't know which difference between GF(4) and K.ideal(2).residue_field() makes everything go boom here.",
    "created_at": "2010-10-28T13:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89244",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

as a simple workaround, this solves the problem:

```
diff -r 1b5dc2667b48 sage/rings/polynomial/polynomial_ring.py
--- a/sage/rings/polynomial/polynomial_ring.py  Sat Oct 23 15:07:20 2010 +0200
+++ b/sage/rings/polynomial/polynomial_ring.py  Thu Oct 28 15:53:58 2010 +0200
@@ -1222,7 +1222,7 @@
         """
         if implementation is None: implementation="NTL"
         from sage.rings.finite_rings.finite_field_base import is_FiniteField
-        if implementation == "NTL" and is_FiniteField(base_ring):
+        if implementation == "NTL" and is_FiniteField(base_ring) and not isinstance(base_ring, sage.rings.residue_field.ResidueField_generic):
             p=base_ring.characteristic()
             from sage.libs.ntl.ntl_ZZ_pEContext import ntl_ZZ_pEContext
             from sage.libs.ntl.ntl_ZZ_pX import ntl_ZZ_pX
```

Though I must admit I don't know which difference between GF(4) and K.ideal(2).residue_field() makes everything go boom here.



---

archive/issue_comments_089245.json:
```json
{
    "body": "Works for me with sage-4.7.2.alpha3.",
    "created_at": "2011-10-09T11:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89245",
    "user": "https://github.com/jdemeyer"
}
```

Works for me with sage-4.7.2.alpha3.



---

archive/issue_comments_089246.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2011-10-09T11:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9389#issuecomment-89246",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_events_023166.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-09T11:11:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9389#event-23166"
}
```



---

archive/issue_events_023167.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-09T11:11:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9389",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9389#event-23167"
}
```
