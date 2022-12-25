# Issue 5496: fix bugs in is_prime  (EASY)

archive/issues_005496.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is not good:\n\n```\nsage: is_prime(GF(5)(3))\nTrue\nsage: is_prime(GF(5)(4))\nFalse\n```\n\n\nThe fix is to totally 100% rewrite is_prime in arith.py so that it first calls x.is_prime() and if that isn't defined, then in some special cases (e.g., python ints) converts to Integer and calls is_prime.  Otherwise, it raises a NotImplementedError. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5496\n\n",
    "created_at": "2009-03-12T02:55:11Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "fix bugs in is_prime  (EASY)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5496",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This is not good:

```
sage: is_prime(GF(5)(3))
True
sage: is_prime(GF(5)(4))
False
```


The fix is to totally 100% rewrite is_prime in arith.py so that it first calls x.is_prime() and if that isn't defined, then in some special cases (e.g., python ints) converts to Integer and calls is_prime.  Otherwise, it raises a NotImplementedError. 

Issue created by migration from https://trac.sagemath.org/ticket/5496





---

archive/issue_comments_042600.json:
```json
{
    "body": "Right now finite fields don't seem to have an is_prime function, so I believe that currently, is_prime(GF(5)(3)) should raise NotImplementedError.  I'm going to try to fix is_prime so that it raises NotImplementedError for is_prime(GF(5)(3)).\n\n\nKevin Stueve",
    "created_at": "2010-01-17T21:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42600",
    "user": "https://trac.sagemath.org/admin/accounts/users/kevin.stueve"
}
```

Right now finite fields don't seem to have an is_prime function, so I believe that currently, is_prime(GF(5)(3)) should raise NotImplementedError.  I'm going to try to fix is_prime so that it raises NotImplementedError for is_prime(GF(5)(3)).


Kevin Stueve



---

archive/issue_comments_042601.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T21:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42601",
    "user": "https://trac.sagemath.org/admin/accounts/users/kevin.stueve"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_042602.json:
```json
{
    "body": "Attachment [5496.patch](tarball://root/attachments/some-uuid/ticket5496/5496.patch) by kevin.stueve created at 2010-01-17 22:11:58\n\nchanged delegation of is_prime calculation to n.is_prime()",
    "created_at": "2010-01-17T22:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42602",
    "user": "https://trac.sagemath.org/admin/accounts/users/kevin.stueve"
}
```

