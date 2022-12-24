# Issue 4377: Building the Sage library with parallel make is broken on OSX 10.4

archive/issues_004377.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  justin\n\nexporting MAKE=make -j2 leads to\n\n```\nTraceback (most recent call last):\n  File \"setup.py\", line 1545, in <module>\n    cython(deps, ext_modules)\n  File \"setup.py\", line 1311, in cython\n    execute_list_of_commands(command_list)\n  File \"setup.py\", line 1403, in execute_list_of_commands\n    n = 2*number_of_cpus()\nTypeError: unsupported operand type(s) for *: 'int' and 'NoneType'\nsage: There was an error installing modified sage library code.\n```\n\non OSX 10.4.\n\nThis is caused by #3765.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4377\n\n",
    "created_at": "2008-10-28T15:03:40Z",
    "labels": [
        "build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Building the Sage library with parallel make is broken on OSX 10.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4377",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  justin

exporting MAKE=make -j2 leads to

```
Traceback (most recent call last):
  File "setup.py", line 1545, in <module>
    cython(deps, ext_modules)
  File "setup.py", line 1311, in cython
    execute_list_of_commands(command_list)
  File "setup.py", line 1403, in execute_list_of_commands
    n = 2*number_of_cpus()
TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
sage: There was an error installing modified sage library code.
```

on OSX 10.4.

This is caused by #3765.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4377





---

archive/issue_comments_032206.json:
```json
{
    "body": "ok, the issue is simple enough and an extra \"\\n\" in the output:\n\n```\n>>> import os\n>>> os.popen2(\"sysctl -n hw.ncpu\")[1].read()\n'2\\n'\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-10-28T15:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4377#issuecomment-32206",
    "user": "mabshoff"
}
```

ok, the issue is simple enough and an extra "\n" in the output:

```
>>> import os
>>> os.popen2("sysctl -n hw.ncpu")[1].read()
'2\n'
```


Cheers,

Michael



---

archive/issue_comments_032207.json:
```json
{
    "body": "Ok, the above wasn't the issue. Strange that number_of_cpus() returns None.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-28T15:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4377#issuecomment-32207",
    "user": "mabshoff"
}
```

Ok, the above wasn't the issue. Strange that number_of_cpus() returns None.

Cheers,

Michael



---

archive/issue_comments_032208.json:
```json
{
    "body": "Attachment [sage-4377.patch](tarball://root/attachments/some-uuid/ticket4377/sage-4377.patch) by @williamstein created at 2008-10-28 15:49:53",
    "created_at": "2008-10-28T15:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4377#issuecomment-32208",
    "user": "@williamstein"
}
```

Attachment [sage-4377.patch](tarball://root/attachments/some-uuid/ticket4377/sage-4377.patch) by @williamstein created at 2008-10-28 15:49:53



---

archive/issue_comments_032209.json:
```json
{
    "body": "The patch fixes the issue. \n\nCheers,\n\nMichael",
    "created_at": "2008-10-28T15:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4377#issuecomment-32209",
    "user": "mabshoff"
}
```

The patch fixes the issue. 

Cheers,

Michael



---

archive/issue_comments_032210.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-28T16:19:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4377#issuecomment-32210",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_comments_032211.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-28T16:19:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4377#issuecomment-32211",
    "user": "mabshoff"
}
```

Resolution: fixed
