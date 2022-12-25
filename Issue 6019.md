# Issue 6019: [with patch, needs review] speed up new_subspace by a factor of > 100

archive/issues_006019.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @craigcitro\n\nI forgot to disable the automatic Hecke-invariance check, and to use the already-calculated dual free module, when calling the submodule constructor to constructing new subspaces of modular forms spaces. \n\nThat meant that the very time-consuming functions `_is_hecke_invariant_free_module` and `dual_free_module` were getting called, which slowed down the computation *ridiculously*.\n\nBefore:\n\n```\nsage: C = CuspForms(12, 8)\nsage: time C.new_submodule()\nCPU times: user 217.98 s, sys: 0.39 s, total: 218.37 s\nWall time: 229.00 s\nModular Forms subspace of dimension 2 of Modular Forms space of dimension 17 for Congruence Subgroup Gamma0(12) ofweight 8 over Rational Field\n```\n\n\nAfter:\n\n```\nsage: time C.new_submodule()\nCPU times: user 1.55 s, sys: 0.02 s, total: 1.57 s\nWall time: 1.58 s\nModular Forms subspace of dimension 2 of Modular Forms space of dimension 17 for Congruence Subgroup Gamma0(12) ofweight 8 over Rational Field\n```\n\n\nSo that's a speedup by a factor of 139 in this example.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6019\n\n",
    "created_at": "2009-05-11T10:16:52Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] speed up new_subspace by a factor of > 100",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6019",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @craigcitro

CC:  @craigcitro

I forgot to disable the automatic Hecke-invariance check, and to use the already-calculated dual free module, when calling the submodule constructor to constructing new subspaces of modular forms spaces. 

That meant that the very time-consuming functions `_is_hecke_invariant_free_module` and `dual_free_module` were getting called, which slowed down the computation *ridiculously*.

Before:

```
sage: C = CuspForms(12, 8)
sage: time C.new_submodule()
CPU times: user 217.98 s, sys: 0.39 s, total: 218.37 s
Wall time: 229.00 s
Modular Forms subspace of dimension 2 of Modular Forms space of dimension 17 for Congruence Subgroup Gamma0(12) ofweight 8 over Rational Field
```


After:

```
sage: time C.new_submodule()
CPU times: user 1.55 s, sys: 0.02 s, total: 1.57 s
Wall time: 1.58 s
Modular Forms subspace of dimension 2 of Modular Forms space of dimension 17 for Congruence Subgroup Gamma0(12) ofweight 8 over Rational Field
```


So that's a speedup by a factor of 139 in this example.

Issue created by migration from https://trac.sagemath.org/ticket/6019





---

archive/issue_comments_047830.json:
```json
{
    "body": "Attachment [trac_6019.2.patch](tarball://root/attachments/some-uuid/ticket6019/trac_6019.2.patch) by @loefflerd created at 2009-05-11 10:25:25",
    "created_at": "2009-05-11T10:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6019#issuecomment-47830",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_6019.2.patch](tarball://root/attachments/some-uuid/ticket6019/trac_6019.2.patch) by @loefflerd created at 2009-05-11 10:25:25



---

archive/issue_comments_047831.json:
```json
{
    "body": "Craig: I'm ccing you on this as it's a followup to #4357, which you reviewed. It's a one-line change.",
    "created_at": "2009-05-11T18:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6019#issuecomment-47831",
    "user": "https://github.com/loefflerd"
}
```

Craig: I'm ccing you on this as it's a followup to #4357, which you reviewed. It's a one-line change.



---

archive/issue_comments_047832.json:
```json
{
    "body": "Nice catch. `:)`",
    "created_at": "2009-05-11T18:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6019#issuecomment-47832",
    "user": "https://github.com/craigcitro"
}
```

Nice catch. `:)`



---

archive/issue_comments_047833.json:
```json
{
    "body": "Wow, that was quick - thanks!",
    "created_at": "2009-05-11T18:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6019#issuecomment-47833",
    "user": "https://github.com/loefflerd"
}
```

Wow, that was quick - thanks!



---

archive/issue_events_006274.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-12T04:55:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6019",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6019#event-6274"
}
```



---

archive/issue_comments_047834.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T04:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6019#issuecomment-47834",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_047835.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-12T04:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6019#issuecomment-47835",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
