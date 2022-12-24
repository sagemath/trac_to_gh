# Issue 1689: document SAGE_FORTRAN_LIB

archive/issues_001689.json:
```json
{
    "body": "Assignee: tba\n\nIt is certainly a special option, but we need to document this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1689\n\n",
    "created_at": "2008-01-05T00:42:56Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "document SAGE_FORTRAN_LIB",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1689",
    "user": "mabshoff"
}
```
Assignee: tba

It is certainly a special option, but we need to document this.

Issue created by migration from https://trac.sagemath.org/ticket/1689





---

archive/issue_comments_010727.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-04-09T18:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1689#issuecomment-10727",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_010728.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-09T18:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1689#issuecomment-10728",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010729.json:
```json
{
    "body": "Changing assignee from tba to mabshoff.",
    "created_at": "2008-04-09T18:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1689#issuecomment-10729",
    "user": "mabshoff"
}
```

Changing assignee from tba to mabshoff.



---

archive/issue_comments_010730.json:
```json
{
    "body": "This is biting people in practice and causes build failures on Itanium for example unless you know what you are doing. So *fix* this. Since this is my ticket now I am yelling at myself :)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-09T18:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1689#issuecomment-10730",
    "user": "mabshoff"
}
```

This is biting people in practice and causes build failures on Itanium for example unless you know what you are doing. So *fix* this. Since this is my ticket now I am yelling at myself :)

Cheers,

Michael



---

archive/issue_comments_010731.json:
```json
{
    "body": "\n```\nNote that you absolutely cannot build Sage on itanium by\njust extracting the tarball and typing make, because Sage\nincludes binaries for Fortran but not on Itanium. Thus you\nhave to explicitly tell the build process about the fortran\ncompiler and library location.  Do this by typing\n\n  export SAGE_FORTRAN=/exact/path/to/gfortran\n  export SAGE_FORTRAN_LIB=/path/to/fortran/libs/\n\nNote that SAGE_FORTRAN_LIB is not documented\nanywhere (http://trac.sagemath.org/sage_trac/ticket/1689),\nand we've got away with this so far since there is only\none Itanium user of Sage in the world, at present.\n\n -- William\n```\n",
    "created_at": "2008-04-11T00:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1689#issuecomment-10731",
    "user": "@williamstein"
}
```


```
Note that you absolutely cannot build Sage on itanium by
just extracting the tarball and typing make, because Sage
includes binaries for Fortran but not on Itanium. Thus you
have to explicitly tell the build process about the fortran
compiler and library location.  Do this by typing

  export SAGE_FORTRAN=/exact/path/to/gfortran
  export SAGE_FORTRAN_LIB=/path/to/fortran/libs/

Note that SAGE_FORTRAN_LIB is not documented
anywhere (http://trac.sagemath.org/sage_trac/ticket/1689),
and we've got away with this so far since there is only
one Itanium user of Sage in the world, at present.

 -- William
```




---

archive/issue_comments_010732.json:
```json
{
    "body": "this is a modified version of README.txt from sage-3.0.alpha3",
    "created_at": "2008-04-11T00:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1689#issuecomment-10732",
    "user": "@williamstein"
}
```

this is a modified version of README.txt from sage-3.0.alpha3



---

archive/issue_comments_010733.json:
```json
{
    "body": "Attachment [README.txt](tarball://root/attachments/some-uuid/ticket1689/README.txt) by @williamstein created at 2008-04-11 00:08:55\n\nThe \"patch\" is just a new README.txt",
    "created_at": "2008-04-11T00:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1689#issuecomment-10733",
    "user": "@williamstein"
}
```

Attachment [README.txt](tarball://root/attachments/some-uuid/ticket1689/README.txt) by @williamstein created at 2008-04-11 00:08:55

The "patch" is just a new README.txt



---

archive/issue_comments_010734.json:
```json
{
    "body": "Attachment [README-update.diff](tarball://root/attachments/some-uuid/ticket1689/README-update.diff) by mabshoff created at 2008-04-11 20:44:34\n\ncorrected  version which also removes the outdated Solaris section",
    "created_at": "2008-04-11T20:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1689#issuecomment-10734",
    "user": "mabshoff"
}
```

Attachment [README-update.diff](tarball://root/attachments/some-uuid/ticket1689/README-update.diff) by mabshoff created at 2008-04-11 20:44:34

corrected  version which also removes the outdated Solaris section



---

archive/issue_comments_010735.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-11T20:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1689#issuecomment-10735",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha4



---

archive/issue_comments_010736.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-11T20:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1689#issuecomment-10736",
    "user": "mabshoff"
}
```

Resolution: fixed
