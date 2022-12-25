# Issue 8722: S-units sometimes broken and sometimes just plain wrong for relative fields

archive/issues_008722.json:
```json
{
    "body": "Assignee: @loefflerd\n\n\n```\nsage: L.<a,b> = NumberField([x^2 + 1, x^2 - 5])\nsage: p = L.ideal((-1/2*b - 1/2)*a + 1/2*b - 1/2)\nsage: p.absolute_norm()\n9\nsage: p.is_prime()\nTrue\nsage: W = L.S_units([p]); W\n[1/2*a + 7/4, a, 1/2*b - 1/2]\nsage: W[0].valuation(L.primes_above(2)[0])\n-4\n```\n\nSo the first element of the list of S-units isn't actually an S-unit! In other examples the code just blows up, because it calls `residue_field` and that dies because of #8721:\n\n```\nsage: L.<a, b> = NumberField([polygen(QQ)^2 - 3, polygen(QQ)^2 - 5])\nsage: L.S_units([L.ideal(a)])\n```\n\nThis is arguably less bad: raising an error is far better than silently a wrong answer.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8722\n\n",
    "created_at": "2010-04-20T09:09:57Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "S-units sometimes broken and sometimes just plain wrong for relative fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8722",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @loefflerd


```
sage: L.<a,b> = NumberField([x^2 + 1, x^2 - 5])
sage: p = L.ideal((-1/2*b - 1/2)*a + 1/2*b - 1/2)
sage: p.absolute_norm()
9
sage: p.is_prime()
True
sage: W = L.S_units([p]); W
[1/2*a + 7/4, a, 1/2*b - 1/2]
sage: W[0].valuation(L.primes_above(2)[0])
-4
```

So the first element of the list of S-units isn't actually an S-unit! In other examples the code just blows up, because it calls `residue_field` and that dies because of #8721:

```
sage: L.<a, b> = NumberField([polygen(QQ)^2 - 3, polygen(QQ)^2 - 5])
sage: L.S_units([L.ideal(a)])
```

This is arguably less bad: raising an error is far better than silently a wrong answer.

Issue created by migration from https://trac.sagemath.org/ticket/8722





---

archive/issue_comments_079520.json:
```json
{
    "body": "Here's a patch. Turns out that the code was using `K.gen` and the correct answer is to call `K.absolute_generator`, which isn't the same in the above example. This fixes the first example; the second is an instance of #8721.",
    "created_at": "2010-04-20T09:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8722#issuecomment-79520",
    "user": "https://github.com/loefflerd"
}
```

Here's a patch. Turns out that the code was using `K.gen` and the correct answer is to call `K.absolute_generator`, which isn't the same in the above example. This fixes the first example; the second is an instance of #8721.



---

archive/issue_comments_079521.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-20T09:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8722#issuecomment-79521",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079522.json:
```json
{
    "body": "Attachment [trac_8722.patch](tarball://root/attachments/some-uuid/ticket8722/trac_8722.patch) by @loefflerd created at 2010-04-20 09:56:16\n\napply over patches at #8446",
    "created_at": "2010-04-20T09:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8722#issuecomment-79522",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_8722.patch](tarball://root/attachments/some-uuid/ticket8722/trac_8722.patch) by @loefflerd created at 2010-04-20 09:56:16

apply over patches at #8446



---

archive/issue_comments_079523.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-21T08:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8722#issuecomment-79523",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079524.json:
```json
{
    "body": "Looks good, applied fine to 4.4.alpha0 + #8446 patches, and all tests in sage/rings/number_field pass.\n\nPositive review!",
    "created_at": "2010-04-21T08:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8722#issuecomment-79524",
    "user": "https://github.com/JohnCremona"
}
```

Looks good, applied fine to 4.4.alpha0 + #8446 patches, and all tests in sage/rings/number_field pass.

Positive review!



---

archive/issue_comments_079525.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-23T17:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8722#issuecomment-79525",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_021169.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-23T17:09:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8722#event-21169"
}
```



---

archive/issue_comments_079526.json:
```json
{
    "body": "Merged into 4.4.alpha2.",
    "created_at": "2010-04-23T17:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8722#issuecomment-79526",
    "user": "https://github.com/jhpalmieri"
}
```

Merged into 4.4.alpha2.



---

archive/issue_events_021170.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-04-24T12:45:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "milestone": "sage-4.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8722#event-21170"
}
```
