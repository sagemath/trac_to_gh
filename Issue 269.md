# Issue 269: add floordiv, mod, invert, pow to arithmetic architecture (at least in RingElement)

archive/issues_000269.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @videlec\n\nSo far we only have add, sub, neg, various versions of mul, and div.\n\nWe also need floordiv, mod, invert, pow.\n\nThese would be very useful in p-adics, and need to happen for other reasons too.\n\nIssue created by migration from https://trac.sagemath.org/ticket/269\n\n",
    "created_at": "2007-02-17T22:43:30Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.3",
    "title": "add floordiv, mod, invert, pow to arithmetic architecture (at least in RingElement)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/269",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

CC:  @videlec

So far we only have add, sub, neg, various versions of mul, and div.

We also need floordiv, mod, invert, pow.

These would be very useful in p-adics, and need to happen for other reasons too.

Issue created by migration from https://trac.sagemath.org/ticket/269





---

archive/issue_comments_001257.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-08-18T09:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1257",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_001258.json:
```json
{
    "body": "Replying to [ticket:269 dmharvey]:\n> So far we only have add, sub, neg, various versions of mul, and div.\n> \n> We also need floordiv, mod, invert, pow.\n> \n> These would be very useful in p-adics, and need to happen for other reasons too.\n\nIs exact division (that is, division where the caller knows that there is no remainder) common enough to belong here?  (There's an implementation for Integer already, where the method is called divide_knowing_divisible_by() and calls mpz_divexact().)",
    "created_at": "2007-10-06T19:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1258",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Replying to [ticket:269 dmharvey]:
> So far we only have add, sub, neg, various versions of mul, and div.
> 
> We also need floordiv, mod, invert, pow.
> 
> These would be very useful in p-adics, and need to happen for other reasons too.

Is exact division (that is, division where the caller knows that there is no remainder) common enough to belong here?  (There's an implementation for Integer already, where the method is called divide_knowing_divisible_by() and calls mpz_divexact().)



---

archive/issue_comments_001259.json:
```json
{
    "body": "Replying to [comment:3 cwitty]:\n> Replying to [ticket:269 dmharvey]:\n> > So far we only have add, sub, neg, various versions of mul, and div.\n> > \n> > We also need floordiv, mod, invert, pow.\n> > \n> > These would be very useful in p-adics, and need to happen for other reasons too.\n> \n> Is exact division (that is, division where the caller knows that there is no remainder) common enough to belong here?  (There's an implementation for Integer already, where the method is called divide_knowing_divisible_by() and calls mpz_divexact().)\n\nI definitely think that exact division should be included in the arithmetic architecture.  This is not because it's common, but because there is a bunch of daft coercion code in most !__floordiv!__ implementations.  All this needs to be fixed and the fix is a common boiler-plate prefix on these functions.  Or, a much better alternative is to include it in the arithmetic hierarchy and write that boilerplate coercion once at the head of the tree.\n\nI think that gcd (and maybe xgcd) should also be on this list.",
    "created_at": "2008-03-19T12:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1259",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Replying to [comment:3 cwitty]:
> Replying to [ticket:269 dmharvey]:
> > So far we only have add, sub, neg, various versions of mul, and div.
> > 
> > We also need floordiv, mod, invert, pow.
> > 
> > These would be very useful in p-adics, and need to happen for other reasons too.
> 
> Is exact division (that is, division where the caller knows that there is no remainder) common enough to belong here?  (There's an implementation for Integer already, where the method is called divide_knowing_divisible_by() and calls mpz_divexact().)

I definitely think that exact division should be included in the arithmetic architecture.  This is not because it's common, but because there is a bunch of daft coercion code in most !__floordiv!__ implementations.  All this needs to be fixed and the fix is a common boiler-plate prefix on these functions.  Or, a much better alternative is to include it in the arithmetic hierarchy and write that boilerplate coercion once at the head of the tree.

I think that gcd (and maybe xgcd) should also be on this list.



---

archive/issue_comments_001260.json:
```json
{
    "body": "Oh, and quo_rem should be here too -- #383",
    "created_at": "2008-03-19T12:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1260",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Oh, and quo_rem should be here too -- #383



---

archive/issue_comments_001261.json:
```json
{
    "body": "Changing component from basic arithmetic to coercion.",
    "created_at": "2016-01-19T17:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1261",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from basic arithmetic to coercion.



---

archive/issue_comments_001262.json:
```json
{
    "body": "Jeroen, what is the rationale for\n\n```\ncpdef _mod_(self, Element other)\n```\n\ninstead of\n\n```\ncpdef Element _mod_(self, Element other)\n```\n\nIn a situtation like `e1._mod_(e2)._add_(e3)` Cython would be happier. No?",
    "created_at": "2016-01-22T12:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1262",
    "user": "https://github.com/videlec"
}
```

Jeroen, what is the rationale for

```
cpdef _mod_(self, Element other)
```

instead of

```
cpdef Element _mod_(self, Element other)
```

In a situtation like `e1._mod_(e2)._add_(e3)` Cython would be happier. No?



---

archive/issue_comments_001263.json:
```json
{
    "body": "Replying to [comment:19 vdelecroix]:\n> In a situtation like `e1._mod_(e2)._add_(e3)` Cython would be happier. No?\n\nSure, but I don't know how common that is.\n\nI want to avoid unneeded checking. If you do something like\n\n```\ncpdef Element _foo_(self, other):\n    x = ...\n    return x\n```\n\nthen Cython will add a check that `x` is actually of type `Element`. I think (but this is just a wild guess) that the slow-down of these extra checks does not justify the few cases where the check might improve performance.",
    "created_at": "2016-01-22T12:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1263",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:19 vdelecroix]:
> In a situtation like `e1._mod_(e2)._add_(e3)` Cython would be happier. No?

Sure, but I don't know how common that is.

I want to avoid unneeded checking. If you do something like

```
cpdef Element _foo_(self, other):
    x = ...
    return x
```

then Cython will add a check that `x` is actually of type `Element`. I think (but this is just a wild guess) that the slow-down of these extra checks does not justify the few cases where the check might improve performance.



---

archive/issue_comments_001264.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-01-22T13:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1264",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_001265.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-01-22T13:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1265",
    "user": "https://github.com/jdemeyer"
}
```

New commits:



---

archive/issue_comments_001266.json:
```json
{
    "body": "Does not apply on last beta.",
    "created_at": "2016-03-11T20:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1266",
    "user": "https://github.com/videlec"
}
```

Does not apply on last beta.



---

archive/issue_comments_001267.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-03-11T20:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1267",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_001268.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2016-05-31T15:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1268",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_001269.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-05-31T15:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1269",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_001270.json:
```json
{
    "body": "About [comment:19 comment:19] I guess that the rationale is that we should follow what was done until now. If you want to change the `cpdef` methods without declaring them as `Element` or `ModuleElement` or whatever I guess you should open a new ticket.",
    "created_at": "2016-05-31T16:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1270",
    "user": "https://github.com/videlec"
}
```

About [comment:19 comment:19] I guess that the rationale is that we should follow what was done until now. If you want to change the `cpdef` methods without declaring them as `Element` or `ModuleElement` or whatever I guess you should open a new ticket.



---

archive/issue_comments_001271.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2016-06-05T09:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1271",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_001272.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2016-06-14T11:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1272",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_001273.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2016-06-14T11:43:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1273",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_001274.json:
```json
{
    "body": "Please, add doctests for `__mod__` in `sage.rings.finite_rings.integer_mod`.",
    "created_at": "2016-07-13T15:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1274",
    "user": "https://github.com/videlec"
}
```

Please, add doctests for `__mod__` in `sage.rings.finite_rings.integer_mod`.



---

archive/issue_comments_001275.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-07-13T15:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1275",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_001276.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-14T16:37:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1276",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_001277.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2016-07-14T16:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1277",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_001278.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-07-14T16:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1278",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_001279.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-15T09:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1279",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_001280.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-07-25T01:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1280",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_001281.json:
```json
{
    "body": "Thanks!",
    "created_at": "2016-07-25T07:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1281",
    "user": "https://github.com/jdemeyer"
}
```

Thanks!



---

archive/issue_events_000284.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2016-07-27T20:24:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/269#event-284"
}
```



---

archive/issue_comments_001282.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-07-27T20:24:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/269#issuecomment-1282",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
