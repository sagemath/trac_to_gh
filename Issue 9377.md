# Issue 9377: unable to coerce matrix over finite field into magma

archive/issues_009377.json:
```json
{
    "body": "Assignee: somebody\n\n```\nsage: F.<a>=GF(4)\nsage: m=matrix(2,[F(1),2,3,4])\nsage: magma(m) \n---------------------------------------------------------------------------\nTypeError  \n...\nTypeError: unable to coerce element into magma\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9377\n\n",
    "created_at": "2010-06-29T18:16:05Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "unable to coerce matrix over finite field into magma",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9377",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```
Assignee: somebody

```
sage: F.<a>=GF(4)
sage: m=matrix(2,[F(1),2,3,4])
sage: magma(m) 
---------------------------------------------------------------------------
TypeError  
...
TypeError: unable to coerce element into magma
```

Issue created by migration from https://trac.sagemath.org/ticket/9377





---

archive/issue_comments_088957.json:
```json
{
    "body": "I investigated a little bit. \n\n\nsage: m._magma_init_(Magma()) \n  --------------------------------------------------------------------------- \n AttributeError \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0Traceback (most recent  call \n last) \n... \n AttributeError: 'FiniteField_givaro' object has no attribute \n '_element_poly_repr' \n\n\nThe version of Magma on my system is \"V2.16-6\".",
    "created_at": "2010-06-30T06:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9377#issuecomment-88957",
    "user": "https://github.com/kwankyu"
}
```

I investigated a little bit. 


sage: m._magma_init_(Magma()) 
  --------------------------------------------------------------------------- 
 AttributeError                            Traceback (most recent  call 
 last) 
... 
 AttributeError: 'FiniteField_givaro' object has no attribute 
 '_element_poly_repr' 


The version of Magma on my system is "V2.16-6".



---

archive/issue_comments_088958.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-06-30T06:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9377#issuecomment-88958",
    "user": "https://github.com/kwankyu"
}
```

Changing priority from major to minor.



---

archive/issue_comments_088959.json:
```json
{
    "body": "Attachment [trac#9377.patch](tarball://root/attachments/some-uuid/ticket9377/trac#9377.patch) by @kwankyu created at 2010-07-10 03:28:00",
    "created_at": "2010-07-10T03:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9377#issuecomment-88959",
    "user": "https://github.com/kwankyu"
}
```

