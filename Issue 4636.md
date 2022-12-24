# Issue 4636: improve polynomial_modn_dense_ntl.Polynomial_dense_mod_p

archive/issues_004636.json:
```json
{
    "body": "Assignee: was\n\nCC:  craigcitro\n\nKeywords: polynomial modn finite field gf\n\nsage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p is very old.\n\nThe attached patch removes (but doesn't yet delete -- could you verify it can be removed, reviewer?) Polynomial_dense_mod_p and implements polynomial_modn_dense_ntl.Polynomial_dense_modp_ntl_zz/ZZ using the newer techniques.\n\nIt makes basic arithmetic faster.  I was finding that arithmetic in GF(next_prime(2^50))['x'] was slower than in Zmod(next_prime(2^50)+1)['x'], but now I cannot find the comparison!  In any case, this is much faster for doing gcd/xgcd in GF(p)['x'].\n\nIssue created by migration from https://trac.sagemath.org/ticket/4636\n\n",
    "created_at": "2008-11-27T04:44:35Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "improve polynomial_modn_dense_ntl.Polynomial_dense_mod_p",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4636",
    "user": "ncalexan"
}
```
Assignee: was

CC:  craigcitro

Keywords: polynomial modn finite field gf

sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p is very old.

The attached patch removes (but doesn't yet delete -- could you verify it can be removed, reviewer?) Polynomial_dense_mod_p and implements polynomial_modn_dense_ntl.Polynomial_dense_modp_ntl_zz/ZZ using the newer techniques.

It makes basic arithmetic faster.  I was finding that arithmetic in GF(next_prime(2^50))['x'] was slower than in Zmod(next_prime(2^50)+1)['x'], but now I cannot find the comparison!  In any case, this is much faster for doing gcd/xgcd in GF(p)['x'].

Issue created by migration from https://trac.sagemath.org/ticket/4636





---

archive/issue_comments_034864.json:
```json
{
    "body": "Attachment [4636-ncalexan-Polynomial_dense_modp_ntl_zz.patch](tarball://root/attachments/some-uuid/ticket4636/4636-ncalexan-Polynomial_dense_modp_ntl_zz.patch) by mabshoff created at 2008-11-27 04:51:09",
    "created_at": "2008-11-27T04:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4636#issuecomment-34864",
    "user": "mabshoff"
}
```

Attachment [4636-ncalexan-Polynomial_dense_modp_ntl_zz.patch](tarball://root/attachments/some-uuid/ticket4636/4636-ncalexan-Polynomial_dense_modp_ntl_zz.patch) by mabshoff created at 2008-11-27 04:51:09



---

archive/issue_comments_034865.json:
```json
{
    "body": "Hi Nick, did you see the 'newest' technique to implement these things? It is not 100% polished yet (e.g. I suppose context handling should be improved) but it should be the most straight forward in terms of avoiding code duplication. See `sage.rings.polynomial.polynomial_gf2x` and `sage.rings.polynomial.polynomial_template` for details.",
    "created_at": "2008-11-27T10:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4636#issuecomment-34865",
    "user": "malb"
}
```

Hi Nick, did you see the 'newest' technique to implement these things? It is not 100% polished yet (e.g. I suppose context handling should be improved) but it should be the most straight forward in terms of avoiding code duplication. See `sage.rings.polynomial.polynomial_gf2x` and `sage.rings.polynomial.polynomial_template` for details.



---

archive/issue_comments_034866.json:
```json
{
    "body": "Nick, Is this supposed be \"with patch; needs review\"?",
    "created_at": "2008-11-27T16:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4636#issuecomment-34866",
    "user": "was"
}
```

Nick, Is this supposed be "with patch; needs review"?



---

archive/issue_comments_034867.json:
```json
{
    "body": "REFEREE REPORT:\n\nI applied this patch and doctested the rings directory.  I get a couple of doctest failures:\n\n\n```\nsage -t  devel/sage-main/sage/rings/integer_mod.pyx\n**********************************************************************\nFile \"/Users/wstein/sage/devel/sage-main/sage/rings/integer_mod.pyx\", line 505:\n    sage: type(a.polynomial())\nExpected:\n    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>\nGot:\n    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modp_ntl_zz'>\n**********************************************************************\n\nsage -t  devel/sage-main/sage/rings/finite_field_givaro.pyx\n**********************************************************************\nFile \"/Users/wstein/sage/devel/sage-main/sage/rings/finite_field_givaro.pyx\", line 1799:\n    sage: type(f)\nExpected:\n    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>\nGot:\n    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modp_ntl_zz'>\n**********************************************************************\n1 items had failures:\n\n\nsage -t  devel/sage-main/sage/rings/finite_field.py\n**********************************************************************\nFile \"/Users/wstein/sage/devel/sage-main/sage/rings/finite_field.py\", line 178:\n    sage: type(f)\nExpected:\n    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>\nGot:\n    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modp_ntl_zz'>\n**********************************************************************\n1 items had failures:\n\n...\n\tsage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 1 doctests failed\n\tsage -t  devel/sage-main/sage/rings/integer_mod.pyx # 1 doctests failed\n\tsage -t  devel/sage-main/sage/rings/finite_field_givaro.pyx # 1 doctests failed\n\tsage -t  devel/sage-main/sage/rings/finite_field.py # 1 doctests failed\n\n```\n",
    "created_at": "2008-11-28T04:45:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4636#issuecomment-34867",
    "user": "was"
}
```

REFEREE REPORT:

I applied this patch and doctested the rings directory.  I get a couple of doctest failures:


```
sage -t  devel/sage-main/sage/rings/integer_mod.pyx
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/rings/integer_mod.pyx", line 505:
    sage: type(a.polynomial())
Expected:
    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>
Got:
    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modp_ntl_zz'>
**********************************************************************

sage -t  devel/sage-main/sage/rings/finite_field_givaro.pyx
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/rings/finite_field_givaro.pyx", line 1799:
    sage: type(f)
Expected:
    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>
Got:
    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modp_ntl_zz'>
**********************************************************************
1 items had failures:


sage -t  devel/sage-main/sage/rings/finite_field.py
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/rings/finite_field.py", line 178:
    sage: type(f)
Expected:
    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>
Got:
    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modp_ntl_zz'>
**********************************************************************
1 items had failures:

...
	sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 1 doctests failed
	sage -t  devel/sage-main/sage/rings/integer_mod.pyx # 1 doctests failed
	sage -t  devel/sage-main/sage/rings/finite_field_givaro.pyx # 1 doctests failed
	sage -t  devel/sage-main/sage/rings/finite_field.py # 1 doctests failed

```




---

archive/issue_comments_034868.json:
```json
{
    "body": "I should reimplement this using `polynomial_template.pxi` and Nick will review it once its done.",
    "created_at": "2009-01-23T07:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4636#issuecomment-34868",
    "user": "malb"
}
```

I should reimplement this using `polynomial_template.pxi` and Nick will review it once its done.



---

archive/issue_comments_034869.json:
```json
{
    "body": "Changing assignee from was to malb.",
    "created_at": "2009-01-25T19:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4636#issuecomment-34869",
    "user": "malb"
}
```

Changing assignee from was to malb.



---

archive/issue_comments_034870.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-25T19:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4636#issuecomment-34870",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034871.json:
```json
{
    "body": "What is the status of this?  If no one is going to do the templated version, then we should probably include this code.",
    "created_at": "2009-10-19T17:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4636#issuecomment-34871",
    "user": "mhansen"
}
```

What is the status of this?  If no one is going to do the templated version, then we should probably include this code.



---

archive/issue_comments_034872.json:
```json
{
    "body": "I vote for closing this ticket\n\n\n```\nsage: f = GF(7)['x']([2, 1, 3])\nsage: type(f)\n<type 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>\n```\n",
    "created_at": "2010-07-21T16:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4636#issuecomment-34872",
    "user": "malb"
}
```

I vote for closing this ticket


```
sage: f = GF(7)['x']([2, 1, 3])
sage: type(f)
<type 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>
```




---

archive/issue_comments_034873.json:
```json
{
    "body": "I agree with malb.",
    "created_at": "2012-05-28T07:33:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4636#issuecomment-34873",
    "user": "mhansen"
}
```

I agree with malb.



---

archive/issue_comments_034874.json:
```json
{
    "body": "Changing keywords from \"polynomial modn finite field gf\" to \"polynomial modn finite field gf sd40.5\".",
    "created_at": "2012-05-28T07:33:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4636#issuecomment-34874",
    "user": "mhansen"
}
```

Changing keywords from "polynomial modn finite field gf" to "polynomial modn finite field gf sd40.5".



---

archive/issue_comments_034875.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-05-28T07:33:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4636#issuecomment-34875",
    "user": "mhansen"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_034876.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-06-02T12:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4636#issuecomment-34876",
    "user": "jdemeyer"
}
```

Resolution: worksforme
