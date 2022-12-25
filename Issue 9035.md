# Issue 9035: add degree argument to univariate polynomial reverse() method

archive/issues_009035.json:
```json
{
    "body": "Assignee: @aghitza\n\nAttached patch adds a `degree` argument to the `reverse()` method of univariate polynomials and wraps the methods provided by FLINT in `polynomial_zmod_flint` and `polynomial_integer_dense_flint` classes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9035\n\n",
    "created_at": "2010-05-24T13:06:18Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "add degree argument to univariate polynomial reverse() method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9035",
    "user": "https://github.com/burcin"
}
```
Assignee: @aghitza

Attached patch adds a `degree` argument to the `reverse()` method of univariate polynomials and wraps the methods provided by FLINT in `polynomial_zmod_flint` and `polynomial_integer_dense_flint` classes.

Issue created by migration from https://trac.sagemath.org/ticket/9035





---

archive/issue_comments_083510.json:
```json
{
    "body": "Attachment [trac_9035-zmod_poly_reverse.patch](tarball://root/attachments/some-uuid/ticket9035/trac_9035-zmod_poly_reverse.patch) by @burcin created at 2010-05-24 13:10:39",
    "created_at": "2010-05-24T13:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9035#issuecomment-83510",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9035-zmod_poly_reverse.patch](tarball://root/attachments/some-uuid/ticket9035/trac_9035-zmod_poly_reverse.patch) by @burcin created at 2010-05-24 13:10:39



---

archive/issue_comments_083511.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-24T13:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9035#issuecomment-83511",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083512.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-27T11:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9035#issuecomment-83512",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083513.json:
```json
{
    "body": "Patch applies fine to 4.4.3.alpha0, and looks good to me.\n\nTests pass (I tested all files in sage/rings/polynomial plus some other random tests).\n\nI am giving this a positive review, but wonder whether the following reverse functions should also be changed to be consistent:\n\n```\nlibs/ntl/ntl_GF2X.pyx:645:    def reverse(self, int hi = -2):\nlibs/ntl/ntl_ZZX.pyx:768:    def reverse(self, hi=None):\nlibs/ntl/ntl_ZZ_pEX.pyx:850:    def reverse(self, hi=None):\nlibs/ntl/ntl_ZZ_pX.pyx:947:    def reverse(self, hi=None):\n...\nrings/polynomial/polynomial_modn_dense_ntl.pyx:1005:    def reverse(self):\nrings/polynomial/polynomial_modn_dense_ntl.pyx:1548:    def reverse(self):\nrings/polynomial/polynomial_real_mpfr_dense.pyx:484:    def reverse(self):\n...\nrings/polynomial/padics/polynomial_padic_capped_relative_dense.py:840:    def reverse(self, n = None):\n```\n",
    "created_at": "2010-05-27T11:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9035#issuecomment-83513",
    "user": "https://github.com/JohnCremona"
}
```

Patch applies fine to 4.4.3.alpha0, and looks good to me.

Tests pass (I tested all files in sage/rings/polynomial plus some other random tests).

I am giving this a positive review, but wonder whether the following reverse functions should also be changed to be consistent:

```
libs/ntl/ntl_GF2X.pyx:645:    def reverse(self, int hi = -2):
libs/ntl/ntl_ZZX.pyx:768:    def reverse(self, hi=None):
libs/ntl/ntl_ZZ_pEX.pyx:850:    def reverse(self, hi=None):
libs/ntl/ntl_ZZ_pX.pyx:947:    def reverse(self, hi=None):
...
rings/polynomial/polynomial_modn_dense_ntl.pyx:1005:    def reverse(self):
rings/polynomial/polynomial_modn_dense_ntl.pyx:1548:    def reverse(self):
rings/polynomial/polynomial_real_mpfr_dense.pyx:484:    def reverse(self):
...
rings/polynomial/padics/polynomial_padic_capped_relative_dense.py:840:    def reverse(self, n = None):
```




---

archive/issue_events_009187.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-06-06T01:24:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9035",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9035#event-9187"
}
```



---

archive/issue_comments_083514.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9035#issuecomment-83514",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
