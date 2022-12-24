# Issue 4395: Sage 3.1.4: magma related optional doctest failure in sage/rings/quotient_ring.py

archive/issues_004395.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage -t -long -optional devel/sage/sage/rings/quotient_ring.py\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/quotient_ring.py\", line 647:\n    sage: Q._magma_() # optional requires Magma\nExpected:\n    Affine Algebra of rank 2 over GF(2)\n    Graded Reverse Lexicographical Order\n    Variables: x, y\n    Quotient relations:\n    [\n    x^2 + x,\n    y^2 + y\n    ]\nGot:\n    Affine Algebra of rank 2 over GF(2)\n    Graded Reverse Lexicographical Order\n    Variables: x, y\n    Quotient relations:\n    [\n    0,\n    0\n    ]\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_23\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/.doctest_quotient_ring.py\n\t [5.4 s]\nexit code: 1024\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4395\n\n",
    "created_at": "2008-10-30T16:56:35Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Sage 3.1.4: magma related optional doctest failure in sage/rings/quotient_ring.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4395",
    "user": "mabshoff"
}
```
Assignee: was


```
sage -t -long -optional devel/sage/sage/rings/quotient_ring.py
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/quotient_ring.py", line 647:
    sage: Q._magma_() # optional requires Magma
Expected:
    Affine Algebra of rank 2 over GF(2)
    Graded Reverse Lexicographical Order
    Variables: x, y
    Quotient relations:
    [
    x^2 + x,
    y^2 + y
    ]
Got:
    Affine Algebra of rank 2 over GF(2)
    Graded Reverse Lexicographical Order
    Variables: x, y
    Quotient relations:
    [
    0,
    0
    ]
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_23
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/.doctest_quotient_ring.py
	 [5.4 s]
exit code: 1024
```


Issue created by migration from https://trac.sagemath.org/ticket/4395





---

archive/issue_comments_032344.json:
```json
{
    "body": "Apply this after #4394",
    "created_at": "2008-10-30T20:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4395#issuecomment-32344",
    "user": "was"
}
```

Apply this after #4394



---

archive/issue_comments_032345.json:
```json
{
    "body": "Where is the patch?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T16:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4395#issuecomment-32345",
    "user": "mabshoff"
}
```

Where is the patch?

Cheers,

Michael



---

archive/issue_comments_032346.json:
```json
{
    "body": "This patch (one it is here :)) also likely fixes the following problem:\n\n```\nsage -t -long -optional devel/sage/sage/rings/polynomial/pbori.pyx\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/pbori.py\", line 988:\n    sage: B._magma_() # optional requires magma\nExpected:\n    Affine Algebra of rank 3 over GF(2)\n    Lexicographical Order\n    Variables: x, y, z\n    Quotient relations:\n    [\n    x^2 + x,\n    y^2 + y,\n    z^2 + z\n    ]\nGot:\n    Affine Algebra of rank 3 over GF(2)\n    Lexicographical Order\n    Variables: x, y, z\n    Quotient relations:\n    [\n    0,\n    0,\n    0\n    ]\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/pbori.py\", line 1024:\n    sage: B._magma_() # optional requires magma, indirect doctest\nExpected:\n    Affine Algebra of rank 3 over GF(2)\n    Lexicographical Order\n    Variables: x, y, z\n    Quotient relations:\n    [\n    x^2 + x,\n    y^2 + y,\n    z^2 + z\n    ]\nGot:\n    Affine Algebra of rank 3 over GF(2)\n    Lexicographical Order\n    Variables: x, y, z\n    Quotient relations:\n    [\n    0,\n    0,\n    0\n    ]\n**********************************************************************\n```\n",
    "created_at": "2008-10-31T21:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4395#issuecomment-32346",
    "user": "mabshoff"
}
```

This patch (one it is here :)) also likely fixes the following problem:

```
sage -t -long -optional devel/sage/sage/rings/polynomial/pbori.pyx
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/pbori.py", line 988:
    sage: B._magma_() # optional requires magma
Expected:
    Affine Algebra of rank 3 over GF(2)
    Lexicographical Order
    Variables: x, y, z
    Quotient relations:
    [
    x^2 + x,
    y^2 + y,
    z^2 + z
    ]
Got:
    Affine Algebra of rank 3 over GF(2)
    Lexicographical Order
    Variables: x, y, z
    Quotient relations:
    [
    0,
    0,
    0
    ]
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/pbori.py", line 1024:
    sage: B._magma_() # optional requires magma, indirect doctest
Expected:
    Affine Algebra of rank 3 over GF(2)
    Lexicographical Order
    Variables: x, y, z
    Quotient relations:
    [
    x^2 + x,
    y^2 + y,
    z^2 + z
    ]
Got:
    Affine Algebra of rank 3 over GF(2)
    Lexicographical Order
    Variables: x, y, z
    Quotient relations:
    [
    0,
    0,
    0
    ]
**********************************************************************
```




---

archive/issue_comments_032347.json:
```json
{
    "body": "Attachment [sage-4395.patch](tarball://root/attachments/some-uuid/ticket4395/sage-4395.patch) by mabshoff created at 2008-11-09 17:39:30\n\nPositive review. It fixes the original problem reported, but not as I suspected the issue in \n\n```\ndevel/sage/sage/rings/polynomial/pbori.pyx\n```\n\nThat issue is now #4482.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-09T17:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4395#issuecomment-32347",
    "user": "mabshoff"
}
```

Attachment [sage-4395.patch](tarball://root/attachments/some-uuid/ticket4395/sage-4395.patch) by mabshoff created at 2008-11-09 17:39:30

Positive review. It fixes the original problem reported, but not as I suspected the issue in 

```
devel/sage/sage/rings/polynomial/pbori.pyx
```

That issue is now #4482.

Cheers,

Michael



---

archive/issue_comments_032348.json:
```json
{
    "body": "Merged in Sage 3.2.rc0",
    "created_at": "2008-11-09T17:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4395#issuecomment-32348",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.rc0



---

archive/issue_comments_032349.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-09T17:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4395#issuecomment-32349",
    "user": "mabshoff"
}
```

Resolution: fixed