Attachment [5496.patch](tarball://root/attachments/some-uuid/ticket5496/5496.patch) by kevin.stueve created at 2010-01-17 22:11:58

changed delegation of is_prime calculation to n.is_prime()



---

archive/issue_comments_042603.json:
```json
{
    "body": "Attachment [5496.2.patch](tarball://root/attachments/some-uuid/ticket5496/5496.2.patch) by kevin.stueve created at 2010-01-17 23:19:31",
    "created_at": "2010-01-17T23:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42603",
    "user": "https://trac.sagemath.org/admin/accounts/users/kevin.stueve"
}
```

Attachment [5496.2.patch](tarball://root/attachments/some-uuid/ticket5496/5496.2.patch) by kevin.stueve created at 2010-01-17 23:19:31



---

archive/issue_comments_042604.json:
```json
{
    "body": "Apply only 5496.2.patch.",
    "created_at": "2010-01-17T23:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42604",
    "user": "https://trac.sagemath.org/admin/accounts/users/kevin.stueve"
}
```

Apply only 5496.2.patch.



---

archive/issue_comments_042605.json:
```json
{
    "body": "Three small changes throughout the Sage library",
    "created_at": "2010-01-18T01:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42605",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Three small changes throughout the Sage library



---

archive/issue_comments_042606.json:
```json
{
    "body": "Attachment [trac5496_symbolic_expressions.patch](tarball://root/attachments/some-uuid/ticket5496/trac5496_symbolic_expressions.patch) by spancratz created at 2010-01-18 04:51:18\n\nSecond addendum, for symbolic expressions",
    "created_at": "2010-01-18T04:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42606",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac5496_symbolic_expressions.patch](tarball://root/attachments/some-uuid/ticket5496/trac5496_symbolic_expressions.patch) by spancratz created at 2010-01-18 04:51:18

Second addendum, for symbolic expressions



---

archive/issue_comments_042607.json:
```json
{
    "body": "Applying Kevin's second patch ``5496.2.patch`` and the two small changes I added, this now passes all doctests done with ``sage -t devel/sage/sage``, and can get a positive review.",
    "created_at": "2010-01-18T04:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42607",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Applying Kevin's second patch ``5496.2.patch`` and the two small changes I added, this now passes all doctests done with ``sage -t devel/sage/sage``, and can get a positive review.



---

archive/issue_comments_042608.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T04:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42608",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042609.json:
```json
{
    "body": "\n```\nif type(n) == int or type(n)==long: \n```\n\nshould be\n\n```\nif isinstance(n, (int, long)):\n```\n",
    "created_at": "2010-01-18T05:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42609",
    "user": "https://github.com/williamstein"
}
```


```
if type(n) == int or type(n)==long: 
```

should be

```
if isinstance(n, (int, long)):
```




---

archive/issue_comments_042610.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-18T05:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42610",
    "user": "https://github.com/williamstein"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_042611.json:
```json
{
    "body": "Also, use `obj.pyobject()` in some cases for symbolics...",
    "created_at": "2010-01-18T05:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42611",
    "user": "https://github.com/williamstein"
}
```

Also, use `obj.pyobject()` in some cases for symbolics...



---

archive/issue_comments_042612.json:
```json
{
    "body": "Third addendum, for one character change for lucas numbers",
    "created_at": "2010-01-18T05:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42612",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Third addendum, for one character change for lucas numbers



---

archive/issue_comments_042613.json:
```json
{
    "body": "Attachment [trac5496_lucas.patch](tarball://root/attachments/some-uuid/ticket5496/trac5496_lucas.patch) by spancratz created at 2010-01-18 06:01:59\n\nI've now incorporated the handling of symbolic expressions as suggested by Burcin.  The sequence of patches should be applied in the order\n\n- 5496.2.patch\n- trac5496_rationals_to_int.patch\n- trac5496_symbolic_expressions.patch\n- trac5496_lucas.patch\n- trac5496_symbolic_expressions2.patch\n\nI am running doctests now, but if they pass this should get positive review again.",
    "created_at": "2010-01-18T06:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42613",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac5496_lucas.patch](tarball://root/attachments/some-uuid/ticket5496/trac5496_lucas.patch) by spancratz created at 2010-01-18 06:01:59

I've now incorporated the handling of symbolic expressions as suggested by Burcin.  The sequence of patches should be applied in the order

- 5496.2.patch
- trac5496_rationals_to_int.patch
- trac5496_symbolic_expressions.patch
- trac5496_lucas.patch
- trac5496_symbolic_expressions2.patch

I am running doctests now, but if they pass this should get positive review again.



---

archive/issue_comments_042614.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-18T06:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42614",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042615.json:
```json
{
    "body": "Attachment [trac5496_symbolic_expressions2.patch](tarball://root/attachments/some-uuid/ticket5496/trac5496_symbolic_expressions2.patch) by spancratz created at 2010-01-18 06:06:58\n\nFourth addendum, for symbolic expressions",
    "created_at": "2010-01-18T06:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42615",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac5496_symbolic_expressions2.patch](tarball://root/attachments/some-uuid/ticket5496/trac5496_symbolic_expressions2.patch) by spancratz created at 2010-01-18 06:06:58

Fourth addendum, for symbolic expressions



---

archive/issue_comments_042616.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T06:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42616",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042617.json:
```json
{
    "body": "This is to confirm that all doctests have been passed, checked with \"./sage -t devel/sage/sage\".",
    "created_at": "2010-01-18T06:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42617",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

This is to confirm that all doctests have been passed, checked with "./sage -t devel/sage/sage".



---

archive/issue_comments_042618.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T01:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42618",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_005749.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2010-01-19T01:15:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5496#event-5749"
}
```
