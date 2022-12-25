# Issue 5340: NTL "context"s can be restored at the wrong time, leading to randomly-wrong answers

archive/issues_005340.json:
```json
{
    "body": "Assignee: cwitty\n\nI should have a fix for this very soon.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5340\n\n",
    "created_at": "2009-02-22T20:03:58Z",
    "labels": [
        "component: number theory",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "NTL \"context\"s can be restored at the wrong time, leading to randomly-wrong answers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5340",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

I should have a fix for this very soon.

Issue created by migration from https://trac.sagemath.org/ticket/5340





---

archive/issue_comments_041060.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-22T20:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5340#issuecomment-41060",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041061.json:
```json
{
    "body": "The problem is that `__dealloc__` can happen at \"random\" times (whenever the garbage collector happens to trigger), so it must not have global side-effects.\n\nTo the reviewer: Note that the NTL documentation explicitly says you don't need to have the correct context when you destroy an object:\n\n```\nNote, however, that if a GF2E object is created under one modulus \nand then used in any way (except destroyed) under another, \nprogram behavior is not predictable.\n```\n\nEssentially identical language occurs in the documentation for lzz_pE, lzz_p, ZZ_pE, and ZZ_p.\n\nI fixed 9 potential instances of the problem, but only added a doctest for one of them; you'll understand why when you see how hard it is to doctest.\n\nAll doctests pass.\n\nThis is based on sage-3.3 + ReST patches, but I think it would probably apply without the ReST patches just fine.",
    "created_at": "2009-02-22T20:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5340#issuecomment-41061",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

The problem is that `__dealloc__` can happen at "random" times (whenever the garbage collector happens to trigger), so it must not have global side-effects.

To the reviewer: Note that the NTL documentation explicitly says you don't need to have the correct context when you destroy an object:

```
Note, however, that if a GF2E object is created under one modulus 
and then used in any way (except destroyed) under another, 
program behavior is not predictable.
```

Essentially identical language occurs in the documentation for lzz_pE, lzz_p, ZZ_pE, and ZZ_p.

I fixed 9 potential instances of the problem, but only added a doctest for one of them; you'll understand why when you see how hard it is to doctest.

All doctests pass.

This is based on sage-3.3 + ReST patches, but I think it would probably apply without the ReST patches just fine.



---

archive/issue_comments_041062.json:
```json
{
    "body": "Attachment [trac5340-ntl-contexts-and-dealloc.patch](tarball://root/attachments/some-uuid/ticket5340/trac5340-ntl-contexts-and-dealloc.patch) by cwitty created at 2009-02-22 20:47:13",
    "created_at": "2009-02-22T20:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5340#issuecomment-41062",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac5340-ntl-contexts-and-dealloc.patch](tarball://root/attachments/some-uuid/ticket5340/trac5340-ntl-contexts-and-dealloc.patch) by cwitty created at 2009-02-22 20:47:13



---

archive/issue_comments_041063.json:
```json
{
    "body": "Positive review. I did valgrind all of the Sage 3.3 doctests + this patch (while testing gsw's libSingular work) and no issue popped up. It also passes doctests on top of the ReST patches.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T20:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5340#issuecomment-41063",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. I did valgrind all of the Sage 3.3 doctests + this patch (while testing gsw's libSingular work) and no issue popped up. It also passes doctests on top of the ReST patches.

Cheers,

Michael



---

archive/issue_comments_041064.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T20:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5340#issuecomment-41064",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041065.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T20:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5340#issuecomment-41065",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Cheers,

Michael



---

archive/issue_events_005597.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-24T20:30:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5340",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5340#event-5597"
}
```
