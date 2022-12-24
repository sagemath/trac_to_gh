# Issue 6218: small changes to jacobian_morphism to make hyperelliptic curve arithmetic faster

archive/issues_006218.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @craigcitro\n\nKeywords: jacobian morphism hyperelliptic curve speed profile time\n\nThe attached patch uses % instead of the generic mod and avoids creating polynomial rings.  The savings are significant:\n\n\n```\nsage: F = GF(next_prime(10^30))\nsage: x = F['x'].gen()\nsage: f = x^7 + x^2 + 1\nsage: H = HyperellipticCurve(f, 2*x); H\nHyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1\nsage: J = H.jacobian()(F); J\nverbose 0 (902: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.\nSet of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057\nsage: Q = J(H.lift_x(F(1))); Q\n(x + 1000000000000000000000000000056, y + 1000000000000000000000000000056)\n```\n\n\nBefore:\n\n```\nsage: %time ZZ.random_element(10**10) * Q\nCPU times: user 0.91 s, sys: 0.02 s, total: 0.93 s\nWall time: 0.93 s\n(x^3 + 402198643461859040647192719684*x^2 + 601836335767969290835741174254*x + 16518729356967251698882316239, y + 473734498489001855322294293716*x^2 + 971294794490578173226993121181*x + 205331062061696832607472618253)\n\nsage: %timeit ZZ.random_element(10**10) * Q\n10 loops, best of 3: 980 ms per loop\n```\n\n\nAfter:\n\n```\nsage: %time ZZ.random_element(10^10) * Q\nCPU times: user 0.22 s, sys: 0.01 s, total: 0.23 s\nWall time: 0.25 s\n(x^3 + 275125861943108889646384133572*x^2 + 753495481691507497462095614898*x + 60041420316935318537784907957, y + 904016250260250717251913633712*x^2 + 297807486916138001851276656278*x + 514899226321704405985204664612)\n\nsage: %timeit ZZ.random_element(10**10) * Q\n10 loops, best of 3: 207 ms per loop\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6218\n\n",
    "created_at": "2009-06-05T00:36:10Z",
    "labels": [
        "algebraic geometry",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "small changes to jacobian_morphism to make hyperelliptic curve arithmetic faster",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6218",
    "user": "@ncalexan"
}
```
Assignee: @williamstein

CC:  @craigcitro

Keywords: jacobian morphism hyperelliptic curve speed profile time

The attached patch uses % instead of the generic mod and avoids creating polynomial rings.  The savings are significant:


```
sage: F = GF(next_prime(10^30))
sage: x = F['x'].gen()
sage: f = x^7 + x^2 + 1
sage: H = HyperellipticCurve(f, 2*x); H
Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1
sage: J = H.jacobian()(F); J
verbose 0 (902: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.
Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057
sage: Q = J(H.lift_x(F(1))); Q
(x + 1000000000000000000000000000056, y + 1000000000000000000000000000056)
```


Before:

```
sage: %time ZZ.random_element(10**10) * Q
CPU times: user 0.91 s, sys: 0.02 s, total: 0.93 s
Wall time: 0.93 s
(x^3 + 402198643461859040647192719684*x^2 + 601836335767969290835741174254*x + 16518729356967251698882316239, y + 473734498489001855322294293716*x^2 + 971294794490578173226993121181*x + 205331062061696832607472618253)

sage: %timeit ZZ.random_element(10**10) * Q
10 loops, best of 3: 980 ms per loop
```


After:

```
sage: %time ZZ.random_element(10^10) * Q
CPU times: user 0.22 s, sys: 0.01 s, total: 0.23 s
Wall time: 0.25 s
(x^3 + 275125861943108889646384133572*x^2 + 753495481691507497462095614898*x + 60041420316935318537784907957, y + 904016250260250717251913633712*x^2 + 297807486916138001851276656278*x + 514899226321704405985204664612)

sage: %timeit ZZ.random_element(10**10) * Q
10 loops, best of 3: 207 ms per loop
```


Issue created by migration from https://trac.sagemath.org/ticket/6218





---

archive/issue_comments_049666.json:
```json
{
    "body": "Attachment [trac_6218-speedup-jacobian-morphism.patch](tarball://root/attachments/some-uuid/ticket6218/trac_6218-speedup-jacobian-morphism.patch) by @ncalexan created at 2009-06-06 04:58:23",
    "created_at": "2009-06-06T04:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6218#issuecomment-49666",
    "user": "@ncalexan"
}
```

Attachment [trac_6218-speedup-jacobian-morphism.patch](tarball://root/attachments/some-uuid/ticket6218/trac_6218-speedup-jacobian-morphism.patch) by @ncalexan created at 2009-06-06 04:58:23



---

archive/issue_comments_049667.json:
```json
{
    "body": "Looks fine aside from one minor doctest failure:\n\n```\nsage -t  \"devel/sage/sage/schemes/hyperelliptic_curves/jacobian_morphism.py\"\n**********************************************************************\nFile \"/home/kedlaya/sage-4.0.1/devel/sage/sage/schemes/hyperelliptic_curves/jacobian_morphism.py\", line 297:\n    sage: J = H.jacobian()(F); J\nExpected:\n    Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057\nGot:\n    verbose 0 (902: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.\n    Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057\n**********************************************************************\n```\n",
    "created_at": "2009-06-08T22:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6218#issuecomment-49667",
    "user": "@kedlaya"
}
```

Looks fine aside from one minor doctest failure:

```
sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/jacobian_morphism.py"
**********************************************************************
File "/home/kedlaya/sage-4.0.1/devel/sage/sage/schemes/hyperelliptic_curves/jacobian_morphism.py", line 297:
    sage: J = H.jacobian()(F); J
Expected:
    Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057
Got:
    verbose 0 (902: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.
    Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057
**********************************************************************
```




---

archive/issue_comments_049668.json:
```json
{
    "body": "Is that even a doctest failure?  Am I supposed to include the (spurious) warning in the output?",
    "created_at": "2009-06-08T22:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6218#issuecomment-49668",
    "user": "@ncalexan"
}
```

Is that even a doctest failure?  Am I supposed to include the (spurious) warning in the output?



---

archive/issue_comments_049669.json:
```json
{
    "body": "Okay, after discussion on IRC, the warning just needs to be copied in (maybe with ... instead of 902).  So this is good to go with the doctest fixed.",
    "created_at": "2009-06-08T22:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6218#issuecomment-49669",
    "user": "@ncalexan"
}
```

Okay, after discussion on IRC, the warning just needs to be copied in (maybe with ... instead of 902).  So this is good to go with the doctest fixed.



---

archive/issue_comments_049670.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T22:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6218#issuecomment-49670",
    "user": "@ncalexan"
}
```

Resolution: fixed
