# Issue 2834: [with patch, needs review] PyLint import cleanup for sage.rings.polynomial

archive/issues_002834.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: pylint\n\nI ran `pylint --enable-checker=imports` on `sage.rings.polynomial` and attempted to fix what it reported\n* relative imports\n* double imports\n* circular imports\n\nThe patch could be considered controversial, please check carefully.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2834\n\n",
    "created_at": "2008-04-06T22:18:51Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] PyLint import cleanup for sage.rings.polynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2834",
    "user": "https://github.com/malb"
}
```
Assignee: cwitty

Keywords: pylint

I ran `pylint --enable-checker=imports` on `sage.rings.polynomial` and attempted to fix what it reported
* relative imports
* double imports
* circular imports

The patch could be considered controversial, please check carefully.

Issue created by migration from https://trac.sagemath.org/ticket/2834





---

archive/issue_comments_019406.json:
```json
{
    "body": "Attachment [pylint_polynomial_import.patch](tarball://root/attachments/some-uuid/ticket2834/pylint_polynomial_import.patch) by @mwhansen created at 2008-04-06 22:49:52\n\nAll tests pass for me.  I'd give it a positive review, but I'd also like to hear others' comments.",
    "created_at": "2008-04-06T22:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19406",
    "user": "https://github.com/mwhansen"
}
```

Attachment [pylint_polynomial_import.patch](tarball://root/attachments/some-uuid/ticket2834/pylint_polynomial_import.patch) by @mwhansen created at 2008-04-06 22:49:52

All tests pass for me.  I'd give it a positive review, but I'd also like to hear others' comments.



---

archive/issue_comments_019407.json:
```json
{
    "body": "I like this patch. But after applying and doing a `sage -ba` I see the following failure with `-long`:\n\n```\nsage -t -long devel/sage/sage/coding/linear_code.py         \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.alpha2/tmp/linear_code.py\", line 724:\n    sage: C.chinen_polynomial()       # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_12[2]>\", line 1, in <module>\n        C.chinen_polynomial()       # long time###line 724:\n    sage: C.chinen_polynomial()       # long time\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 737, in chinen_polynomial\n        from sage.rings.polynomial.polynomial_ring import PolynomialRing, polygen\n    ImportError: cannot import name PolynomialRing\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T00:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19407",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I like this patch. But after applying and doing a `sage -ba` I see the following failure with `-long`:

```
sage -t -long devel/sage/sage/coding/linear_code.py         
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/tmp/linear_code.py", line 724:
    sage: C.chinen_polynomial()       # long time
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_12[2]>", line 1, in <module>
        C.chinen_polynomial()       # long time###line 724:
    sage: C.chinen_polynomial()       # long time
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 737, in chinen_polynomial
        from sage.rings.polynomial.polynomial_ring import PolynomialRing, polygen
    ImportError: cannot import name PolynomialRing
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_019408.json:
```json
{
    "body": "Attachment [pylint_linear_code_long_fix_and_cleanup.patch](tarball://root/attachments/some-uuid/ticket2834/pylint_linear_code_long_fix_and_cleanup.patch) by @malb created at 2008-04-07 13:07:09",
    "created_at": "2008-04-07T13:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19408",
    "user": "https://github.com/malb"
}
```

Attachment [pylint_linear_code_long_fix_and_cleanup.patch](tarball://root/attachments/some-uuid/ticket2834/pylint_linear_code_long_fix_and_cleanup.patch) by @malb created at 2008-04-07 13:07:09



---

archive/issue_comments_019409.json:
```json
{
    "body": "The attached patch fixes the issue reported by mabshoff and also cleans up `linear_code.py`.",
    "created_at": "2008-04-07T13:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19409",
    "user": "https://github.com/malb"
}
```

The attached patch fixes the issue reported by mabshoff and also cleans up `linear_code.py`.



---

archive/issue_comments_019410.json:
```json
{
    "body": "The new patch fixes the issue I reported. Doctests pass after a `-ba` now. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T16:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19410",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The new patch fixes the issue I reported. Doctests pass after a `-ba` now. Positive review.

Cheers,

Michael



---

archive/issue_comments_019411.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-07T16:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19411",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha3



---

archive/issue_comments_019412.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2 - an now it is closed, too. ;)",
    "created_at": "2008-04-07T16:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19412",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha2 - an now it is closed, too. ;)



---

archive/issue_comments_019413.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T16:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19413",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003024.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-07T16:08:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2834#event-3024"
}
```
