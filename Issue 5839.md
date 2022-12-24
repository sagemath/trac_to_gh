# Issue 5839: [with patch, needs review] MPolynomialRing_libsingular __dealloc__ is buggy, can lead to crash

archive/issues_005839.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @malb\n\nIn `__dealloc__`, if currRing is NULL on entry, then currRing will be the ring we just deleted on exit.  The patch fixes this bug, so that currRing never points to freed memory.\n\nIt took me quite a while to come up with a small reproducible test case for the problem; here it is.  (This test case is also in the patch, as a doctest.)\n\n```\nimport gc\nfrom sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular\nR1 = MPolynomialRing_libsingular(GF(5), 2, ('x', 'y'), TermOrder('degrevlex', 2))\nR2 = MPolynomialRing_libsingular(GF(11), 2, ('x', 'y'), TermOrder('degrevlex', 2))\nR3 = MPolynomialRing_libsingular(GF(13), 2, ('x', 'y'), TermOrder('degrevlex', 2))\ngc.collect()\nfoo = R1.gen(0)\ndel foo\ndel R1\ngc.collect()\ndel R2\ngc.collect()\ndel R3\ngc.collect()\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5839\n\n",
    "created_at": "2009-04-20T22:22:09Z",
    "labels": [
        "commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] MPolynomialRing_libsingular __dealloc__ is buggy, can lead to crash",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5839",
    "user": "cwitty"
}
```
Assignee: cwitty

CC:  @malb

In `__dealloc__`, if currRing is NULL on entry, then currRing will be the ring we just deleted on exit.  The patch fixes this bug, so that currRing never points to freed memory.

It took me quite a while to come up with a small reproducible test case for the problem; here it is.  (This test case is also in the patch, as a doctest.)

```
import gc
from sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular
R1 = MPolynomialRing_libsingular(GF(5), 2, ('x', 'y'), TermOrder('degrevlex', 2))
R2 = MPolynomialRing_libsingular(GF(11), 2, ('x', 'y'), TermOrder('degrevlex', 2))
R3 = MPolynomialRing_libsingular(GF(13), 2, ('x', 'y'), TermOrder('degrevlex', 2))
gc.collect()
foo = R1.gen(0)
del foo
del R1
gc.collect()
del R2
gc.collect()
del R3
gc.collect()
```



Issue created by migration from https://trac.sagemath.org/ticket/5839





---

archive/issue_comments_045904.json:
```json
{
    "body": "Attachment [fix-mp-libsingular-dealloc.patch](tarball://root/attachments/some-uuid/ticket5839/fix-mp-libsingular-dealloc.patch) by @malb created at 2009-04-21 09:13:14\n\nDoctests pass, patch reads good.",
    "created_at": "2009-04-21T09:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45904",
    "user": "@malb"
}
```

Attachment [fix-mp-libsingular-dealloc.patch](tarball://root/attachments/some-uuid/ticket5839/fix-mp-libsingular-dealloc.patch) by @malb created at 2009-04-21 09:13:14

Doctests pass, patch reads good.



---

archive/issue_comments_045905.json:
```json
{
    "body": "Merged in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T07:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45905",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_045906.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-22T07:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45906",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045907.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-04-22T07:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45907",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_045908.json:
```json
{
    "body": "Mmmh, I seem to be seeing random doctest failure with 3.4.1 + only this patch merged, so I am reopening this ticket for now. Can someone do extensive testing on sage.math to see if they can reproduce it?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T07:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45908",
    "user": "mabshoff"
}
```

Mmmh, I seem to be seeing random doctest failure with 3.4.1 + only this patch merged, so I am reopening this ticket for now. Can someone do extensive testing on sage.math to see if they can reproduce it?

Cheers,

Michael



---

archive/issue_comments_045909.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-04-22T07:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45909",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_045910.json:
```json
{
    "body": "Ok, given that this causes issues for me I am changing it to 'needs work' for now.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T18:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45910",
    "user": "mabshoff"
}
```

Ok, given that this causes issues for me I am changing it to 'needs work' for now.

Cheers,

Michael



---

archive/issue_comments_045911.json:
```json
{
    "body": "What sort of errors?  (Crashes?  Wrong answers?  Any particular files?)",
    "created_at": "2009-04-22T19:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45911",
    "user": "cwitty"
}
```

What sort of errors?  (Crashes?  Wrong answers?  Any particular files?)



---

archive/issue_comments_045912.json:
```json
{
    "body": "I have come to believe that the issues I saw were due to other issues, so I am reinstating the positive review. But I will do some more extensive testing before merging this. Sorry for the noise.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-08T00:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45912",
    "user": "mabshoff"
}
```

I have come to believe that the issues I saw were due to other issues, so I am reinstating the positive review. But I will do some more extensive testing before merging this. Sorry for the noise.

Cheers,

Michael



---

archive/issue_comments_045913.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-14T05:16:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45913",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045914.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-14T05:16:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45914",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael
