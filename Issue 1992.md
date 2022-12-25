# Issue 1992: Loading and attaching spyx/pyx files -- automatic compilation and nsf locking

archive/issues_001992.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen\n\n```\n sage: load filename.spyx\n```\nis done repeatedly on a specific single file filename.spyx, after about 3-4\ntries Sage tries to delete some files.  On some NFS mounted filesystems, there\nare lock files, and these can't be deleted for permissions reasons.  Instead of \nsage gracefully continuing on it fails at this point, and bombs out.  This makes\nloading cython files fail henceforth, making spyx files completely useless.\n\nThe fix is probably just to put a try/except block around any code that deletes files that is related to attaching and loading [s]pyx files.\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1992\n\n",
    "closed_at": "2008-01-31T04:53:44Z",
    "created_at": "2008-01-31T04:28:15Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Loading and attaching spyx/pyx files -- automatic compilation and nsf locking",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1992",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

When

```
 sage: load filename.spyx
```
is done repeatedly on a specific single file filename.spyx, after about 3-4
tries Sage tries to delete some files.  On some NFS mounted filesystems, there
are lock files, and these can't be deleted for permissions reasons.  Instead of 
sage gracefully continuing on it fails at this point, and bombs out.  This makes
loading cython files fail henceforth, making spyx files completely useless.

The fix is probably just to put a try/except block around any code that deletes files that is related to attaching and loading [s]pyx files.




Issue created by migration from https://trac.sagemath.org/ticket/1992





---

archive/issue_comments_012862.json:
```json
{
    "body": "This is a dupe of #1559 - so which one should we close?\n\nCheers,\n\nMichael",
    "created_at": "2008-01-31T04:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1992#issuecomment-12862",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a dupe of #1559 - so which one should we close?

Cheers,

Michael



---

archive/issue_comments_012863.json:
```json
{
    "body": "closed as a dupe",
    "created_at": "2008-01-31T04:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1992#issuecomment-12863",
    "user": "https://github.com/williamstein"
}
```

closed as a dupe



---

archive/issue_comments_012864.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-01-31T04:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1992#issuecomment-12864",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate



---

archive/issue_events_004805.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-01-31T04:53:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1992",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1992#event-4805"
}
```
