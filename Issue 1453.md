# Issue 1453: [with patch, positive review] fix cython dependency computation for new files

archive/issues_001453.json:
```json
{
    "body": "Assignee: was\n\n\n```\nBuilding sage/structure/coerce.c because it depends on sage/structure/\ncoerce.pyx.\ncython --embed-positions --incref-local-binop -I/tmp/Work-mabshoff/\nrelease-cycles-2.9/sage-2.9.alpha4/devel/sage-main -o sage/structure/\ncoerce.c sage/structure/coerce.pyx\nTraceback (most recent call last):\n  File \"setup.py\", line 1124, in <module>\n    cython(ext_modules)\n  File \"setup.py\", line 1111, in cython\n    new_sources += process_cython_file(f, m, deps_of)\n  File \"setup.py\", line 1061, in process_cython_file\n    if need_to_cython(f, outfile, deps_of):\n  File \"setup.py\", line 1035, in need_to_cython\n    if os.path.exists(pxd) and check_dependencies(pxd, outfile, deps):\n  File \"setup.py\", line 1011, in check_dependencies\n    deps = deps_of[filename]\nKeyError: 'sage/rings/polynomial/pbori.pxd'\nsage: There was an error installing modified sage library code. \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1453\n\n",
    "created_at": "2007-12-10T21:35:48Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "[with patch, positive review] fix cython dependency computation for new files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1453",
    "user": "mabshoff"
}
```
Assignee: was


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

archive/issue_comments_009370.json:
```json
{
    "body": "Attachment\n\nMerged in 2.9.alpha5.",
    "created_at": "2007-12-10T21:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9370",
    "user": "mabshoff"
}
```

Attachment

Merged in 2.9.alpha5.



---

archive/issue_comments_009371.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-10T21:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9371",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009372.json:
```json
{
    "body": "Since this was a fix for #1366 which I reverted also reverted this patch. It fixes some of the issues of #1366, but since `sage -ba` was completely broken I had little choice  but to revert them for now.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-10T23:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9372",
    "user": "mabshoff"
}
```

Since this was a fix for #1366 which I reverted also reverted this patch. It fixes some of the issues of #1366, but since `sage -ba` was completely broken I had little choice  but to revert them for now.

Cheers,

Michael



---

archive/issue_comments_009373.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-10T23:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9373",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_009374.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-10T23:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9374",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_009375.json:
```json
{
    "body": "I sent the correct patch for this now. Cython deps checking still has poor asymptotic behavior, but now is very quick.",
    "created_at": "2008-02-07T05:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9375",
    "user": "moretti"
}
```

I sent the correct patch for this now. Cython deps checking still has poor asymptotic behavior, but now is very quick.



---

archive/issue_comments_009376.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-12T17:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9376",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009377.json:
```json
{
    "body": "The issue was fixed by Bobby Moretti via a patch at #1366.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-12T17:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1453#issuecomment-9377",
    "user": "mabshoff"
}
```

The issue was fixed by Bobby Moretti via a patch at #1366.

Cheers,

Michael