Attachment [trac#9377.patch](tarball://root/attachments/some-uuid/ticket9377/trac#9377.patch) by @kwankyu created at 2010-07-10 03:28:00



---

archive/issue_comments_088960.json:
```json
{
    "body": "The problem was with the finite field givaro implementation.",
    "created_at": "2010-07-10T03:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9377#issuecomment-88960",
    "user": "https://github.com/kwankyu"
}
```

The problem was with the finite field givaro implementation.



---

archive/issue_comments_088961.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-10T03:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9377#issuecomment-88961",
    "user": "https://github.com/kwankyu"
}
```

Changing status from new to needs_review.



---

archive/issue_events_023126.json:
```json
{
    "actor": "https://github.com/kwankyu",
    "created_at": "2010-07-10T03:30:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9377#event-23126"
}
```



---

archive/issue_comments_088962.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-12T19:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9377#issuecomment-88962",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_088963.json:
```json
{
    "body": "```\nUsing magma-2.16-11, I get the following with this patch\n\neno% ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: F.<a>=GF(4)\nsage: m=matrix(2,[F(1),2,3,4])\nsage: magma(m)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n| Sage Version 4.4.4.1, Release Date: 2010-06-28                     |\n| Type notebook() for the GUI, and license() for information.        |\n/home/mariah/sage/sage-4.4.4.1-x86_64-Linux-core2-fc-trac9377/<ipython console> in <module>()\n\n/home/mariah/sage/sage-4.4.4.1-x86_64-Linux-core2-fc-trac9377/local/lib/python2.6/site-packages/sage/interfaces/magma.pyc in __call__(self, x, gens)\n    735             pass\n    736         \n--> 737         A = Expect.__call__(self, x)\n    738         if has_cache:\n    739             x._magma_cache[self] = A\n   1034             return self._coerce_from_special_method(x)\n\n/home/mariah/sage/sage-4.4.4.1-x86_64-Linux-core2-fc-trac9377/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)\n   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:\n   1450                 self._session_number = -1\n-> 1451                 raise TypeError, x\n   1452         self._session_number = parent._session_number\n   1453 \n\nTypeError: Error evaluating Magma code.\nIN:_sage_[7]:=_sage_[3]![_sage_[4]!(1),_sage_[4]!(0),_sage_[4]!(1),_sage_[4]!(0)];\nOUT:\n>> _sage_[7]:=_sage_[3]![_sage_[4]!(1),_sage_[4]!(0),_sage_[4]!(1),_sage_[4]!(\n                       ^\nRuntime error in '!': Cannot coerce sequence element 1 into the coefficient ring\n\nsage: \n```",
    "created_at": "2010-07-12T19:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9377#issuecomment-88963",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

```
Using magma-2.16-11, I get the following with this patch

eno% ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: F.<a>=GF(4)
sage: m=matrix(2,[F(1),2,3,4])
sage: magma(m)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.4.4.1, Release Date: 2010-06-28                     |
| Type notebook() for the GUI, and license() for information.        |
/home/mariah/sage/sage-4.4.4.1-x86_64-Linux-core2-fc-trac9377/<ipython console> in <module>()

/home/mariah/sage/sage-4.4.4.1-x86_64-Linux-core2-fc-trac9377/local/lib/python2.6/site-packages/sage/interfaces/magma.pyc in __call__(self, x, gens)
    735             pass
    736         
--> 737         A = Expect.__call__(self, x)
    738         if has_cache:
    739             x._magma_cache[self] = A
   1034             return self._coerce_from_special_method(x)

/home/mariah/sage/sage-4.4.4.1-x86_64-Linux-core2-fc-trac9377/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1450                 self._session_number = -1
-> 1451                 raise TypeError, x
   1452         self._session_number = parent._session_number
   1453 

TypeError: Error evaluating Magma code.
IN:_sage_[7]:=_sage_[3]![_sage_[4]!(1),_sage_[4]!(0),_sage_[4]!(1),_sage_[4]!(0)];
OUT:
>> _sage_[7]:=_sage_[3]![_sage_[4]!(1),_sage_[4]!(0),_sage_[4]!(1),_sage_[4]!(
                       ^
Runtime error in '!': Cannot coerce sequence element 1 into the coefficient ring

sage: 
```



---

archive/issue_comments_088964.json:
```json
{
    "body": "Attachment [trac#9377_revised.patch](tarball://root/attachments/some-uuid/ticket9377/trac#9377_revised.patch) by @kwankyu created at 2010-07-13 01:57:22\n\ncontains the previous patch and more",
    "created_at": "2010-07-13T01:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9377#issuecomment-88964",
    "user": "https://github.com/kwankyu"
}
```

Attachment [trac#9377_revised.patch](tarball://root/attachments/some-uuid/ticket9377/trac#9377_revised.patch) by @kwankyu created at 2010-07-13 01:57:22

contains the previous patch and more



---

archive/issue_comments_088965.json:
```json
{
    "body": "Sorry for the incomplete patch. The revised patch fixes another bug in Sage that caused the error.",
    "created_at": "2010-07-13T02:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9377#issuecomment-88965",
    "user": "https://github.com/kwankyu"
}
```

Sorry for the incomplete patch. The revised patch fixes another bug in Sage that caused the error.



---

archive/issue_comments_088966.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-13T02:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9377#issuecomment-88966",
    "user": "https://github.com/kwankyu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_088967.json:
```json
{
    "body": "The revised patch fixes the reported problem.\n\nsage-4.4.4.1 with the revised patch passes all tests when I do \"make testlong\"\n\nsage-4.4.4.1 with the revised patch and using magma-2.16-11 has\nfewer doctest failures when I do \n\n```\n./sage -t -only_optional=magma devel/sage/sage \n```\nthan without the patch - and no new failures were introduced.\n\nPositive review!",
    "created_at": "2010-07-13T19:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9377#issuecomment-88967",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

The revised patch fixes the reported problem.

sage-4.4.4.1 with the revised patch passes all tests when I do "make testlong"

sage-4.4.4.1 with the revised patch and using magma-2.16-11 has
fewer doctest failures when I do 

```
./sage -t -only_optional=magma devel/sage/sage 
```
than without the patch - and no new failures were introduced.

Positive review!



---

archive/issue_comments_088968.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-13T19:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9377#issuecomment-88968",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088969.json:
```json
{
    "body": "Merged trac#9377_revised.patch in 4.5.2.alpha1.",
    "created_at": "2010-07-22T08:21:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9377#issuecomment-88969",
    "user": "https://github.com/dandrake"
}
```

Merged trac#9377_revised.patch in 4.5.2.alpha1.



---

archive/issue_events_023127.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-22T08:21:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9377#event-23127"
}
```



---

archive/issue_comments_088970.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T08:21:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9377#issuecomment-88970",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed
