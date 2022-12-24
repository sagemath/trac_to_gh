# Issue 1539: bdist of sage should include devel/doc

archive/issues_001539.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nwstein: note-to-self devel/doc is missing from the bdist.\n[08:33am] wstein: maybe it shouldn't be.\n[08:33am] wstein: I don't know.\n[08:33am] wstein: I think bdist should have it...\n[08:33am] wstein: trac ticket\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1539\n\n",
    "created_at": "2007-12-16T16:35:16Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "bdist of sage should include devel/doc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1539",
    "user": "was"
}
```
Assignee: mabshoff


```
wstein: note-to-self devel/doc is missing from the bdist.
[08:33am] wstein: maybe it shouldn't be.
[08:33am] wstein: I don't know.
[08:33am] wstein: I think bdist should have it...
[08:33am] wstein: trac ticket
```


Issue created by migration from https://trac.sagemath.org/ticket/1539





---

archive/issue_comments_009827.json:
```json
{
    "body": "#1708 duplicated this\n\nAlso, here is a comment from Kate Minola, which is the same problem.  I've thus\npromoted this to a blocker:\n\n```\nFor sage-2.10.1, if I compile from source and run\n'make check' - all is fine.  If I then build a binary\ndistribution (using -bdist), and then inside the binary\ndistribution run 'make check' I get the following errors.\n\nKate\n\nTesting SAGE tutorial\n/home/kate/sage/sage-2.10.1-x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/\nlocal/bin/sage-maketest: line 18: cd: /home/kate/sage/sage-2.10.1-\nx86_64-Linux/dist/sage-2.10.1-x86_64-Linux/devel/doc/tut: No such file\nor directory\nERROR: File ./tut.tex is missing\nexit code: 1\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n       ./tut.tex\nTotal time for all tests: 0.0 seconds\nTesting SAGE programming guide\n/home/kate/sage/sage-2.10.1-x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/\nlocal/bin/sage-maketest: line 22: cd: /home/kate/sage/sage-2.10.1-\nx86_64-Linux/dist/sage-2.10.1-x86_64-Linux/devel/doc/prog: No such\nfile or directory\nERROR: File ./prog.tex is missing\nexit code: 1\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n       ./prog.tex\nTotal time for all tests: 0.0 seconds\nTesting SAGE constructions guide\n/home/kate/sage/sage-2.10.1-x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/\nlocal/bin/sage-maketest: line 26: cd: /home/kate/sage/sage-2.10.1-\nx86_64-Linux/dist/sage-2.10.1-x86_64-Linux/devel/doc/const: No such\nfile or directory\nERROR: File ./const.tex is missing\nexit code: 1\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n       ./const.tex\nTotal time for all tests: 0.0 seconds\n```\n",
    "created_at": "2008-02-12T16:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1539#issuecomment-9827",
    "user": "was"
}
```

#1708 duplicated this

Also, here is a comment from Kate Minola, which is the same problem.  I've thus
promoted this to a blocker:

```
For sage-2.10.1, if I compile from source and run
'make check' - all is fine.  If I then build a binary
distribution (using -bdist), and then inside the binary
distribution run 'make check' I get the following errors.

Kate

Testing SAGE tutorial
/home/kate/sage/sage-2.10.1-x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/
local/bin/sage-maketest: line 18: cd: /home/kate/sage/sage-2.10.1-
x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/devel/doc/tut: No such file
or directory
ERROR: File ./tut.tex is missing
exit code: 1

----------------------------------------------------------------------
The following tests failed:


       ./tut.tex
Total time for all tests: 0.0 seconds
Testing SAGE programming guide
/home/kate/sage/sage-2.10.1-x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/
local/bin/sage-maketest: line 22: cd: /home/kate/sage/sage-2.10.1-
x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/devel/doc/prog: No such
file or directory
ERROR: File ./prog.tex is missing
exit code: 1

----------------------------------------------------------------------
The following tests failed:


       ./prog.tex
Total time for all tests: 0.0 seconds
Testing SAGE constructions guide
/home/kate/sage/sage-2.10.1-x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/
local/bin/sage-maketest: line 26: cd: /home/kate/sage/sage-2.10.1-
x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/devel/doc/const: No such
file or directory
ERROR: File ./const.tex is missing
exit code: 1

----------------------------------------------------------------------
The following tests failed:


       ./const.tex
Total time for all tests: 0.0 seconds
```




---

archive/issue_comments_009828.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-02-12T16:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1539#issuecomment-9828",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_009829.json:
```json
{
    "body": "Attachment [scripts-1539.patch](tarball://root/attachments/some-uuid/ticket1539/scripts-1539.patch) by was created at 2008-08-26 09:16:19",
    "created_at": "2008-08-26T09:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1539#issuecomment-9829",
    "user": "was"
}
```

Attachment [scripts-1539.patch](tarball://root/attachments/some-uuid/ticket1539/scripts-1539.patch) by was created at 2008-08-26 09:16:19



---

archive/issue_comments_009830.json:
```json
{
    "body": "Patch is good. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-26T09:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1539#issuecomment-9830",
    "user": "mabshoff"
}
```

Patch is good. Positive review.

Cheers,

Michael



---

archive/issue_comments_009831.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-26T09:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1539#issuecomment-9831",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009832.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-26T09:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1539#issuecomment-9832",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha1
