# Issue 3736: pairwise_product fails for vectors over CDF

archive/issues_003736.json:
```json
{
    "body": "Assignee: malb\n\nCC:  bryan.head@gmail.com\n\n\n```\nsage: x = vector(CDF, range(10))\nsage: y = vector(CDF, range(10))\nsage: x.pa\nx.pairwise_product  x.parent            \nsage: x.pairwise_product(y)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/mike/src/combinat/branches/multisort-experiment/combinat/<ipython console> in <module>()\n\n/home/mike/src/combinat/branches/multisort-experiment/combinat/free_module_element.pyx in sage.modules.free_module_element.FreeModuleElement.pairwise_product (sage/modules/free_module_element.c:7363)()\n\n/home/mike/src/combinat/branches/multisort-experiment/combinat/element.pyx in sage.structure.element.Vector._pairwise_product_c (sage/structure/element.c:11073)()\n\n/home/mike/src/combinat/branches/multisort-experiment/combinat/element.pyx in sage.structure.element.Vector._pairwise_product_c_impl (sage/structure/element.c:11134)()\n\nTypeError: unsupported operation for 'Vector space of dimension 10 over Complex Double Field' and 'Vector space of dimension 10 over Complex Double Field'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3736\n\n",
    "created_at": "2008-07-29T00:22:13Z",
    "labels": [
        "commutative algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "pairwise_product fails for vectors over CDF",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3736",
    "user": "mhansen"
}
```
Assignee: malb

CC:  bryan.head@gmail.com


```
sage: x = vector(CDF, range(10))
sage: y = vector(CDF, range(10))
sage: x.pa
x.pairwise_product  x.parent            
sage: x.pairwise_product(y)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/mike/src/combinat/branches/multisort-experiment/combinat/<ipython console> in <module>()

/home/mike/src/combinat/branches/multisort-experiment/combinat/free_module_element.pyx in sage.modules.free_module_element.FreeModuleElement.pairwise_product (sage/modules/free_module_element.c:7363)()

/home/mike/src/combinat/branches/multisort-experiment/combinat/element.pyx in sage.structure.element.Vector._pairwise_product_c (sage/structure/element.c:11073)()

/home/mike/src/combinat/branches/multisort-experiment/combinat/element.pyx in sage.structure.element.Vector._pairwise_product_c_impl (sage/structure/element.c:11134)()

TypeError: unsupported operation for 'Vector space of dimension 10 over Complex Double Field' and 'Vector space of dimension 10 over Complex Double Field'
```


Issue created by migration from https://trac.sagemath.org/ticket/3736





---

archive/issue_comments_026519.json:
```json
{
    "body": "Attachment [trac_3736.patch](tarball://root/attachments/some-uuid/ticket3736/trac_3736.patch) by mhansen created at 2008-07-29 02:21:56",
    "created_at": "2008-07-29T02:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3736#issuecomment-26519",
    "user": "mhansen"
}
```

Attachment [trac_3736.patch](tarball://root/attachments/some-uuid/ticket3736/trac_3736.patch) by mhansen created at 2008-07-29 02:21:56



---

archive/issue_comments_026520.json:
```json
{
    "body": "Works well for me.",
    "created_at": "2008-08-09T07:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3736#issuecomment-26520",
    "user": "robertwb"
}
```

Works well for me.



---

archive/issue_comments_026521.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-10T03:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3736#issuecomment-26521",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha1



---

archive/issue_comments_026522.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-10T03:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3736#issuecomment-26522",
    "user": "mabshoff"
}
```

Resolution: fixed
