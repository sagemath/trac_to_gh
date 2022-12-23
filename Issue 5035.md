# Issue 5035: get doctest coverage of matrix_generic_dense.pyx up to 100%

archive/issues_005035.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5035\n\n",
    "created_at": "2009-01-20T07:14:41Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "get doctest coverage of matrix_generic_dense.pyx up to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5035",
    "user": "was"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/5035





---

archive/issue_comments_038338.json:
```json
{
    "body": "this is against sage-3.3.alpha0",
    "created_at": "2009-01-20T07:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5035#issuecomment-38338",
    "user": "was"
}
```

this is against sage-3.3.alpha0



---

archive/issue_comments_038339.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-20T07:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5035#issuecomment-38339",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_038340.json:
```json
{
    "body": "The patch applies cleanly, but I get a doctest error:\n\n```\nsage -t  \"devel/sage-main/sage/matrix/matrix_generic_dense.pyx\"\n**********************************************************************\nFile \"/var/tmp/sage-3.3.alpha0/devel/sage-main/sage/matrix/matrix_generic_dense.pyx\", line 161:\n    sage: hash(A)\nExpected:\n    -623270016\nGot:\n    139665060168050560\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_6\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /var/tmp/sage-3.3.alpha0/tmp/.doctest_matrix_generic_dense.py\n\t [1.1 s]\nexit code: 1024\n```\n",
    "created_at": "2009-01-20T07:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5035#issuecomment-38340",
    "user": "ddrake"
}
```

The patch applies cleanly, but I get a doctest error:

```
sage -t  "devel/sage-main/sage/matrix/matrix_generic_dense.pyx"
**********************************************************************
File "/var/tmp/sage-3.3.alpha0/devel/sage-main/sage/matrix/matrix_generic_dense.pyx", line 161:
    sage: hash(A)
Expected:
    -623270016
Got:
    139665060168050560
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file /var/tmp/sage-3.3.alpha0/tmp/.doctest_matrix_generic_dense.py
	 [1.1 s]
exit code: 1024
```




---

archive/issue_comments_038341.json:
```json
{
    "body": "Attachment\n\nWith both patches applied, we have 100% coverage, and the examples are nice. Positive review.",
    "created_at": "2009-01-20T07:37:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5035#issuecomment-38341",
    "user": "ddrake"
}
```

Attachment

With both patches applied, we have 100% coverage, and the examples are nice. Positive review.



---

archive/issue_comments_038342.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T09:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5035#issuecomment-38342",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038343.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha1",
    "created_at": "2009-01-23T09:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5035#issuecomment-38343",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.3.alpha1
