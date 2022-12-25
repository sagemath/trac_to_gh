# Issue 1583: [with patch, positive review] simple modules of modular symbols over finite fields

archive/issues_001583.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThere are instances in which Sage thinks that a one-dimensional space of modular symbols is not simple, and it decomposes the space into a one-dimensional and a zero-dimensional subspace:\n\n```\nsage: C=ModularSymbols(1,14,0,GF(5)).cuspidal_submodule()\nsage: C\nModular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 14 with sign 0 over Finite Field of size 5\nsage: C.is_simple()\nFalse\nsage: C.simple_factors()\n\n[Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 14 with sign 0 over Finite Field of size 5,\n Modular Symbols subspace of dimension 0 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 14 with sign 0 over Finite Field of size 5]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1583\n\n",
    "closed_at": "2008-01-21T07:59:43Z",
    "created_at": "2007-12-21T17:47:00Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch, positive review] simple modules of modular symbols over finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1583",
    "user": "https://github.com/aghitza"
}
```
Assignee: @craigcitro

There are instances in which Sage thinks that a one-dimensional space of modular symbols is not simple, and it decomposes the space into a one-dimensional and a zero-dimensional subspace:

```
sage: C=ModularSymbols(1,14,0,GF(5)).cuspidal_submodule()
sage: C
Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 14 with sign 0 over Finite Field of size 5
sage: C.is_simple()
False
sage: C.simple_factors()

[Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 14 with sign 0 over Finite Field of size 5,
 Modular Symbols subspace of dimension 0 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 14 with sign 0 over Finite Field of size 5]
```


Issue created by migration from https://trac.sagemath.org/ticket/1583





---

archive/issue_comments_010054.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2008-01-21T06:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1583#issuecomment-10054",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_010055.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-21T06:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1583#issuecomment-10055",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010056.json:
```json
{
    "body": "Attachment [craigcitro-1583.patch](tarball://root/attachments/some-uuid/ticket1583/craigcitro-1583.patch) by @craigcitro created at 2008-01-21 06:10:22\n\nAdded a patch to fix this. I actually add the _is_simple flag when the cuspidal subspace is created -- when that's one-dimensional, we know it must be simple, so it seems easier to tag it then, rather than do something involving checking stability under the Hecke operators ...",
    "created_at": "2008-01-21T06:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1583#issuecomment-10056",
    "user": "https://github.com/craigcitro"
}
```

Attachment [craigcitro-1583.patch](tarball://root/attachments/some-uuid/ticket1583/craigcitro-1583.patch) by @craigcitro created at 2008-01-21 06:10:22

Added a patch to fix this. I actually add the _is_simple flag when the cuspidal subspace is created -- when that's one-dimensional, we know it must be simple, so it seems easier to tag it then, rather than do something involving checking stability under the Hecke operators ...



---

archive/issue_comments_010057.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T07:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1583#issuecomment-10057",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010058.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T07:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1583#issuecomment-10058",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_events_003947.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-21T07:59:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1583",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1583#event-3947"
}
```
