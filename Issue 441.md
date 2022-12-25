# Issue 441: add sage-valgrind command line option analog to sage-gdb

archive/issues_000441.json:
```json
{
    "body": "Assignee: mabshoff\n\nIntegrate valgrind into sage so people can conveniently attempt to debug. This requires Sage's python to be build with the configure flag \"--without-pymalloc\" to prevent valgrind from reporting false positives because pymalloc mallocs large chunks of memory and returns fractions of the memory when the python interpreter requests memory.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/441\n\n",
    "created_at": "2007-08-18T18:50:23Z",
    "labels": [
        "component: packages: standard",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "add sage-valgrind command line option analog to sage-gdb",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/441",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Integrate valgrind into sage so people can conveniently attempt to debug. This requires Sage's python to be build with the configure flag "--without-pymalloc" to prevent valgrind from reporting false positives because pymalloc mallocs large chunks of memory and returns fractions of the memory when the python interpreter requests memory.


Issue created by migration from https://trac.sagemath.org/ticket/441





---

archive/issue_comments_002198.json:
```json
{
    "body": "Basic support has been merged, but \"./sage -valgrind -testall\" ignores the -testall for now.",
    "created_at": "2007-08-18T19:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/441#issuecomment-2198",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Basic support has been merged, but "./sage -valgrind -testall" ignores the -testall for now.



---

archive/issue_comments_002199.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-19T07:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/441#issuecomment-2199",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000468.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-19T07:04:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/441",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/441#event-468"
}
```
