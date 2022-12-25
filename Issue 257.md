# Issue 257: restart needed after segfault

archive/issues_000257.json:
```json
{
    "body": "Assignee: boothby\n\nFollowing a null pointer gives the user an oh-so-friendly message.  Then (s)he has to use the mouse to restart the notebook manually.\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\nIssue created by migration from https://trac.sagemath.org/ticket/257\n\n",
    "created_at": "2007-02-10T06:33:51Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "title": "restart needed after segfault",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/257",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: boothby

Following a null pointer gives the user an oh-so-friendly message.  Then (s)he has to use the mouse to restart the notebook manually.

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

Issue created by migration from https://trac.sagemath.org/ticket/257





---

archive/issue_comments_001149.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-03-22T20:01:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/257#issuecomment-1149",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: fixed



---

archive/issue_events_000271.json:
```json
{
    "actor": "boothby",
    "created_at": "2007-03-22T20:01:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/257",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/257#event-271"
}
```
