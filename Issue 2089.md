# Issue 2089: major finite field printing (?) bug

archive/issues_002089.json:
```json
{
    "body": "Assignee: somebody\n\nIn sage-2.10.1\n\n```\nsage: sage: F.<u> = GF(2^20)\nsage: sage: F.gens()\n(a,)\nsage: u^3\nu^3\nsage: u\na\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2089\n\n",
    "created_at": "2008-02-07T22:12:40Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "major finite field printing (?) bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2089",
    "user": "@williamstein"
}
```
Assignee: somebody

In sage-2.10.1

```
sage: sage: F.<u> = GF(2^20)
sage: sage: F.gens()
(a,)
sage: u^3
u^3
sage: u
a
```


Issue created by migration from https://trac.sagemath.org/ticket/2089





---

archive/issue_comments_013517.json:
```json
{
    "body": "Changing assignee from somebody to @malb.",
    "created_at": "2008-02-07T22:13:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2089#issuecomment-13517",
    "user": "@williamstein"
}
```

Changing assignee from somebody to @malb.



---

archive/issue_comments_013518.json:
```json
{
    "body": "\n```\nsage: GF(2**15, 'u').gens()\n(u,)\nsage: GF(3**15, 'u').gens()\n(u,)\nsage: GF(2**16, 'u').gens()\n(a,)\n```\n\n\nConclusion: this only happens for GF(2**n) when n>=16, so FiniteField_ntl_gf2e is at fault here.  I've stared at it for a while now and I have no idea what's wrong.",
    "created_at": "2008-02-17T23:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2089#issuecomment-13518",
    "user": "@aghitza"
}
```


```
sage: GF(2**15, 'u').gens()
(u,)
sage: GF(3**15, 'u').gens()
(u,)
sage: GF(2**16, 'u').gens()
(a,)
```


Conclusion: this only happens for GF(2**n) when n>=16, so FiniteField_ntl_gf2e is at fault here.  I've stared at it for a while now and I have no idea what's wrong.



---

archive/issue_comments_013519.json:
```json
{
    "body": "fix",
    "created_at": "2008-02-18T15:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2089#issuecomment-13519",
    "user": "@malb"
}
```

fix



---

archive/issue_comments_013520.json:
```json
{
    "body": "Attachment [trac_2089.patch](tarball://root/attachments/some-uuid/ticket2089/trac_2089.patch) by @malb created at 2008-02-18 15:17:16\n\nThe attached patch fixes the issue for me.",
    "created_at": "2008-02-18T15:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2089#issuecomment-13520",
    "user": "@malb"
}
```

Attachment [trac_2089.patch](tarball://root/attachments/some-uuid/ticket2089/trac_2089.patch) by @malb created at 2008-02-18 15:17:16

The attached patch fixes the issue for me.



---

archive/issue_comments_013521.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-18T15:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2089#issuecomment-13521",
    "user": "@malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013522.json:
```json
{
    "body": "Perfect.",
    "created_at": "2008-02-19T02:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2089#issuecomment-13522",
    "user": "@williamstein"
}
```

Perfect.



---

archive/issue_comments_013523.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-19T15:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2089#issuecomment-13523",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013524.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-19T15:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2089#issuecomment-13524",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
