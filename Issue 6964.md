# Issue 6964: implement computation of Dirichlet character of irreducible cuspidal modular symbols space

archive/issues_006964.json:
```json
{
    "body": "Assignee: tbd\n\nImplement this function q_eigenform_character described below:\n\n```\nsage: f = ModularSymbols(Gamma1(13),2,sign=1).cuspidal_subspace().decomposition()[0]\nsage: f.q_eigenform(5,'a')\nq + a*q^2 + (-2*a - 4)*q^3 + (-a - 1)*q^4 + O(q^5)\nsage: f.q_eigenform_character('a')\nTraceback (most recent call last):\n...\nAttributeError: 'ModularSymbolsSubspace' object has no attribute 'q_eigenform_character'\n```\n\n\nIn case f.character() is not None, the above function should be easy to implement -- just return the character.  Otherwise it is harder.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6964\n\n",
    "created_at": "2009-09-20T00:43:57Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "implement computation of Dirichlet character of irreducible cuspidal modular symbols space",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6964",
    "user": "@williamstein"
}
```
Assignee: tbd

Implement this function q_eigenform_character described below:

```
sage: f = ModularSymbols(Gamma1(13),2,sign=1).cuspidal_subspace().decomposition()[0]
sage: f.q_eigenform(5,'a')
q + a*q^2 + (-2*a - 4)*q^3 + (-a - 1)*q^4 + O(q^5)
sage: f.q_eigenform_character('a')
Traceback (most recent call last):
...
AttributeError: 'ModularSymbolsSubspace' object has no attribute 'q_eigenform_character'
```


In case f.character() is not None, the above function should be easy to implement -- just return the character.  Otherwise it is harder.

Issue created by migration from https://trac.sagemath.org/ticket/6964





---

archive/issue_comments_057616.json:
```json
{
    "body": "Attachment [trac_6964-part2.patch](tarball://root/attachments/some-uuid/ticket6964/trac_6964-part2.patch) by @williamstein created at 2009-09-20 04:59:07",
    "created_at": "2009-09-20T04:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6964#issuecomment-57616",
    "user": "@williamstein"
}
```

Attachment [trac_6964-part2.patch](tarball://root/attachments/some-uuid/ticket6964/trac_6964-part2.patch) by @williamstein created at 2009-09-20 04:59:07



---

archive/issue_comments_057617.json:
```json
{
    "body": "Attachment [trac_6964-part3.patch](tarball://root/attachments/some-uuid/ticket6964/trac_6964-part3.patch) by @williamstein created at 2009-09-20 05:21:19",
    "created_at": "2009-09-20T05:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6964#issuecomment-57617",
    "user": "@williamstein"
}
```

Attachment [trac_6964-part3.patch](tarball://root/attachments/some-uuid/ticket6964/trac_6964-part3.patch) by @williamstein created at 2009-09-20 05:21:19



---

archive/issue_comments_057618.json:
```json
{
    "body": "Attachment [trac_6964-part4.patch](tarball://root/attachments/some-uuid/ticket6964/trac_6964-part4.patch) by @syazdani77 created at 2009-09-20 05:44:47",
    "created_at": "2009-09-20T05:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6964#issuecomment-57618",
    "user": "@syazdani77"
}
```

Attachment [trac_6964-part4.patch](tarball://root/attachments/some-uuid/ticket6964/trac_6964-part4.patch) by @syazdani77 created at 2009-09-20 05:44:47



---

archive/issue_comments_057619.json:
```json
{
    "body": "Attachment [trac_6964-formatting-fix.patch](tarball://root/attachments/some-uuid/ticket6964/trac_6964-formatting-fix.patch) by mvngu created at 2009-09-24 15:36:11\n\nfix warning when building reference manual",
    "created_at": "2009-09-24T15:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6964#issuecomment-57619",
    "user": "mvngu"
}
```

Attachment [trac_6964-formatting-fix.patch](tarball://root/attachments/some-uuid/ticket6964/trac_6964-formatting-fix.patch) by mvngu created at 2009-09-24 15:36:11

fix warning when building reference manual



---

archive/issue_comments_057620.json:
```json
{
    "body": "The patch `trac_6964-formatting-fix.patch` fix a warning when building the reference manual with the previous patches.",
    "created_at": "2009-09-24T15:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6964#issuecomment-57620",
    "user": "mvngu"
}
```

The patch `trac_6964-formatting-fix.patch` fix a warning when building the reference manual with the previous patches.



---

archive/issue_comments_057621.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6964.patch`\n2. `trac_6964-part2.patch`\n3. `trac_6964-part3.patch`\n4. `trac_6964-part4.patch`\n5. `trac_6964-formatting-fix.patch`",
    "created_at": "2009-09-24T16:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6964#issuecomment-57621",
    "user": "mvngu"
}
```

Merged patches in this order:

1. `trac_6964.patch`
2. `trac_6964-part2.patch`
3. `trac_6964-part3.patch`
4. `trac_6964-part4.patch`
5. `trac_6964-formatting-fix.patch`



---

archive/issue_comments_057622.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-24T16:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6964#issuecomment-57622",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057623.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6964#issuecomment-57623",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
