# Issue 5207: remove unnecessary use of symbolics in doctests in weierstrass_morphism.py

archive/issues_005207.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @JohnCremona\n\nAs discussed at\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/48b893e904634273\n\nthere are two doctests in weierstrass_morphism.py that use symbolic variables.  This is slow, completely unnecessary, and causes trouble given that Maxima has a tendency to hang.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5207\n\n",
    "created_at": "2009-02-08T13:11:37Z",
    "labels": [
        "component: number theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "remove unnecessary use of symbolics in doctests in weierstrass_morphism.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5207",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

CC:  @JohnCremona

As discussed at

http://groups.google.com/group/sage-devel/browse_thread/thread/48b893e904634273

there are two doctests in weierstrass_morphism.py that use symbolic variables.  This is slow, completely unnecessary, and causes trouble given that Maxima has a tendency to hang.


Issue created by migration from https://trac.sagemath.org/ticket/5207





---

archive/issue_comments_039817.json:
```json
{
    "body": "Attachment [trac_5207.patch](tarball://root/attachments/some-uuid/ticket5207/trac_5207.patch) by @aghitza created at 2009-02-08 13:13:57\n\nAs suggested by John Cremona, the attached patch replaces the use of symbolic variables by variables in a polynomial ring over QQ.",
    "created_at": "2009-02-08T13:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5207#issuecomment-39817",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5207.patch](tarball://root/attachments/some-uuid/ticket5207/trac_5207.patch) by @aghitza created at 2009-02-08 13:13:57

As suggested by John Cremona, the attached patch replaces the use of symbolic variables by variables in a polynomial ring over QQ.



---

archive/issue_comments_039818.json:
```json
{
    "body": "Thanks, Alex.  Patch applies fine to 3.3.alpha5 and tests pass, so positive review (unsurprisingly!).\n\nNote that this only affects docstrings/tests so cannot affect anything else.",
    "created_at": "2009-02-08T14:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5207#issuecomment-39818",
    "user": "https://github.com/JohnCremona"
}
```

Thanks, Alex.  Patch applies fine to 3.3.alpha5 and tests pass, so positive review (unsurprisingly!).

Note that this only affects docstrings/tests so cannot affect anything else.



---

archive/issue_comments_039819.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-09T07:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5207#issuecomment-39819",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039820.json:
```json
{
    "body": "Merged in Sage 3.3.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T07:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5207#issuecomment-39820",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc0.

Cheers,

Michael



---

archive/issue_events_012059.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-09T07:54:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5207",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5207#event-12059"
}
```
