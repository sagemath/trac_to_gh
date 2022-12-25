# Issue 1453: [with patch, positive review] fix cython dependency computation for new files

archive/issues_001453.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nBuilding sage/structure/coerce.c because it depends on sage/structure/\ncoerce.pyx.\ncython --embed-positions --incref-local-binop -I/tmp/Work-mabshoff/\nrelease-cycles-2.9/sage-2.9.alpha4/devel/sage-main -o sage/structure/\ncoerce.c sage/structure/coerce.pyx\nTraceback (most recent call last):\n  File \"setup.py\", line 1124, in <module>\n    cython(ext_modules)\n  File \"setup.py\", line 1111, in cython\n    new_sources += process_cython_file(f, m, deps_of)\n  File \"setup.py\", line 1061, in process_cython_file\n    if need_to_cython(f, outfile, deps_of):\n  File \"setup.py\", line 1035, in need_to_cython\n    if os.path.exists(pxd) and check_dependencies(pxd, outfile, deps):\n  File \"setup.py\", line 1011, in check_dependencies\n    deps = deps_of[filename]\nKeyError: 'sage/rings/polynomial/pbori.pxd'\nsage: There was an error installing modified sage library code. \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1453\n\n",
    "created_at": "2007-12-10T21:35:48Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, positive review] fix cython dependency computation for new files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1453",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein


```
Building sage/structure/coerce.c because it depends on sage/structure/
coerce.pyx.
cython --embed-positions --incref-local-binop -I/tmp/Work-mabshoff/
release-cycles-2.9/sage-2.9.alpha4/devel/sage-main -o sage/structure/
coerce.c sage/structure/coerce.pyx
Traceback (most recent call last):
  File "setup.py", line 1124, in <module>
    cython(ext_modules)
  File "setup.py", line 1111, in cython
    new_sources += process_cython_file(f, m, deps_of)
  File "setup.py", line 1061, in process_cython_file
    if need_to_cython(f, outfile, deps_of):
  File "setup.py", line 1035, in need_to_cython
    if os.path.exists(pxd) and check_dependencies(pxd, outfile, deps):
  File "setup.py", line 1011, in check_dependencies
    deps = deps_of[filename]
KeyError: 'sage/rings/polynomial/pbori.pxd'
sage: There was an error installing modified sage library code. 
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1453





---

archive/issue_events_001602.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-10T21:39:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1453#event-1602"
}
```



---

archive/issue_comments_009345.json:
```json
{
    "body": "Attachment [cython-dependencies.patch](tarball://root/attachments/some-uuid/ticket1453/cython-dependencies.patch) by mabshoff created at 2007-12-10 21:39:42\n\nMerged in 2.9.alpha5.",
    "created_at": "2007-12-10T21:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9345",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [cython-dependencies.patch](tarball://root/attachments/some-uuid/ticket1453/cython-dependencies.patch) by mabshoff created at 2007-12-10 21:39:42

Merged in 2.9.alpha5.



---

archive/issue_comments_009346.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-10T21:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9346",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009347.json:
```json
{
    "body": "Since this was a fix for #1366 which I reverted also reverted this patch. It fixes some of the issues of #1366, but since `sage -ba` was completely broken I had little choice  but to revert them for now.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-10T23:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9347",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Since this was a fix for #1366 which I reverted also reverted this patch. It fixes some of the issues of #1366, but since `sage -ba` was completely broken I had little choice  but to revert them for now.

Cheers,

Michael



---

archive/issue_comments_009348.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-10T23:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9348",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001603.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-10T23:46:17Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1453#event-1603"
}
```



---

archive/issue_comments_009349.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-10T23:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9349",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_009350.json:
```json
{
    "body": "I sent the correct patch for this now. Cython deps checking still has poor asymptotic behavior, but now is very quick.",
    "created_at": "2008-02-07T05:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9350",
    "user": "https://github.com/bobmoretti"
}
```

I sent the correct patch for this now. Cython deps checking still has poor asymptotic behavior, but now is very quick.



---

archive/issue_comments_009351.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-12T17:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9351",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001604.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-12T17:56:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1453#event-1604"
}
```



---

archive/issue_comments_009352.json:
```json
{
    "body": "The issue was fixed by Bobby Moretti via a patch at #1366.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-12T17:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9352",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue was fixed by Bobby Moretti via a patch at #1366.

Cheers,

Michael
