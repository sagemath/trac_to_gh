# Issue 2866: [with patch, positive review] use tempfile.NamedTemporaryFile for unit tests

archive/issues_002866.json:
```json
{
    "body": "Assignee: @yqiang\n\nSwitch from using hard coded 'test.db' to use the tempfile module's NamedTemporaryFile().\n\nIssue created by migration from https://trac.sagemath.org/ticket/2866\n\n",
    "closed_at": "2008-04-10T03:14:16Z",
    "created_at": "2008-04-09T23:05:27Z",
    "labels": [
        "component: dsage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, positive review] use tempfile.NamedTemporaryFile for unit tests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2866",
    "user": "https://github.com/yqiang"
}
```
Assignee: @yqiang

Switch from using hard coded 'test.db' to use the tempfile module's NamedTemporaryFile().

Issue created by migration from https://trac.sagemath.org/ticket/2866





---

archive/issue_comments_019628.json:
```json
{
    "body": "William reviewed it looking over my shoulder =)",
    "created_at": "2008-04-09T23:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2866#issuecomment-19628",
    "user": "https://github.com/yqiang"
}
```

William reviewed it looking over my shoulder =)



---

archive/issue_comments_019629.json:
```json
{
    "body": "I like this patch, but it doesn't pass doctests:\n\n```\nsage -t -long devel/sage/sage/dsage/tests/testdoc.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.alpha4/tmp/testdoc.py\", line 6:\n    sage: dsage.server(blocking=False, port=port, verbose=False, ssl=False, log_level=3)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha4/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[3]>\", line 1, in <module>\n        dsage.server(blocking=False, port=port, verbose=False, ssl=False, log_level=Integer(3))###line 6:\n    sage: dsage.server(blocking=False, port=port, verbose=False, ssl=False, log_level=3)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/dsage/dsage.py\", line 228, in server\n        db_file = test_db.name\n    NameError: global name 'test_db' is not defined\n```\nRepeat after me: **No positive review without at least minimal doctesting** ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-10T00:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2866#issuecomment-19629",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I like this patch, but it doesn't pass doctests:

```
sage -t -long devel/sage/sage/dsage/tests/testdoc.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha4/tmp/testdoc.py", line 6:
    sage: dsage.server(blocking=False, port=port, verbose=False, ssl=False, log_level=3)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha4/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[3]>", line 1, in <module>
        dsage.server(blocking=False, port=port, verbose=False, ssl=False, log_level=Integer(3))###line 6:
    sage: dsage.server(blocking=False, port=port, verbose=False, ssl=False, log_level=3)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/dsage/dsage.py", line 228, in server
        db_file = test_db.name
    NameError: global name 'test_db' is not defined
```
Repeat after me: **No positive review without at least minimal doctesting** ;)

Cheers,

Michael



---

archive/issue_comments_019630.json:
```json
{
    "body": "Attachment [use_tempfile_module.patch](tarball://root/attachments/some-uuid/ticket2866/use_tempfile_module.patch) by @yqiang created at 2008-04-10 01:44:12\n\nThanks for catching this, I updated the patch, it was a one liner blunder! Could you please reapply, should pass doctests now on sage.math at least :-)",
    "created_at": "2008-04-10T01:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2866#issuecomment-19630",
    "user": "https://github.com/yqiang"
}
```

Attachment [use_tempfile_module.patch](tarball://root/attachments/some-uuid/ticket2866/use_tempfile_module.patch) by @yqiang created at 2008-04-10 01:44:12

Thanks for catching this, I updated the patch, it was a one liner blunder! Could you please reapply, should pass doctests now on sage.math at least :-)



---

archive/issue_comments_019631.json:
```json
{
    "body": "The updated patch fixes the issue and is also a proper Mercurial patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-10T03:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2866#issuecomment-19631",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The updated patch fixes the issue and is also a proper Mercurial patch.

Cheers,

Michael



---

archive/issue_events_006558.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-10T03:14:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2866",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2866#event-6558"
}
```



---

archive/issue_comments_019632.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-10T03:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2866#issuecomment-19632",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019633.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-10T03:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2866#issuecomment-19633",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha4
