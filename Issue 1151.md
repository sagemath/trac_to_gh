# Issue 1151: [with patch, positive review] Bug in creating elements in multivariate quotient rings that cannot be coerced to singular

archive/issues_001151.json:
```json
{
    "body": "Assignee: @malb\n\n```\nA.<x> = QQ[]\nGauss.<i> = A.quotient(x^2+1)\nR.<c,d,X1,Y1,X2,Y2,Z1,Z2> = Gauss[]\nS = R.quotient([(X1^2+Y1^2)*Z1^2-c^2*(Z1^4+d*X1^2*Y1^2),\n                    (X2^2+Y2^2)*Z2^2-c^2*(Z2^4+d*X2^2*Y2^2)])\nS(1)\n```\nProduces the traceback:\n\n```\nsage: S(1)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/users/spaces/zimmerma/try/<ipython console> in <module>()\n\n/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/quotient_ring.py in __call__(self, x, coerce)\n   257             R = self.cover_ring()\n   258             x = R(x)\n--> 259         return quotient_ring_element.QuotientRingElement(self, x)\n   260\n   261     def _coerce_impl(self, x):\n\n/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/quotient_ring_element.py in __init__(self, parent, rep, reduce)\n    70         self.__rep = rep\n    71         if reduce:\n---> 72             self._reduce_()\n    73\n    74     def _reduce_(self):\n\n/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/quotient_ring_element.py in _reduce_(self)\n    74     def _reduce_(self):\n    75         I = self.parent().defining_ideal()\n---> 76         self.__rep = I.reduce(self.__rep)\n    77\n    78     def copy(self):\n\n/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in reduce(self, f)\n   805\n   806         try:\n--> 807             singular = self._singular_groebner_basis().parent()\n   808         except (AttributeError, RuntimeError):\n   809             singular = self._singular_groebner_basis().parent()\n\n/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in _singular_groebner_basis(self)\n   623             S = self.__singular_groebner_basis\n   624         except AttributeError:\n--> 625             G = self.groebner_basis()\n   626             try:\n   627                 return self.__singular_groebner_basis\n\n/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in groebner_basis(self, algorithm)\n  1348                 return self._macaulay2_groebner_basis()\n  1349             else:\n-> 1350                 return self._groebner_basis_using_singular(\"groebner\")\n  1351         elif algorithm.startswith('singular:'):\n  1352             return self._groebner_basis_using_singular(algorithm[9:])\n\n/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in _groebner_basis_using_singular(self, algorithm)\n   565         except AttributeError:\n   566             if algorithm==\"groebner\":\n--> 567                 S = self._singular_().groebner()\n   568             elif algorithm==\"std\":\n   569                 S = self._singular_().std()\n\n/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in _singular_(self, singular)\n   214         if singular is None: singular = singular_default\n   215         try:\n--> 216             self.ring()._singular_(singular).set_ring()\n   217             I = self.__singular\n   218             if not (I.parent() is singular):\n\n/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in _singular_(self, singular, force)\n   169             return R\n   170         except (AttributeError, ValueError):\n--> 171             return self._singular_init_(singular, force)\n   172\n   173     def _singular_init_(self, singular=singular_default, force=False):\n\n/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in _singular_init_(self, singular, force)\n   176         \"\"\"\n   177         if not self._can_convert_to_singular() and not force:\n--> 178             raise TypeError, \"no conversion of this ring to a Singular ring defined\"\n   179\n   180         if self.ngens()==1:\n\n<type 'exceptions.TypeError'>: no conversion of this ring to a Singular ring defined\n```\nThe problem is that `QQ[x]/(x^2+1)` cannot be a base ring in singular, and when we try to reduce (in creating an element), we can't compute a Grobner basis.\n\nWe need to handle multivariable quotients better over general rings.  One solution would be to write a naive groebner basis implementation that works over an arbitrary ring.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1151\n\n",
    "closed_at": "2008-02-27T23:20:14Z",
    "created_at": "2007-11-12T00:16:56Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch, positive review] Bug in creating elements in multivariate quotient rings that cannot be coerced to singular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1151",
    "user": "https://github.com/roed314"
}
```
Assignee: @malb

```
A.<x> = QQ[]
Gauss.<i> = A.quotient(x^2+1)
R.<c,d,X1,Y1,X2,Y2,Z1,Z2> = Gauss[]
S = R.quotient([(X1^2+Y1^2)*Z1^2-c^2*(Z1^4+d*X1^2*Y1^2),
                    (X2^2+Y2^2)*Z2^2-c^2*(Z2^4+d*X2^2*Y2^2)])
