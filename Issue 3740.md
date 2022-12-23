# Issue 3740: sage-3.0.6 blocker -- pickle jar -- exactly one failure

archive/issues_003740.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  mhansen\n\n\n```\nsage: sage.structure.sage_object.unpickle_all('pickle_jar-3.0.3')\n** failed:  _class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj\nFailed:\n_class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj\nSuccessfully unpickled 355 objects.\nFailed to unpickle 1 objects.\n```\n\n\nEmail to sage-combinat-devel:\n\n```\nHi,\n\nThe only object from sage-3.0.3 that doesn't unpickle in sage-3.0.3.final is \n\n-----------------------\nsage: sage.structure.sage_object.unpickle_all('pickle_jar-3.0.3')\n** failed:  _class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj\nFailed:\n_class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj\nSuccessfully unpickled 355 objects.\nFailed to unpickle 1 objects.\n-----------------------\n\nI don't know anything about the stability of TensorProductOfCrystals.    I've attached the sobj\nthat doesn't unpickle.  This was pickled using sage-3.0.3 because of a loads/dumps doctest.\nPlease clarify if you want to fix this problem ASAP, or consider this to be a nonissue because\nyou consider that particular code unstable.\n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3740\n\n",
    "created_at": "2008-07-29T14:58:24Z",
    "labels": [
        "misc",
        "blocker",
        "bug"
    ],
    "title": "sage-3.0.6 blocker -- pickle jar -- exactly one failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3740",
    "user": "was"
}
```
Assignee: cwitty

CC:  mhansen


```
sage: sage.structure.sage_object.unpickle_all('pickle_jar-3.0.3')
** failed:  _class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj
Failed:
_class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj
Successfully unpickled 355 objects.
Failed to unpickle 1 objects.
```


Email to sage-combinat-devel:

```
Hi,

The only object from sage-3.0.3 that doesn't unpickle in sage-3.0.3.final is 

-----------------------
sage: sage.structure.sage_object.unpickle_all('pickle_jar-3.0.3')
** failed:  _class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj
Failed:
_class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj
Successfully unpickled 355 objects.
Failed to unpickle 1 objects.
-----------------------

I don't know anything about the stability of TensorProductOfCrystals.    I've attached the sobj
that doesn't unpickle.  This was pickled using sage-3.0.3 because of a loads/dumps doctest.
Please clarify if you want to fix this problem ASAP, or consider this to be a nonissue because
you consider that particular code unstable.

 -- William
```


Issue created by migration from https://trac.sagemath.org/ticket/3740





---

archive/issue_comments_026569.json:
```json
{
    "body": "Presumably the same bug:\n\n\n```\nsage: C = CrystalOfLetters(['A',3])\nsage: v = C.list()[0]\nsage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])\nsage: T == loads(dumps(T))\n```\n\n\nReturns an exception.",
    "created_at": "2008-07-30T00:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3740#issuecomment-26569",
    "user": "bump"
}
```

Presumably the same bug:


```
sage: C = CrystalOfLetters(['A',3])
sage: v = C.list()[0]
sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])
sage: T == loads(dumps(T))
```


Returns an exception.



---

archive/issue_comments_026570.json:
```json
{
    "body": "This is no longer valid\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sage: C = CrystalOfLetters(['A',3])\nsage: sage: v = C.list()[0]\nsage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])\nsage: sage: T == loads(dumps(T))\nTrue\nsage: sage: C = CrystalOfLetters(['A',3])\nsage: sage: v = C.list()[0]\nsage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])\nsage: sage: T == loads(dumps(T))\nTrue\nsage: sage: C = CrystalOfLetters(['A',3])\nsage: sage: v = C.list()[0]\nsage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])\nsage: sage: T == loads(dumps(T))\nTrue\n```\n",
    "created_at": "2009-06-04T20:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3740#issuecomment-26570",
    "user": "mhansen"
}
```

This is no longer valid


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: C = CrystalOfLetters(['A',3])
sage: sage: v = C.list()[0]
sage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])
sage: sage: T == loads(dumps(T))
True
sage: sage: C = CrystalOfLetters(['A',3])
sage: sage: v = C.list()[0]
sage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])
sage: sage: T == loads(dumps(T))
True
sage: sage: C = CrystalOfLetters(['A',3])
sage: sage: v = C.list()[0]
sage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])
sage: sage: T == loads(dumps(T))
True
```




---

archive/issue_comments_026571.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-04T20:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3740#issuecomment-26571",
    "user": "mhansen"
}
```

Resolution: invalid
