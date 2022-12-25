# Issue 3597: building sage on opensuse x86_64 fails with readline detection error

archive/issues_003597.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is on menas on skynet:\n\n\n```\n\nConfigure findings:\n  FFI:        no (user requested: default)\n  readline:   no (user requested: /home/wstein/menas/build/sage-3.0.4.alpha2/local)\n  libsigsegv: no, consider installing GNU libsigsegv\nAs you requested, we will proceed without libsigsegv...\n./makemake  --with-readline=/home/wstein/menas/build/sage-3.0.4.alpha2/local --prefix=/home/wstein/menas/build/sage-3.0.4.alpha2/local --without-libintl    > Makefile\nmakemake: configure failed to detect readline\nError configuring clisp\n\nreal    0m35.648s\nuser    0m10.957s\nsys     0m10.445s\nsage: An error occurred while installing clisp-2.46.p1\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3597\n\n",
    "created_at": "2008-07-07T23:30:37Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "building sage on opensuse x86_64 fails with readline detection error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3597",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

This is on menas on skynet:


```

Configure findings:
  FFI:        no (user requested: default)
  readline:   no (user requested: /home/wstein/menas/build/sage-3.0.4.alpha2/local)
  libsigsegv: no, consider installing GNU libsigsegv
As you requested, we will proceed without libsigsegv...
./makemake  --with-readline=/home/wstein/menas/build/sage-3.0.4.alpha2/local --prefix=/home/wstein/menas/build/sage-3.0.4.alpha2/local --without-libintl    > Makefile
makemake: configure failed to detect readline
Error configuring clisp

real    0m35.648s
user    0m10.957s
sys     0m10.445s
sage: An error occurred while installing clisp-2.46.p1

```


Issue created by migration from https://trac.sagemath.org/ticket/3597





---

archive/issue_comments_025366.json:
```json
{
    "body": "Here it is:\n\n  http://sage.math.washington.edu/home/was/patches/clisp-2.46.p2.spkg",
    "created_at": "2008-07-07T23:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3597#issuecomment-25366",
    "user": "https://github.com/williamstein"
}
```

Here it is:

  http://sage.math.washington.edu/home/was/patches/clisp-2.46.p2.spkg



---

archive/issue_comments_025367.json:
```json
{
    "body": "Positive review, it builds for me, but cripples Maxima for now. Oh well, Maxima without readline is better than no Maxima at all.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-08T00:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3597#issuecomment-25367",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review, it builds for me, but cripples Maxima for now. Oh well, Maxima without readline is better than no Maxima at all.

Cheers,

Michael



---

archive/issue_comments_025368.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-08T00:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3597#issuecomment-25368",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_003816.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2008-07-08T00:18:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3597",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3597#event-3816"
}
```



---

archive/issue_comments_025369.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc0",
    "created_at": "2008-07-08T00:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3597#issuecomment-25369",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.rc0
