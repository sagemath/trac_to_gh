# Issue 2701: simple bug fixed for linear_codes

archive/issues_002701.json:
```json
{
    "body": "Assignee: rlm\n\nThe attached patch fixes two bugs - one in spectrum and one in zeta_polynomial,\nboth of which either failed or behaved badly for codes over non-prime fields.\nI also added som doctests for non-prime fields. \n\nIt passes sage -testall except for plot.py and polynomial_modn_dense_ntl.pyx.\n(I reran sage -t on polynomial_modn_dense_ntl.pyx and it passed the second time.)\nI think these have nothing to do with the patch but here are the details:\n\nsage -t  devel/sage-coding/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx**********************************************************************\nFile \"polynomial_modn_dense_ntl.pyx\", line 495:\n    sage: q == qbar - d\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n1 items had failures:\n   1 of  37 in __main__.example_10\n***Test Failed*** 1 failures.\n\nsage -t  devel/sage-coding/sage/plot/plot.py                **********************************************************************\nFile \"plot.py\", line 3506:\n    sage: plot(x^(1/3), (x,-1,1))\nExpected nothing\nGot:\n    WARNING: When plotting, failed to evaluate function at 100 points.\n    Last error message: 'negative number cannot be raised to a fractional power'\n    <BLANKLINE>\n**********************************************************************\n1 items had failures:\n   1 of  28 in __main__.example_111\n***Test Failed*** 1 failures.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2701\n\n",
    "created_at": "2008-03-28T17:22:00Z",
    "labels": [
        "coding theory",
        "major",
        "bug"
    ],
    "title": "simple bug fixed for linear_codes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2701",
    "user": "wdj"
}
```
Assignee: rlm

The attached patch fixes two bugs - one in spectrum and one in zeta_polynomial,
both of which either failed or behaved badly for codes over non-prime fields.
I also added som doctests for non-prime fields. 

It passes sage -testall except for plot.py and polynomial_modn_dense_ntl.pyx.
(I reran sage -t on polynomial_modn_dense_ntl.pyx and it passed the second time.)
I think these have nothing to do with the patch but here are the details:

sage -t  devel/sage-coding/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx**********************************************************************
File "polynomial_modn_dense_ntl.pyx", line 495:
    sage: q == qbar - d
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   1 of  37 in __main__.example_10
***Test Failed*** 1 failures.

sage -t  devel/sage-coding/sage/plot/plot.py                **********************************************************************
File "plot.py", line 3506:
    sage: plot(x^(1/3), (x,-1,1))
Expected nothing
Got:
    WARNING: When plotting, failed to evaluate function at 100 points.
    Last error message: 'negative number cannot be raised to a fractional power'
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  28 in __main__.example_111
***Test Failed*** 1 failures.

Issue created by migration from https://trac.sagemath.org/ticket/2701





---

archive/issue_comments_018625.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-28T17:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2701#issuecomment-18625",
    "user": "wdj"
}
```

Attachment



---

archive/issue_comments_018626.json:
```json
{
    "body": "The attachment is based on sage-2.11.alpha1",
    "created_at": "2008-03-28T17:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2701#issuecomment-18626",
    "user": "wdj"
}
```

The attachment is based on sage-2.11.alpha1



---

archive/issue_comments_018627.json:
```json
{
    "body": "Both of the above failures have been fixed in 2.11.alpha2, out in a couple hours at the most.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T18:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2701#issuecomment-18627",
    "user": "mabshoff"
}
```

Both of the above failures have been fixed in 2.11.alpha2, out in a couple hours at the most.

Cheers,

Michael



---

archive/issue_comments_018628.json:
```json
{
    "body": "Looks good. As long as the tests pass, I say apply.",
    "created_at": "2008-03-28T22:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2701#issuecomment-18628",
    "user": "rlm"
}
```

Looks good. As long as the tests pass, I say apply.



---

archive/issue_comments_018629.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-29T00:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2701#issuecomment-18629",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_comments_018630.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T00:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2701#issuecomment-18630",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018631.json:
```json
{
    "body": "Attachment\n\nA doctest fix for a long case",
    "created_at": "2008-03-29T00:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2701#issuecomment-18631",
    "user": "mabshoff"
}
```

Attachment

A doctest fix for a long case



---

archive/issue_comments_018632.json:
```json
{
    "body": "David,\n\nthe new patch fixes a doctest failure. Mathematically those two polynomials are mathematically equivalent, but can you confirm that this is the correct fix.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T00:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2701#issuecomment-18632",
    "user": "mabshoff"
}
```

David,

the new patch fixes a doctest failure. Mathematically those two polynomials are mathematically equivalent, but can you confirm that this is the correct fix.

Cheers,

Michael
