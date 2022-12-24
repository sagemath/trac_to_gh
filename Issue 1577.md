# Issue 1577: .coefficients() and .monomials() differ in order in multivariate polynomial rings

archive/issues_001577.json:
```json
{
    "body": "Assignee: malb\n\nCC:  jbmohler\n\nKeywords: multi polynomial rings coefficients monomials\n\nA small annoyance -- the ordering on the lists below is different:\n\n```\nsage: R.<fx,fy,gx,gy> = ZZ[]\nsage: F = ((fx*gy - fy*gx)^3)\nsage: F\n-1*fy^3*gx^3 + 3*fx*fy^2*gx^2*gy - 3*fx^2*fy*gx*gy^2 + fx^3*gy^3\nsage: F.monomials()\n[fx^2*fy*gx*gy^2, fy^3*gx^3, fx*fy^2*gx^2*gy, fx^3*gy^3]\nsage: F.coefficients()\n[-3, -1, 3, 1]\n```\n\n\n`F.coefficients?` says\n\"The order the coefficients appear in depends on the ordering used on self's parent.\"\n`F.monomials?` says\n\"Returns list of all monomials which occure in this multivariate polynomial.\"\n\nI think the latter should be changed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1577\n\n",
    "created_at": "2007-12-21T01:34:55Z",
    "labels": [
        "commutative algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": ".coefficients() and .monomials() differ in order in multivariate polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1577",
    "user": "ncalexan"
}
```
Assignee: malb

CC:  jbmohler

Keywords: multi polynomial rings coefficients monomials

A small annoyance -- the ordering on the lists below is different:

```
sage: R.<fx,fy,gx,gy> = ZZ[]
sage: F = ((fx*gy - fy*gx)^3)
sage: F
-1*fy^3*gx^3 + 3*fx*fy^2*gx^2*gy - 3*fx^2*fy*gx*gy^2 + fx^3*gy^3
sage: F.monomials()
[fx^2*fy*gx*gy^2, fy^3*gx^3, fx*fy^2*gx^2*gy, fx^3*gy^3]
sage: F.coefficients()
[-3, -1, 3, 1]
```


`F.coefficients?` says
"The order the coefficients appear in depends on the ordering used on self's parent."
`F.monomials?` says
"Returns list of all monomials which occure in this multivariate polynomial."

I think the latter should be changed.

Issue created by migration from https://trac.sagemath.org/ticket/1577





---

archive/issue_comments_010035.json:
```json
{
    "body": "Looks like monomials and coefficients line up, but it's not in the same order as they print?",
    "created_at": "2007-12-21T01:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1577#issuecomment-10035",
    "user": "rlm"
}
```

Looks like monomials and coefficients line up, but it's not in the same order as they print?



---

archive/issue_comments_010036.json:
```json
{
    "body": "While we're here:\n\nThe elements of list() don't have the correct types -- the final line should be a libsingular poly as well:\n\n```\nsage: R.<x, y> = QQ[]\nsage: (x + y).monomials()\n[x, y]\nsage: type((x + y).monomials()[0])\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\nsage: list(x + y)[0]\n(1, x)\nsage: type(list(x + y)[0][-1])\n<class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>\n```\n",
    "created_at": "2007-12-21T04:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1577#issuecomment-10036",
    "user": "ncalexan"
}
```

While we're here:

The elements of list() don't have the correct types -- the final line should be a libsingular poly as well:

```
sage: R.<x, y> = QQ[]
sage: (x + y).monomials()
[x, y]
sage: type((x + y).monomials()[0])
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
sage: list(x + y)[0]
(1, x)
sage: type(list(x + y)[0][-1])
<class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>
```




---

archive/issue_comments_010037.json:
```json
{
    "body": "Attachment [trac_1577.patch](tarball://root/attachments/some-uuid/ticket1577/trac_1577.patch) by malb created at 2008-01-06 17:09:38",
    "created_at": "2008-01-06T17:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1577#issuecomment-10037",
    "user": "malb"
}
```

