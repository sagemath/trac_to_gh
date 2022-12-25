# Issue 721: refactoring ell_rational_field

archive/issues_000721.json:
```json
{
    "body": "Assignee: @roed314\n\nell_rational_field is too big.  I therefore propose the following changes.\n\n1.  Create an ell_nf as a common parent for ell_rational_field and ell_number_field.  Factor up as many functions as possible.\n\n2.  Create an Lseries_ell class in sage/schemes/elliptic_curves/lseries_ell.py, and factor out the L-series functions to there (Lseries_dokchitser, Lseries_sympow, Lseries_sympow_derivs, Lseries_zeros, Lseries_zeros_in_interval, Lseries_values_along_line, Lseries_twist_values, Lseries_twist_zeros, Lseries_at1, Lseries_deriv_at1, Lseries, Lseries_extended, L1_vanishes, Lratio, ).\n\n3.  Create a Sha_group class (inheriting from AbelianGroup).  Move the functions (sha_an_numerical, sha_an, sha_an_padic, sha_p_primary_bound, two_selmer_shabound, shabound_kolyvagin, shabound_kato, shabound) to this new class.\n\nIssue created by migration from https://trac.sagemath.org/ticket/721\n\n",
    "created_at": "2007-09-20T22:32:45Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "refactoring ell_rational_field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/721",
    "user": "https://github.com/roed314"
}
```
Assignee: @roed314

ell_rational_field is too big.  I therefore propose the following changes.

1.  Create an ell_nf as a common parent for ell_rational_field and ell_number_field.  Factor up as many functions as possible.

2.  Create an Lseries_ell class in sage/schemes/elliptic_curves/lseries_ell.py, and factor out the L-series functions to there (Lseries_dokchitser, Lseries_sympow, Lseries_sympow_derivs, Lseries_zeros, Lseries_zeros_in_interval, Lseries_values_along_line, Lseries_twist_values, Lseries_twist_zeros, Lseries_at1, Lseries_deriv_at1, Lseries, Lseries_extended, L1_vanishes, Lratio, ).

3.  Create a Sha_group class (inheriting from AbelianGroup).  Move the functions (sha_an_numerical, sha_an, sha_an_padic, sha_p_primary_bound, two_selmer_shabound, shabound_kolyvagin, shabound_kato, shabound) to this new class.

Issue created by migration from https://trac.sagemath.org/ticket/721





---

archive/issue_comments_004180.json:
```json
{
    "body": "please apply #635 before doing this!",
    "created_at": "2007-09-20T22:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4180",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

please apply #635 before doing this!



---

archive/issue_comments_004181.json:
```json
{
    "body": "Splits ell_rational_field, work in progress on Tate's algorithm",
    "created_at": "2007-10-01T19:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4181",
    "user": "https://github.com/roed314"
}
```

Splits ell_rational_field, work in progress on Tate's algorithm



---

archive/issue_comments_004182.json:
```json
{
    "body": "Attachment [6557.patch](tarball://root/attachments/some-uuid/ticket721/6557.patch) by @williamstein created at 2007-10-02 03:51:34\n\nTHIS is the one you *really* want to apply!",
    "created_at": "2007-10-02T03:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4182",
    "user": "https://github.com/williamstein"
}
```

Attachment [6557.patch](tarball://root/attachments/some-uuid/ticket721/6557.patch) by @williamstein created at 2007-10-02 03:51:34

THIS is the one you *really* want to apply!



---

archive/issue_comments_004183.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-02T03:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4183",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000802.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-02T03:52:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/721#event-802"
}
```



---

archive/issue_comments_004184.json:
```json
{
    "body": "Actually, the patch I just posted is completely broken.  Re-opening the ticket!",
    "created_at": "2007-10-02T04:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4184",
    "user": "https://github.com/williamstein"
}
```

Actually, the patch I just posted is completely broken.  Re-opening the ticket!



---

archive/issue_comments_004185.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-10-02T04:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4185",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_004186.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-02T04:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4186",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_000803.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-02T04:08:21Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/721#event-803"
}
```



---

archive/issue_comments_004187.json:
```json
{
    "body": "Do not apply any of the above patches yet!!!!",
    "created_at": "2007-10-04T17:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4187",
    "user": "https://github.com/williamstein"
}
```

Do not apply any of the above patches yet!!!!



---

archive/issue_comments_004188.json:
```json
{
    "body": "Attachment [ell_curves.hg](tarball://root/attachments/some-uuid/ticket721/ell_curves.hg) by @roed314 created at 2007-10-05 12:51:32\n\nThis one is even better.",
    "created_at": "2007-10-05T12:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4188",
    "user": "https://github.com/roed314"
}
```

Attachment [ell_curves.hg](tarball://root/attachments/some-uuid/ticket721/ell_curves.hg) by @roed314 created at 2007-10-05 12:51:32

This one is even better.



---

archive/issue_comments_004189.json:
```json
{
    "body": "Hello,\n\nthe patch doesn't apply cleanly to 2.8.6, so please rebase and try again.\n\nYou should also delete obsolte version of the patch.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-13T03:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4189",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hello,

the patch doesn't apply cleanly to 2.8.6, so please rebase and try again.

You should also delete obsolte version of the patch.

Cheers,

Michael



---

archive/issue_comments_004190.json:
```json
{
    "body": "Bundled against 2.8.6, with additional material (added ntl ZZ_pE and ZZ_pEX)",
    "created_at": "2007-10-13T07:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4190",
    "user": "https://github.com/roed314"
}
```

Bundled against 2.8.6, with additional material (added ntl ZZ_pE and ZZ_pEX)



---

archive/issue_events_000804.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-13T07:46:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/721#event-804"
}
```



---

archive/issue_comments_004191.json:
```json
{
    "body": "Attachment [ntl_and_ell.hg](tarball://root/attachments/some-uuid/ticket721/ntl_and_ell.hg) by @williamstein created at 2007-10-13 07:46:08",
    "created_at": "2007-10-13T07:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4191",
    "user": "https://github.com/williamstein"
}
```

Attachment [ntl_and_ell.hg](tarball://root/attachments/some-uuid/ticket721/ntl_and_ell.hg) by @williamstein created at 2007-10-13 07:46:08



---

archive/issue_comments_004192.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/721#issuecomment-4192",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
