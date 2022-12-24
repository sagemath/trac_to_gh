# Issue 2105: Constructor for ntl.GF2X polynomials does not take Polynomials over  GF(2) as advertised by docstring

archive/issues_002105.json:
```json
{
    "body": "Assignee: somebody\n\nMarshall Buck on [sage-support] writes:\n\n\n```\nsage: R.<x> = GF(2)[]\nsage: f = x^5+x^2+1\nsage: fx = ntl.GF2X(f)\n```\n\ngives error:\n\n```\nTraceback (most recent call last):    fx\n  File \"ntl_GF2X.pyx\", line 141, in\nsage.libs.ntl.ntl_GF2X.ntl_GF2X.__init__\nAttributeError: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute '_Polynomial_dense_mod_n__poly'\n```\n\n\n`fx = ntl.GF2X(f.list())` works, as well as `fx = ntl.GF2X(f.ntl_ZZ_pX())`\n\nIssue created by migration from https://trac.sagemath.org/ticket/2105\n\n",
    "created_at": "2008-02-08T09:42:46Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Constructor for ntl.GF2X polynomials does not take Polynomials over  GF(2) as advertised by docstring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2105",
    "user": "malb"
}
```
Assignee: somebody

Marshall Buck on [sage-support] writes:


```
sage: R.<x> = GF(2)[]
sage: f = x^5+x^2+1
sage: fx = ntl.GF2X(f)
```

gives error:

```
Traceback (most recent call last):    fx
  File "ntl_GF2X.pyx", line 141, in
sage.libs.ntl.ntl_GF2X.ntl_GF2X.__init__
AttributeError: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute '_Polynomial_dense_mod_n__poly'
```


`fx = ntl.GF2X(f.list())` works, as well as `fx = ntl.GF2X(f.ntl_ZZ_pX())`

Issue created by migration from https://trac.sagemath.org/ticket/2105





---

archive/issue_comments_013725.json:
```json
{
    "body": "Changing assignee from somebody to malb.",
    "created_at": "2008-02-18T15:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2105#issuecomment-13725",
    "user": "malb"
}
```

Changing assignee from somebody to malb.



---

archive/issue_comments_013726.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-18T15:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2105#issuecomment-13726",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013727.json:
```json
{
    "body": "fix",
    "created_at": "2008-02-18T15:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2105#issuecomment-13727",
    "user": "malb"
}
```

fix



---

archive/issue_comments_013728.json:
```json
{
    "body": "Attachment [trac_2105.patch](tarball://root/attachments/some-uuid/ticket2105/trac_2105.patch) by malb created at 2008-02-18 15:34:20",
    "created_at": "2008-02-18T15:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2105#issuecomment-13728",
    "user": "malb"
}
```

Attachment [trac_2105.patch](tarball://root/attachments/some-uuid/ticket2105/trac_2105.patch) by malb created at 2008-02-18 15:34:20



---

archive/issue_comments_013729.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-02-27T18:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2105#issuecomment-13729",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_013730.json:
```json
{
    "body": "And to me.",
    "created_at": "2008-02-27T18:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2105#issuecomment-13730",
    "user": "cremona"
}
```

And to me.



---

archive/issue_comments_013731.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T00:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2105#issuecomment-13731",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013732.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T00:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2105#issuecomment-13732",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc0
