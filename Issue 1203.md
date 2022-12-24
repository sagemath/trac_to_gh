# Issue 1203: 2.8.13.alpha0: flint doctest failures

archive/issues_001203.json:
```json
{
    "body": "Assignee: failure\n\n\n```\nsage -t  devel/sage-main/sage/libs/flint/fmpz_poly.pyx      **********************************************************************\nFile \"fmpz_poly.pyx\", line 271:\n    sage: g / f\nException raised:\n    Traceback (most recent call last):\n      File \"/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_13[3]>\", line 1, in <module>\n        g / f###line 271:\n    sage: g / f\n    TypeError: unsupported operand type(s) for /: 'sage.libs.flint.fmpz_poly.Fmpz_poly' and 'sage.libs.flint.fmpz_poly.Fmpz_poly'\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1203\n\n",
    "created_at": "2007-11-18T23:12:10Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "2.8.13.alpha0: flint doctest failures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1203",
    "user": "mabshoff"
}
```
Assignee: failure


```
sage -t  devel/sage-main/sage/libs/flint/fmpz_poly.pyx      **********************************************************************
File "fmpz_poly.pyx", line 271:
    sage: g / f
Exception raised:
    Traceback (most recent call last):
      File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[3]>", line 1, in <module>
        g / f###line 271:
    sage: g / f
    TypeError: unsupported operand type(s) for /: 'sage.libs.flint.fmpz_poly.Fmpz_poly' and 'sage.libs.flint.fmpz_poly.Fmpz_poly'
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/1203





---

archive/issue_comments_007451.json:
```json
{
    "body": "Attachment [7376.patch](tarball://root/attachments/some-uuid/ticket1203/7376.patch) by mabshoff created at 2007-11-19 23:53:27\n\nfix doctest failure",
    "created_at": "2007-11-19T23:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1203#issuecomment-7451",
    "user": "mabshoff"
}
```

Attachment [7376.patch](tarball://root/attachments/some-uuid/ticket1203/7376.patch) by mabshoff created at 2007-11-19 23:53:27

fix doctest failure



---

archive/issue_comments_007452.json:
```json
{
    "body": "Nobody complained about the patch. I also updated the description to reflect the \"//\". With the updated flint.spkg from \n\nhttp://sage.math.washington.edu/home/mabshoff/flint-0.9-r1072.spkg\n\nit compiles on OSX 10.5 and passes testall on OSX 10.5 and sage.math.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-20T09:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1203#issuecomment-7452",
    "user": "mabshoff"
}
```

Nobody complained about the patch. I also updated the description to reflect the "//". With the updated flint.spkg from 

http://sage.math.washington.edu/home/mabshoff/flint-0.9-r1072.spkg

it compiles on OSX 10.5 and passes testall on OSX 10.5 and sage.math.

Cheers,

Michael



---

archive/issue_comments_007453.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-20T09:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1203#issuecomment-7453",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007454.json:
```json
{
    "body": "Merged in 2.8.13.rc0.",
    "created_at": "2007-11-20T09:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1203#issuecomment-7454",
    "user": "mabshoff"
}
```

Merged in 2.8.13.rc0.
