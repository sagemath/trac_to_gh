# Issue 678: Solaris 10: fix scipy compiler selection

archive/issues_000678.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn Solaris scipy looks for \n\n* g77\n* f77\n* f90\n\nbut fails to detect either g95 or gfortran. It should look for those two, but a quick fix is usually to symbolically link gfortran or g95 as g77.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/678\n\n",
    "created_at": "2007-09-17T05:22:27Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "Solaris 10: fix scipy compiler selection",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/678",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

On Solaris scipy looks for 

* g77
* f77
* f90

but fails to detect either g95 or gfortran. It should look for those two, but a quick fix is usually to symbolically link gfortran or g95 as g77.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/678





---

archive/issue_comments_003500.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-17T05:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/678#issuecomment-3500",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003501.json:
```json
{
    "body": "I know how the scipy chooses fortran compilers (its actually in numpy's distutils/fcompiler).\n\nI could probably help with this if I had access to a solaris box.",
    "created_at": "2007-11-18T09:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/678#issuecomment-3501",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

I know how the scipy chooses fortran compilers (its actually in numpy's distutils/fcompiler).

I could probably help with this if I had access to a solaris box.



---

archive/issue_comments_003502.json:
```json
{
    "body": "I believe this has been fixed. I will investigate this.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-04T14:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/678#issuecomment-3502",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I believe this has been fixed. I will investigate this.

Cheers,

Michael



---

archive/issue_comments_003503.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-29T17:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/678#issuecomment-3503",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_003504.json:
```json
{
    "body": "By introducing sage_fortran this issue has been fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-29T17:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/678#issuecomment-3504",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

By introducing sage_fortran this issue has been fixed.

Cheers,

Michael



---

archive/issue_events_000746.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-07-29T17:27:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/678",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/678#event-746"
}
```
