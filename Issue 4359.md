# Issue 4359: [with patch, needs review] Huge number of small fixes to modular forms code

archive/issues_004359.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThis is just a big bundle of fixes to the modular forms code that I had piled up.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4359\n\n",
    "created_at": "2008-10-24T08:43:50Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] Huge number of small fixes to modular forms code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4359",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

This is just a big bundle of fixes to the modular forms code that I had piled up.

Issue created by migration from https://trac.sagemath.org/ticket/4359





---

archive/issue_comments_031959.json:
```json
{
    "body": "Attachment [trac-4359.patch](tarball://root/attachments/some-uuid/ticket4359/trac-4359.patch) by @aghitza created at 2008-10-25 22:05:41\n\nLooks good.  I have some questions about `_ensure_is_compatible()` in modform/element.py\n\n1. I guess I don't quite know what the function is meant to be used for; the docstring says \"compatible for arithmetic and comparison operations\". I assume arithmetic here means addition or subtraction?\n\n2. With the patch, two forms of the same weight but different groups of the same level are deemed compatible.  For instance, if f is on Gamma0(11) and g is on Gamma1(11), or if f and g are on Gamma1(17) but with different Dirichlet characters.  Is this the desired behaviour?",
    "created_at": "2008-10-25T22:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4359#issuecomment-31959",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac-4359.patch](tarball://root/attachments/some-uuid/ticket4359/trac-4359.patch) by @aghitza created at 2008-10-25 22:05:41

Looks good.  I have some questions about `_ensure_is_compatible()` in modform/element.py

1. I guess I don't quite know what the function is meant to be used for; the docstring says "compatible for arithmetic and comparison operations". I assume arithmetic here means addition or subtraction?

2. With the patch, two forms of the same weight but different groups of the same level are deemed compatible.  For instance, if f is on Gamma0(11) and g is on Gamma1(11), or if f and g are on Gamma1(17) but with different Dirichlet characters.  Is this the desired behaviour?



---

archive/issue_comments_031960.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-26T00:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4359#issuecomment-31960",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031961.json:
```json
{
    "body": "Attachment [trac-4359-2.patch](tarball://root/attachments/some-uuid/ticket4359/trac-4359-2.patch) by @craigcitro created at 2008-10-26 00:18:49\n\nAh, good point. I added a patch that changes it to test that they have the same ambient space, which is what the docstring claims.",
    "created_at": "2008-10-26T00:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4359#issuecomment-31961",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4359-2.patch](tarball://root/attachments/some-uuid/ticket4359/trac-4359-2.patch) by @craigcitro created at 2008-10-26 00:18:49

Ah, good point. I added a patch that changes it to test that they have the same ambient space, which is what the docstring claims.



---

archive/issue_comments_031962.json:
```json
{
    "body": "OK, I'm happy.",
    "created_at": "2008-10-26T00:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4359#issuecomment-31962",
    "user": "https://github.com/aghitza"
}
```

OK, I'm happy.



---

archive/issue_comments_031963.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T01:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4359#issuecomment-31963",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031964.json:
```json
{
    "body": "Merged both patches in Sage 3.2.alpha1",
    "created_at": "2008-10-26T01:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4359#issuecomment-31964",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.2.alpha1