S(1)
```
Produces the traceback:

```
sage: S(1)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/users/spaces/zimmerma/try/<ipython console> in <module>()

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/quotient_ring.py in __call__(self, x, coerce)
   257             R = self.cover_ring()
   258             x = R(x)
--> 259         return quotient_ring_element.QuotientRingElement(self, x)
   260
   261     def _coerce_impl(self, x):

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/quotient_ring_element.py in __init__(self, parent, rep, reduce)
    70         self.__rep = rep
    71         if reduce:
---> 72             self._reduce_()
    73
    74     def _reduce_(self):

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/quotient_ring_element.py in _reduce_(self)
    74     def _reduce_(self):
    75         I = self.parent().defining_ideal()
---> 76         self.__rep = I.reduce(self.__rep)
    77
    78     def copy(self):

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in reduce(self, f)
   805
   806         try:
--> 807             singular = self._singular_groebner_basis().parent()
   808         except (AttributeError, RuntimeError):
   809             singular = self._singular_groebner_basis().parent()

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in _singular_groebner_basis(self)
   623             S = self.__singular_groebner_basis
   624         except AttributeError:
--> 625             G = self.groebner_basis()
   626             try:
   627                 return self.__singular_groebner_basis

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in groebner_basis(self, algorithm)
  1348                 return self._macaulay2_groebner_basis()
  1349             else:
-> 1350                 return self._groebner_basis_using_singular("groebner")
  1351         elif algorithm.startswith('singular:'):
  1352             return self._groebner_basis_using_singular(algorithm[9:])

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in _groebner_basis_using_singular(self, algorithm)
   565         except AttributeError:
   566             if algorithm=="groebner":
--> 567                 S = self._singular_().groebner()
   568             elif algorithm=="std":
   569                 S = self._singular_().std()

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in _singular_(self, singular)
   214         if singular is None: singular = singular_default
   215         try:
--> 216             self.ring()._singular_(singular).set_ring()
   217             I = self.__singular
   218             if not (I.parent() is singular):

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in _singular_(self, singular, force)
   169             return R
   170         except (AttributeError, ValueError):
