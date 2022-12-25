# Issue 5192: Improve factor documentation

archive/issues_005192.json:
```json
{
    "body": "Assignee: tbd\n\nIntegers which result from symbolic expressions live in the symbolic ring, so they are not factored by factor().  E.g.\n\n```\nsage: f(n)=n^2+n+41\nsage: a=f(40)\nsage: factor(a),is_prime(a),a\n(1681, False, 1681)\nsage: factor(1681)\n41^2\n```\n\nBut this is not obvious from the documentation of factor(), which only refers to e.g. a.factor? as the source of this.  Some example like this should be added to the documentation of the global factor().\n\nIssue created by migration from https://trac.sagemath.org/ticket/5192\n\n",
    "created_at": "2009-02-06T01:17:59Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Improve factor documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5192",
    "user": "https://github.com/kcrisman"
}
```
Assignee: tbd

Integers which result from symbolic expressions live in the symbolic ring, so they are not factored by factor().  E.g.

```
sage: f(n)=n^2+n+41
sage: a=f(40)
sage: factor(a),is_prime(a),a
(1681, False, 1681)
sage: factor(1681)
41^2
```

But this is not obvious from the documentation of factor(), which only refers to e.g. a.factor? as the source of this.  Some example like this should be added to the documentation of the global factor().

Issue created by migration from https://trac.sagemath.org/ticket/5192





---

archive/issue_comments_039726.json:
```json
{
    "body": "Attachment [trac_5192.patch](tarball://root/attachments/some-uuid/ticket5192/trac_5192.patch) by @kcrisman created at 2009-02-06 17:28:38\n\nBased on 3.3.alpha5",
    "created_at": "2009-02-06T17:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5192#issuecomment-39726",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_5192.patch](tarball://root/attachments/some-uuid/ticket5192/trac_5192.patch) by @kcrisman created at 2009-02-06 17:28:38

Based on 3.3.alpha5



---

archive/issue_comments_039727.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-07T00:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5192#issuecomment-39727",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039728.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-07T00:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5192#issuecomment-39728",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael
