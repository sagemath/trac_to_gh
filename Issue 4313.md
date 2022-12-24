# Issue 4313: Add some functionality to matrices in eclib

archive/issues_004313.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason\n\nKeywords: eclib CremonaModularSymbols\n\nThe attached patch (based on 3.1.4) makes two changes in libs/cremona/mat*:\n1. Adds getitem methods to the matric class so i,j entries may be extracted;\n2. Changes the conversion to sage of matrices so that matrices over ZZ are constructed instead of ZZ.\n\nThese were done as part of a hands-on tutorial William gave to John in Bordeaux.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4313\n\n",
    "created_at": "2008-10-17T17:11:47Z",
    "labels": [
        "interfaces",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Add some functionality to matrices in eclib",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4313",
    "user": "cremona"
}
```
Assignee: was

CC:  jason

Keywords: eclib CremonaModularSymbols

The attached patch (based on 3.1.4) makes two changes in libs/cremona/mat*:
1. Adds getitem methods to the matric class so i,j entries may be extracted;
2. Changes the conversion to sage of matrices so that matrices over ZZ are constructed instead of ZZ.

These were done as part of a hands-on tutorial William gave to John in Bordeaux.

Issue created by migration from https://trac.sagemath.org/ticket/4313





---

archive/issue_comments_031578.json:
```json
{
    "body": "Attachment [sage-cremona-matrices.patch](tarball://root/attachments/some-uuid/ticket4313/sage-cremona-matrices.patch) by cremona created at 2008-10-17 17:12:10",
    "created_at": "2008-10-17T17:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4313#issuecomment-31578",
    "user": "cremona"
}
```

Attachment [sage-cremona-matrices.patch](tarball://root/attachments/some-uuid/ticket4313/sage-cremona-matrices.patch) by cremona created at 2008-10-17 17:12:10



---

archive/issue_comments_031579.json:
```json
{
    "body": "Code looks good. Only thing needed are some doctests on `__getitem__` in `mat.pyx` -- it would be nice to see a few doctests there, especially ones written to test weird corner cases.\n\n(Also edited a typo in the description for this ticket.)",
    "created_at": "2008-11-27T08:40:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4313#issuecomment-31579",
    "user": "craigcitro"
}
```

Code looks good. Only thing needed are some doctests on `__getitem__` in `mat.pyx` -- it would be nice to see a few doctests there, especially ones written to test weird corner cases.

(Also edited a typo in the description for this ticket.)



---

archive/issue_comments_031580.json:
```json
{
    "body": "Attachment [sage-cremona-matrices.2.patch](tarball://root/attachments/some-uuid/ticket4313/sage-cremona-matrices.2.patch) by cremona created at 2009-05-30 15:42:07\n\nReplace previous one with this",
    "created_at": "2009-05-30T15:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4313#issuecomment-31580",
    "user": "cremona"
}
```

Attachment [sage-cremona-matrices.2.patch](tarball://root/attachments/some-uuid/ticket4313/sage-cremona-matrices.2.patch) by cremona created at 2009-05-30 15:42:07

Replace previous one with this



---

archive/issue_comments_031581.json:
```json
{
    "body": "I added a docstring for the getitem function with doctest, and also fixed one other doctest.  Now the coverage is 100% (though there is no loads(dumps) test).\n\nShould work on 4.0.",
    "created_at": "2009-05-30T15:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4313#issuecomment-31581",
    "user": "cremona"
}
```

I added a docstring for the getitem function with doctest, and also fixed one other doctest.  Now the coverage is 100% (though there is no loads(dumps) test).

Should work on 4.0.



---

archive/issue_comments_031582.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T10:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4313#issuecomment-31582",
    "user": "rlm"
}
```

Resolution: fixed
