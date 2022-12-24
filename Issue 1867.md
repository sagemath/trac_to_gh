# Issue 1867: suggested way to fix #1705 -- factoring multivariate polynomials over finite fields is broken in Singular

archive/issues_001867.json:
```json
{
    "body": "Assignee: malb\n\nThere is a standard algorithm to factor polynomials over a non-prime field that reduces the problem to factoring over a prime field and using gcd over the non-prime field.  It seems that gcd works fine over non-prime fields in Singular, as does factoring over prime fields, so this should work for us.   Probably singular doesn't do this because either it is slower or it is too much of a pain to implement in Singular (which isn't much of a language), or maybe they just don't care about this problem.\n\nAnyway, to start this off, here is a sample session that illustrates the idea:\n\n```\nsage: k.<a> = GF(9)\nsage: R.<x,y> = PolynomialRing(k)\nsage: f = (x-a)*(y-a)\nsage: f.factor()\nTraceback (most recent call last):\n...\nNotImplementedError: factorization of multivariate polynomials over non-prime fields explicitly disabled due to bugs in Singular\nsage: singular(f)\nsage: x*y+(-a)*x+(-a)*y+(a+1)\nx*y + ( - a)*x + ( - a)*y + (a + 1)\nsage: singular(f).factorH()\n[1]:\n   _[1]=1\n   _[2]=x*y+(-a)*x+(-a)*y+(a+1)\n[2]:\n   1,1\nsage: g = f*(x-a^3)*(y-a^3); g\nx^2*y^2 - x^2*y - x*y^2 - x^2 + x*y - y^2 + x + y + 1\nsage: gg = GF(3)['x,y'](repr(g))    # why doesn't change ring or coerce work\nsage: F = gg.factor()\nsage: factor1 = R(F[0][0])\nsage: factor2 = R(F[1][0])\nsage: factor1.gcd(f)\n(a)*y + ( - a - 1)\nsage: factor2.gcd(f)\n(a)*x + ( - a - 1)\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1867\n\n",
    "created_at": "2008-01-20T16:50:41Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "suggested way to fix #1705 -- factoring multivariate polynomials over finite fields is broken in Singular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1867",
    "user": "was"
}
```
Assignee: malb

There is a standard algorithm to factor polynomials over a non-prime field that reduces the problem to factoring over a prime field and using gcd over the non-prime field.  It seems that gcd works fine over non-prime fields in Singular, as does factoring over prime fields, so this should work for us.   Probably singular doesn't do this because either it is slower or it is too much of a pain to implement in Singular (which isn't much of a language), or maybe they just don't care about this problem.

Anyway, to start this off, here is a sample session that illustrates the idea:

```
sage: k.<a> = GF(9)
sage: R.<x,y> = PolynomialRing(k)
sage: f = (x-a)*(y-a)
sage: f.factor()
Traceback (most recent call last):
...
NotImplementedError: factorization of multivariate polynomials over non-prime fields explicitly disabled due to bugs in Singular
sage: singular(f)
sage: x*y+(-a)*x+(-a)*y+(a+1)
x*y + ( - a)*x + ( - a)*y + (a + 1)
sage: singular(f).factorH()
[1]:
   _[1]=1
   _[2]=x*y+(-a)*x+(-a)*y+(a+1)
[2]:
   1,1
sage: g = f*(x-a^3)*(y-a^3); g
x^2*y^2 - x^2*y - x*y^2 - x^2 + x*y - y^2 + x + y + 1
sage: gg = GF(3)['x,y'](repr(g))    # why doesn't change ring or coerce work
sage: F = gg.factor()
sage: factor1 = R(F[0][0])
sage: factor2 = R(F[1][0])
sage: factor1.gcd(f)
(a)*y + ( - a - 1)
sage: factor2.gcd(f)
(a)*x + ( - a - 1)

