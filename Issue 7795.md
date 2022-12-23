# Issue 7795: MPolynomialRing segfaults when getting high exponents

archive/issues_007795.json:
```json
{
    "body": "Assignee: malb\n\nKeywords: MPolynomialRing_libsingular segfault with high exponents\n\nIn the following example, a segfault occurs. Shouldn't an error be raised instead?\n\n```\nsage: F.<a> = FiniteField(3)\nsage: P.<T,z> = PolynomialRing(F)\nsage: type(P)\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular'>\nsage: z^(3^10)\nz^59049\nsage: z^(3^11)\nz^177147\nsage: (z^3 + T*z)^(3^4)\nz^243 + T^81*z^81\nsage: (z^3 + T*z)^(3^7)\nz^6561 + T^2187*z^2187\nsage: (z^3 + T*z)^(3^10)\nz^177147 + T^59049*z^59049\nsage: (z^3 + T*z)^(3^15)\n/home/king/SAGE/sage-4.3/local/bin/sage-sage: line 206: 20938 Segmentation fault      sage-ipython \"$@\" -i\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7795\n\n",
    "created_at": "2009-12-30T11:05:21Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "MPolynomialRing segfaults when getting high exponents",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7795",
    "user": "SimonKing"
}
```
Assignee: malb

Keywords: MPolynomialRing_libsingular segfault with high exponents

In the following example, a segfault occurs. Shouldn't an error be raised instead?

```
sage: F.<a> = FiniteField(3)
sage: P.<T,z> = PolynomialRing(F)
sage: type(P)
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular'>
sage: z^(3^10)
z^59049
sage: z^(3^11)
z^177147
sage: (z^3 + T*z)^(3^4)
z^243 + T^81*z^81
sage: (z^3 + T*z)^(3^7)
z^6561 + T^2187*z^2187
sage: (z^3 + T*z)^(3^10)
z^177147 + T^59049*z^59049
sage: (z^3 + T*z)^(3^15)
/home/king/SAGE/sage-4.3/local/bin/sage-sage: line 206: 20938 Segmentation fault      sage-ipython "$@" -i
```



Issue created by migration from https://trac.sagemath.org/ticket/7795





---

archive/issue_comments_067300.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-14T21:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67300",
    "user": "malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067301.json:
```json
{
    "body": "The patch does not provide tests for the new functionality. Can these be added, please?\n\nAnyway. The patch applies, sage builds and starts. I'll now do `sage -testall`. Then I'll try some timings involving exponentiation and multiplication. And, unless Martin is quicker, I'll try to add doc tests.",
    "created_at": "2010-07-15T20:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67301",
    "user": "SimonKing"
}
```

The patch does not provide tests for the new functionality. Can these be added, please?

Anyway. The patch applies, sage builds and starts. I'll now do `sage -testall`. Then I'll try some timings involving exponentiation and multiplication. And, unless Martin is quicker, I'll try to add doc tests.



---

archive/issue_comments_067302.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-15T21:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67302",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067303.json:
```json
{
    "body": "I did `sage -tp 2 devel/sage` and obtained\n\n```\nThe following tests failed:\n\n        sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 1 doctests failed\n        sage -t  devel/sage/sage/rings/polynomial/laurent_polynomial_ring.py # 89 doctests failed\n        sage -t  devel/sage/sage/rings/polynomial/laurent_polynomial.pyx # 123 doctests failed\n        sage -t  devel/sage/sage/combinat/kazhdan_lusztig.py # 5 doctests failed\n        sage -t  devel/sage/sage/algebras/iwahori_hecke_algebra.py # 17 doctests failed\n```\n\n\nAt least in one case, it seems that in some places one needed to add further arguments to ring constructors.",
    "created_at": "2010-07-15T21:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67303",
    "user": "SimonKing"
}
```

I did `sage -tp 2 devel/sage` and obtained

```
The following tests failed:

        sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 1 doctests failed
        sage -t  devel/sage/sage/rings/polynomial/laurent_polynomial_ring.py # 89 doctests failed
        sage -t  devel/sage/sage/rings/polynomial/laurent_polynomial.pyx # 123 doctests failed
        sage -t  devel/sage/sage/combinat/kazhdan_lusztig.py # 5 doctests failed
        sage -t  devel/sage/sage/algebras/iwahori_hecke_algebra.py # 17 doctests failed
