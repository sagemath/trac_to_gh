# Issue 6040: Added Doctests for QuadraticForms methods

archive/issues_006040.json:
```json
{
    "body": "Assignee: justin\n\nCC:  mabshoff wstein @tornaria\n\nKeywords: quadraticform\n\nAdding Doctests to bring coverage up to 100% (coming soon).\n\nIssue created by migration from https://trac.sagemath.org/ticket/6040\n\n",
    "created_at": "2009-05-15T03:40:59Z",
    "labels": [
        "component: quadratic forms"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Added Doctests for QuadraticForms methods",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6040",
    "user": "https://github.com/jonhanke"
}
```
Assignee: justin

CC:  mabshoff wstein @tornaria

Keywords: quadraticform

Adding Doctests to bring coverage up to 100% (coming soon).

Issue created by migration from https://trac.sagemath.org/ticket/6040





---

archive/issue_comments_047999.json:
```json
{
    "body": "Attachment [patch-3__QF_misc_doctests__3.4.1.patch](tarball://root/attachments/some-uuid/ticket6040/patch-3__QF_misc_doctests__3.4.1.patch) by @jonhanke created at 2009-05-15 03:43:18\n\nNote:  There are currently two broken doctests in this patch (using the older routine IsPadic Square()), which should resolve themselves once Cremona's patch (Ticket #5834) is applied.",
    "created_at": "2009-05-15T03:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6040#issuecomment-47999",
    "user": "https://github.com/jonhanke"
}
```

