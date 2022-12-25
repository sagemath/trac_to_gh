# Issue 5563: [with patch, needs review] Doctest failure in devel/sage/doc/en/bordeaux_2008/modular_....rst

archive/issues_005563.json:
```json
{
    "body": "Assignee: mabshoff\n\nmodular_forms_and_hecke_operators.rst\ncontains a call to sloane_find() which requires internet access, leading to a failure if you don't\n\nIssue created by migration from https://trac.sagemath.org/ticket/5563\n\n",
    "created_at": "2009-03-18T23:37:35Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] Doctest failure in devel/sage/doc/en/bordeaux_2008/modular_....rst",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5563",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```
Assignee: mabshoff

modular_forms_and_hecke_operators.rst
contains a call to sloane_find() which requires internet access, leading to a failure if you don't

Issue created by migration from https://trac.sagemath.org/ticket/5563





---

archive/issue_comments_043214.json:
```json
{
    "body": "Attachment [sloane_find_optional.patch](tarball://root/attachments/some-uuid/ticket5563/sloane_find_optional.patch) by GeorgSWeber created at 2009-03-18 23:38:06\n\npatch against Sage 3.4",
    "created_at": "2009-03-18T23:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5563#issuecomment-43214",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [sloane_find_optional.patch](tarball://root/attachments/some-uuid/ticket5563/sloane_find_optional.patch) by GeorgSWeber created at 2009-03-18 23:38:06

patch against Sage 3.4



---

archive/issue_comments_043215.json:
```json
{
    "body": "The issue had been reported originally by Minh Nguyen in the thread\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/ce81352fe52292bd/a199ed5de16c81a8#a199ed5de16c81a8",
    "created_at": "2009-03-18T23:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5563#issuecomment-43215",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

The issue had been reported originally by Minh Nguyen in the thread

http://groups.google.com/group/sage-devel/browse_thread/thread/ce81352fe52292bd/a199ed5de16c81a8#a199ed5de16c81a8



---

archive/issue_comments_043216.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nThe patch **sloane_find_optional.patch** applies OK against Sage 3.4. All tests passed, both on machines with and without Internet connection. Just to be on the safe side, I rebuilt the HTML version of the whole reference manual; rebuilding went fine as expected on machines with and without Internet connection. Positive review.",
    "created_at": "2009-03-19T04:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5563#issuecomment-43216",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

REFEREE REPORT



The patch **sloane_find_optional.patch** applies OK against Sage 3.4. All tests passed, both on machines with and without Internet connection. Just to be on the safe side, I rebuilt the HTML version of the whole reference manual; rebuilding went fine as expected on machines with and without Internet connection. Positive review.



---

archive/issue_comments_043217.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T18:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5563#issuecomment-43217",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_013087.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-23T18:39:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5563",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5563#event-13087"
}
```



---

archive/issue_comments_043218.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T18:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5563#issuecomment-43218",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
