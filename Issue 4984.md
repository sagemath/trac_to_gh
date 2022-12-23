# Issue 4984: Clean up __getitem__ for matrices once Cython is smarter

archive/issues_004984.json:
```json
{
    "body": "Assignee: was\n\nSo we currently use several Python/C API calls to speed up the `__getitem__` method in `sage/matrix/matrix0.pyx`. In particular, we do several typechecks against standard Python types, and replacing generic `PY_TYPE_CHECK` calls with specific Python/C API calls (like `PySlice_Check`) provides a significant speedup. Once Cython can do all these things for us, we should clean up `__getitem__` so that it's more readable/portable. \n\nAlternatively, if such functionality still doesn't exist in Cython, one should feel free to go, implement that functionality, get it merged, create a new Cython spkg, and then make these changes. `:)`\n\nIssue created by migration from https://trac.sagemath.org/ticket/4984\n\n",
    "created_at": "2009-01-16T02:36:55Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "Clean up __getitem__ for matrices once Cython is smarter",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4984",
    "user": "craigcitro"
}
```
Assignee: was

So we currently use several Python/C API calls to speed up the `__getitem__` method in `sage/matrix/matrix0.pyx`. In particular, we do several typechecks against standard Python types, and replacing generic `PY_TYPE_CHECK` calls with specific Python/C API calls (like `PySlice_Check`) provides a significant speedup. Once Cython can do all these things for us, we should clean up `__getitem__` so that it's more readable/portable. 

Alternatively, if such functionality still doesn't exist in Cython, one should feel free to go, implement that functionality, get it merged, create a new Cython spkg, and then make these changes. `:)`

Issue created by migration from https://trac.sagemath.org/ticket/4984





---

archive/issue_comments_038014.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4984#issuecomment-38014",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_038015.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-01-22T10:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4984#issuecomment-38015",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_038016.json:
```json
{
    "body": "`PY_TYPE_CHECK` is gone.",
    "created_at": "2016-01-22T10:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4984#issuecomment-38016",
    "user": "jdemeyer"
}
```

`PY_TYPE_CHECK` is gone.



---

archive/issue_comments_038017.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-01-22T10:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4984#issuecomment-38017",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_038018.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-02-23T22:59:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4984#issuecomment-38018",
    "user": "vbraun"
}
```

Resolution: fixed
