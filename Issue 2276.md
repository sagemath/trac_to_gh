# Issue 2276: M.divides(N) gives an error if M and N are monomials in R.<x,y> = PolynomialRing(QQ); ok for R.<x>

archive/issues_002276.json:
```json
{
    "body": "Assignee: was\n\nsage: R.<x,y> = PolynomialRing(QQ)\nsage: M = x*y\nsage: N = x<sup>2*y</sup>3\nsage: M.divides(N)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/carlson/docs`@`chiquito/_Research/CIMAT_Lectures/Computation/sageprogs/<ipython console> in <module>()\n\n/Users/carlson/docs`@`chiquito/_Research/CIMAT_Lectures/Computation/sageprogs/element.pyx in sage.structure.element.CommutativeRingElement.divides()\n\n<type 'exceptions.TypeError'>: unsupported operand type(s) for %: 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular' and 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'\n\nIssue created by migration from https://trac.sagemath.org/ticket/2276\n\n",
    "created_at": "2008-02-23T08:41:02Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "M.divides(N) gives an error if M and N are monomials in R.<x,y> = PolynomialRing(QQ); ok for R.<x>",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2276",
    "user": "jxxcarlson"
}
```
Assignee: was

sage: R.<x,y> = PolynomialRing(QQ)
sage: M = x*y
sage: N = x<sup>2*y</sup>3
sage: M.divides(N)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/carlson/docs`@`chiquito/_Research/CIMAT_Lectures/Computation/sageprogs/<ipython console> in <module>()

/Users/carlson/docs`@`chiquito/_Research/CIMAT_Lectures/Computation/sageprogs/element.pyx in sage.structure.element.CommutativeRingElement.divides()

<type 'exceptions.TypeError'>: unsupported operand type(s) for %: 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular' and 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'

Issue created by migration from https://trac.sagemath.org/ticket/2276





---

archive/issue_comments_015100.json:
```json
{
    "body": "Changing component from algebraic geometry to commutative algebra.",
    "created_at": "2008-02-23T14:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15100",
    "user": "mabshoff"
}
```

Changing component from algebraic geometry to commutative algebra.



---

archive/issue_comments_015101.json:
```json
{
    "body": "Changing assignee from was to malb.",
    "created_at": "2008-02-23T14:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15101",
    "user": "mabshoff"
}
```

Changing assignee from was to malb.



---

archive/issue_comments_015102.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-03-18T21:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15102",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_015103.json:
```json
{
    "body": "This is still an issue with 2.10.4. \n\nCheers,\n\nMichael",
    "created_at": "2008-03-18T21:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15103",
    "user": "mabshoff"
}
```

This is still an issue with 2.10.4. 

Cheers,

Michael



---

archive/issue_comments_015104.json:
```json
{
    "body": "Attachment\n\nThe attached patch implements `__mod__` which fixes the issue. Note, that type checking is performed in `quo_rem` and thus is not needed in `__mod__`.",
    "created_at": "2008-03-28T12:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15104",
    "user": "malb"
}
```

Attachment

The attached patch implements `__mod__` which fixes the issue. Note, that type checking is performed in `quo_rem` and thus is not needed in `__mod__`.



---

archive/issue_comments_015105.json:
```json
{
    "body": "Patch looks good to me, is sufficiently doctested. Nice. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T12:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15105",
    "user": "mabshoff"
}
```

Patch looks good to me, is sufficiently doctested. Nice. Positive review.

Cheers,

Michael



---

archive/issue_comments_015106.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-28T13:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15106",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_comments_015107.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-28T13:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15107",
    "user": "mabshoff"
}
```

Resolution: fixed
