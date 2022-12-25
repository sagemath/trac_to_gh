# Issue 5839: [with patch, needs review] MPolynomialRing_libsingular __dealloc__ is buggy, can lead to crash

archive/issues_005839.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @malb\n\nIn `__dealloc__`, if currRing is NULL on entry, then currRing will be the ring we just deleted on exit.  The patch fixes this bug, so that currRing never points to freed memory.\n\nIt took me quite a while to come up with a small reproducible test case for the problem; here it is.  (This test case is also in the patch, as a doctest.)\n\n```\nimport gc\nfrom sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular\nR1 = MPolynomialRing_libsingular(GF(5), 2, ('x', 'y'), TermOrder('degrevlex', 2))\nR2 = MPolynomialRing_libsingular(GF(11), 2, ('x', 'y'), TermOrder('degrevlex', 2))\nR3 = MPolynomialRing_libsingular(GF(13), 2, ('x', 'y'), TermOrder('degrevlex', 2))\ngc.collect()\nfoo = R1.gen(0)\ndel foo\ndel R1\ngc.collect()\ndel R2\ngc.collect()\ndel R3\ngc.collect()\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5839\n\n",
    "created_at": "2009-04-20T22:22:09Z",
    "labels": [
        "component: commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] MPolynomialRing_libsingular __dealloc__ is buggy, can lead to crash",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5839",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
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

archive/issue_comments_045815.json:
```json
{
    "body": "Attachment [fix-mp-libsingular-dealloc.patch](tarball://root/attachments/some-uuid/ticket5839/fix-mp-libsingular-dealloc.patch) by @malb created at 2009-04-21 09:13:14\n\nDoctests pass, patch reads good.",
    "created_at": "2009-04-21T09:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45815",
    "user": "https://github.com/malb"
}
```

Attachment [fix-mp-libsingular-dealloc.patch](tarball://root/attachments/some-uuid/ticket5839/fix-mp-libsingular-dealloc.patch) by @malb created at 2009-04-21 09:13:14

Doctests pass, patch reads good.



---

archive/issue_events_013732.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-21T22:37:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5839#event-13732"
}
```



---

archive/issue_comments_045816.json:
```json
{
    "body": "Merged in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T07:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45816",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_045817.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-22T07:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45817",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_013733.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-22T07:27:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5839#event-13733"
}
```



---

archive/issue_comments_045818.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-04-22T07:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45818",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_045819.json:
```json
{
    "body": "Mmmh, I seem to be seeing random doctest failure with 3.4.1 + only this patch merged, so I am reopening this ticket for now. Can someone do extensive testing on sage.math to see if they can reproduce it?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T07:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45819",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mmmh, I seem to be seeing random doctest failure with 3.4.1 + only this patch merged, so I am reopening this ticket for now. Can someone do extensive testing on sage.math to see if they can reproduce it?

Cheers,

Michael



---

archive/issue_comments_045820.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-04-22T07:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45820",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_013734.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-22T07:47:32Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5839#event-13734"
}
```



---

archive/issue_comments_045821.json:
```json
{
    "body": "Ok, given that this causes issues for me I am changing it to 'needs work' for now.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T18:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45821",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, given that this causes issues for me I am changing it to 'needs work' for now.

Cheers,

Michael



---

archive/issue_comments_045822.json:
```json
{
    "body": "What sort of errors?  (Crashes?  Wrong answers?  Any particular files?)",
    "created_at": "2009-04-22T19:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45822",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

What sort of errors?  (Crashes?  Wrong answers?  Any particular files?)



---

archive/issue_comments_045823.json:
```json
{
    "body": "I have come to believe that the issues I saw were due to other issues, so I am reinstating the positive review. But I will do some more extensive testing before merging this. Sorry for the noise.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-08T00:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45823",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I have come to believe that the issues I saw were due to other issues, so I am reinstating the positive review. But I will do some more extensive testing before merging this. Sorry for the noise.

Cheers,

Michael



---

archive/issue_comments_045824.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-14T05:16:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45824",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045825.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-14T05:16:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5839#issuecomment-45825",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_events_013735.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-14T05:16:49Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5839#event-13735"
}
```



---

archive/issue_events_013736.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-14T05:16:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5839#event-13736"
}
```



---

archive/issue_events_013737.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-14T05:16:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5839",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5839#event-13737"
}
```