Attachment [patch-3__QF_misc_doctests__3.4.1.patch](tarball://root/attachments/some-uuid/ticket6040/patch-3__QF_misc_doctests__3.4.1.patch) by @jonhanke created at 2009-05-15 03:43:18

Note:  There are currently two broken doctests in this patch (using the older routine IsPadic Square()), which should resolve themselves once Cremona's patch (Ticket #5834) is applied.



---

archive/issue_comments_048000.json:
```json
{
    "body": "Additional patch to bring QuadraticForm doctests to 100%.\n\nKnown Issues:\n    Several doctests fail because of the need for hilbert_symbol() to accept rational numbers, and similarly for IsPadicSquare().  These should be addressed by the changes made in Ticket #5834.",
    "created_at": "2009-05-15T11:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6040#issuecomment-48000",
    "user": "https://github.com/jonhanke"
}
```

Additional patch to bring QuadraticForm doctests to 100%.

Known Issues:
    Several doctests fail because of the need for hilbert_symbol() to accept rational numbers, and similarly for IsPadicSquare().  These should be addressed by the changes made in Ticket #5834.



---

archive/issue_comments_048001.json:
```json
{
    "body": "Attachment [patch-4__QF_more_doctests__3.4.1.patch](tarball://root/attachments/some-uuid/ticket6040/patch-4__QF_more_doctests__3.4.1.patch) by @jonhanke created at 2009-05-15 11:16:06",
    "created_at": "2009-05-15T11:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6040#issuecomment-48001",
    "user": "https://github.com/jonhanke"
}
```

Attachment [patch-4__QF_more_doctests__3.4.1.patch](tarball://root/attachments/some-uuid/ticket6040/patch-4__QF_more_doctests__3.4.1.patch) by @jonhanke created at 2009-05-15 11:16:06



---

archive/issue_comments_048002.json:
```json
{
    "body": "Together with #5954 this brings coverage in the QF code to 100%.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T11:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6040#issuecomment-48002",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Together with #5954 this brings coverage in the QF code to 100%.

Cheers,

Michael



---

archive/issue_comments_048003.json:
```json
{
    "body": "Also the patch in Ticket #6037 (rewrite and careful documentation of local density routines) is related to getting the doctest coverage to 100%.",
    "created_at": "2009-05-15T18:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6040#issuecomment-48003",
    "user": "https://github.com/jonhanke"
}
```

Also the patch in Ticket #6037 (rewrite and careful documentation of local density routines) is related to getting the doctest coverage to 100%.



---

archive/issue_comments_048004.json:
```json
{
    "body": "So, it turns out there are 4 patches in this series, and they must be applied in order. In particular, patch-3 depends on patch-2, which is at #6037, but I misunderstood that.\nThe correct sequence is to apply patch-1 in #5954, then patch-2 in #6037, then patch-3 and patch-4 in this ticket.\n\nIf that order is followed, the patch sequence applies cleanly to 3.4.1 as well as 4.0.alpha0.",
    "created_at": "2009-05-17T21:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6040#issuecomment-48004",
    "user": "https://github.com/tornaria"
}
```

So, it turns out there are 4 patches in this series, and they must be applied in order. In particular, patch-3 depends on patch-2, which is at #6037, but I misunderstood that.
The correct sequence is to apply patch-1 in #5954, then patch-2 in #6037, then patch-3 and patch-4 in this ticket.

If that order is followed, the patch sequence applies cleanly to 3.4.1 as well as 4.0.alpha0.



---

archive/issue_comments_048005.json:
```json
{
    "body": "Attachment [patch-5__QF_reviewer__4.0.alpha0.patch](tarball://root/attachments/some-uuid/ticket6040/patch-5__QF_reviewer__4.0.alpha0.patch) by @tornaria created at 2009-05-18 05:46:41\n\nfix doctests for 4.0.alpha0",
    "created_at": "2009-05-18T05:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6040#issuecomment-48005",
    "user": "https://github.com/tornaria"
}
```

Attachment [patch-5__QF_reviewer__4.0.alpha0.patch](tarball://root/attachments/some-uuid/ticket6040/patch-5__QF_reviewer__4.0.alpha0.patch) by @tornaria created at 2009-05-18 05:46:41

fix doctests for 4.0.alpha0



---

archive/issue_comments_048006.json:
```json
{
    "body": "Some doctests were broken on 4.0.alpha0 + patch-1 (#5954) + patch-2 (#6037) + patch-3 + patch-4.\n\nAll doctests pass for me when adding on top of that\n- attachment:patch-5__QF_reviewer__4.0.alpha0.patch\n- patch in #6059\n- patch in #6062\n- patch in #6064\n\nNote that the `patch-3__QF_misc_doctests__4.0.alpha0.patch` I uploaded earlier is a mistake, just ignore it.",
    "created_at": "2009-05-18T05:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6040#issuecomment-48006",
    "user": "https://github.com/tornaria"
}
```

Some doctests were broken on 4.0.alpha0 + patch-1 (#5954) + patch-2 (#6037) + patch-3 + patch-4.

All doctests pass for me when adding on top of that
- attachment:patch-5__QF_reviewer__4.0.alpha0.patch
- patch in #6059
- patch in #6062
- patch in #6064

Note that the `patch-3__QF_misc_doctests__4.0.alpha0.patch` I uploaded earlier is a mistake, just ignore it.



---

archive/issue_comments_048007.json:
```json
{
    "body": "Note: the patch-5 also adds a few \"#long time\" comments to file `quadratic_form__local_representation_conditions.py`. Skipping these reduces the time for doctesting the whole file from 48 s to 20 s.",
    "created_at": "2009-05-18T05:59:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6040#issuecomment-48007",
    "user": "https://github.com/tornaria"
}
```

Note: the patch-5 also adds a few "#long time" comments to file `quadratic_form__local_representation_conditions.py`. Skipping these reduces the time for doctesting the whole file from 48 s to 20 s.



---

archive/issue_comments_048008.json:
```json
{
    "body": "Add positive review due to Gonzalo.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-18T23:57:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6040#issuecomment-48008",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Add positive review due to Gonzalo.

Cheers,

Michael



---

archive/issue_comments_048009.json:
```json
{
    "body": "I'm ok with the positive review. I'll list the renamed/removed functions as for the other tickets, and I'll post a ticket to add compatibility functions with deprecation warnings.\n- `hanke_mass__maximal` was removed.\n- `GHY_mass_maximal` was renamed `GHY_mass__maximal`.\n- `conway_generic_mass` was removed.\n- `conway_p_mass_adjustment` was removed.\n- `local_diagonal` was removed.\n- `find_primitive_p_divisible_vector__all` was removed.",
    "created_at": "2009-05-19T00:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6040#issuecomment-48009",
    "user": "https://github.com/tornaria"
}
```

I'm ok with the positive review. I'll list the renamed/removed functions as for the other tickets, and I'll post a ticket to add compatibility functions with deprecation warnings.
- `hanke_mass__maximal` was removed.
- `GHY_mass_maximal` was renamed `GHY_mass__maximal`.
- `conway_generic_mass` was removed.
- `conway_p_mass_adjustment` was removed.
- `local_diagonal` was removed.
- `find_primitive_p_divisible_vector__all` was removed.



---

archive/issue_comments_048010.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T00:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6040#issuecomment-48010",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_events_006295.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-19T00:41:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6040",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6040#event-6295"
}
```



---

archive/issue_comments_048011.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T00:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6040#issuecomment-48011",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
