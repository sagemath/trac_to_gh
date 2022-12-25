# Issue 3869: CremonaDatabase functions iter() and isogeny_classes() sort keys wrongly

archive/issues_003869.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nKeywords: elliptic curve database\n\nExample:\n\n```\nsage: CDB=CremonaDatabase()    \nsage: [[EllipticCurve(ai[0]).label() for ai in C] for C in CDB.isogeny_classes(1728)]\n\n[['1728a1', '1728a2', '1728a3', '1728a4'],\n ['1728b1'],\n ['1728ba1'],\n ['1728bb1', '1728bb2', '1728bb3'],\n ['1728c1'],\n ['1728d1'],\n ['1728e1', '1728e2', '1728e3'],\n ['1728f1', '1728f2'],\n ['1728g1'],\n ['1728h1'],\n ['1728i1'],\n ['1728j1', '1728j2', '1728j3'],\n ['1728k1'],\n ['1728l1'],\n ['1728m1', '1728m2'],\n ['1728n1'],\n ['1728o1'],\n ['1728p1'],\n ['1728q1'],\n ['1728r1'],\n ['1728s1', '1728s2', '1728s3'],\n ['1728t1'],\n ['1728u1'],\n ['1728v1', '1728v2', '1728v3', '1728v4'],\n ['1728w1'],\n ['1728x1'],\n ['1728y1'],\n ['1728z1']]\n```\n\n\nThe keys are strings like '1728a1',...,'1728z1','1728ba1',... and these a wrongly sorted by the standard sort function.  What this means is that when iterating through the database, the isogeny classes are not listed in the standard order a,b,...,z,ba,bb,...,bz,...\n\nIn the above example, classes ba and bb should come after class z, and not between classes b and c.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3869\n\n",
    "created_at": "2008-08-15T08:43:49Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "CremonaDatabase functions iter() and isogeny_classes() sort keys wrongly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3869",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @JohnCremona

Keywords: elliptic curve database

Example:

```
sage: CDB=CremonaDatabase()    
sage: [[EllipticCurve(ai[0]).label() for ai in C] for C in CDB.isogeny_classes(1728)]

[['1728a1', '1728a2', '1728a3', '1728a4'],
 ['1728b1'],
 ['1728ba1'],
 ['1728bb1', '1728bb2', '1728bb3'],
 ['1728c1'],
 ['1728d1'],
 ['1728e1', '1728e2', '1728e3'],
 ['1728f1', '1728f2'],
 ['1728g1'],
 ['1728h1'],
 ['1728i1'],
 ['1728j1', '1728j2', '1728j3'],
 ['1728k1'],
 ['1728l1'],
 ['1728m1', '1728m2'],
 ['1728n1'],
 ['1728o1'],
 ['1728p1'],
 ['1728q1'],
 ['1728r1'],
 ['1728s1', '1728s2', '1728s3'],
 ['1728t1'],
 ['1728u1'],
 ['1728v1', '1728v2', '1728v3', '1728v4'],
 ['1728w1'],
 ['1728x1'],
 ['1728y1'],
 ['1728z1']]
```


The keys are strings like '1728a1',...,'1728z1','1728ba1',... and these a wrongly sorted by the standard sort function.  What this means is that when iterating through the database, the isogeny classes are not listed in the standard order a,b,...,z,ba,bb,...,bz,...

In the above example, classes ba and bb should come after class z, and not between classes b and c.


Issue created by migration from https://trac.sagemath.org/ticket/3869





---

archive/issue_comments_027520.json:
```json
{
    "body": "Attachment [sage-trac3869.patch](tarball://root/attachments/some-uuid/ticket3869/sage-trac3869.patch) by @JohnCremona created at 2008-08-15 10:29:33\n\nThe attached patch fixes this by defining a new cmp function for curve codes which gets it right.\n\nThis should apply to 3.1.\n\nI have doctested the new functions, and also checked that ell_rational_field doctests ok.",
    "created_at": "2008-08-15T10:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3869#issuecomment-27520",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [sage-trac3869.patch](tarball://root/attachments/some-uuid/ticket3869/sage-trac3869.patch) by @JohnCremona created at 2008-08-15 10:29:33

The attached patch fixes this by defining a new cmp function for curve codes which gets it right.

This should apply to 3.1.

I have doctested the new functions, and also checked that ell_rational_field doctests ok.



---

archive/issue_comments_027521.json:
```json
{
    "body": ":)\n\nCheers,\n\nMichael",
    "created_at": "2008-08-15T10:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3869#issuecomment-27521",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

:)

Cheers,

Michael



---

archive/issue_comments_027522.json:
```json
{
    "body": "Attachment [trac3869-extra-doctest.patch](tarball://root/attachments/some-uuid/ticket3869/trac3869-extra-doctest.patch) by cwitty created at 2008-08-23 21:35:34\n\nLooks good to me.\n\nI added one more doctest; both patches should be applied.",
    "created_at": "2008-08-23T21:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3869#issuecomment-27522",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac3869-extra-doctest.patch](tarball://root/attachments/some-uuid/ticket3869/trac3869-extra-doctest.patch) by cwitty created at 2008-08-23 21:35:34

Looks good to me.

I added one more doctest; both patches should be applied.



---

archive/issue_comments_027523.json:
```json
{
    "body": "I like the extra doctest!  Thanks.",
    "created_at": "2008-08-24T08:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3869#issuecomment-27523",
    "user": "https://github.com/JohnCremona"
}
```

I like the extra doctest!  Thanks.



---

archive/issue_comments_027524.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-25T02:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3869#issuecomment-27524",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027525.json:
```json
{
    "body": "Merged sage-trac3869.patch and trac3869-extra-doctest.patch in Sage 3.1.2.alpha1",
    "created_at": "2008-08-25T02:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3869#issuecomment-27525",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged sage-trac3869.patch and trac3869-extra-doctest.patch in Sage 3.1.2.alpha1
