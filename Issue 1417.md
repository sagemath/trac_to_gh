# Issue 1417: update symmetrica

archive/issues_001417.json:
```json
{
    "body": "Assignee: was\n\nThere is an spkg at http://sage.math.washington.edu/home/mhansen/symmetrica-2.0.spkg \n\nIssue created by migration from https://trac.sagemath.org/ticket/1417\n\n",
    "created_at": "2007-12-07T09:54:27Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "update symmetrica",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1417",
    "user": "mhansen"
}
```
Assignee: was

There is an spkg at http://sage.math.washington.edu/home/mhansen/symmetrica-2.0.spkg 

Issue created by migration from https://trac.sagemath.org/ticket/1417





---

archive/issue_comments_009140.json:
```json
{
    "body": "Attachment [1417.patch](tarball://root/attachments/some-uuid/ticket1417/1417.patch) by mhansen created at 2007-12-07 10:26:04",
    "created_at": "2007-12-07T10:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1417#issuecomment-9140",
    "user": "mhansen"
}
```

Attachment [1417.patch](tarball://root/attachments/some-uuid/ticket1417/1417.patch) by mhansen created at 2007-12-07 10:26:04



---

archive/issue_comments_009141.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-12-07T10:27:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1417#issuecomment-9141",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_009142.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-07T10:27:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1417#issuecomment-9142",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009143.json:
```json
{
    "body": "Build time has increased. On neron, i.e an Ultra III Sparc:\n\n```\nreal    61m13.083s\nuser    60m26.070s\nsys     0m35.080s\nSuccessfully installed symmetrica-2.0\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-12-07T10:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1417#issuecomment-9143",
    "user": "mabshoff"
}
```

Build time has increased. On neron, i.e an Ultra III Sparc:

```
real    61m13.083s
user    60m26.070s
sys     0m35.080s
Successfully installed symmetrica-2.0
```


Cheers,

Michael



---

archive/issue_comments_009144.json:
```json
{
    "body": "Mike Hansen and I did some more testing and all the following figures are from sage.math:\n\n```\n0.3.3:\n\nreal    0m51.192s\nuser    0m46.991s\nsys     0m3.044s\n\n2.0 vanilla, i.e. \"-O2\":\n\nreal    31m30.192s\nuser    30m48.360s\nsys     0m35.214s\n\n2.0 \"-O0\" +pch:\n\nreal    4m6.438s\nuser    3m45.962s\nsys     0m15.149s\n\n2.0 \"-O0\":\n\nreal    4m14.650s\nuser    3m56.743s\nsys     0m16.057s\n\n2.0 \"-O1\":\n\nabout 13 minutes\n```\n\nMike Hanson did some benchmarking:  \"It looks like O1 is just as fast (and in some cases faster) than O2.\"\n\nSo, \"-O1\" it ought to be.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-08T04:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1417#issuecomment-9144",
    "user": "mabshoff"
}
```

Mike Hansen and I did some more testing and all the following figures are from sage.math:

```
0.3.3:

real    0m51.192s
user    0m46.991s
sys     0m3.044s

2.0 vanilla, i.e. "-O2":

real    31m30.192s
user    30m48.360s
sys     0m35.214s

2.0 "-O0" +pch:

real    4m6.438s
user    3m45.962s
sys     0m15.149s

2.0 "-O0":

real    4m14.650s
user    3m56.743s
sys     0m16.057s

2.0 "-O1":

about 13 minutes
```

Mike Hanson did some benchmarking:  "It looks like O1 is just as fast (and in some cases faster) than O2."

So, "-O1" it ought to be.

Cheers,

Michael



---

archive/issue_comments_009145.json:
```json
{
    "body": "Build tested on Solaris, OSX 10.4 and OSX 10.5.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-09T10:09:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1417#issuecomment-9145",
    "user": "mabshoff"
}
```

Build tested on Solaris, OSX 10.4 and OSX 10.5.

Cheers,

Michael



---

archive/issue_comments_009146.json:
```json
{
    "body": "Merged in 2.9.alpha2.",
    "created_at": "2007-12-09T10:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1417#issuecomment-9146",
    "user": "mabshoff"
}
```

Merged in 2.9.alpha2.



---

archive/issue_comments_009147.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-09T10:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1417#issuecomment-9147",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009148.json:
```json
{
    "body": "I just tested this on my osx 10.5.1 laptop and it took 6 minutes to build and everything seems to work.   Thanks guys!!",
    "created_at": "2007-12-10T04:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1417#issuecomment-9148",
    "user": "was"
}
```

I just tested this on my osx 10.5.1 laptop and it took 6 minutes to build and everything seems to work.   Thanks guys!!
