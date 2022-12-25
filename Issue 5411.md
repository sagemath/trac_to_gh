# Issue 5411: [with patch, positive review] QuadraticForm: implement clifford_invariant and replace hasse_conductor with clifford_conductor

archive/issues_005411.json:
```json
{
    "body": "Assignee: @tornaria\n\nThe `hasse_invariant` of a quadratic form doesn't match the standard invariant (brauer class) for quaternion algebras (e.g. for ternary quadratic forms, the ramification of the corresponding quaternion algebra).\n\nThe `clifford_invariant` can defined in terms of the clifford algebra of the quadratic form. See Lam (AMS GSM 67) p. 117 for the definition, and p. 119 for the formula relating it to the Hasse invariant.\n\nIt also has the property that hyperbolic spaces have `clifford_invariant == +1` at all primes.\n\nIt also makes more sense to define a `clifford_conductor` instead of a `hasse_conductor` as the product of all the primes with `clifford_invariant == -1`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5411\n\n",
    "closed_at": "2009-03-02T06:37:17Z",
    "created_at": "2009-03-01T15:30:07Z",
    "labels": [
        "component: quadratic forms"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, positive review] QuadraticForm: implement clifford_invariant and replace hasse_conductor with clifford_conductor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5411",
    "user": "https://github.com/tornaria"
}
```
Assignee: @tornaria

The `hasse_invariant` of a quadratic form doesn't match the standard invariant (brauer class) for quaternion algebras (e.g. for ternary quadratic forms, the ramification of the corresponding quaternion algebra).

The `clifford_invariant` can defined in terms of the clifford algebra of the quadratic form. See Lam (AMS GSM 67) p. 117 for the definition, and p. 119 for the formula relating it to the Hasse invariant.

It also has the property that hyperbolic spaces have `clifford_invariant == +1` at all primes.

It also makes more sense to define a `clifford_conductor` instead of a `hasse_conductor` as the product of all the primes with `clifford_invariant == -1`.

Issue created by migration from https://trac.sagemath.org/ticket/5411





---

archive/issue_comments_041751.json:
```json
{
    "body": "Attachment [patch.5411.clifford_invariant](tarball://root/attachments/some-uuid/ticket5411/patch.5411.clifford_invariant) by @tornaria created at 2009-03-01 15:33:47",
    "created_at": "2009-03-01T15:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41751",
    "user": "https://github.com/tornaria"
}
```

Attachment [patch.5411.clifford_invariant](tarball://root/attachments/some-uuid/ticket5411/patch.5411.clifford_invariant) by @tornaria created at 2009-03-01 15:33:47



---

archive/issue_comments_041752.json:
```json
{
    "body": "same file with correct name",
    "created_at": "2009-03-01T16:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41752",
    "user": "https://github.com/tornaria"
}
```

same file with correct name



---

archive/issue_comments_041753.json:
```json
{
    "body": "Attachment [trac_5411.clifford_invariant.patch](tarball://root/attachments/some-uuid/ticket5411/trac_5411.clifford_invariant.patch) by @tornaria created at 2009-03-01 16:04:31",
    "created_at": "2009-03-01T16:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41753",
    "user": "https://github.com/tornaria"
}
```

Attachment [trac_5411.clifford_invariant.patch](tarball://root/attachments/some-uuid/ticket5411/trac_5411.clifford_invariant.patch) by @tornaria created at 2009-03-01 16:04:31



---

archive/issue_comments_041754.json:
```json
{
    "body": "Changing assignee from gonzalo to @tornaria.",
    "created_at": "2009-03-01T16:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41754",
    "user": "https://github.com/tornaria"
}
```

Changing assignee from gonzalo to @tornaria.



---

archive/issue_comments_041755.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-01T16:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41755",
    "user": "https://github.com/tornaria"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041756.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T03:41:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41756",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_041757.json:
```json
{
    "body": "Jon expressed some further wishes, so \"needs review\" again for now :-)\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T03:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41757",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Jon expressed some further wishes, so "needs review" again for now :-)

Cheers,

Michael



---

archive/issue_comments_041758.json:
```json
{
    "body": "replaces previous patch --- this one doesn't remove hasse_conductor",
    "created_at": "2009-03-02T04:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41758",
    "user": "https://github.com/tornaria"
}
```

replaces previous patch --- this one doesn't remove hasse_conductor



---

archive/issue_comments_041759.json:
```json
{
    "body": "Attachment [trac_5411.clifford_invariant.2nd.patch](tarball://root/attachments/some-uuid/ticket5411/trac_5411.clifford_invariant.2nd.patch) by @tornaria created at 2009-03-02 04:24:33\n\nThe new patch (2nd patch) preserves `hasse_conductor` as requested by Jon, and it also fixes the imports in `quadratic_form.py`, so it is meant to be applied on top of #5403.",
    "created_at": "2009-03-02T04:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41759",
    "user": "https://github.com/tornaria"
}
```

Attachment [trac_5411.clifford_invariant.2nd.patch](tarball://root/attachments/some-uuid/ticket5411/trac_5411.clifford_invariant.2nd.patch) by @tornaria created at 2009-03-02 04:24:33

The new patch (2nd patch) preserves `hasse_conductor` as requested by Jon, and it also fixes the imports in `quadratic_form.py`, so it is meant to be applied on top of #5403.



---

archive/issue_comments_041760.json:
```json
{
    "body": "Looks good.  Positive review.",
    "created_at": "2009-03-02T05:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41760",
    "user": "https://github.com/jonhanke"
}
```

Looks good.  Positive review.



---

archive/issue_events_012594.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-02T06:37:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5411#event-12594"
}
```



---

archive/issue_comments_041761.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-02T06:37:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41761",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041762.json:
```json
{
    "body": "Merged trac_5411.clifford_invariant.2nd.patch in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T06:37:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41762",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_5411.clifford_invariant.2nd.patch in Sage 3.4.rc0.

Cheers,

Michael
