# Issue 9502: Basis parent bug in FreeModule

archive/issues_009502.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @vbraun\n\nThere is an inconsistency in the example below for the echelonized basis of submodules with basis:\n\n```\nsage: F = FreeModule(ZZ, 3)\nsage: S = F.submodule_with_basis([(1,2,3),(3,2,1)])\nsage: parent(S.basis()[0])\nFree module of degree 3 and rank 2 over Integer Ring\nUser basis matrix:\n[1 2 3]\n[3 2 1]\nsage: parent(S.echelonized_basis()[0])\nAmbient free module of rank 3 over the principal ideal domain Integer Ring\n```\n\n\nFor automatic bases everything is OK:\n\n```\nsage: S = F.submodule([(1,2,3),(3,2,1)])\nsage: parent(S.echelonized_basis()[0])\nFree module of degree 3 and rank 2 over Integer Ring\nEchelon basis matrix:\n[1 2 3]\n[0 4 8]\nsage: parent(S.basis()[0])\nFree module of degree 3 and rank 2 over Integer Ring\nEchelon basis matrix:\n[1 2 3]\n[0 4 8]\n```\n\n\nI am working on a patch to fix this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9502\n\n",
    "created_at": "2010-07-15T02:49:51Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Basis parent bug in FreeModule",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9502",
    "user": "@novoselt"
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

archive/issue_comments_091259.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-15T07:23:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91259",
    "user": "@novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091260.json:
```json
{
    "body": "Attachment [trac_9502_basis_parent_bug_in_FreeModule.patch](tarball://root/attachments/some-uuid/ticket9502/trac_9502_basis_parent_bug_in_FreeModule.patch) by @vbraun created at 2010-07-21 00:28:12",
    "created_at": "2010-07-21T00:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91260",
    "user": "@vbraun"
}
```

Attachment [trac_9502_basis_parent_bug_in_FreeModule.patch](tarball://root/attachments/some-uuid/ticket9502/trac_9502_basis_parent_bug_in_FreeModule.patch) by @vbraun created at 2010-07-21 00:28:12



---

archive/issue_comments_091261.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-21T04:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91261",
    "user": "@vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091262.json:
```json
{
    "body": "Fixes the original issue and is a general improvement! Tests OK on Sage 4.5, too.",
    "created_at": "2010-07-21T04:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91262",
    "user": "@vbraun"
}
```

Fixes the original issue and is a general improvement! Tests OK on Sage 4.5, too.



---

archive/issue_comments_091263.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-22T08:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91263",
    "user": "@dandrake"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_091264.json:
```json
{
    "body": "I applied the patch to 4.5.2.alpha0 and when I try to start Sage, I get \"ImportError: cannot import name SR\". Any ideas? I've rebuilt the entire Sage library and the problem persists.",
    "created_at": "2010-07-22T08:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91264",
    "user": "@dandrake"
}
```

I applied the patch to 4.5.2.alpha0 and when I try to start Sage, I get "ImportError: cannot import name SR". Any ideas? I've rebuilt the entire Sage library and the problem persists.



---

archive/issue_comments_091265.json:
```json
{
    "body": "Replying to [comment:4 ddrake]:\n> I applied the patch to 4.5.2.alpha0 and when I try to start Sage, I get \"ImportError: cannot import name SR\". Any ideas? I've rebuilt the entire Sage library and the problem persists. \n\nThat's strange, since the patch does not mention `SR`...",
    "created_at": "2010-07-22T14:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91265",
    "user": "@novoselt"
}
```

Replying to [comment:4 ddrake]:
> I applied the patch to 4.5.2.alpha0 and when I try to start Sage, I get "ImportError: cannot import name SR". Any ideas? I've rebuilt the entire Sage library and the problem persists. 

That's strange, since the patch does not mention `SR`...



---

archive/issue_comments_091266.json:
```json
{
    "body": "Replying to [comment:5 novoselt]:\n> Replying to [comment:4 ddrake]:\n> > I applied the patch to 4.5.2.alpha0 and when I try to start Sage, I get \"ImportError: cannot import name SR\". Any ideas? I've rebuilt the entire Sage library and the problem persists. \n> \n> That's strange, since the patch does not mention `SR`...\nSure it does, implicitly - the final bit is part of \n\n```\ncdef class SymbolicRing(CommutativeRing):\n```\n\nwhich is changed.   And #8562 in alpha0 did change the behavior of Fields, though it's not clear to me how that change would affect SR's ability to import...",
    "created_at": "2010-07-23T01:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91266",
    "user": "@kcrisman"
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

archive/issue_comments_091267.json:
```json
{
    "body": "Attachment [trac_9502_basis_parent_bug_in_FreeModule.2.patch](tarball://root/attachments/some-uuid/ticket9502/trac_9502_basis_parent_bug_in_FreeModule.2.patch) by @novoselt created at 2010-07-24 07:40:27\n\nReverted change to symbolic/ring.pyx",
    "created_at": "2010-07-24T07:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91267",
    "user": "@novoselt"
}
```

Attachment [trac_9502_basis_parent_bug_in_FreeModule.2.patch](tarball://root/attachments/some-uuid/ticket9502/trac_9502_basis_parent_bug_in_FreeModule.2.patch) by @novoselt created at 2010-07-24 07:40:27

Reverted change to symbolic/ring.pyx



---

archive/issue_comments_091268.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-24T07:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91268",
    "user": "@novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_091269.json:
```json
{
    "body": "I have reverted the change to `symbolic/ring.pyx` since it is actually not necessary for this ticket (it may be relevant for #9503). Now I don't have problems with 4.5.2.alpha0.",
    "created_at": "2010-07-24T07:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91269",
    "user": "@novoselt"
}
```

I have reverted the change to `symbolic/ring.pyx` since it is actually not necessary for this ticket (it may be relevant for #9503). Now I don't have problems with 4.5.2.alpha0.



---

archive/issue_comments_091270.json:
```json
{
    "body": "Works on 4.5.2. Positive review!\n\nFor the maintainer: Apply `trac_9502_basis_parent_bug_in_FreeModule.2.patch` only.",
    "created_at": "2010-08-09T22:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91270",
    "user": "@vbraun"
}
```

Works on 4.5.2. Positive review!

For the maintainer: Apply `trac_9502_basis_parent_bug_in_FreeModule.2.patch` only.



---

archive/issue_comments_091271.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-09T22:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91271",
    "user": "@vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091272.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2010-09-02T11:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91272",
    "user": "@aghitza"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_091273.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91273",
    "user": "@qed777"
}
```

Resolution: fixed



---

archive/issue_comments_091274.json:
```json
{
    "body": "For future reference: this ticket might have introduced a segfault; see http://groups.google.com/group/sage-devel/t/b1f3a7bec3ba655f and #10250.",
    "created_at": "2010-11-12T01:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9502#issuecomment-91274",
    "user": "@dandrake"
}
```

For future reference: this ticket might have introduced a segfault; see http://groups.google.com/group/sage-devel/t/b1f3a7bec3ba655f and #10250.
