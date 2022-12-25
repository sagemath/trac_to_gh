# Issue 9932: BooleanPolynomialRing not recognizing leading term of elements

archive/issues_009932.json:
```json
{
    "body": "Assignee: @malb\n\n\n```\nR = BooleanPolynomialRing(5,'x')\ne = R.random_element()\nprint e\nprint e.lt()\nprint e.lt() in R  ## says false???\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9933\n\n",
    "created_at": "2010-09-17T13:57:20Z",
    "labels": [
        "component: commutative algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "BooleanPolynomialRing not recognizing leading term of elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9932",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```
Assignee: @malb


```
R = BooleanPolynomialRing(5,'x')
e = R.random_element()
print e
print e.lt()
print e.lt() in R  ## says false???
```


Issue created by migration from https://trac.sagemath.org/ticket/9933





---

archive/issue_comments_098734.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-10-12T16:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9932#issuecomment-98734",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098735.json:
```json
{
    "body": "Attachment [trac_9933.patch](tarball://root/attachments/some-uuid/ticket9933/trac_9933.patch) by @malb created at 2010-10-12 16:41:44\n\nThe attached patch fixes the reported issue. In the process I also fixed a very annoying performance issue\n\n\n```python\n# Old\nsage: B = BooleanPolynomialRing(200,'x')\nsage: %timeit B(\"x0\")\n25 loops, best of 3: 17.1 ms per loop\n\n# New\nsage: B = BooleanPolynomialRing(200,'x')\nsage: %timeit B(\"x0\")\n625 loops, best of 3: 11.6 \u00b5s per loop\n\n# \"optimal\"\nsage: gd = B.gens_dict()\nsage: %timeit gd['x0']\n625 loops, best of 3: 94.2 ns per loop\n```\n",
    "created_at": "2010-10-12T16:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9932#issuecomment-98735",
    "user": "https://github.com/malb"
}
```

Attachment [trac_9933.patch](tarball://root/attachments/some-uuid/ticket9933/trac_9933.patch) by @malb created at 2010-10-12 16:41:44

The attached patch fixes the reported issue. In the process I also fixed a very annoying performance issue


```python
# Old
sage: B = BooleanPolynomialRing(200,'x')
sage: %timeit B("x0")
25 loops, best of 3: 17.1 ms per loop

# New
sage: B = BooleanPolynomialRing(200,'x')
sage: %timeit B("x0")
625 loops, best of 3: 11.6 µs per loop

# "optimal"
sage: gd = B.gens_dict()
sage: %timeit gd['x0']
625 loops, best of 3: 94.2 ns per loop
```




---

archive/issue_comments_098736.json:
```json
{
    "body": "Patch applies to 4.6.1.alpha2 and passes `make ptestlong` on sage.math.",
    "created_at": "2010-11-23T19:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9932#issuecomment-98736",
    "user": "https://github.com/malb"
}
```

Patch applies to 4.6.1.alpha2 and passes `make ptestlong` on sage.math.



---

archive/issue_comments_098737.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-24T19:12:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9932#issuecomment-98737",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098738.json:
```json
{
    "body": "\n```\nApplied patch to sage-4.6 on skynet/lena.  Patch fixes\nreported problem.  Ran 'make testlong'. All tests passed.  Positive review!\n```\n",
    "created_at": "2010-11-24T19:12:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9932#issuecomment-98738",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```


```
Applied patch to sage-4.6 on skynet/lena.  Patch fixes
reported problem.  Ran 'make testlong'. All tests passed.  Positive review!
```




---

archive/issue_comments_098739.json:
```json
{
    "body": "The patch fixes the problem. All tests passed with \"make ptestlong\", although certain tests had to be repeated due to \"time out\".",
    "created_at": "2010-11-30T08:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9932#issuecomment-98739",
    "user": "https://trac.sagemath.org/admin/accounts/users/sbulygin"
}
```

The patch fixes the problem. All tests passed with "make ptestlong", although certain tests had to be repeated due to "time out".



---

archive/issue_comments_098740.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-12-02T16:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9932#issuecomment-98740",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
