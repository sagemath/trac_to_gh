# Issue 3601: Reimplementation of tensor products

archive/issues_003601.json:
```json
{
    "body": "Assignee: Mike Hansen\n\nCC:  sage-combinat-commits@googlegroups.com\n\nKeywords: tensor products of crystals\n\nI split TensorProductOfCrystals into TensorProductOfCrystalsWithGenerators and\nFullTensorProductOfCrystals (with or without the option of being a classical crystal).\nThis makes it possible to have a more efficient way to access list, count, etc for \ntensor products that do not have module generators.\n\nAlso, the distinction between the specifications of module_generators and \nhighest_weight_vectors is made more precise (which made it necessary to slightly \nchange the implementation of Daniel Bump on characters).\n\nThis change is necessary for the upcoming implementation of affine crystals.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3601\n\n",
    "created_at": "2008-07-08T03:30:36Z",
    "labels": [
        "component: combinatorics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "Reimplementation of tensor products",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3601",
    "user": "https://github.com/anneschilling"
}
```
Assignee: Mike Hansen

CC:  sage-combinat-commits@googlegroups.com

Keywords: tensor products of crystals

I split TensorProductOfCrystals into TensorProductOfCrystalsWithGenerators and
FullTensorProductOfCrystals (with or without the option of being a classical crystal).
This makes it possible to have a more efficient way to access list, count, etc for 
tensor products that do not have module generators.

Also, the distinction between the specifications of module_generators and 
highest_weight_vectors is made more precise (which made it necessary to slightly 
change the implementation of Daniel Bump on characters).

This change is necessary for the upcoming implementation of affine crystals.

Issue created by migration from https://trac.sagemath.org/ticket/3601





---

archive/issue_comments_025402.json:
```json
{
    "body": "Attachment [tensor_product-for_trac.patch](tarball://root/attachments/some-uuid/ticket3601/tensor_product-for_trac.patch) by @anneschilling created at 2008-07-08 03:39:19",
    "created_at": "2008-07-08T03:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3601#issuecomment-25402",
    "user": "https://github.com/anneschilling"
}
```

Attachment [tensor_product-for_trac.patch](tarball://root/attachments/some-uuid/ticket3601/tensor_product-for_trac.patch) by @anneschilling created at 2008-07-08 03:39:19



---

archive/issue_comments_025403.json:
```json
{
    "body": "Attachment [tensor_product-3601-review.patch](tarball://root/attachments/some-uuid/ticket3601/tensor_product-3601-review.patch) by @mwhansen created at 2008-07-09 20:46:43\n\nHi Anne,\n\nI added a few doctests and fixed some whitespace issues (there were tabs instead of spaces).  If you're fine with these changes, I'll go ahead and give it a positive review so it can get merged.\n\n--Mike",
    "created_at": "2008-07-09T20:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3601#issuecomment-25403",
    "user": "https://github.com/mwhansen"
}
```

Attachment [tensor_product-3601-review.patch](tarball://root/attachments/some-uuid/ticket3601/tensor_product-3601-review.patch) by @mwhansen created at 2008-07-09 20:46:43

Hi Anne,

I added a few doctests and fixed some whitespace issues (there were tabs instead of spaces).  If you're fine with these changes, I'll go ahead and give it a positive review so it can get merged.

--Mike



---

archive/issue_comments_025404.json:
```json
{
    "body": "Hi Mike,\n\nYes, your changes look fine to me (I wonder how the tabs instead of \nspaces happened to be wrong?).\n\nAnne",
    "created_at": "2008-07-09T21:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3601#issuecomment-25404",
    "user": "https://github.com/anneschilling"
}
```

Hi Mike,

Yes, your changes look fine to me (I wonder how the tabs instead of 
spaces happened to be wrong?).

Anne



---

archive/issue_comments_025405.json:
```json
{
    "body": "I'm not sure.  Usually the editor picks that up just fine.",
    "created_at": "2008-07-09T21:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3601#issuecomment-25405",
    "user": "https://github.com/mwhansen"
}
```

I'm not sure.  Usually the editor picks that up just fine.



---

archive/issue_comments_025406.json:
```json
{
    "body": "Anne, Mike,\n\nto be 100% clear: both patches should be applied in this case?\n\nCheers,\n\nMichael",
    "created_at": "2008-07-10T01:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3601#issuecomment-25406",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Anne, Mike,

to be 100% clear: both patches should be applied in this case?

Cheers,

Michael



---

archive/issue_comments_025407.json:
```json
{
    "body": "Yes, both patches.",
    "created_at": "2008-07-10T01:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3601#issuecomment-25407",
    "user": "https://github.com/mwhansen"
}
```

Yes, both patches.



---

archive/issue_events_003820.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-16T03:51:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3601",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3601#event-3820"
}
```



---

archive/issue_comments_025408.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-16T03:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3601#issuecomment-25408",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.6.alpha0



---

archive/issue_comments_025409.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-16T03:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3601#issuecomment-25409",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