--> 171             return self._singular_init_(singular, force)
   172
   173     def _singular_init_(self, singular=singular_default, force=False):

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in _singular_init_(self, singular, force)
   176         """
   177         if not self._can_convert_to_singular() and not force:
--> 178             raise TypeError, "no conversion of this ring to a Singular ring defined"
   179
   180         if self.ngens()==1:

<type 'exceptions.TypeError'>: no conversion of this ring to a Singular ring defined
```
The problem is that `QQ[x]/(x^2+1)` cannot be a base ring in singular, and when we try to reduce (in creating an element), we can't compute a Grobner basis.

We need to handle multivariable quotients better over general rings.  One solution would be to write a naive groebner basis implementation that works over an arbitrary ring.

Issue created by migration from https://trac.sagemath.org/ticket/1151





---

archive/issue_events_003095.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-18T09:14:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1151",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1151#event-3095"
}
```



---

archive/issue_comments_007000.json:
```json
{
    "body": "Changing component from algebraic geometry to commutative algebra.",
    "created_at": "2008-01-24T08:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1151#issuecomment-7000",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebraic geometry to commutative algebra.



---

archive/issue_comments_007001.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2008-01-24T08:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1151#issuecomment-7001",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_007002.json:
```json
{
    "body": "I've got a possibly very stupid question first. Isn't \n\n```\nsage: A.<x> = QQ[]\nsage: Gauss.<i> = A.quotient(x^2+1)\n```\n\nequivalent to:\n\n```\nsage: A.<x> = QQ[]\nsage: Gauss.<i> = NumberField(x^2+1)\n```\n\n? If so, then the base field can be coerced to Singular:\n\n```\nsage: R.<c,d,X1,Y1,X2,Y2,Z1,Z2> = Gauss[]\nsage: S = R.quotient([(X1^2+Y1^2)*Z1^2-c^2*(Z1^4+d*X1^2*Y1^2),\n....:                     (X2^2+Y2^2)*Z2^2-c^2*(Z2^4+d*X2^2*Y2^2)])\nsage: S(1)\n1\n```\n\nThe behaviour described above would still be a bug but a different one.\n\nBesides that detail, I have a 100% generic Gr\u00f6bner basis implementation in pure Python (very very slow) that -- once integrated -- will resolve this bug for any base field (and ZZ).",
    "created_at": "2008-01-24T11:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1151#issuecomment-7002",
    "user": "https://github.com/malb"
}
```

I've got a possibly very stupid question first. Isn't 

```
sage: A.<x> = QQ[]
sage: Gauss.<i> = A.quotient(x^2+1)
```

equivalent to:

```
sage: A.<x> = QQ[]
sage: Gauss.<i> = NumberField(x^2+1)
```

? If so, then the base field can be coerced to Singular:

```
sage: R.<c,d,X1,Y1,X2,Y2,Z1,Z2> = Gauss[]
sage: S = R.quotient([(X1^2+Y1^2)*Z1^2-c^2*(Z1^4+d*X1^2*Y1^2),
....:                     (X2^2+Y2^2)*Z2^2-c^2*(Z2^4+d*X2^2*Y2^2)])
sage: S(1)
1
```

The behaviour described above would still be a bug but a different one.

Besides that detail, I have a 100% generic Gröbner basis implementation in pure Python (very very slow) that -- once integrated -- will resolve this bug for any base field (and ZZ).



---

archive/issue_comments_007003.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-24T11:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1151#issuecomment-7003",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007004.json:
```json
{
    "body": "malb -- A number field is a totally different sort of object in Sage than\n`A.quotient(x^2 + 1)`.   It happens that the two are  abstractly isomorphic, though, so whatever coercion you're thinking about can probably be made to work.",
    "created_at": "2008-01-24T16:21:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1151#issuecomment-7004",
    "user": "https://github.com/williamstein"
}
```

malb -- A number field is a totally different sort of object in Sage than
`A.quotient(x^2 + 1)`.   It happens that the two are  abstractly isomorphic, though, so whatever coercion you're thinking about can probably be made to work.



---

archive/issue_comments_007005.json:
```json
{
    "body": "Attachment [trac_1151.patch](tarball://root/attachments/some-uuid/ticket1151/trac_1151.patch) by @malb created at 2008-02-08 12:19:27\n\nafter #2111 has been merged, this patch fixes the issue of this ticket",
    "created_at": "2008-02-08T12:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1151#issuecomment-7005",
    "user": "https://github.com/malb"
}
```

Attachment [trac_1151.patch](tarball://root/attachments/some-uuid/ticket1151/trac_1151.patch) by @malb created at 2008-02-08 12:19:27

after #2111 has been merged, this patch fixes the issue of this ticket



---

archive/issue_comments_007006.json:
```json
{
    "body": "I claim that this issue was resolved in Sage 2.10.2.alpha0.",
    "created_at": "2008-02-18T15:18:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1151#issuecomment-7006",
    "user": "https://github.com/malb"
}
```

I claim that this issue was resolved in Sage 2.10.2.alpha0.



---

archive/issue_comments_007007.json:
```json
{
    "body": "When I apply trac_1151.patch the above example works, so if somebody gives it a positive review I will merge it.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-18T15:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1151#issuecomment-7007",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

When I apply trac_1151.patch the above example works, so if somebody gives it a positive review I will merge it.

Cheers,

Michael



---

archive/issue_comments_007008.json:
```json
{
    "body": "patch still applies to 2.10.2 and make test passes.",
    "created_at": "2008-02-27T13:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1151#issuecomment-7008",
    "user": "https://github.com/malb"
}
```

patch still applies to 2.10.2 and make test passes.



---

archive/issue_comments_007009.json:
```json
{
    "body": "The patch looks good to me.\n\nMaybe we should add the original example as a test somewhere, but where?",
    "created_at": "2008-02-27T13:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1151#issuecomment-7009",
    "user": "https://github.com/burcin"
}
```

The patch looks good to me.

Maybe we should add the original example as a test somewhere, but where?



---

archive/issue_events_003096.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-27T23:20:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1151",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1151#event-3096"
}
```



---

archive/issue_comments_007010.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-27T23:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1151#issuecomment-7010",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc0



---

archive/issue_comments_007011.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-27T23:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1151#issuecomment-7011",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
