# Issue 4984: Clean up __getitem__ for matrices once Cython is smarter

archive/issues_004984.json:
```json
{
    "body": "Assignee: @williamstein\n\nSo we currently use several Python/C API calls to speed up the `__getitem__` method in `sage/matrix/matrix0.pyx`. In particular, we do several typechecks against standard Python types, and replacing generic `PY_TYPE_CHECK` calls with specific Python/C API calls (like `PySlice_Check`) provides a significant speedup. Once Cython can do all these things for us, we should clean up `__getitem__` so that it's more readable/portable. \n\nAlternatively, if such functionality still doesn't exist in Cython, one should feel free to go, implement that functionality, get it merged, create a new Cython spkg, and then make these changes. `:)`\n\nIssue created by migration from https://trac.sagemath.org/ticket/4984\n\n",
    "created_at": "2009-01-16T02:36:55Z",
    "labels": [
        "component: linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Clean up __getitem__ for matrices once Cython is smarter",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4984",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @williamstein

So we currently use several Python/C API calls to speed up the `__getitem__` method in `sage/matrix/matrix0.pyx`. In particular, we do several typechecks against standard Python types, and replacing generic `PY_TYPE_CHECK` calls with specific Python/C API calls (like `PySlice_Check`) provides a significant speedup. Once Cython can do all these things for us, we should clean up `__getitem__` so that it's more readable/portable. 

Alternatively, if such functionality still doesn't exist in Cython, one should feel free to go, implement that functionality, get it merged, create a new Cython spkg, and then make these changes. `:)`

Issue created by migration from https://trac.sagemath.org/ticket/4984





---

archive/issue_comments_037942.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4984#issuecomment-37942",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_037943.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-01-22T10:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4984#issuecomment-37943",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_037944.json:
```json
{
    "body": "`PY_TYPE_CHECK` is gone.",
    "created_at": "2016-01-22T10:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4984#issuecomment-37944",
    "user": "https://github.com/jdemeyer"
}
```

`PY_TYPE_CHECK` is gone.



---

archive/issue_comments_037945.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-01-22T10:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4984#issuecomment-37945",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_037946.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-02-23T22:59:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4984#issuecomment-37946",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_005227.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2016-02-23T22:59:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4984",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4984#event-5227"
}
```
