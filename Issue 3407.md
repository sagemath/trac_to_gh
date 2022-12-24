# Issue 3407: [with patch, needs review] better error handling for GB calculations

archive/issues_003407.json:
```json
{
    "body": "Assignee: malb\n\nCC:  cremona wstein mhansen\n\n* bail out of toy_buchberger if the term ordering is unknown\n* bail out of Singular conversion if number field is relative. Singular supports this, but our conversion not just yet.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3407\n\n",
    "created_at": "2008-06-12T22:42:15Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] better error handling for GB calculations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3407",
    "user": "malb"
}
```
Assignee: malb

CC:  cremona wstein mhansen

* bail out of toy_buchberger if the term ordering is unknown
* bail out of Singular conversion if number field is relative. Singular supports this, but our conversion not just yet.

Issue created by migration from https://trac.sagemath.org/ticket/3407





---

archive/issue_comments_023896.json:
```json
{
    "body": "Attachment [gb_errors.patch](tarball://root/attachments/some-uuid/ticket3407/gb_errors.patch) by craigcitro created at 2008-06-15 21:54:18",
    "created_at": "2008-06-15T21:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23896",
    "user": "craigcitro"
}
```

Attachment [gb_errors.patch](tarball://root/attachments/some-uuid/ticket3407/gb_errors.patch) by craigcitro created at 2008-06-15 21:54:18



---

archive/issue_comments_023897.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_malb\".",
    "created_at": "2008-06-15T21:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23897",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_malb".



---

archive/issue_comments_023898.json:
```json
{
    "body": "IIRC mhansen wants to review it. mhansen can you confirm or deny.",
    "created_at": "2008-06-16T03:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23898",
    "user": "malb"
}
```

IIRC mhansen wants to review it. mhansen can you confirm or deny.



---

archive/issue_comments_023899.json:
```json
{
    "body": "Yep -- I'll do it in the next hour.",
    "created_at": "2008-06-16T03:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23899",
    "user": "mhansen"
}
```

Yep -- I'll do it in the next hour.



---

archive/issue_comments_023900.json:
```json
{
    "body": "I am seeing doctest failures:\n\n```\n        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py # 13 doctests failed\n        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 13 doctests failed\n        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 1 doctests failed\n```\n\n#3406 shows issue in similar areas.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-23T08:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23900",
    "user": "mabshoff"
}
```

I am seeing doctest failures:

```
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py # 13 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 13 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 1 doctests failed
```

#3406 shows issue in similar areas.

Cheers,

Michael



---

archive/issue_comments_023901.json:
```json
{
    "body": "After fixing #3406.\n\n\n```\nsage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py\nsage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py\nsage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\n----------------------------------------------------------------------\nAll tests passed!\n```\n\n\nSince this patch depends on #3406 anyway, I'll add the positive review back.",
    "created_at": "2008-06-23T17:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23901",
    "user": "malb"
}
```

After fixing #3406.


```
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py
sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py
----------------------------------------------------------------------
All tests passed!
```


Since this patch depends on #3406 anyway, I'll add the positive review back.



---

archive/issue_comments_023902.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-25T00:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23902",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_comments_023903.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-25T00:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23903",
    "user": "mabshoff"
}
```

Resolution: fixed
