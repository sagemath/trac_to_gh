# Issue 585: Problem with PARI number field interface

archive/issues_000585.json:
```json
{
    "body": "Assignee: @williamstein\n\nThere are two issues with the PARI interface for number fields. The first is that it isn't clear what F._pari_ should return -- it currently returns the defining polynomial, but there are other objects that might be more appropriate. It's actually running very generic code for this; since number fields are about to be redone anyway, this is worth keeping in mind. The second is a printing problem:\n\nsage: F = NumberField(x^3-2,'alpha')\n\nsage: F\n Number Field in alpha with defining polynomial x^3 - 2\n\nsage: F._pari_()\n NumberFieldinalphawithdefiningpolynomialx^3 - 2\n\nThis comes from the fact that the entire output of the second line gets passed into PARI's gp_read_str function, which isn't the right thing to do.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/585\n\n",
    "created_at": "2007-09-04T00:34:20Z",
    "labels": [
        "interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "Problem with PARI number field interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/585",
    "user": "@craigcitro"
}
```
Assignee: @williamstein

There are two issues with the PARI interface for number fields. The first is that it isn't clear what F._pari_ should return -- it currently returns the defining polynomial, but there are other objects that might be more appropriate. It's actually running very generic code for this; since number fields are about to be redone anyway, this is worth keeping in mind. The second is a printing problem:

sage: F = NumberField(x^3-2,'alpha')

sage: F
 Number Field in alpha with defining polynomial x^3 - 2

sage: F._pari_()
 NumberFieldinalphawithdefiningpolynomialx^3 - 2

This comes from the fact that the entire output of the second line gets passed into PARI's gp_read_str function, which isn't the right thing to do.



Issue created by migration from https://trac.sagemath.org/ticket/585





---

archive/issue_comments_003020.json:
```json
{
    "body": "Attachment [6115.patch](tarball://root/attachments/some-uuid/ticket585/6115.patch) by @williamstein created at 2007-09-04 17:14:55",
    "created_at": "2007-09-04T17:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/585#issuecomment-3020",
    "user": "@williamstein"
}
```

Attachment [6115.patch](tarball://root/attachments/some-uuid/ticket585/6115.patch) by @williamstein created at 2007-09-04 17:14:55



---

archive/issue_comments_003021.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T03:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/585#issuecomment-3021",
    "user": "@williamstein"
}
```

Resolution: fixed
