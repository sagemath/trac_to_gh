# Issue 5946: bug in content for p-adic polynomials

archive/issues_005946.json:
```json
{
    "body": "Assignee: roed\n\nKeywords: content p-adic polynomial\n\nWe ran into this at #5921.  There are two separate issues: polynomials with coefficients in a p-adic field should not have a `content()` method, since it doesn't make sense (the same way that having a `content()` method for polynomials with rational coefficients doesn't make sense).\n\nThe second issue is with the `content()` method for polynomials with coefficients in p-adic rings.  Here's an example:\n\n\n```\nsage: P.<x> = ZZ[]\nsage: f = x + 2\nsage: f.content()\n1\nsage: fp = f.change_ring(pAdicRing(2, 10))\nsage: fp\n(1 + O(2^10))*x + (2 + O(2^11))\nsage: fp.content()\n0\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5946\n\n",
    "created_at": "2009-04-30T06:44:15Z",
    "labels": [
        "padics",
        "minor",
        "bug"
    ],
    "title": "bug in content for p-adic polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5946",
    "user": "AlexGhitza"
}
```
Assignee: roed

Keywords: content p-adic polynomial

We ran into this at #5921.  There are two separate issues: polynomials with coefficients in a p-adic field should not have a `content()` method, since it doesn't make sense (the same way that having a `content()` method for polynomials with rational coefficients doesn't make sense).

The second issue is with the `content()` method for polynomials with coefficients in p-adic rings.  Here's an example:


```
sage: P.<x> = ZZ[]
sage: f = x + 2
sage: f.content()
1
sage: fp = f.change_ring(pAdicRing(2, 10))
sage: fp
(1 + O(2^10))*x + (2 + O(2^11))
sage: fp.content()
0
```



Issue created by migration from https://trac.sagemath.org/ticket/5946





---

archive/issue_comments_047045.json:
```json
{
    "body": "Looks good and passes doctests.",
    "created_at": "2009-04-30T07:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5946#issuecomment-47045",
    "user": "AlexGhitza"
}
```

Looks good and passes doctests.



---

archive/issue_comments_047046.json:
```json
{
    "body": "Fixed",
    "created_at": "2009-04-30T08:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5946#issuecomment-47046",
    "user": "roed"
}
```

Fixed



---

archive/issue_comments_047047.json:
```json
{
    "body": "Attachment [trac_5946.patch](tarball://root/attachments/some-uuid/ticket5946/trac_5946.patch) by mabshoff created at 2009-04-30 08:52:22\n\nMerged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T08:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5946#issuecomment-47047",
    "user": "mabshoff"
}
```

Attachment [trac_5946.patch](tarball://root/attachments/some-uuid/ticket5946/trac_5946.patch) by mabshoff created at 2009-04-30 08:52:22

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_047048.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T08:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5946#issuecomment-47048",
    "user": "mabshoff"
}
```

Resolution: fixed
