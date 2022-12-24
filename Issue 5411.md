# Issue 5411: QuadraticForm: implement clifford_invariant and replace hasse_conductor with clifford_conductor

archive/issues_005411.json:
```json
{
    "body": "Assignee: gonzalo\n\nThe `hasse_invariant` of a quadratic form doesn't match the standard invariant (brauer class) for quaternion algebras (e.g. for ternary quadratic forms, the ramification of the corresponding quaternion algebra).\n\nThe `clifford_invariant` can defined in terms of the clifford algebra of the quadratic form. See Lam (AMS GSM 67) p. 117 for the definition, and p. 119 for the formula relating it to the Hasse invariant.\n\nIt also has the property that hyperbolic spaces have `clifford_invariant == +1` at all primes.\n\nIt also makes more sense to define a `clifford_conductor` instead of a `hasse_conductor` as the product of all the primes with `clifford_invariant == -1`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5411\n\n",
    "created_at": "2009-03-01T15:30:07Z",
    "labels": [
        "quadratic forms",
        "major",
        "enhancement"
    ],
    "title": "QuadraticForm: implement clifford_invariant and replace hasse_conductor with clifford_conductor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5411",
    "user": "tornaria"
}
```
Assignee: gonzalo

The `hasse_invariant` of a quadratic form doesn't match the standard invariant (brauer class) for quaternion algebras (e.g. for ternary quadratic forms, the ramification of the corresponding quaternion algebra).

The `clifford_invariant` can defined in terms of the clifford algebra of the quadratic form. See Lam (AMS GSM 67) p. 117 for the definition, and p. 119 for the formula relating it to the Hasse invariant.

It also has the property that hyperbolic spaces have `clifford_invariant == +1` at all primes.

It also makes more sense to define a `clifford_conductor` instead of a `hasse_conductor` as the product of all the primes with `clifford_invariant == -1`.

Issue created by migration from https://trac.sagemath.org/ticket/5411





---

archive/issue_comments_041833.json:
```json
{
    "body": "Attachment [patch.5411.clifford_invariant](tarball://root/attachments/some-uuid/ticket5411/patch.5411.clifford_invariant) by tornaria created at 2009-03-01 15:33:47",
    "created_at": "2009-03-01T15:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41833",
    "user": "tornaria"
}
```

Attachment [patch.5411.clifford_invariant](tarball://root/attachments/some-uuid/ticket5411/patch.5411.clifford_invariant) by tornaria created at 2009-03-01 15:33:47



---

archive/issue_comments_041834.json:
```json
{
    "body": "same file with correct name",
    "created_at": "2009-03-01T16:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41834",
    "user": "tornaria"
}
```

same file with correct name



---

archive/issue_comments_041835.json:
```json
{
    "body": "Attachment [trac_5411.clifford_invariant.patch](tarball://root/attachments/some-uuid/ticket5411/trac_5411.clifford_invariant.patch) by tornaria created at 2009-03-01 16:04:31",
    "created_at": "2009-03-01T16:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41835",
    "user": "tornaria"
}
```

Attachment [trac_5411.clifford_invariant.patch](tarball://root/attachments/some-uuid/ticket5411/trac_5411.clifford_invariant.patch) by tornaria created at 2009-03-01 16:04:31



---

archive/issue_comments_041836.json:
```json
{
    "body": "Changing assignee from gonzalo to tornaria.",
    "created_at": "2009-03-01T16:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41836",
    "user": "tornaria"
}
```

Changing assignee from gonzalo to tornaria.



---

archive/issue_comments_041837.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-01T16:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41837",
    "user": "tornaria"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041838.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T03:41:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41838",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_041839.json:
```json
{
    "body": "Jon expressed some further wishes, so \"needs review\" again for now :-)\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T03:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41839",
    "user": "mabshoff"
}
```

Jon expressed some further wishes, so "needs review" again for now :-)

Cheers,

Michael



---

archive/issue_comments_041840.json:
```json
{
    "body": "replaces previous patch --- this one doesn't remove hasse_conductor",
    "created_at": "2009-03-02T04:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41840",
    "user": "tornaria"
}
```

replaces previous patch --- this one doesn't remove hasse_conductor



---

archive/issue_comments_041841.json:
```json
{
    "body": "Attachment [trac_5411.clifford_invariant.2nd.patch](tarball://root/attachments/some-uuid/ticket5411/trac_5411.clifford_invariant.2nd.patch) by tornaria created at 2009-03-02 04:24:33\n\nThe new patch (2nd patch) preserves `hasse_conductor` as requested by Jon, and it also fixes the imports in `quadratic_form.py`, so it is meant to be applied on top of #5403.",
    "created_at": "2009-03-02T04:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41841",
    "user": "tornaria"
}
```

Attachment [trac_5411.clifford_invariant.2nd.patch](tarball://root/attachments/some-uuid/ticket5411/trac_5411.clifford_invariant.2nd.patch) by tornaria created at 2009-03-02 04:24:33

The new patch (2nd patch) preserves `hasse_conductor` as requested by Jon, and it also fixes the imports in `quadratic_form.py`, so it is meant to be applied on top of #5403.



---

archive/issue_comments_041842.json:
```json
{
    "body": "Looks good.  Positive review.",
    "created_at": "2009-03-02T05:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41842",
    "user": "jonhanke"
}
```

Looks good.  Positive review.



---

archive/issue_comments_041843.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-02T06:37:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41843",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041844.json:
```json
{
    "body": "Merged trac_5411.clifford_invariant.2nd.patch in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T06:37:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5411#issuecomment-41844",
    "user": "mabshoff"
}
```

Merged trac_5411.clifford_invariant.2nd.patch in Sage 3.4.rc0.

Cheers,

Michael
