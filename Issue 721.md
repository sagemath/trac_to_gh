# Issue 721: refactoring ell_rational_field

archive/issues_000721.json:
```json
{
    "body": "Assignee: roed\n\nell_rational_field is too big.  I therefore propose the following changes.\n\n1.  Create an ell_nf as a common parent for ell_rational_field and ell_number_field.  Factor up as many functions as possible.\n\n2.  Create an Lseries_ell class in sage/schemes/elliptic_curves/lseries_ell.py, and factor out the L-series functions to there (Lseries_dokchitser, Lseries_sympow, Lseries_sympow_derivs, Lseries_zeros, Lseries_zeros_in_interval, Lseries_values_along_line, Lseries_twist_values, Lseries_twist_zeros, Lseries_at1, Lseries_deriv_at1, Lseries, Lseries_extended, L1_vanishes, Lratio, ).\n\n3.  Create a Sha_group class (inheriting from AbelianGroup).  Move the functions (sha_an_numerical, sha_an, sha_an_padic, sha_p_primary_bound, two_selmer_shabound, shabound_kolyvagin, shabound_kato, shabound) to this new class.\n\nIssue created by migration from https://trac.sagemath.org/ticket/721\n\n",
    "created_at": "2007-09-20T22:32:45Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "refactoring ell_rational_field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/721",
    "user": "roed"
}
```
Assignee: roed

ell_rational_field is too big.  I therefore propose the following changes.

1.  Create an ell_nf as a common parent for ell_rational_field and ell_number_field.  Factor up as many functions as possible.

2.  Create an Lseries_ell class in sage/schemes/elliptic_curves/lseries_ell.py, and factor out the L-series functions to there (Lseries_dokchitser, Lseries_sympow, Lseries_sympow_derivs, Lseries_zeros, Lseries_zeros_in_interval, Lseries_values_along_line, Lseries_twist_values, Lseries_twist_zeros, Lseries_at1, Lseries_deriv_at1, Lseries, Lseries_extended, L1_vanishes, Lratio, ).

3.  Create a Sha_group class (inheriting from AbelianGroup).  Move the functions (sha_an_numerical, sha_an, sha_an_padic, sha_p_primary_bound, two_selmer_shabound, shabound_kolyvagin, shabound_kato, shabound) to this new class.

Issue created by migration from https://trac.sagemath.org/ticket/721





---

archive/issue_comments_004193.json:
```json
{
    "body": "please apply #635 before doing this!",
    "created_at": "2007-09-20T22:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4193",
    "user": "dmharvey"
}
```

please apply #635 before doing this!



---

archive/issue_comments_004194.json:
```json
{
    "body": "Splits ell_rational_field, work in progress on Tate's algorithm",
    "created_at": "2007-10-01T19:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4194",
    "user": "roed"
}
```

Splits ell_rational_field, work in progress on Tate's algorithm



---

archive/issue_comments_004195.json:
```json
{
    "body": "Attachment\n\nTHIS is the one you *really* want to apply!",
    "created_at": "2007-10-02T03:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4195",
    "user": "was"
}
```

Attachment

THIS is the one you *really* want to apply!



---

archive/issue_comments_004196.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-02T03:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4196",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_004197.json:
```json
{
    "body": "Actually, the patch I just posted is completely broken.  Re-opening the ticket!",
    "created_at": "2007-10-02T04:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4197",
    "user": "was"
}
```

Actually, the patch I just posted is completely broken.  Re-opening the ticket!



---

archive/issue_comments_004198.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-10-02T04:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4198",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_004199.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-02T04:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4199",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_004200.json:
```json
{
    "body": "Do not apply any of the above patches yet!!!!",
    "created_at": "2007-10-04T17:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4200",
    "user": "was"
}
```

Do not apply any of the above patches yet!!!!



---

archive/issue_comments_004201.json:
```json
{
    "body": "Attachment\n\nThis one is even better.",
    "created_at": "2007-10-05T12:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4201",
    "user": "roed"
}
```

Attachment

This one is even better.



---

archive/issue_comments_004202.json:
```json
{
    "body": "Hello,\n\nthe patch doesn't apply cleanly to 2.8.6, so please rebase and try again.\n\nYou should also delete obsolte version of the patch.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-13T03:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4202",
    "user": "mabshoff"
}
```

Hello,

the patch doesn't apply cleanly to 2.8.6, so please rebase and try again.

You should also delete obsolte version of the patch.

Cheers,

Michael



---

archive/issue_comments_004203.json:
```json
{
    "body": "Bundled against 2.8.6, with additional material (added ntl ZZ_pE and ZZ_pEX)",
    "created_at": "2007-10-13T07:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4203",
    "user": "roed"
}
```

Bundled against 2.8.6, with additional material (added ntl ZZ_pE and ZZ_pEX)



---

archive/issue_comments_004204.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-10-13T07:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4204",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_004205.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4205",
    "user": "was"
}
```

Resolution: fixed
