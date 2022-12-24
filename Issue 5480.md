# Issue 5480: R.quotient_by_principal_ideal() is self-contradictory

archive/issues_005480.json:
```json
{
    "body": "Assignee: was\n\nThe following seems absurd:\n\n```\nsage: R.<x> = PolynomialRing(QQ)\nsage: I = (x^2-1)*R\nsage: S = R.quotient_by_principal_ideal(I)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/justin/.sage/temp/Hasse_2.local/32509/_tmp_z_sage_9.py in <module>()\n\n/SandBox/Justin/sb/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.pyc in quotient_by_principal_ideal(self=Univariate Polynomial Ring in x over Rational Field, f=Principal ideal (x^2 - 1) of Univariate Polynomial Ring in x over Rational Field, names=None)\n   1004         \"\"\"\n   1005         import sage.rings.polynomial.polynomial_quotient_ring\n-> 1006         return sage.rings.polynomial.polynomial_quotient_ring.PolynomialQuotientRing(self, f, names)\n   1007 \n   1008 \n\n/SandBox/Justin/sb/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in PolynomialQuotientRing(ring=Univariate Polynomial Ring in x over Rational Field, polynomial=Principal ideal (x^2 - 1) of Univariate Polynomial Ring in x over Rational Field, names=None)\n    128         raise TypeError, \"ring must be a polynomial ring\"\n    129     if not isinstance(polynomial, polynomial_element.Polynomial):\n--> 130         raise TypeError, \"must be a polynomial\"\n        global EXAMPLES = undefined\n    131     if not polynomial.parent() == ring:\n    132         raise TypeError, \"polynomial must be in ring\"\n\nTypeError: must be a polynomial\n```\n\nEither the procedure should be ...by_polynomial(), or it should really accept an ideal as an argument.\n\nSheesh.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5480\n\n",
    "created_at": "2009-03-11T05:23:45Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "R.quotient_by_principal_ideal() is self-contradictory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5480",
    "user": "justin"
}
```
Assignee: was

The following seems absurd:

```
sage: R.<x> = PolynomialRing(QQ)
sage: I = (x^2-1)*R
sage: S = R.quotient_by_principal_ideal(I)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/justin/.sage/temp/Hasse_2.local/32509/_tmp_z_sage_9.py in <module>()

/SandBox/Justin/sb/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.pyc in quotient_by_principal_ideal(self=Univariate Polynomial Ring in x over Rational Field, f=Principal ideal (x^2 - 1) of Univariate Polynomial Ring in x over Rational Field, names=None)
   1004         """
   1005         import sage.rings.polynomial.polynomial_quotient_ring
-> 1006         return sage.rings.polynomial.polynomial_quotient_ring.PolynomialQuotientRing(self, f, names)
   1007 
   1008 

/SandBox/Justin/sb/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in PolynomialQuotientRing(ring=Univariate Polynomial Ring in x over Rational Field, polynomial=Principal ideal (x^2 - 1) of Univariate Polynomial Ring in x over Rational Field, names=None)
    128         raise TypeError, "ring must be a polynomial ring"
    129     if not isinstance(polynomial, polynomial_element.Polynomial):
--> 130         raise TypeError, "must be a polynomial"
        global EXAMPLES = undefined
    131     if not polynomial.parent() == ring:
    132         raise TypeError, "polynomial must be in ring"

TypeError: must be a polynomial
```

Either the procedure should be ...by_polynomial(), or it should really accept an ideal as an argument.

Sheesh.



Issue created by migration from https://trac.sagemath.org/ticket/5480





---

archive/issue_comments_042512.json:
```json
{
    "body": "Attachment [sage-5480.patch](tarball://root/attachments/some-uuid/ticket5480/sage-5480.patch) by justin created at 2009-03-11 07:01:18\n\nThe fix is to permit both a polynomial (for backward compatibility) and an ideal as the argument.  Doctested the rings/polynomial directory w/o problems.",
    "created_at": "2009-03-11T07:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5480#issuecomment-42512",
    "user": "justin"
}
```

Attachment [sage-5480.patch](tarball://root/attachments/some-uuid/ticket5480/sage-5480.patch) by justin created at 2009-03-11 07:01:18

The fix is to permit both a polynomial (for backward compatibility) and an ideal as the argument.  Doctested the rings/polynomial directory w/o problems.



---

archive/issue_comments_042513.json:
```json
{
    "body": "The patch looks ok but there should be doctests to illustrate the new behaviour, and the docstring should also say what input is valid.",
    "created_at": "2009-03-14T20:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5480#issuecomment-42513",
    "user": "cremona"
}
```

The patch looks ok but there should be doctests to illustrate the new behaviour, and the docstring should also say what input is valid.



---

archive/issue_comments_042514.json:
```json
{
    "body": "Changing assignee from was to justin.",
    "created_at": "2009-03-16T03:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5480#issuecomment-42514",
    "user": "justin"
}
```

Changing assignee from was to justin.



---

archive/issue_comments_042515.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-16T03:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5480#issuecomment-42515",
    "user": "justin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042516.json:
```json
{
    "body": "Justin,\n\nany chance you can add some doctests here? I am marking this as \"needs works\" until then.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T06:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5480#issuecomment-42516",
    "user": "mabshoff"
}
```

Justin,

any chance you can add some doctests here? I am marking this as "needs works" until then.

Cheers,

Michael



---

archive/issue_comments_042517.json:
```json
{
    "body": "Changing component from algebraic geometry to algebra.",
    "created_at": "2009-11-15T11:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5480#issuecomment-42517",
    "user": "AlexGhitza"
}
```

Changing component from algebraic geometry to algebra.



---

archive/issue_comments_042518.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-15T12:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5480#issuecomment-42518",
    "user": "AlexGhitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042519.json:
```json
{
    "body": "The new patch fixes the issue and has doctests.  It depends on the patch at #5482.\n\nApply only trac_5480.patch",
    "created_at": "2009-11-15T12:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5480#issuecomment-42519",
    "user": "AlexGhitza"
}
```

The new patch fixes the issue and has doctests.  It depends on the patch at #5482.

Apply only trac_5480.patch



---

archive/issue_comments_042520.json:
```json
{
    "body": "apply this patch only; depends on #5482",
    "created_at": "2009-11-15T12:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5480#issuecomment-42520",
    "user": "AlexGhitza"
}
```

apply this patch only; depends on #5482



---

archive/issue_comments_042521.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-17T08:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5480#issuecomment-42521",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042522.json:
```json
{
    "body": "Attachment [trac_5480.patch](tarball://root/attachments/some-uuid/ticket5480/trac_5480.patch) by mhansen created at 2009-11-17 08:04:35\n\nLooks good to me.",
    "created_at": "2009-11-17T08:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5480#issuecomment-42522",
    "user": "mhansen"
}
```

Attachment [trac_5480.patch](tarball://root/attachments/some-uuid/ticket5480/trac_5480.patch) by mhansen created at 2009-11-17 08:04:35

Looks good to me.



---

archive/issue_comments_042523.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T08:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5480#issuecomment-42523",
    "user": "mhansen"
}
```

Resolution: fixed
