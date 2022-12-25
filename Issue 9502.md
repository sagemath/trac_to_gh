# Issue 9502: Basis parent bug in FreeModule

archive/issues_009502.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @vbraun\n\nThere is an inconsistency in the example below for the echelonized basis of submodules with basis:\n\n```\nsage: F = FreeModule(ZZ, 3)\nsage: S = F.submodule_with_basis([(1,2,3),(3,2,1)])\nsage: parent(S.basis()[0])\nFree module of degree 3 and rank 2 over Integer Ring\nUser basis matrix:\n[1 2 3]\n[3 2 1]\nsage: parent(S.echelonized_basis()[0])\nAmbient free module of rank 3 over the principal ideal domain Integer Ring\n```\n\n\nFor automatic bases everything is OK:\n\n```\nsage: S = F.submodule([(1,2,3),(3,2,1)])\nsage: parent(S.echelonized_basis()[0])\nFree module of degree 3 and rank 2 over Integer Ring\nEchelon basis matrix:\n[1 2 3]\n[0 4 8]\nsage: parent(S.basis()[0])\nFree module of degree 3 and rank 2 over Integer Ring\nEchelon basis matrix:\n[1 2 3]\n[0 4 8]\n```\n\n\nI am working on a patch to fix this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9502\n\n",
    "created_at": "2010-07-15T02:49:51Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Basis parent bug in FreeModule",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9502",
    "user": "https://github.com/novoselt"
}
```
Assignee: @aghitza

CC:  @vbraun

There is an inconsistency in the example below for the echelonized basis of submodules with basis:

```
sage: F = FreeModule(ZZ, 3)
sage: S = F.submodule_with_basis([(1,2,3),(3,2,1)])
sage: parent(S.basis()[0])
Free module of degree 3 and rank 2 over Integer Ring
User basis matrix:
[1 2 3]
[3 2 1]
sage: parent(S.echelonized_basis()[0])
Ambient free module of rank 3 over the principal ideal domain Integer Ring
```


For automatic bases everything is OK:

```
sage: S = F.submodule([(1,2,3),(3,2,1)])
sage: parent(S.echelonized_basis()[0])
Free module of degree 3 and rank 2 over Integer Ring
Echelon basis matrix:
[1 2 3]
[0 4 8]
sage: parent(S.basis()[0])
Free module of degree 3 and rank 2 over Integer Ring
Echelon basis matrix:
[1 2 3]
[0 4 8]
```


I am working on a patch to fix this.

Issue created by migration from https://trac.sagemath.org/ticket/9502





---

archive/issue_comments_091106.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-15T07:23:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91106",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091107.json:
```json
{
    "body": "Attachment [trac_9502_basis_parent_bug_in_FreeModule.patch](tarball://root/attachments/some-uuid/ticket9502/trac_9502_basis_parent_bug_in_FreeModule.patch) by @vbraun created at 2010-07-21 00:28:12",
    "created_at": "2010-07-21T00:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91107",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_9502_basis_parent_bug_in_FreeModule.patch](tarball://root/attachments/some-uuid/ticket9502/trac_9502_basis_parent_bug_in_FreeModule.patch) by @vbraun created at 2010-07-21 00:28:12



---

archive/issue_comments_091108.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-21T04:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91108",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091109.json:
```json
{
    "body": "Fixes the original issue and is a general improvement! Tests OK on Sage 4.5, too.",
    "created_at": "2010-07-21T04:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91109",
    "user": "https://github.com/vbraun"
}
```

Fixes the original issue and is a general improvement! Tests OK on Sage 4.5, too.



---

archive/issue_comments_091110.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-22T08:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91110",
    "user": "https://github.com/dandrake"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_091111.json:
```json
{
    "body": "I applied the patch to 4.5.2.alpha0 and when I try to start Sage, I get \"ImportError: cannot import name SR\". Any ideas? I've rebuilt the entire Sage library and the problem persists.",
    "created_at": "2010-07-22T08:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91111",
    "user": "https://github.com/dandrake"
}
```

I applied the patch to 4.5.2.alpha0 and when I try to start Sage, I get "ImportError: cannot import name SR". Any ideas? I've rebuilt the entire Sage library and the problem persists.



---

archive/issue_comments_091112.json:
```json
{
    "body": "Replying to [comment:4 ddrake]:\n> I applied the patch to 4.5.2.alpha0 and when I try to start Sage, I get \"ImportError: cannot import name SR\". Any ideas? I've rebuilt the entire Sage library and the problem persists. \n\nThat's strange, since the patch does not mention `SR`...",
    "created_at": "2010-07-22T14:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91112",
    "user": "https://github.com/novoselt"
}
```

Replying to [comment:4 ddrake]:
> I applied the patch to 4.5.2.alpha0 and when I try to start Sage, I get "ImportError: cannot import name SR". Any ideas? I've rebuilt the entire Sage library and the problem persists. 

That's strange, since the patch does not mention `SR`...



---

archive/issue_comments_091113.json:
```json
{
    "body": "Replying to [comment:5 novoselt]:\n> Replying to [comment:4 ddrake]:\n> > I applied the patch to 4.5.2.alpha0 and when I try to start Sage, I get \"ImportError: cannot import name SR\". Any ideas? I've rebuilt the entire Sage library and the problem persists. \n> \n> That's strange, since the patch does not mention `SR`...\nSure it does, implicitly - the final bit is part of \n\n```\ncdef class SymbolicRing(CommutativeRing):\n```\n\nwhich is changed.   And #8562 in alpha0 did change the behavior of Fields, though it's not clear to me how that change would affect SR's ability to import...",
    "created_at": "2010-07-23T01:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91113",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:5 novoselt]:
> Replying to [comment:4 ddrake]:
> > I applied the patch to 4.5.2.alpha0 and when I try to start Sage, I get "ImportError: cannot import name SR". Any ideas? I've rebuilt the entire Sage library and the problem persists. 
> 
> That's strange, since the patch does not mention `SR`...
Sure it does, implicitly - the final bit is part of 

```
cdef class SymbolicRing(CommutativeRing):
```

which is changed.   And #8562 in alpha0 did change the behavior of Fields, though it's not clear to me how that change would affect SR's ability to import...



---

archive/issue_comments_091114.json:
```json
{
    "body": "Attachment [trac_9502_basis_parent_bug_in_FreeModule.2.patch](tarball://root/attachments/some-uuid/ticket9502/trac_9502_basis_parent_bug_in_FreeModule.2.patch) by @novoselt created at 2010-07-24 07:40:27\n\nReverted change to symbolic/ring.pyx",
    "created_at": "2010-07-24T07:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91114",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9502_basis_parent_bug_in_FreeModule.2.patch](tarball://root/attachments/some-uuid/ticket9502/trac_9502_basis_parent_bug_in_FreeModule.2.patch) by @novoselt created at 2010-07-24 07:40:27

Reverted change to symbolic/ring.pyx



---

archive/issue_comments_091115.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-24T07:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91115",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_091116.json:
```json
{
    "body": "I have reverted the change to `symbolic/ring.pyx` since it is actually not necessary for this ticket (it may be relevant for #9503). Now I don't have problems with 4.5.2.alpha0.",
    "created_at": "2010-07-24T07:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91116",
    "user": "https://github.com/novoselt"
}
```

I have reverted the change to `symbolic/ring.pyx` since it is actually not necessary for this ticket (it may be relevant for #9503). Now I don't have problems with 4.5.2.alpha0.



---

archive/issue_comments_091117.json:
```json
{
    "body": "Works on 4.5.2. Positive review!\n\nFor the maintainer: Apply `trac_9502_basis_parent_bug_in_FreeModule.2.patch` only.",
    "created_at": "2010-08-09T22:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91117",
    "user": "https://github.com/vbraun"
}
```

Works on 4.5.2. Positive review!

For the maintainer: Apply `trac_9502_basis_parent_bug_in_FreeModule.2.patch` only.



---

archive/issue_comments_091118.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-09T22:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91118",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091119.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2010-09-02T11:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91119",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_events_009650.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-09-15T10:00:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9502#event-9650"
}
```



---

archive/issue_comments_091120.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91120",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_091121.json:
```json
{
    "body": "For future reference: this ticket might have introduced a segfault; see http://groups.google.com/group/sage-devel/t/b1f3a7bec3ba655f and #10250.",
    "created_at": "2010-11-12T01:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91121",
    "user": "https://github.com/dandrake"
}
```

For future reference: this ticket might have introduced a segfault; see http://groups.google.com/group/sage-devel/t/b1f3a7bec3ba655f and #10250.