Attachment [trac_1577.patch](tarball://root/attachments/some-uuid/ticket1577/trac_1577.patch) by malb created at 2008-01-06 17:09:38



---

archive/issue_comments_010038.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-06T17:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1577#issuecomment-10038",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010039.json:
```json
{
    "body": "I entirely agree with the actual code of this patch.  One of the doc-string changes is not representative though -- we are not sorting largest to smallest (whatever that might mean for a monomial).\n\nI think that ZZ mpolys doc-string for monomials should read \n\n```\n        Return the list of monomials in self. The returned list is\n        ordered by the term ordering of self.parent().\n```\n\njust like for QQ mpolys.",
    "created_at": "2008-01-10T10:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1577#issuecomment-10039",
    "user": "jbmohler"
}
```

I entirely agree with the actual code of this patch.  One of the doc-string changes is not representative though -- we are not sorting largest to smallest (whatever that might mean for a monomial).

I think that ZZ mpolys doc-string for monomials should read 

```
        Return the list of monomials in self. The returned list is
        ordered by the term ordering of self.parent().
```

just like for QQ mpolys.



---

archive/issue_comments_010040.json:
```json
{
    "body": "Oh, perhaps I should add that I doc-tested 'sage/rings' and verified that the patch fixes the original bug as well as the bug mentioned in the comments.",
    "created_at": "2008-01-10T10:47:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1577#issuecomment-10040",
    "user": "jbmohler"
}
```

Oh, perhaps I should add that I doc-tested 'sage/rings' and verified that the patch fixes the original bug as well as the bug mentioned in the comments.



---

archive/issue_comments_010041.json:
```json
{
    "body": "I am okay with changing the docstring but want to point out that \"from largest to smallest\" is well defined for a multivariate polynomial in a given ring. It means to sort according to the monomial ordering of the ring (which is a property of that ring) but in _descending_ order. This fact is not clear -- though probably 'natural' -- when writing \"The returned list is ordered by the term ordering of self.parent()\"",
    "created_at": "2008-01-10T10:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1577#issuecomment-10041",
    "user": "malb"
}
```

I am okay with changing the docstring but want to point out that "from largest to smallest" is well defined for a multivariate polynomial in a given ring. It means to sort according to the monomial ordering of the ring (which is a property of that ring) but in _descending_ order. This fact is not clear -- though probably 'natural' -- when writing "The returned list is ordered by the term ordering of self.parent()"



---

archive/issue_comments_010042.json:
```json
{
    "body": "Attachment [trac_1577_comment_4.patch](tarball://root/attachments/some-uuid/ticket1577/trac_1577_comment_4.patch) by malb created at 2008-01-10 15:03:32\n\nJoel's suggested change is in `trac_1577_comment_4.patch`.",
    "created_at": "2008-01-10T15:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1577#issuecomment-10042",
    "user": "malb"
}
```

Attachment [trac_1577_comment_4.patch](tarball://root/attachments/some-uuid/ticket1577/trac_1577_comment_4.patch) by malb created at 2008-01-10 15:03:32

Joel's suggested change is in `trac_1577_comment_4.patch`.



---

archive/issue_comments_010043.json:
```json
{
    "body": "jbmohler can you verify this is correct now?",
    "created_at": "2008-01-16T15:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1577#issuecomment-10043",
    "user": "malb"
}
```

jbmohler can you verify this is correct now?



---

archive/issue_comments_010044.json:
```json
{
    "body": "I reported this bug, and I approved this patch!  Apply.",
    "created_at": "2008-01-20T06:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1577#issuecomment-10044",
    "user": "ncalexan"
}
```

I reported this bug, and I approved this patch!  Apply.



---

archive/issue_comments_010045.json:
```json
{
    "body": "Merged both patches in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T05:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1577#issuecomment-10045",
    "user": "mabshoff"
}
```

Merged both patches in Sage 2.10.1.alpha1



---

archive/issue_comments_010046.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T05:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1577#issuecomment-10046",
    "user": "mabshoff"
}
```

Resolution: fixed
