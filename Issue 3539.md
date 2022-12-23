# Issue 3539: bug in DirichletGroup -- bad code

archive/issues_003539.json:
```json
{
    "body": "Assignee: craigcitro\n\n\n```\nDear SAGE community,\n\nI am trying to compute characters for some finite fields.\n\nWith \"small\" fields, everything is fine:\n sage:   K=CyclotomicField(10);\n sage:   p=10151;\n sage:   Character=DirichletGroup(p,K);\n sage:   Khi=Character.0;\n sage:   Khi(7)\n zeta10\n\nHowever, with slightly larger fields:\n sage:   K=CyclotomicField(10);\n sage:   p=100151;\n sage:   Character=DirichletGroup(p,K);\n sage:   Khi=Character.0;\n sage:   Khi(7)\n ---------------------------------------------------------------------------\n AttributeError                            Traceback (most recent call\n last)\n\n /users/cacao/bissogae/<ipython console> in <module>()\n\n /localdisk/tmp/sage-3.0.3/local/lib/python2.5/site-packages/sage/modular/dirichlet.py\n in __call__(self, m)\n\n /localdisk/tmp/sage-3.0.3/local/lib/python2.5/site-packages/sage/modular/dirichlet.py\n in values(self)\n\n AttributeError: 'sage.rings.integer_mod.IntegerMod_int64' object has no\n attribute 'ivalue'\n\nIs there something I am missing?\n\nThanks,\n --Gaetan\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3539\n\n",
    "created_at": "2008-07-01T00:55:36Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "bug in DirichletGroup -- bad code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3539",
    "user": "was"
}
```
Assignee: craigcitro


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

archive/issue_comments_025011.json:
```json
{
    "body": "This is because `IntegerMod_int.ivalue` is cdef'ed public but `IntegerMod_int64.ivalue` isn't. The attached patch makes replaces the use of `ivalue` by the `__int___()` method. Timings are somewhat variable, but seem to suggest this makes the `values()` function about 2% slower for the p=10151,100151 cases reported.",
    "created_at": "2008-07-06T01:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-25011",
    "user": "wjp"
}
```

This is because `IntegerMod_int.ivalue` is cdef'ed public but `IntegerMod_int64.ivalue` isn't. The attached patch makes replaces the use of `ivalue` by the `__int___()` method. Timings are somewhat variable, but seem to suggest this makes the `values()` function about 2% slower for the p=10151,100151 cases reported.



---

archive/issue_comments_025012.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-06T01:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-25012",
    "user": "wjp"
}
```

Attachment



---

archive/issue_comments_025013.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-06T20:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-25013",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025014.json:
```json
{
    "body": "I'm adding a new patch, that is intended as a replacement of the old one. Rob Bradshaw suggseted that directly indexing with the integer mod n would actually be faster than using `n.ivalue` anyway -- on my machine, at least, they're nearly identical, with using `n` directly edging slightly ahead. This patch also includes a doctest to catch this in the future.",
    "created_at": "2008-07-06T20:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-25014",
    "user": "craigcitro"
}
```

I'm adding a new patch, that is intended as a replacement of the old one. Rob Bradshaw suggseted that directly indexing with the integer mod n would actually be faster than using `n.ivalue` anyway -- on my machine, at least, they're nearly identical, with using `n` directly edging slightly ahead. This patch also includes a doctest to catch this in the future.



---

archive/issue_comments_025015.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-06T20:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-25015",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_025016.json:
```json
{
    "body": "I forgot to mention this on the ticket -- credit should also go to wjp and robertwb.",
    "created_at": "2008-07-06T21:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-25016",
    "user": "craigcitro"
}
```

I forgot to mention this on the ticket -- credit should also go to wjp and robertwb.



---

archive/issue_comments_025017.json:
```json
{
    "body": "Merged trac-3539-new-patch.patch in Sage 3.0.4.alpha2",
    "created_at": "2008-07-07T01:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-25017",
    "user": "mabshoff"
}
```

Merged trac-3539-new-patch.patch in Sage 3.0.4.alpha2



---

archive/issue_comments_025018.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T01:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3539#issuecomment-25018",
    "user": "mabshoff"
}
```

Resolution: fixed
