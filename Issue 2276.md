# Issue 2276: M.divides(N) gives an error if M and N are monomials in R.<x,y> = PolynomialRing(QQ); ok for R.<x>

archive/issues_002276.json:
```json
{
    "body": "Assignee: @williamstein\n\nsage: R.<x,y> = PolynomialRing(QQ)\nsage: M = x*y\nsage: N = x<sup>2*y</sup>3\nsage: M.divides(N)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/carlson/docs`@`chiquito/_Research/CIMAT_Lectures/Computation/sageprogs/<ipython console> in <module>()\n\n/Users/carlson/docs`@`chiquito/_Research/CIMAT_Lectures/Computation/sageprogs/element.pyx in sage.structure.element.CommutativeRingElement.divides()\n\n<type 'exceptions.TypeError'>: unsupported operand type(s) for %: 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular' and 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'\n\nIssue created by migration from https://trac.sagemath.org/ticket/2276\n\n",
    "created_at": "2008-02-23T08:41:02Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "M.divides(N) gives an error if M and N are monomials in R.<x,y> = PolynomialRing(QQ); ok for R.<x>",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2276",
    "user": "https://trac.sagemath.org/admin/accounts/users/jxxcarlson"
}
```
Assignee: @williamstein

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

archive/issue_comments_015067.json:
```json
{
    "body": "Changing component from algebraic geometry to commutative algebra.",
    "created_at": "2008-02-23T14:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15067",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from algebraic geometry to commutative algebra.



---

archive/issue_comments_015068.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2008-02-23T14:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15068",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_015069.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-03-18T21:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15069",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_015070.json:
```json
{
    "body": "This is still an issue with 2.10.4. \n\nCheers,\n\nMichael",
    "created_at": "2008-03-18T21:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15070",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is still an issue with 2.10.4. 

Cheers,

Michael



---

archive/issue_comments_015071.json:
```json
{
    "body": "Attachment [trac_2276.patch](tarball://root/attachments/some-uuid/ticket2276/trac_2276.patch) by @malb created at 2008-03-28 12:00:36\n\nThe attached patch implements `__mod__` which fixes the issue. Note, that type checking is performed in `quo_rem` and thus is not needed in `__mod__`.",
    "created_at": "2008-03-28T12:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15071",
    "user": "https://github.com/malb"
}
```

Attachment [trac_2276.patch](tarball://root/attachments/some-uuid/ticket2276/trac_2276.patch) by @malb created at 2008-03-28 12:00:36

The attached patch implements `__mod__` which fixes the issue. Note, that type checking is performed in `quo_rem` and thus is not needed in `__mod__`.



---

archive/issue_comments_015072.json:
```json
{
    "body": "Patch looks good to me, is sufficiently doctested. Nice. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T12:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15072",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me, is sufficiently doctested. Nice. Positive review.

Cheers,

Michael



---

archive/issue_comments_015073.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-28T13:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15073",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_events_002447.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-28T13:27:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2276#event-2447"
}
```



---

archive/issue_comments_015074.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-28T13:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2276#issuecomment-15074",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
