# Issue 1711: SIGSEGV in PolyBoRi

archive/issues_001711.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: sigsegv\n\nHow to reproduce:\n\n\n```\nsage: P.<a,b,c> = BooleanPolynomialRing(3,order='degrevlex')\nsage: list(a.set())\n```\n\n\nBacktrace:\n\n\n```\n#0  0x00002b62d02c9277 in std::deque<polybori::CCuddNavigator, std::allocator<polybori::CCuddNavigator> >::operator= (this=0x3073ba8, __x=@0x7fffedfa4268) at /usr/include/c++/4.2/bits/stl_algobase.h:283\n#1  0x00002b62d02ab7f8 in __pyx_pf_4sage_5rings_10polynomial_5pbori_8BooleSet___iter__ (__pyx_v_self=0x30d08d0) at /home/malb/SAGE/local/include/polybori/CTermStack.h:196\n#2  0x000000000041914f in PyObject_GetIter (o=0x30d08d0) at Objects/abstract.c:2350\n#3  0x00000000004382a5 in listextend (self=0x30d95f0, b=0x7fffedfa4268) at Objects/listobject.c:776\n#4  0x0000000000438837 in list_init (self=0x30d95f0, args=<value optimized out>, kw=<value optimized out>) at Objects/listobject.c:2372\n#5  0x000000000045cbd1 in type_call (type=0x721d60, args=0x30d0ed0, kwds=0x0) at Objects/typeobject.c:436\n#6  0x0000000000417bb3 in PyObject_Call (func=0xffffffffffffffc0, arg=0x7fffedfa4268, kw=0x3218e00) at Objects/abstract.c:1860\n...\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1711\n\n",
    "created_at": "2008-01-07T13:30:53Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "SIGSEGV in PolyBoRi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1711",
    "user": "https://github.com/malb"
}
```
Assignee: @burcin

Keywords: sigsegv

How to reproduce:


```
sage: P.<a,b,c> = BooleanPolynomialRing(3,order='degrevlex')
sage: list(a.set())
```


Backtrace:


```
#0  0x00002b62d02c9277 in std::deque<polybori::CCuddNavigator, std::allocator<polybori::CCuddNavigator> >::operator= (this=0x3073ba8, __x=@0x7fffedfa4268) at /usr/include/c++/4.2/bits/stl_algobase.h:283
#1  0x00002b62d02ab7f8 in __pyx_pf_4sage_5rings_10polynomial_5pbori_8BooleSet___iter__ (__pyx_v_self=0x30d08d0) at /home/malb/SAGE/local/include/polybori/CTermStack.h:196
#2  0x000000000041914f in PyObject_GetIter (o=0x30d08d0) at Objects/abstract.c:2350
#3  0x00000000004382a5 in listextend (self=0x30d95f0, b=0x7fffedfa4268) at Objects/listobject.c:776
#4  0x0000000000438837 in list_init (self=0x30d95f0, args=<value optimized out>, kw=<value optimized out>) at Objects/listobject.c:2372
#5  0x000000000045cbd1 in type_call (type=0x721d60, args=0x30d0ed0, kwds=0x0) at Objects/typeobject.c:436
#6  0x0000000000417bb3 in PyObject_Call (func=0xffffffffffffffc0, arg=0x7fffedfa4268, kw=0x3218e00) at Objects/abstract.c:1860
...
```


Issue created by migration from https://trac.sagemath.org/ticket/1711





---

archive/issue_comments_010817.json:
```json
{
    "body": "This is still a problem in Sage 2.10.",
    "created_at": "2008-01-19T20:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1711#issuecomment-10817",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is still a problem in Sage 2.10.



---

archive/issue_comments_010818.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-20T10:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1711#issuecomment-10818",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010819.json:
```json
{
    "body": "I'll look at this in more detail as part of an effort to make the iterators for the polybori wrapper look more uniform. \n\nFor now, I cannot figure out why this specific iterator fails, and the others don't.",
    "created_at": "2008-01-20T10:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1711#issuecomment-10819",
    "user": "https://github.com/burcin"
}
```

I'll look at this in more detail as part of an effort to make the iterators for the polybori wrapper look more uniform. 

For now, I cannot figure out why this specific iterator fails, and the others don't.



---

archive/issue_comments_010820.json:
```json
{
    "body": "Attachment [1711_BooleSet_iterator_workaround.patch](tarball://root/attachments/some-uuid/ticket1711/1711_BooleSet_iterator_workaround.patch) by @burcin created at 2008-03-07 10:10:26\n\nworkaround the crash by using BooleanPolynomial iterators",
    "created_at": "2008-03-07T10:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1711#issuecomment-10820",
    "user": "https://github.com/burcin"
}
```

Attachment [1711_BooleSet_iterator_workaround.patch](tarball://root/attachments/some-uuid/ticket1711/1711_BooleSet_iterator_workaround.patch) by @burcin created at 2008-03-07 10:10:26

workaround the crash by using BooleanPolynomial iterators



---

archive/issue_comments_010821.json:
```json
{
    "body": "attachment:1711_BooleSet_iterator_workaround.patch does not really fix the issue, but at least prevents the segfault.\n\nI think the patch should be applied before 2.10.3, and this ticket still kept open so we remember the problem.",
    "created_at": "2008-03-07T10:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1711#issuecomment-10821",
    "user": "https://github.com/burcin"
}
```

attachment:1711_BooleSet_iterator_workaround.patch does not really fix the issue, but at least prevents the segfault.

I think the patch should be applied before 2.10.3, and this ticket still kept open so we remember the problem.



---

archive/issue_comments_010822.json:
```json
{
    "body": "Works for me in rc2.",
    "created_at": "2008-03-07T10:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1711#issuecomment-10822",
    "user": "https://github.com/mwhansen"
}
```

Works for me in rc2.



---

archive/issue_comments_010823.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-07T15:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1711#issuecomment-10823",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010824.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc3",
    "created_at": "2008-03-07T15:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1711#issuecomment-10824",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc3
