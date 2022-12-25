# Issue 2674: Bug in modforms

archive/issues_002674.json:
```json
{
    "body": "Assignee: @williamstein\n\nReported by Jay Pottharst <sharlaon`@`gmail.com>:\n\n```\nsage: b=CuspForms(22).basis()\nsage: sum(b)\nTraceback (most recent call last):\n...\nNameError: global name 'other' is not defined\n```\n\nThis covers up a possibly larger problem:\n\n```\nsage: ssum=0\nsage: for u in b:\n...     ssum=(ssum+u)\n...\nTraceback (most recent call last):\n...\nTypeError: unsupported operand parent(s) for '+': 'Integer Ring' and\n'Cuspidal subspace of dimension 2 of Modular Forms space of dimension\n5 for Congruence Subgroup Gamma0(22) of weight 2 over Rational Field'\n```\n\n\nThe first problem is easily fixed.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2674\n\n",
    "created_at": "2008-03-26T16:37:12Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "Bug in modforms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2674",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @williamstein

Reported by Jay Pottharst <sharlaon`@`gmail.com>:

```
sage: b=CuspForms(22).basis()
sage: sum(b)
Traceback (most recent call last):
...
NameError: global name 'other' is not defined
```

This covers up a possibly larger problem:

```
sage: ssum=0
sage: for u in b:
...     ssum=(ssum+u)
...
Traceback (most recent call last):
...
TypeError: unsupported operand parent(s) for '+': 'Integer Ring' and
'Cuspidal subspace of dimension 2 of Modular Forms space of dimension
5 for Congruence Subgroup Gamma0(22) of weight 2 over Rational Field'
```


The first problem is easily fixed.



Issue created by migration from https://trac.sagemath.org/ticket/2674





---

archive/issue_comments_018361.json:
```json
{
    "body": "Fix for the first of the two reported problms.",
    "created_at": "2008-03-26T16:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2674#issuecomment-18361",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Fix for the first of the two reported problms.



---

archive/issue_events_006247.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-03-26T18:03:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2674",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2674#event-6247"
}
```



---

archive/issue_comments_018362.json:
```json
{
    "body": "Attachment [modbug.patch](tarball://root/attachments/some-uuid/ticket2674/modbug.patch) by @williamstein created at 2008-03-26 18:03:40\n\nI disagree that the second issue is a bug:\n\n```\n\nNote that \n\n  b[0] + 0\n\nand \n\n  0 + b[0]\n\nshould *not* work, since in each case that's a canonical coercion,\nand there is no natural map from ZZ (the parent of 0) into CuspForms(...)\nfor any weight except 0.   In Sage coercions should not happen automatically\nunless they are in some way natural and well defined on the whole domain\nof the coercion (in this case ZZ).\n```\n",
    "created_at": "2008-03-26T18:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2674#issuecomment-18362",
    "user": "https://github.com/williamstein"
}
```

Attachment [modbug.patch](tarball://root/attachments/some-uuid/ticket2674/modbug.patch) by @williamstein created at 2008-03-26 18:03:40

I disagree that the second issue is a bug:

```

Note that 

  b[0] + 0

and 

  0 + b[0]

should *not* work, since in each case that's a canonical coercion,
and there is no natural map from ZZ (the parent of 0) into CuspForms(...)
for any weight except 0.   In Sage coercions should not happen automatically
unless they are in some way natural and well defined on the whole domain
of the coercion (in this case ZZ).
```




---

archive/issue_comments_018363.json:
```json
{
    "body": "Attachment [trac-2674.patch](tarball://root/attachments/some-uuid/ticket2674/trac-2674.patch) by @craigcitro created at 2008-03-26 18:34:31\n\nThis new patch fixes the first issue reported above, as well as making the natural coercion from a subspace of modular forms into its parent work. \n\nInterestingly, this makes the second issue work, too.\n\nSo I'm not sure whether or not I like that this second issue works, because I agree with William's point that it should only work if there is a coercion from ZZ to a space of ModularForms. However, it's working \"for free\" for us, because it ultimately uses that the following works:\n\n\n```\nsage: M = ZZ**5\nsage: M(0)\n(0, 0, 0, 0, 0)\nsage: M(1)\n...\n<type 'exceptions.TypeError'>: can't initialize vector from nonzero non-list\n```\n\n\nThe issue is that a free module knows how to coerce 0 in, but no other integer (even when the module is rank 1 over ZZ, which I think is a good thing). So we could easily change it to make William's expectations correct by changing free modules, where the same issue arises.",
    "created_at": "2008-03-26T18:34:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2674#issuecomment-18363",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2674.patch](tarball://root/attachments/some-uuid/ticket2674/trac-2674.patch) by @craigcitro created at 2008-03-26 18:34:31

This new patch fixes the first issue reported above, as well as making the natural coercion from a subspace of modular forms into its parent work. 

Interestingly, this makes the second issue work, too.

So I'm not sure whether or not I like that this second issue works, because I agree with William's point that it should only work if there is a coercion from ZZ to a space of ModularForms. However, it's working "for free" for us, because it ultimately uses that the following works:


```
sage: M = ZZ**5
sage: M(0)
(0, 0, 0, 0, 0)
sage: M(1)
...
<type 'exceptions.TypeError'>: can't initialize vector from nonzero non-list
```


The issue is that a free module knows how to coerce 0 in, but no other integer (even when the module is rank 1 over ZZ, which I think is a good thing). So we could easily change it to make William's expectations correct by changing free modules, where the same issue arises.



---

archive/issue_comments_018364.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2008-03-26T22:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2674#issuecomment-18364",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_018365.json:
```json
{
    "body": "Attachment [trac-2674-pt2.patch](tarball://root/attachments/some-uuid/ticket2674/trac-2674-pt2.patch) by @craigcitro created at 2008-03-26 22:56:23\n\nApply the bottom two patches in order, and this should also make coercion from `ModularForms(Gamma0(N))` to `ModularForms(Gamma0(Nd))` work. Note that it's currently *not* going to work involving `Gamma1(N)` -- this is because of a bug in `sturm_bound` (namely that it assumes it's working on `Gamma0`); I'm going to file another ticket for this, because I don't have time to fix it right now.",
    "created_at": "2008-03-26T22:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2674#issuecomment-18365",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2674-pt2.patch](tarball://root/attachments/some-uuid/ticket2674/trac-2674-pt2.patch) by @craigcitro created at 2008-03-26 22:56:23

Apply the bottom two patches in order, and this should also make coercion from `ModularForms(Gamma0(N))` to `ModularForms(Gamma0(Nd))` work. Note that it's currently *not* going to work involving `Gamma1(N)` -- this is because of a bug in `sturm_bound` (namely that it assumes it's working on `Gamma0`); I'm going to file another ticket for this, because I don't have time to fix it right now.



---

archive/issue_comments_018366.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-26T22:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2674#issuecomment-18366",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018367.json:
```json
{
    "body": "Nice work. Apply only the second two patches in order (they do more than just fix this bug).",
    "created_at": "2008-03-26T23:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2674#issuecomment-18367",
    "user": "https://github.com/robertwb"
}
```

Nice work. Apply only the second two patches in order (they do more than just fix this bug).



---

archive/issue_comments_018368.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-26T23:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2674#issuecomment-18368",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006248.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-26T23:18:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2674",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2674#event-6248"
}
```



---

archive/issue_comments_018369.json:
```json
{
    "body": "Merged trac-2674.patch and trac-2674-pt2.patch in Sage 2.11.alpha2",
    "created_at": "2008-03-26T23:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2674#issuecomment-18369",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac-2674.patch and trac-2674-pt2.patch in Sage 2.11.alpha2
