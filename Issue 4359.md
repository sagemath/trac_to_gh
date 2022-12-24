# Issue 4359: [with patch, needs review] Huge number of small fixes to modular forms code

archive/issues_004359.json:
```json
{
    "body": "Assignee: craigcitro\n\nThis is just a big bundle of fixes to the modular forms code that I had piled up.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4359\n\n",
    "created_at": "2008-10-24T08:43:50Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Huge number of small fixes to modular forms code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4359",
    "user": "craigcitro"
}
```
Assignee: craigcitro

This is just a big bundle of fixes to the modular forms code that I had piled up.

Issue created by migration from https://trac.sagemath.org/ticket/4359





---

archive/issue_comments_032021.json:
```json
{
    "body": "Attachment [trac-4359.patch](tarball://root/attachments/some-uuid/ticket4359/trac-4359.patch) by AlexGhitza created at 2008-10-25 22:05:41\n\nLooks good.  I have some questions about `_ensure_is_compatible()` in modform/element.py\n\n1. I guess I don't quite know what the function is meant to be used for; the docstring says \"compatible for arithmetic and comparison operations\". I assume arithmetic here means addition or subtraction?\n\n2. With the patch, two forms of the same weight but different groups of the same level are deemed compatible.  For instance, if f is on Gamma0(11) and g is on Gamma1(11), or if f and g are on Gamma1(17) but with different Dirichlet characters.  Is this the desired behaviour?",
    "created_at": "2008-10-25T22:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4359#issuecomment-32021",
    "user": "AlexGhitza"
}
```

Attachment [trac-4359.patch](tarball://root/attachments/some-uuid/ticket4359/trac-4359.patch) by AlexGhitza created at 2008-10-25 22:05:41

Looks good.  I have some questions about `_ensure_is_compatible()` in modform/element.py

1. I guess I don't quite know what the function is meant to be used for; the docstring says "compatible for arithmetic and comparison operations". I assume arithmetic here means addition or subtraction?

2. With the patch, two forms of the same weight but different groups of the same level are deemed compatible.  For instance, if f is on Gamma0(11) and g is on Gamma1(11), or if f and g are on Gamma1(17) but with different Dirichlet characters.  Is this the desired behaviour?



---

archive/issue_comments_032022.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-26T00:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4359#issuecomment-32022",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032023.json:
```json
{
    "body": "Attachment [trac-4359-2.patch](tarball://root/attachments/some-uuid/ticket4359/trac-4359-2.patch) by craigcitro created at 2008-10-26 00:18:49\n\nAh, good point. I added a patch that changes it to test that they have the same ambient space, which is what the docstring claims.",
    "created_at": "2008-10-26T00:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4359#issuecomment-32023",
    "user": "craigcitro"
}
```

Attachment [trac-4359-2.patch](tarball://root/attachments/some-uuid/ticket4359/trac-4359-2.patch) by craigcitro created at 2008-10-26 00:18:49

Ah, good point. I added a patch that changes it to test that they have the same ambient space, which is what the docstring claims.



---

archive/issue_comments_032024.json:
```json
{
    "body": "OK, I'm happy.",
    "created_at": "2008-10-26T00:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4359#issuecomment-32024",
    "user": "AlexGhitza"
}
```

OK, I'm happy.



---

archive/issue_comments_032025.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T01:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4359#issuecomment-32025",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032026.json:
```json
{
    "body": "Merged both patches in Sage 3.2.alpha1",
    "created_at": "2008-10-26T01:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4359#issuecomment-32026",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.alpha1
