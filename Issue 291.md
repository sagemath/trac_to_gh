# Issue 291: strange printing of -1 in multivariate polynomial rings

archive/issues_000291.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: multivariate polynomial ring printing\n\n\n```\nsage: R.<r1, r0, s1, s2, z> = QQ['r1', 'r0', 's1', 's2', 'z']\nsage: R(-r1)\n-1*r1\n```\n\n\nThis is tricky.  This is an issue with stacking rings... how does QQ['x']['y'] tell (QQ['x'](-1))*y to print as '-y'?  I don't know.\n\nIssue created by migration from https://trac.sagemath.org/ticket/291\n\n",
    "created_at": "2007-02-24T05:13:52Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "strange printing of -1 in multivariate polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/291",
    "user": "ncalexan"
}
```
Assignee: somebody

Keywords: multivariate polynomial ring printing


```
sage: R.<r1, r0, s1, s2, z> = QQ['r1', 'r0', 's1', 's2', 'z']
sage: R(-r1)
-1*r1
```


This is tricky.  This is an issue with stacking rings... how does QQ['x']['y'] tell (QQ['x'](-1))*y to print as '-y'?  I don't know.

Issue created by migration from https://trac.sagemath.org/ticket/291





---

archive/issue_comments_001370.json:
```json
{
    "body": "Changing assignee from somebody to ncalexan.",
    "created_at": "2007-02-25T09:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/291#issuecomment-1370",
    "user": "ncalexan"
}
```

Changing assignee from somebody to ncalexan.



---

archive/issue_comments_001371.json:
```json
{
    "body": "The following demonstrates this nicely:\n\n\n```\nsage: K.<a> = NumberField(ZZ['x'].0^2 - 3)\n\nsage: L.<b> = K.extension(K['x'].0^2 - 5)\n\nsage: L\n Extension by x^2 + -5 of the Number Field in a with defining polynomial x^2 - 3\n```\n",
    "created_at": "2007-02-25T09:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/291#issuecomment-1371",
    "user": "ncalexan"
}
```

The following demonstrates this nicely:


```
sage: K.<a> = NumberField(ZZ['x'].0^2 - 3)

sage: L.<b> = K.extension(K['x'].0^2 - 5)

sage: L
 Extension by x^2 + -5 of the Number Field in a with defining polynomial x^2 - 3
