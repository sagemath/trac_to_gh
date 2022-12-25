# Issue 3539: [with patch, positive review] bug in DirichletGroup -- bad code

archive/issues_003539.json:
```json
{
    "body": "Assignee: @craigcitro\n\n```\nDear SAGE community,\n\nI am trying to compute characters for some finite fields.\n\nWith \"small\" fields, everything is fine:\n sage:   K=CyclotomicField(10);\n sage:   p=10151;\n sage:   Character=DirichletGroup(p,K);\n sage:   Khi=Character.0;\n sage:   Khi(7)\n zeta10\n\nHowever, with slightly larger fields:\n sage:   K=CyclotomicField(10);\n sage:   p=100151;\n sage:   Character=DirichletGroup(p,K);\n sage:   Khi=Character.0;\n sage:   Khi(7)\n ---------------------------------------------------------------------------\n AttributeError                            Traceback (most recent call\n last)\n\n /users/cacao/bissogae/<ipython console> in <module>()\n\n /localdisk/tmp/sage-3.0.3/local/lib/python2.5/site-packages/sage/modular/dirichlet.py\n in __call__(self, m)\n\n /localdisk/tmp/sage-3.0.3/local/lib/python2.5/site-packages/sage/modular/dirichlet.py\n in values(self)\n\n AttributeError: 'sage.rings.integer_mod.IntegerMod_int64' object has no\n attribute 'ivalue'\n\nIs there something I am missing?\n\nThanks,\n --Gaetan\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3539\n\n",
    "closed_at": "2008-07-07T01:39:44Z",
    "created_at": "2008-07-01T00:55:36Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, positive review] bug in DirichletGroup -- bad code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3539",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro

```
Dear SAGE community,

I am trying to compute characters for some finite fields.

With "small" fields, everything is fine:
 sage:   K=CyclotomicField(10);
 sage:   p=10151;
 sage:   Character=DirichletGroup(p,K);
 sage:   Khi=Character.0;
 sage:   Khi(7)
 zeta10

However, with slightly larger fields:
 sage:   K=CyclotomicField(10);
 sage:   p=100151;
 sage:   Character=DirichletGroup(p,K);
 sage:   Khi=Character.0;
 sage:   Khi(7)
 ---------------------------------------------------------------------------
 AttributeError                            Traceback (most recent call
 last)

 /users/cacao/bissogae/<ipython console> in <module>()

 /localdisk/tmp/sage-3.0.3/local/lib/python2.5/site-packages/sage/modular/dirichlet.py
 in __call__(self, m)

 /localdisk/tmp/sage-3.0.3/local/lib/python2.5/site-packages/sage/modular/dirichlet.py
 in values(self)

 AttributeError: 'sage.rings.integer_mod.IntegerMod_int64' object has no
 attribute 'ivalue'

Is there something I am missing?

Thanks,
 --Gaetan
```

Issue created by migration from https://trac.sagemath.org/ticket/3539





---

archive/issue_comments_024961.json:
```json
{
    "body": "This is because `IntegerMod_int.ivalue` is cdef'ed public but `IntegerMod_int64.ivalue` isn't. The attached patch makes replaces the use of `ivalue` by the `__int___()` method. Timings are somewhat variable, but seem to suggest this makes the `values()` function about 2% slower for the p=10151,100151 cases reported.",
    "created_at": "2008-07-06T01:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-24961",
    "user": "https://github.com/wjp"
}
```

This is because `IntegerMod_int.ivalue` is cdef'ed public but `IntegerMod_int64.ivalue` isn't. The attached patch makes replaces the use of `ivalue` by the `__int___()` method. Timings are somewhat variable, but seem to suggest this makes the `values()` function about 2% slower for the p=10151,100151 cases reported.



---

archive/issue_comments_024962.json:
```json
{
    "body": "Attachment [trac3539_ivalue_to_int.patch](tarball://root/attachments/some-uuid/ticket3539/trac3539_ivalue_to_int.patch) by @wjp created at 2008-07-06 01:28:18",
    "created_at": "2008-07-06T01:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-24962",
    "user": "https://github.com/wjp"
}
```

Attachment [trac3539_ivalue_to_int.patch](tarball://root/attachments/some-uuid/ticket3539/trac3539_ivalue_to_int.patch) by @wjp created at 2008-07-06 01:28:18



---

archive/issue_comments_024963.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-06T20:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-24963",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024964.json:
```json
{
    "body": "I'm adding a new patch, that is intended as a replacement of the old one. Rob Bradshaw suggseted that directly indexing with the integer mod n would actually be faster than using `n.ivalue` anyway -- on my machine, at least, they're nearly identical, with using `n` directly edging slightly ahead. This patch also includes a doctest to catch this in the future.",
    "created_at": "2008-07-06T20:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-24964",
    "user": "https://github.com/craigcitro"
}
```

I'm adding a new patch, that is intended as a replacement of the old one. Rob Bradshaw suggseted that directly indexing with the integer mod n would actually be faster than using `n.ivalue` anyway -- on my machine, at least, they're nearly identical, with using `n` directly edging slightly ahead. This patch also includes a doctest to catch this in the future.



---

archive/issue_comments_024965.json:
```json
{
    "body": "Attachment [trac-3539-new-patch.patch](tarball://root/attachments/some-uuid/ticket3539/trac-3539-new-patch.patch) by @craigcitro created at 2008-07-06 20:51:22",
    "created_at": "2008-07-06T20:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-24965",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-3539-new-patch.patch](tarball://root/attachments/some-uuid/ticket3539/trac-3539-new-patch.patch) by @craigcitro created at 2008-07-06 20:51:22



---

archive/issue_comments_024966.json:
```json
{
    "body": "I forgot to mention this on the ticket -- credit should also go to wjp and robertwb.",
    "created_at": "2008-07-06T21:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-24966",
    "user": "https://github.com/craigcitro"
}
```

I forgot to mention this on the ticket -- credit should also go to wjp and robertwb.



---

archive/issue_comments_024967.json:
```json
{
    "body": "Merged trac-3539-new-patch.patch in Sage 3.0.4.alpha2",
    "created_at": "2008-07-07T01:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-24967",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac-3539-new-patch.patch in Sage 3.0.4.alpha2



---

archive/issue_comments_024968.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T01:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-24968",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008090.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-07T01:39:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3539#event-8090"
}
```
