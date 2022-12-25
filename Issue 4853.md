# Issue 4853: Sage 3.2.2: numerical noise in sage/rings/number_field/number_field_morphisms.pyx

archive/issues_004853.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is cicero on SkyNet with gcc 4.3.2:\n\n```\nsage -t  \"devel/sage/sage/rings/number_field/number_field_morphisms.pyx\"\n**********************************************************************\nFile \"/home/mariah/sage/sage-3.2.2-x86-Linux-fc/devel/sage/sage/rings/number_field/number_field_morphisms.pyx\",\nline 44:\n    sage: sigma_a = K.polynomial().change_ring(CC).roots()[1][0]; sigma_a\nExpected:\n    -0.629960524947436 + 1.09112363597172*I\nGot:\n    -0.629960524947437 + 1.09112363597172*I\n**********************************************************************\nFile \"/home/mariah/sage/sage-3.2.2-x86-Linux-fc/devel/sage/sage/rings/number_field/number_field_morphisms.pyx\",\nline 47:\n    sage: g(a+1)\nExpected:\n    0.370039475052564 + 1.09112363597172*I\nGot:\n    0.370039475052563 + 1.09112363597172*I\n**********************************************************************\n```\n\n\nPatch coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4853\n\n",
    "created_at": "2008-12-22T18:50:02Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "Sage 3.2.2: numerical noise in sage/rings/number_field/number_field_morphisms.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4853",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

This is cicero on SkyNet with gcc 4.3.2:

```
sage -t  "devel/sage/sage/rings/number_field/number_field_morphisms.pyx"
**********************************************************************
File "/home/mariah/sage/sage-3.2.2-x86-Linux-fc/devel/sage/sage/rings/number_field/number_field_morphisms.pyx",
line 44:
    sage: sigma_a = K.polynomial().change_ring(CC).roots()[1][0]; sigma_a
Expected:
    -0.629960524947436 + 1.09112363597172*I
Got:
    -0.629960524947437 + 1.09112363597172*I
**********************************************************************
File "/home/mariah/sage/sage-3.2.2-x86-Linux-fc/devel/sage/sage/rings/number_field/number_field_morphisms.pyx",
line 47:
    sage: g(a+1)
Expected:
    0.370039475052564 + 1.09112363597172*I
Got:
    0.370039475052563 + 1.09112363597172*I
**********************************************************************
```


Patch coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4853





---

archive/issue_comments_036724.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-22T22:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4853#issuecomment-36724",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036725.json:
```json
{
    "body": "Note the difference:\n\n```\n    -0.629960524947436 + 1.09112363597172*I\n    -0.629960524947437 + 1.09112363597172*I\n```\n\nand\n\n```\n    0.370039475052564 + 1.09112363597172*I\n    0.370039475052563 + 1.09112363597172*I\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-12-22T22:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4853#issuecomment-36725",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Note the difference:

```
    -0.629960524947436 + 1.09112363597172*I
    -0.629960524947437 + 1.09112363597172*I
```

and

```
    0.370039475052564 + 1.09112363597172*I
    0.370039475052563 + 1.09112363597172*I
```


Cheers,

Michael



---

archive/issue_comments_036726.json:
```json
{
    "body": "Attachment [trac_4853.patch](tarball://root/attachments/some-uuid/ticket4853/trac_4853.patch) by @rlmill created at 2008-12-23 23:11:30\n\n+1 \u00b1 0.000001",
    "created_at": "2008-12-23T23:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4853#issuecomment-36726",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_4853.patch](tarball://root/attachments/some-uuid/ticket4853/trac_4853.patch) by @rlmill created at 2008-12-23 23:11:30

+1 ± 0.000001



---

archive/issue_comments_036727.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-23T23:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4853#issuecomment-36727",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.alpha0



---

archive/issue_comments_036728.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-23T23:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4853#issuecomment-36728",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