```


Issue created by migration from https://trac.sagemath.org/ticket/1867





---

archive/issue_comments_011820.json:
```json
{
    "body": "Change ring being broken, e.g.,\n\n\n```\ng.change_ring(GF(3))\n```\n\n\nin the above example, is now trac #5068.",
    "created_at": "2009-01-23T10:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1867#issuecomment-11820",
    "user": "was"
}
```

Change ring being broken, e.g.,


```
g.change_ring(GF(3))
```


in the above example, is now trac #5068.



---

archive/issue_comments_011821.json:
```json
{
    "body": "I have attached a patch that:\n\n* fully implements this idea.  This works with dramatically higher probability than singular itself.  Singular usually gives wrong answers, whereas with this code it seems right \"about 99% of the time\".  E.g., this runs for a long time before finding a problem:\n\n```\nk.<a> = GF(3^2); R.<x,y> = PolynomialRing(k)\nfor i in range(500):\n    v = [R.random_element() for _ in range(3)]; print i; assert prod(v).factor(proof=False).prod() == prod(v)\n\n1\n...\n328\nboom!\nAssertionError: bug in Singular factoring an auxiliary polynomial over GF(p): bad multiplicity (1, 2)\n```\n\n\nand\n\n\n\n* found bugs in factorization over GF(p) -- see ticket #5068.  Added a proof flag, and *only* allow factoring if proof=False.\n\nI think this should go into sage because: \n1. It works massively better than singular currently does over GF(q).\n2. Even if singular does fix say factoring, maybe they will only fix GF(p) factorization and not GF(p^e).  Then this code will make factoring over GF(p^e) work too.\n3. If we ever implement our own factorization then this code means we only have to implement GF(p), at least for starters.  It would be very nice if we at least had *some* implementation that works, even if is slow.\n4. This patch adds some useful functions such as map_coefficients (which has the same api as the corresponding function in sage-combinat), and _norm_over_nonprime_finite_field. \n\n\n---\n\nTEST CODE:\n\n\n```\nk.<a> = GF(3^5); R.<x,y> = PolynomialRing(k)\nfor i in range(100):\n    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)\n#good\n\n\nk.<a> = GF(997^2); R.<x,y> = PolynomialRing(k)\nfor i in range(100):\n    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)\n#good\n\n\nk.<a> = GF(4); R.<x,y,z> = PolynomialRing(k)\nfor i in range(100):\n    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)\n\n# HORRIBLE: \nsage: k.<a> = GF(4); R.<x,y,z> = PolynomialRing(k)\nsage: for i in range(100):\n....:         v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)\n....: \n0\n1\n...\n30\nconvertFacCF2NTLGF2X: coefficient not immidiate!\n[immediately exits sage!]\n\n\nk.<a> = GF(7^2); R.<x,y> = PolynomialRing(k)\nfor i in range(100):\n    v = [R.random_element() for _ in range(3)]; print i; assert prod(v).factor(False).prod() == prod(v)\n#good\n\n\nk.<a> = GF(7^2); R.<x,y,z> = PolynomialRing(k)\nfor i in range(100):\n    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)\n#good\n\nk.<a> = GF(3^6); R.<x,y> = PolynomialRing(k)\nfor i in range(100):\n    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)\n#good\n\n```\n",
    "created_at": "2009-01-23T15:38:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1867#issuecomment-11821",
    "user": "was"
}
```

I have attached a patch that:

* fully implements this idea.  This works with dramatically higher probability than singular itself.  Singular usually gives wrong answers, whereas with this code it seems right "about 99% of the time".  E.g., this runs for a long time before finding a problem:

```
k.<a> = GF(3^2); R.<x,y> = PolynomialRing(k)
for i in range(500):
    v = [R.random_element() for _ in range(3)]; print i; assert prod(v).factor(proof=False).prod() == prod(v)

1
...
328
boom!
AssertionError: bug in Singular factoring an auxiliary polynomial over GF(p): bad multiplicity (1, 2)
```


and



* found bugs in factorization over GF(p) -- see ticket #5068.  Added a proof flag, and *only* allow factoring if proof=False.

I think this should go into sage because: 
1. It works massively better than singular currently does over GF(q).
2. Even if singular does fix say factoring, maybe they will only fix GF(p) factorization and not GF(p^e).  Then this code will make factoring over GF(p^e) work too.
3. If we ever implement our own factorization then this code means we only have to implement GF(p), at least for starters.  It would be very nice if we at least had *some* implementation that works, even if is slow.
4. This patch adds some useful functions such as map_coefficients (which has the same api as the corresponding function in sage-combinat), and _norm_over_nonprime_finite_field. 


---

TEST CODE:


```
k.<a> = GF(3^5); R.<x,y> = PolynomialRing(k)
for i in range(100):
    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)
#good


k.<a> = GF(997^2); R.<x,y> = PolynomialRing(k)
for i in range(100):
    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)
#good


