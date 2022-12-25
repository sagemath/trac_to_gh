# Issue 2253: sage-2.10.2 -- timeit doctests not robust enough

archive/issues_002253.json:
```json
{
    "body": "Assignee: failure\n\n\n```\n\nAlpha2 installed and tested on Toshiba Laptop under Ubuntu.\n\nmake test failures:\n\n\n       sage -t  devel/sage-main/sage/groups/group.pyx\n       sage -t  devel/sage-main/sage/functions/special.py\n       sage -t  devel/sage-main/sage/misc/sage_timeit_class.pyx\n       sage -t  devel/sage-main/sage/misc/functional.py\n       sage -t  devel/sage-main/sage/schemes/elliptic_curves/padics.py\n       sage -t  devel/sage-main/sage/rings/number_field/totallyreal_rel.py\n       sage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_CR_element.pyx\n       sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx\nTotal time for all tests: 4938.4 seconds\n\ntest log is on my server:\n\n       http://www.billp.org/alpha2-test.log\n\nif you need any further details.\nTime for bed!\n\n```\n\n\nLooking at the actual doctest log suggest what to do to fix such things,\nand I'll do it now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2253\n\n",
    "created_at": "2008-02-21T22:50:39Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "sage-2.10.2 -- timeit doctests not robust enough",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2253",
    "user": "https://github.com/williamstein"
}
```
Assignee: failure


```

Alpha2 installed and tested on Toshiba Laptop under Ubuntu.

make test failures:


       sage -t  devel/sage-main/sage/groups/group.pyx
       sage -t  devel/sage-main/sage/functions/special.py
       sage -t  devel/sage-main/sage/misc/sage_timeit_class.pyx
       sage -t  devel/sage-main/sage/misc/functional.py
       sage -t  devel/sage-main/sage/schemes/elliptic_curves/padics.py
       sage -t  devel/sage-main/sage/rings/number_field/totallyreal_rel.py
       sage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_CR_element.pyx
       sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx
Total time for all tests: 4938.4 seconds

test log is on my server:

       http://www.billp.org/alpha2-test.log

if you need any further details.
Time for bed!

```


Looking at the actual doctest log suggest what to do to fix such things,
and I'll do it now.

Issue created by migration from https://trac.sagemath.org/ticket/2253





---

archive/issue_comments_014891.json:
```json
{
    "body": "Attachment [8652.patch](tarball://root/attachments/some-uuid/ticket2253/8652.patch) by @williamstein created at 2008-02-21 22:55:53",
    "created_at": "2008-02-21T22:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2253#issuecomment-14891",
    "user": "https://github.com/williamstein"
}
```

Attachment [8652.patch](tarball://root/attachments/some-uuid/ticket2253/8652.patch) by @williamstein created at 2008-02-21 22:55:53



---

archive/issue_comments_014892.json:
```json
{
    "body": "Patch looks good to me, is obviously correct.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T23:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2253#issuecomment-14892",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me, is obviously correct.

Cheers,

Michael



---

archive/issue_comments_014893.json:
```json
{
    "body": "Merged in Sage 2.10.2.rc0",
    "created_at": "2008-02-21T23:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2253#issuecomment-14893",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.rc0



---

archive/issue_comments_014894.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-21T23:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2253#issuecomment-14894",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
