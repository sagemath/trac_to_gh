# Issue 2188: mathematically senseless bit-shift operations in integer_mod.pyx

archive/issues_002188.json:
```json
{
    "body": "Assignee: cwitty\n\nThe current bit-shift operations are straight wrappers for the C bit-shift operators, which means that they are architecture-specific and mathematically very strange.  For instance, currently, on 32-bit x86 with a smallish modulus, `mod(a,n)<<s` evaluates to `mod((a<<(s%32))%2^32%n, n)`.\n\nWilliam, Robert Bradshaw, and I decided on IRC that the best we can do for bit-shift is this:\nif 0<=a<n, then mod(a,n)<<s == mod(a<<s,n); and similarly for right-shift.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2188\n\n",
    "created_at": "2008-02-17T05:45:40Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "mathematically senseless bit-shift operations in integer_mod.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2188",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

The current bit-shift operations are straight wrappers for the C bit-shift operators, which means that they are architecture-specific and mathematically very strange.  For instance, currently, on 32-bit x86 with a smallish modulus, `mod(a,n)<<s` evaluates to `mod((a<<(s%32))%2^32%n, n)`.

William, Robert Bradshaw, and I decided on IRC that the best we can do for bit-shift is this:
if 0<=a<n, then mod(a,n)<<s == mod(a<<s,n); and similarly for right-shift.

Issue created by migration from https://trac.sagemath.org/ticket/2188





---

archive/issue_comments_014333.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-16T08:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2188#issuecomment-14333",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Resolution: invalid



---

archive/issue_comments_014334.json:
```json
{
    "body": "The bit-shift method uses the GMP function ``mpz_mul_2exp``, thus this ticket is no longer valid.",
    "created_at": "2010-01-16T08:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2188#issuecomment-14334",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

The bit-shift method uses the GMP function ``mpz_mul_2exp``, thus this ticket is no longer valid.



---

archive/issue_events_002355.json:
```json
{
    "actor": "spancratz",
    "created_at": "2010-01-16T08:06:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2188",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2188#event-2355"
}
```