```




---

archive/issue_comments_001372.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-08-18T21:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/291#issuecomment-1372",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_001373.json:
```json
{
    "body": "nick's xeample is annoying, but it illustrates a completely different problem.\n\nIn any case the original multivariate example no longer fails since singular does the printing.\nHowever this example fails:\n\n\n```\nsage: K.<a> = NumberField(ZZ['x'].0^2 - 3) \nsage: R.<r1, r0, s1, s2, z> = K['r1', 'r0', 's1', 's2', 'z']\nsage: -r1\n(-1)*r1\n```\n\n\nHowever, since the output is correct, this is not a bug, but an enhancement issue.",
    "created_at": "2007-08-18T21:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/291#issuecomment-1373",
    "user": "was"
}
```

nick's xeample is annoying, but it illustrates a completely different problem.

In any case the original multivariate example no longer fails since singular does the printing.
However this example fails:


```
sage: K.<a> = NumberField(ZZ['x'].0^2 - 3) 
sage: R.<r1, r0, s1, s2, z> = K['r1', 'r0', 's1', 's2', 'z']
sage: -r1
(-1)*r1
```


However, since the output is correct, this is not a bug, but an enhancement issue.



---

archive/issue_comments_001374.json:
```json
{
    "body": "The original printing issue has been solved by 2.8.1pre:\n\n```\nsage: R.<r1, r0, s1, s2, z> = QQ['r1', 'r0', 's1', 's2', 'z']\nsage: R(-r1)\n-r1\n```\n\nThe points made by was in the replies still apply.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-21T13:03:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/291#issuecomment-1374",
    "user": "mabshoff"
}
```

The original printing issue has been solved by 2.8.1pre:

```
sage: R.<r1, r0, s1, s2, z> = QQ['r1', 'r0', 's1', 's2', 'z']
sage: R(-r1)
-r1
```

The points made by was in the replies still apply.

Cheers,

Michael



---

archive/issue_comments_001375.json:
```json
{
    "body": "Attachment [mpoly-str.patch](tarball://root/attachments/some-uuid/ticket291/mpoly-str.patch) by jbmohler created at 2008-03-20 12:01:47",
    "created_at": "2008-03-20T12:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/291#issuecomment-1375",
    "user": "jbmohler"
}
```

Attachment [mpoly-str.patch](tarball://root/attachments/some-uuid/ticket291/mpoly-str.patch) by jbmohler created at 2008-03-20 12:01:47



---

archive/issue_comments_001376.json:
```json
{
    "body": "The attached patch fixes this bug and the associated doc-tests.  As an added bonus, it speeds up the str conversion just a little bit too.\n\nBefore patch:\n\n```\nsage: R.<x,y,z> = ZZ[]\nsage: f=prod([2*g^2-4*g+8 for g in R.gens()])\nsage: len(f.monomials())\n27\nsage: %timeit str(f)\n100 loops, best of 3: 2.85 ms per loop\n```\n\n\nAfter patch:\n\n```\nsage: R.<x,y,z> = ZZ[]\nsage: f=prod([2*g^2-4*g+8 for g in R.gens()])\nsage: len(f.monomials())\n27\nsage: %timeit str(f)\n100 loops, best of 3: 2.43 ms per loop\n```\n",
    "created_at": "2008-03-20T12:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/291#issuecomment-1376",
    "user": "jbmohler"
}
```

The attached patch fixes this bug and the associated doc-tests.  As an added bonus, it speeds up the str conversion just a little bit too.

Before patch:

```
sage: R.<x,y,z> = ZZ[]
sage: f=prod([2*g^2-4*g+8 for g in R.gens()])
sage: len(f.monomials())
27
sage: %timeit str(f)
100 loops, best of 3: 2.85 ms per loop
```


After patch:

```
sage: R.<x,y,z> = ZZ[]
sage: f=prod([2*g^2-4*g+8 for g in R.gens()])
sage: len(f.monomials())
27
sage: %timeit str(f)
100 loops, best of 3: 2.43 ms per loop
```




---

archive/issue_comments_001377.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-03-21T22:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/291#issuecomment-1377",
    "user": "AlexGhitza"
}
```

Looks good.



---

archive/issue_comments_001378.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T23:29:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/291#issuecomment-1378",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_001379.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-21T23:29:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/291#issuecomment-1379",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha1



---

archive/issue_comments_001380.json:
```json
{
    "body": "fixes two trivial doctest failures in const.tex",
    "created_at": "2008-03-22T00:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/291#issuecomment-1380",
    "user": "mabshoff"
}
```

fixes two trivial doctest failures in const.tex



---

archive/issue_comments_001381.json:
```json
{
    "body": "Attachment [trac_291-doctest-failures.patch](tarball://root/attachments/some-uuid/ticket291/trac_291-doctest-failures.patch) by mabshoff created at 2008-03-22 00:05:37\n\nMerged trac_291-doctest-failures.patch in Sage 2.11.alpha1 - if anybody does want to review this patch feel free to do so.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T00:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/291#issuecomment-1381",
    "user": "mabshoff"
}
```

Attachment [trac_291-doctest-failures.patch](tarball://root/attachments/some-uuid/ticket291/trac_291-doctest-failures.patch) by mabshoff created at 2008-03-22 00:05:37

Merged trac_291-doctest-failures.patch in Sage 2.11.alpha1 - if anybody does want to review this patch feel free to do so.

Cheers,

Michael
