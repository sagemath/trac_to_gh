# Issue 2834: [with patch, needs review] PyLint import cleanup for sage.rings.polynomial

archive/issues_002834.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: pylint\n\nI ran `pylint --enable-checker=imports` on `sage.rings.polynomial` and attempted to fix what it reported\n* relative imports\n* double imports\n* circular imports\n\nThe patch could be considered controversial, please check carefully.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2834\n\n",
    "created_at": "2008-04-06T22:18:51Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] PyLint import cleanup for sage.rings.polynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2834",
    "user": "malb"
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

archive/issue_comments_019447.json:
```json
{
    "body": "Attachment\n\nAll tests pass for me.  I'd give it a positive review, but I'd also like to hear others' comments.",
    "created_at": "2008-04-06T22:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19447",
    "user": "mhansen"
}
```

Attachment

All tests pass for me.  I'd give it a positive review, but I'd also like to hear others' comments.



---

archive/issue_comments_019448.json:
```json
{
    "body": "I like this patch. But after applying and doing a `sage -ba` I see the following failure with `-long`:\n\n```\nsage -t -long devel/sage/sage/coding/linear_code.py         \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.alpha2/tmp/linear_code.py\", line 724:\n    sage: C.chinen_polynomial()       # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_12[2]>\", line 1, in <module>\n        C.chinen_polynomial()       # long time###line 724:\n    sage: C.chinen_polynomial()       # long time\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 737, in chinen_polynomial\n        from sage.rings.polynomial.polynomial_ring import PolynomialRing, polygen\n    ImportError: cannot import name PolynomialRing\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T00:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19448",
    "user": "mabshoff"
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

archive/issue_comments_019449.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-07T13:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19449",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_019450.json:
```json
{
    "body": "The attached patch fixes the issue reported by mabshoff and also cleans up `linear_code.py`.",
    "created_at": "2008-04-07T13:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19450",
    "user": "malb"
}
```

The attached patch fixes the issue reported by mabshoff and also cleans up `linear_code.py`.



---

archive/issue_comments_019451.json:
```json
{
    "body": "The new patch fixes the issue I reported. Doctests pass after a `-ba` now. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T16:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19451",
    "user": "mabshoff"
}
```

The new patch fixes the issue I reported. Doctests pass after a `-ba` now. Positive review.

Cheers,

Michael



---

archive/issue_comments_019452.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-07T16:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19452",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha3



---

archive/issue_comments_019453.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2 - an now it is closed, too. ;)",
    "created_at": "2008-04-07T16:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19453",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2 - an now it is closed, too. ;)



---

archive/issue_comments_019454.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T16:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2834#issuecomment-19454",
    "user": "mabshoff"
}
```

Resolution: fixed
