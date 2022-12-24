# Issue 5207: remove unnecessary use of symbolics in doctests in weierstrass_morphism.py

archive/issues_005207.json:
```json
{
    "body": "Assignee: was\n\nCC:  cremona\n\nAs discussed at\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/48b893e904634273\n\nthere are two doctests in weierstrass_morphism.py that use symbolic variables.  This is slow, completely unnecessary, and causes trouble given that Maxima has a tendency to hang.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5207\n\n",
    "created_at": "2009-02-08T13:11:37Z",
    "labels": [
        "number theory",
        "minor",
        "enhancement"
    ],
    "title": "remove unnecessary use of symbolics in doctests in weierstrass_morphism.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5207",
    "user": "AlexGhitza"
}
```
Assignee: was

CC:  cremona

As discussed at

http://groups.google.com/group/sage-devel/browse_thread/thread/48b893e904634273

there are two doctests in weierstrass_morphism.py that use symbolic variables.  This is slow, completely unnecessary, and causes trouble given that Maxima has a tendency to hang.


Issue created by migration from https://trac.sagemath.org/ticket/5207





---

archive/issue_comments_039895.json:
```json
{
    "body": "Attachment [trac_5207.patch](tarball://root/attachments/some-uuid/ticket5207/trac_5207.patch) by AlexGhitza created at 2009-02-08 13:13:57\n\nAs suggested by John Cremona, the attached patch replaces the use of symbolic variables by variables in a polynomial ring over QQ.",
    "created_at": "2009-02-08T13:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5207#issuecomment-39895",
    "user": "AlexGhitza"
}
```

Attachment [trac_5207.patch](tarball://root/attachments/some-uuid/ticket5207/trac_5207.patch) by AlexGhitza created at 2009-02-08 13:13:57

As suggested by John Cremona, the attached patch replaces the use of symbolic variables by variables in a polynomial ring over QQ.



---

archive/issue_comments_039896.json:
```json
{
    "body": "Thanks, Alex.  Patch applies fine to 3.3.alpha5 and tests pass, so positive review (unsurprisingly!).\n\nNote that this only affects docstrings/tests so cannot affect anything else.",
    "created_at": "2009-02-08T14:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5207#issuecomment-39896",
    "user": "cremona"
}
```

Thanks, Alex.  Patch applies fine to 3.3.alpha5 and tests pass, so positive review (unsurprisingly!).

Note that this only affects docstrings/tests so cannot affect anything else.



---

archive/issue_comments_039897.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-09T07:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5207#issuecomment-39897",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039898.json:
```json
{
    "body": "Merged in Sage 3.3.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T07:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5207#issuecomment-39898",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc0.

Cheers,

Michael