```


At least in one case, it seems that in some places one needed to add further arguments to ring constructors.



---

archive/issue_comments_067304.json:
```json
{
    "body": "Fixes all but one doctest failure.",
    "created_at": "2010-07-15T22:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67304",
    "user": "malb"
}
```

Fixes all but one doctest failure.



---

archive/issue_comments_067305.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-16T09:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67305",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067306.json:
```json
{
    "body": "Some random timings:\n\nWithout the patch\n\n```\nsage: R.<x,y,z> = GF(3)[]\nsage: p = R.random_element()\nsage: p\n-y^2 + x*z - z^2 - z\nsage: timeit('q=p^100')\n125 loops, best of 3: 6.24 ms per loop\n```\n\n\nWith the new patch and the same polynomial, I get:\n\n```\nsage: timeit('q=p^100')\n125 loops, best of 3: 2.99 ms per loop\n```\n\n\nSo, this is already good news!\n\nCriticism: The patch still does not provide doctests showing that the problem is fixed. I am now running doctests, and if they pass, I'll try to add a proper doctest via reviewer patch.",
    "created_at": "2010-07-21T14:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67306",
    "user": "SimonKing"
}
```

Some random timings:

Without the patch

```
sage: R.<x,y,z> = GF(3)[]
sage: p = R.random_element()
sage: p
-y^2 + x*z - z^2 - z
sage: timeit('q=p^100')
125 loops, best of 3: 6.24 ms per loop
```


With the new patch and the same polynomial, I get:

```
sage: timeit('q=p^100')
125 loops, best of 3: 2.99 ms per loop
```


So, this is already good news!

Criticism: The patch still does not provide doctests showing that the problem is fixed. I am now running doctests, and if they pass, I'll try to add a proper doctest via reviewer patch.



---

archive/issue_comments_067307.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-21T16:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67307",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067308.json:
```json
{
    "body": "The original problem -- namely the segfault when doing `(z^3 + T*z)<sup>(3</sup>15)` is not resolved. It segfaults, even with the patch.",
    "created_at": "2010-07-21T16:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67308",
    "user": "SimonKing"
}
```

The original problem -- namely the segfault when doing `(z^3 + T*z)<sup>(3</sup>15)` is not resolved. It segfaults, even with the patch.



---

archive/issue_comments_067309.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2012-03-24T14:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67309",
    "user": "malb"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_067310.json:
```json
{
    "body": "* I reported this bug upstream as it seems to be an upstream bug\n  * I deleted the attachment because I moved that code to #12718",
    "created_at": "2012-03-24T14:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67310",
    "user": "malb"
}
```

* I reported this bug upstream as it seems to be an upstream bug
  * I deleted the attachment because I moved that code to #12718



---

archive/issue_comments_067311.json:
```json
{
    "body": "Hans posted a fix here: https://groups.google.com/group/libsingular-devel/msg/39fe65f67ae44ca2?hl=en",
    "created_at": "2012-03-26T11:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67311",
    "user": "malb"
}
```

Hans posted a fix here: https://groups.google.com/group/libsingular-devel/msg/39fe65f67ae44ca2?hl=en



---

archive/issue_comments_067312.json:
```json
{
    "body": "Apparently, this bug is fixed in sage 5.5. I could run `(z^3 + T*z)<sup>(3</sup>15)` and it gives the expected answer (after... 9h of computation of a fast machine !). I thus suggest we close this ticket... I don't know how we could doctest that though without running a test for hours.",
    "created_at": "2012-12-30T17:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67312",
    "user": "Bouillaguet"
}
```

Apparently, this bug is fixed in sage 5.5. I could run `(z^3 + T*z)<sup>(3</sup>15)` and it gives the expected answer (after... 9h of computation of a fast machine !). I thus suggest we close this ticket... I don't know how we could doctest that though without running a test for hours.



---

archive/issue_comments_067313.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-12-30T17:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67313",
    "user": "Bouillaguet"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_067314.json:
```json
{
    "body": "NOTE : it worked on a 64-bit machine.",
    "created_at": "2012-12-31T10:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67314",
    "user": "Bouillaguet"
}
```

NOTE : it worked on a 64-bit machine.



---

archive/issue_comments_067315.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-04T16:55:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67315",
    "user": "Bouillaguet"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067316.json:
```json
{
    "body": "This cannot possibly be doctested, so we might as well close this.",
    "created_at": "2013-01-04T16:55:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67316",
    "user": "Bouillaguet"
}
```

This cannot possibly be doctested, so we might as well close this.



---

archive/issue_comments_067317.json:
```json
{
    "body": "In this case, please set the milestone to sage-duplicate/invalid/wontfix.",
    "created_at": "2013-01-04T20:43:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67317",
    "user": "jdemeyer"
}
```

In this case, please set the milestone to sage-duplicate/invalid/wontfix.



---

archive/issue_comments_067318.json:
```json
{
    "body": "Replying to [comment:13 Bouillaguet]:\n> This cannot possibly be doctested, so we might as well close this.\n\nI disagree, in two regards.\n\nFirst of all, if no error is raised and no crash occurs, then apparently the example is different. Could be a 32-bit versus 64-bit problem. Or not? I don't think that the problem I originally reported was 32 bit.\n\nSo, one should try to find an example in which a segfault used to occur, but an error is raised now. Can someone please test whether the following segfaults with sage-4.3?\n\n```\nsage: F.<a> = FiniteField(3)\nsage: P.<T,z> = PolynomialRing(F)\nsage: (T+z)^(5^15)\nTraceback (most recent call last):\n...\nOverflowError: Exponent overflow (30517578125).\n```\n\n\nIf that test segfaults in old Sage versions, then it is a valid test (in particular, those types of bugs *can* be tested against).\n\nSo, who has old Sage versions hanging around?",
    "created_at": "2013-01-04T21:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67318",
    "user": "SimonKing"
}
```

Replying to [comment:13 Bouillaguet]:
> This cannot possibly be doctested, so we might as well close this.

I disagree, in two regards.

First of all, if no error is raised and no crash occurs, then apparently the example is different. Could be a 32-bit versus 64-bit problem. Or not? I don't think that the problem I originally reported was 32 bit.

So, one should try to find an example in which a segfault used to occur, but an error is raised now. Can someone please test whether the following segfaults with sage-4.3?

```
sage: F.<a> = FiniteField(3)
sage: P.<T,z> = PolynomialRing(F)
sage: (T+z)^(5^15)
Traceback (most recent call last):
...
OverflowError: Exponent overflow (30517578125).
```


If that test segfaults in old Sage versions, then it is a valid test (in particular, those types of bugs *can* be tested against).

So, who has old Sage versions hanging around?



---

archive/issue_comments_067319.json:
```json
{
    "body": "Replying to [comment:15 SimonKing]:\n> So, who has old Sage versions hanging around?\n\nUnfortunately, with sage-4.7.beta1, the error is already raised (i.e., no segfault).",
    "created_at": "2013-01-04T21:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67319",
    "user": "SimonKing"
}
```

Replying to [comment:15 SimonKing]:
> So, who has old Sage versions hanging around?

Unfortunately, with sage-4.7.beta1, the error is already raised (i.e., no segfault).



---

archive/issue_comments_067320.json:
```json
{
    "body": "I am now building sage-3.4.1, from which I found the sources somewhere on my machines...",
    "created_at": "2013-01-04T22:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67320",
    "user": "SimonKing"
}
```

I am now building sage-3.4.1, from which I found the sources somewhere on my machines...



---

archive/issue_comments_067321.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2013-01-04T22:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67321",
    "user": "SimonKing"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_067322.json:
```json
{
    "body": "Replying to [comment:15 SimonKing]:\n> First of all, if no error is raised and no crash occurs, then apparently the example is different. \n\nI don't think so. My understanding is that the problem has been fixed inside [lib]singular. Testing this particular example is difficult because the computation takes many hours. It used to crash, but it now works.",
    "created_at": "2013-01-06T09:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67322",
    "user": "Bouillaguet"
}
```

Replying to [comment:15 SimonKing]:
> First of all, if no error is raised and no crash occurs, then apparently the example is different. 

I don't think so. My understanding is that the problem has been fixed inside [lib]singular. Testing this particular example is difficult because the computation takes many hours. It used to crash, but it now works.



---

archive/issue_comments_067323.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2014-03-16T08:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67323",
    "user": "rws"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_067324.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-16T09:16:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67324",
    "user": "mmezzarobba"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067325.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-03-19T04:36:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7795#issuecomment-67325",
    "user": "vbraun"
}
```

Resolution: fixed
