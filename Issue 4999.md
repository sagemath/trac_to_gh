# Issue 4999: Solaris 10/Sparc: numerical noise doctest failure in sage/gsl/integration.pyx

archive/issues_004999.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t  \"devel/sage/sage/gsl/integration.pyx\"              \n**********************************************************************\nFile \"/home/mabshoff/build-3.2.3/sage-3.2.3-mark/devel/sage/sage/gsl/integration.pyx\", line 163:\n    sage: numerical_integral(exp(-1/x), 1, 2)\nExpected:\n    (0.50479221787318407, 5.6043194293440744e-15)\nGot:\n    (0.50479221787318396, 5.6043194293440728e-15)\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4999\n\n",
    "created_at": "2009-01-17T16:02:24Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Solaris 10/Sparc: numerical noise doctest failure in sage/gsl/integration.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4999",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
sage -t  "devel/sage/sage/gsl/integration.pyx"              
**********************************************************************
File "/home/mabshoff/build-3.2.3/sage-3.2.3-mark/devel/sage/sage/gsl/integration.pyx", line 163:
    sage: numerical_integral(exp(-1/x), 1, 2)
Expected:
    (0.50479221787318407, 5.6043194293440744e-15)
Got:
    (0.50479221787318396, 5.6043194293440728e-15)
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4999





---

archive/issue_comments_038059.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-17T16:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4999#issuecomment-38059",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038060.json:
```json
{
    "body": "Attachment [trac_4999_integration.pyx-sparc.patch](tarball://root/attachments/some-uuid/ticket4999/trac_4999_integration.pyx-sparc.patch) by mabshoff created at 2009-01-18 06:30:16",
    "created_at": "2009-01-18T06:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4999#issuecomment-38060",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4999_integration.pyx-sparc.patch](tarball://root/attachments/some-uuid/ticket4999/trac_4999_integration.pyx-sparc.patch) by mabshoff created at 2009-01-18 06:30:16



---

archive/issue_comments_038061.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-18T14:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4999#issuecomment-38061",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_comments_038062.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-18T14:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4999#issuecomment-38062",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005243.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-18T14:06:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4999",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4999#event-5243"
}
```
