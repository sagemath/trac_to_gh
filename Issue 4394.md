# Issue 4394: Sage 3.1.4: magma related optional doctest failure in sage/rings/polynomial/polynomial_element.pyx

archive/issues_004394.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nmabshoff@iras:~/build-3.2.a1/sage-3.2.alpha1-iras> ./sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx\nsage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/polynomial_element.py\", line 2833:\n    sage: g = magma(f); g              # optional -- requires Magma\nExpected:\n    y^3 - 17*y + 5\nGot:\n    $.1^3 - 17*$.1 + 5\n**********************************************************************\n1 items had failures:\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4394\n\n",
    "created_at": "2008-10-30T16:51:51Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Sage 3.1.4: magma related optional doctest failure in sage/rings/polynomial/polynomial_element.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4394",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

```
mabshoff@iras:~/build-3.2.a1/sage-3.2.alpha1-iras> ./sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx
sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/polynomial_element.py", line 2833:
    sage: g = magma(f); g              # optional -- requires Magma
Expected:
    y^3 - 17*y + 5
Got:
    $.1^3 - 17*$.1 + 5
**********************************************************************
1 items had failures:
```

Issue created by migration from https://trac.sagemath.org/ticket/4394





---

archive/issue_comments_032277.json:
```json
{
    "body": "Attachment [sage-4394.patch](tarball://root/attachments/some-uuid/ticket4394/sage-4394.patch) by @williamstein created at 2008-10-30 20:17:23",
    "created_at": "2008-10-30T20:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4394#issuecomment-32277",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4394.patch](tarball://root/attachments/some-uuid/ticket4394/sage-4394.patch) by @williamstein created at 2008-10-30 20:17:23



---

archive/issue_comments_032278.json:
```json
{
    "body": "Positive review. The patch makes the doctests pass:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ \n./sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx\nsage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx\n\t [11.4 s]\n \n----------------------------------------------------------------------\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T20:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4394#issuecomment-32278",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. The patch makes the doctests pass:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ 
./sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx
sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx
	 [11.4 s]
 
----------------------------------------------------------------------
```

Cheers,

Michael



---

archive/issue_comments_032279.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T20:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4394#issuecomment-32279",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_comments_032280.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T20:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4394#issuecomment-32280",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009917.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T20:21:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4394",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4394#event-9917"
}
```
