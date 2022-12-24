# Issue 144: Numpy build breaks on sage-1.4.1.2

archive/issues_000144.json:
```json
{
    "body": "Assignee: was\n\nGets a key error here:\n\nnumpy-2006-08-16: blew chunks here;\n    File \"/SandBox/Justin/sb/sage-1.4/spkg/build/numpy-2006-08-16/numpy/distutils/\\\n            ..../fcompiler/__init__.py\", line 199, in get_flags_linker_exe\n      if self.executables['linker_exe']:\n    KeyError: 'linker_exe'\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/144\n\n",
    "created_at": "2006-10-21T20:44:08Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "Numpy build breaks on sage-1.4.1.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/144",
    "user": "justin"
}
```
Assignee: was

Gets a key error here:

numpy-2006-08-16: blew chunks here;
    File "/SandBox/Justin/sb/sage-1.4/spkg/build/numpy-2006-08-16/numpy/distutils/\
            ..../fcompiler/__init__.py", line 199, in get_flags_linker_exe
      if self.executables['linker_exe']:
    KeyError: 'linker_exe'


Issue created by migration from https://trac.sagemath.org/ticket/144





---

archive/issue_comments_000662.json:
```json
{
    "body": "Attachment [Numpy.errlog](tarball://root/attachments/some-uuid/ticket144/Numpy.errlog) by justin created at 2006-10-21 20:44:34\n\nNumpy build log",
    "created_at": "2006-10-21T20:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/144#issuecomment-662",
    "user": "justin"
}
```

Attachment [Numpy.errlog](tarball://root/attachments/some-uuid/ticket144/Numpy.errlog) by justin created at 2006-10-21 20:44:34

Numpy build log



---

archive/issue_comments_000663.json:
```json
{
    "body": "Changing component from algebraic geometry to packages.",
    "created_at": "2006-10-21T20:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/144#issuecomment-663",
    "user": "justin"
}
```

Changing component from algebraic geometry to packages.



---

archive/issue_comments_000664.json:
```json
{
    "body": "Changed component to 'packages'",
    "created_at": "2006-10-21T20:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/144#issuecomment-664",
    "user": "justin"
}
```

Changed component to 'packages'



---

archive/issue_comments_000665.json:
```json
{
    "body": "Numpy is now a standard sage component.",
    "created_at": "2007-01-08T19:28:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/144#issuecomment-665",
    "user": "was"
}
```

Numpy is now a standard sage component.



---

archive/issue_comments_000666.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-08T19:28:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/144#issuecomment-666",
    "user": "was"
}
```

Resolution: fixed
