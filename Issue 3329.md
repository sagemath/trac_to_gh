# Issue 3329: attempting to convert relative number field elements to Singular should fail quickly

archive/issues_003329.json:
```json
{
    "body": "Assignee: @williamstein\n\nConsider this example:\n\n```\n  R.<a,b> = NumberField(x^2-3,'g').extension(x^2-7,'h')[]\n  h = R.base_ring().gen()    \n  S.<y> = R.fraction_field()[]\n  xgcd(y^2, a*h*y+b) \n```\n\n(reported by Ga\u00ebtan Bisson here: http://groups.google.com/group/sage-support/browse_thread/thread/5338608bd7508b00/cd1d6555592e472f#cd1d6555592e472f)\n\nThis fails because it tries to use Singular to take the gcd of multivariate polynomials over a relative number field, and Singular does not support relative number fields.  However, the error message is quite poor; it would be better if it failed with a better error message.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3329\n\n",
    "created_at": "2008-05-29T17:32:53Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "attempting to convert relative number field elements to Singular should fail quickly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3329",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

Consider this example:

```
  R.<a,b> = NumberField(x^2-3,'g').extension(x^2-7,'h')[]
  h = R.base_ring().gen()    
  S.<y> = R.fraction_field()[]
  xgcd(y^2, a*h*y+b) 
```

(reported by Gaëtan Bisson here: http://groups.google.com/group/sage-support/browse_thread/thread/5338608bd7508b00/cd1d6555592e472f#cd1d6555592e472f)

This fails because it tries to use Singular to take the gcd of multivariate polynomials over a relative number field, and Singular does not support relative number fields.  However, the error message is quite poor; it would be better if it failed with a better error message.

Issue created by migration from https://trac.sagemath.org/ticket/3329





---

archive/issue_comments_023037.json:
```json
{
    "body": "See also #3330, which is about the exact same test case, but requests a working implementation of GCD (rather than just a better error message).",
    "created_at": "2008-05-29T17:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3329#issuecomment-23037",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

See also #3330, which is about the exact same test case, but requests a working implementation of GCD (rather than just a better error message).



---

archive/issue_comments_023038.json:
```json
{
    "body": "This fails before Singular:\n\n```\nTypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in y over Fraction Field of Multivariate Polynomial Ring in a, b over Number Field in h with defining polynomial x^2 - 7 over its base field' and 'Multivariate Polynomial Ring in a, b over Number Field in h with defining polynomial x^2 - 7 over its base field'\n```\n",
    "created_at": "2008-08-18T14:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3329#issuecomment-23038",
    "user": "https://github.com/malb"
}
```

This fails before Singular:

```
TypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in y over Fraction Field of Multivariate Polynomial Ring in a, b over Number Field in h with defining polynomial x^2 - 7 over its base field' and 'Multivariate Polynomial Ring in a, b over Number Field in h with defining polynomial x^2 - 7 over its base field'
```




---

archive/issue_comments_023039.json:
```json
{
    "body": "This seems to work now because we avoid Singular\n\n\n```\nsage: R.<a,b> = NumberField(x^2-3,'g').extension(x^2-7,'h')[]\nsage: h = R.base_ring().gen()\nsage: S.<y> = R.fraction_field()[]\nsage: xgcd(y^2, a*h*y+b)\n(49*a^4*b^2/(343*a^6), 1, ((-1)/(h*a))*y + 49*a^4*b/(343*a^6))\n```\n\n\nCarl, any thoughts on this?",
    "created_at": "2009-01-23T07:21:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3329#issuecomment-23039",
    "user": "https://github.com/malb"
}
```

This seems to work now because we avoid Singular


```
sage: R.<a,b> = NumberField(x^2-3,'g').extension(x^2-7,'h')[]
sage: h = R.base_ring().gen()
sage: S.<y> = R.fraction_field()[]
sage: xgcd(y^2, a*h*y+b)
(49*a^4*b^2/(343*a^6), 1, ((-1)/(h*a))*y + 49*a^4*b/(343*a^6))
```


Carl, any thoughts on this?



---

archive/issue_comments_023040.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2009-01-25T19:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3329#issuecomment-23040",
    "user": "https://github.com/malb"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_023041.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-25T19:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3329#issuecomment-23041",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023042.json:
```json
{
    "body": "Since Carl's not involved any more, and this now works fine (in sage-4.3.1.rc0 too), I'm closing this as fixed:\n\n\n```\nbash$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage:   R.<a,b> = NumberField(x^2-3,'g').extension(x^2-7,'h')[]\nsage:   h = R.base_ring().gen()\nsage:   S.<y> = R.fraction_field()[]\nsage:   xgcd(y^2, a*h*y+b)\n(7*a^2*b^2/(7*a^2*b^2), 7*a^2/b^2, (((-7)*a^2)/(h*a*b^2))*y + 7*a^2*b/(7*a^2*b^2))\n```\n",
    "created_at": "2010-01-18T13:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3329#issuecomment-23042",
    "user": "https://github.com/williamstein"
}
```

Since Carl's not involved any more, and this now works fine (in sage-4.3.1.rc0 too), I'm closing this as fixed:


```
bash$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage:   R.<a,b> = NumberField(x^2-3,'g').extension(x^2-7,'h')[]
sage:   h = R.base_ring().gen()
sage:   S.<y> = R.fraction_field()[]
sage:   xgcd(y^2, a*h*y+b)
(7*a^2*b^2/(7*a^2*b^2), 7*a^2/b^2, (((-7)*a^2)/(h*a*b^2))*y + 7*a^2*b/(7*a^2*b^2))
```




---

archive/issue_comments_023043.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-18T13:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3329#issuecomment-23043",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
