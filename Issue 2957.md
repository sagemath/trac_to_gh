# Issue 2957: Singular multivariate polynomials are buggy on exponent overflow

archive/issues_002957.json:
```json
{
    "body": "Assignee: somebody\n\nOn 64-bit x86, exponents truncate to 32 bits:\n\n```\nsage: K.<x,y> = QQ[]\nsage: ((x^12345)^54321)^12345\nx^2065457633\nsage: 12345*54321*12345\n8278467437025\nsage: (12345*54321*12345) % 2^32\n2065457633\n```\n\n\nOn 32-bit x86, exponents truncate to 16 bits, and overflow from one variable to another (!!!):\n\n```\nsage: K.<x,y> = QQ[]\nsage: (x^12345)^54321\nx^28393*y^10232\nsage: (12345*54321) // 2^16\n10232\nsage: (12345*54321) % 2^16\n28393\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2957\n\n",
    "created_at": "2008-04-19T15:33:21Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Singular multivariate polynomials are buggy on exponent overflow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2957",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: somebody

On 64-bit x86, exponents truncate to 32 bits:

```
sage: K.<x,y> = QQ[]
sage: ((x^12345)^54321)^12345
x^2065457633
sage: 12345*54321*12345
8278467437025
sage: (12345*54321*12345) % 2^32
2065457633
```


On 32-bit x86, exponents truncate to 16 bits, and overflow from one variable to another (!!!):

```
sage: K.<x,y> = QQ[]
sage: (x^12345)^54321
x^28393*y^10232
sage: (12345*54321) // 2^16
10232
sage: (12345*54321) % 2^16
28393
```



Issue created by migration from https://trac.sagemath.org/ticket/2957





---

archive/issue_comments_020356.json:
```json
{
    "body": "I'm going to upload a fix in a sec, but it comes at a cost:\n\n## Before\n\n```\nsage: P.<x,y> = PolynomialRing(QQ)\nsage: %timeit x*y\n1000000 loops, best of 3: 288 ns per loop\n\nsage: f = x + 1\nsage: g = y + 1\nsage: %timeit f*g\n1000000 loops, best of 3: 462 ns per loop\n```\n\n\n## After\n\n```\nsage: P.<x,y> = PolynomialRing(QQ)\nsage: %timeit x*y\n1000000 loops, best of 3: 314 ns per loop\n\nsage: f = x + 1\nsage: g = y + 1\nsage: %timeit f*g\n1000000 loops, best of 3: 501 ns per loop\n```\n",
    "created_at": "2009-01-23T08:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2957#issuecomment-20356",
    "user": "https://github.com/malb"
}
```

I'm going to upload a fix in a sec, but it comes at a cost:

## Before

```
sage: P.<x,y> = PolynomialRing(QQ)
sage: %timeit x*y
1000000 loops, best of 3: 288 ns per loop

sage: f = x + 1
sage: g = y + 1
sage: %timeit f*g
1000000 loops, best of 3: 462 ns per loop
```


## After

```
sage: P.<x,y> = PolynomialRing(QQ)
sage: %timeit x*y
1000000 loops, best of 3: 314 ns per loop

sage: f = x + 1
sage: g = y + 1
sage: %timeit f*g
1000000 loops, best of 3: 501 ns per loop
```




---

archive/issue_comments_020357.json:
```json
{
    "body": "I just replaced the existing patch with a new one which improves performance. Burcin spotted earlier, that I forgot to assign a type to `max_exponent_size`. With that, the timing difference is in the range of the normal noise.",
    "created_at": "2009-01-24T10:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2957#issuecomment-20357",
    "user": "https://github.com/malb"
}
```

I just replaced the existing patch with a new one which improves performance. Burcin spotted earlier, that I forgot to assign a type to `max_exponent_size`. With that, the timing difference is in the range of the normal noise.



---

archive/issue_comments_020358.json:
```json
{
    "body": "We already discussed this with malb, boothby and was extensively. Here are the points here for reference:\n* the return value of the function `p_GetMaxExp` is an unsigned long, fixing this should let one remove the esum < 0 check\n* `max_exponent_size` in `multi_polynomial_libsingular.pyx` should be declared an `unsigned long`\n* adding an `unlikely` hint for `esum > max_exponent_size` might reduce the speed regression even further\n\nBoothby also remarked that checking for total degree before the degree of each variable might help. Looking at the code again, I think we only check the total degree.",
    "created_at": "2009-01-24T18:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2957#issuecomment-20358",
    "user": "https://github.com/burcin"
}
```

We already discussed this with malb, boothby and was extensively. Here are the points here for reference:
* the return value of the function `p_GetMaxExp` is an unsigned long, fixing this should let one remove the esum < 0 check
* `max_exponent_size` in `multi_polynomial_libsingular.pyx` should be declared an `unsigned long`
* adding an `unlikely` hint for `esum > max_exponent_size` might reduce the speed regression even further

Boothby also remarked that checking for total degree before the degree of each variable might help. Looking at the code again, I think we only check the total degree.



---

archive/issue_comments_020359.json:
```json
{
    "body": "The `_imul_` method also needs the check.",
    "created_at": "2009-01-24T23:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2957#issuecomment-20359",
    "user": "https://github.com/burcin"
}
```

The `_imul_` method also needs the check.



---

archive/issue_comments_020360.json:
```json
{
    "body": "newest version",
    "created_at": "2009-01-25T09:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2957#issuecomment-20360",
    "user": "https://github.com/malb"
}
```

newest version



---

archive/issue_comments_020361.json:
```json
{
    "body": "Attachment [mpoly_singular_overflow.patch](tarball://root/attachments/some-uuid/ticket2957/mpoly_singular_overflow.patch) by @malb created at 2009-01-25 09:03:18\n\nBurcin agrees that this is a positive review now.",
    "created_at": "2009-01-25T09:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2957#issuecomment-20361",
    "user": "https://github.com/malb"
}
```

Attachment [mpoly_singular_overflow.patch](tarball://root/attachments/some-uuid/ticket2957/mpoly_singular_overflow.patch) by @malb created at 2009-01-25 09:03:18

Burcin agrees that this is a positive review now.



---

archive/issue_comments_020362.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T14:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2957#issuecomment-20362",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_020363.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T14:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2957#issuecomment-20363",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