k.<a> = GF(4); R.<x,y,z> = PolynomialRing(k)
for i in range(100):
    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)

# HORRIBLE: 
sage: k.<a> = GF(4); R.<x,y,z> = PolynomialRing(k)
sage: for i in range(100):
....:         v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)
....: 
0
1
...
30
convertFacCF2NTLGF2X: coefficient not immidiate!
[immediately exits sage!]


k.<a> = GF(7^2); R.<x,y> = PolynomialRing(k)
for i in range(100):
    v = [R.random_element() for _ in range(3)]; print i; assert prod(v).factor(False).prod() == prod(v)
#good


k.<a> = GF(7^2); R.<x,y,z> = PolynomialRing(k)
for i in range(100):
    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)
#good

k.<a> = GF(3^6); R.<x,y> = PolynomialRing(k)
for i in range(100):
    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)
#good

```




---

archive/issue_comments_011822.json:
```json
{
    "body": "Attachment [trac_1867.patch](tarball://root/attachments/some-uuid/ticket1867/trac_1867.patch) by was created at 2009-01-23 15:51:51",
    "created_at": "2009-01-23T15:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1867#issuecomment-11822",
    "user": "was"
}
```

Attachment [trac_1867.patch](tarball://root/attachments/some-uuid/ticket1867/trac_1867.patch) by was created at 2009-01-23 15:51:51



---

archive/issue_comments_011823.json:
```json
{
    "body": "Almost, but \n\n```\n\tsage -t  \"devel/sage-dev1/sage/rings/polynomial/multi_polynomial_libsingular.pyx\"\n```\n\nfails a few doctests when I try it because of missing `proof=False` arguments. See lines 3432, 3461, 3491, 3502.",
    "created_at": "2009-01-24T04:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1867#issuecomment-11823",
    "user": "kedlaya"
}
```

Almost, but 

```
	sage -t  "devel/sage-dev1/sage/rings/polynomial/multi_polynomial_libsingular.pyx"
```

fails a few doctests when I try it because of missing `proof=False` arguments. See lines 3432, 3461, 3491, 3502.



---

archive/issue_comments_011824.json:
```json
{
    "body": "Attachment [trac_1867-part2.patch](tarball://root/attachments/some-uuid/ticket1867/trac_1867-part2.patch) by was created at 2009-01-24 06:43:33\n\nthis fixes the other problems in the doctests",
    "created_at": "2009-01-24T06:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1867#issuecomment-11824",
    "user": "was"
}
```

Attachment [trac_1867-part2.patch](tarball://root/attachments/some-uuid/ticket1867/trac_1867-part2.patch) by was created at 2009-01-24 06:43:33

this fixes the other problems in the doctests



---

archive/issue_comments_011825.json:
```json
{
    "body": "NOTE (from Noam Elkies):\n\nMaxima can factor multivariate polynomials mod p.  However it sometimes will fail, as the example below illustrates. \n\n\n```\nsage: R.<x,y> = GF(5)[]\n\nsage: f = 2*x^2*y^2 + 2*y^4 + x^3 - 2*x^2*y + x*y^2 + y^3 + x^2 - x*y - y^2 - 2*x - 2*y - 2\n\nsage: maxima.eval('modulus:5')\nsage: maxima(f).factor()\nNot enough choices for substitution.\n```\n\n\nThis is a known issue.",
    "created_at": "2009-01-24T07:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1867#issuecomment-11825",
    "user": "was"
}
```

NOTE (from Noam Elkies):

Maxima can factor multivariate polynomials mod p.  However it sometimes will fail, as the example below illustrates. 


```
sage: R.<x,y> = GF(5)[]

sage: f = 2*x^2*y^2 + 2*y^4 + x^3 - 2*x^2*y + x*y^2 + y^3 + x^2 - x*y - y^2 - 2*x - 2*y - 2

sage: maxima.eval('modulus:5')
sage: maxima(f).factor()
Not enough choices for substitution.
```


This is a known issue.



---

archive/issue_comments_011826.json:
```json
{
    "body": "All doctests pass now. Positive review.",
    "created_at": "2009-01-24T14:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1867#issuecomment-11826",
    "user": "kedlaya"
}
```

All doctests pass now. Positive review.



---

archive/issue_comments_011827.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T20:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1867#issuecomment-11827",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_011828.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-25T20:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1867#issuecomment-11828",
    "user": "mabshoff"
}
```

Resolution: fixed
