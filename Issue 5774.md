# Issue 5774: running "make" on a -bdisted binary is broken

archive/issues_005774.json:
```json
{
    "body": "Assignee: mabshoff\n\nTo reproduce this build Sage, bdist, unpack the binary in a new place and run **make**':\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc3$ make\ncd spkg && ./install all 2>&1 | tee -a ../install.log\n/bin/ls: cannot access bzip2-*-install: No such file or directory\n/bin/ls: cannot access dir-*-install: No such file or directory\n/bin/ls: cannot access prereq-*-install: No such file or directory\nmake[1]: Entering directory `/scratch/mabshoff/sage-3.4.1.rc3/spkg'\nstandard/deps:42: warning: overriding commands for target `installed/'\nstandard/deps:39: warning: ignoring old commands for target `installed/'\nstandard/deps:45: warning: overriding commands for target `installed/'\nstandard/deps:42: warning: ignoring old commands for target `installed/'\nstandard/deps:177: warning: overriding commands for target `installed/'\nstandard/deps:45: warning: ignoring old commands for target `installed/'\nmake[1]: Circular installed/python-2.5.2.p9 <- installed/ dependency dropped.\nmake[1]: Circular installed/python-2.5.2.p9 <- installed/ dependency dropped.\nmake[1]: Circular installed/python-2.5.2.p9 <- installed/ dependency dropped.\nmake[1]: Circular installed/zlib-1.2.3.p4 <- installed/ dependency dropped.\nmake[1]: Circular installed/zlib-1.2.3.p4 <- installed/ dependency dropped.\nmake[1]: Circular installed/zlib-1.2.3.p4 <- installed/ dependency dropped.\nmake[1]: Circular installed/termcap-1.3.1.p0 <- installed/ dependency dropped.\nmake[1]: Circular installed/termcap-1.3.1.p0 <- installed/ dependency dropped.\nmake[1]: Circular installed/termcap-1.3.1.p0 <- installed/ dependency dropped.\nmake[1]: Circular installed/readline-5.2.p6 <- installed/ dependency dropped.\nmake[1]: Circular installed/readline-5.2.p6 <- installed/ dependency dropped.\nmake[1]: Circular installed/readline-5.2.p6 <- installed/ dependency dropped.\nmake[1]: Circular installed/libpng-1.2.35 <- installed/ dependency dropped.\nmake[1]: Circular installed/libpng-1.2.35 <- installed/ dependency dropped.\nmake[1]: Circular installed/libpng-1.2.35 <- installed/ dependency dropped.\nmake[1]: Circular installed/ <- installed/ dependency dropped.\nmake[1]: Circular installed/ <- installed/ dependency dropped.\nmake[1]: Circular installed/ <- installed/ dependency dropped.\n```\n\n\nThis is due to the directory **$SAGE_ROOT/spkg/base** not being picked up by -bdist.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5774\n\n",
    "created_at": "2009-04-13T07:47:47Z",
    "labels": [
        "component: distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "running \"make\" on a -bdisted binary is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5774",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

To reproduce this build Sage, bdist, unpack the binary in a new place and run **make**':

```
mabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc3$ make
cd spkg && ./install all 2>&1 | tee -a ../install.log
/bin/ls: cannot access bzip2-*-install: No such file or directory
/bin/ls: cannot access dir-*-install: No such file or directory
/bin/ls: cannot access prereq-*-install: No such file or directory
make[1]: Entering directory `/scratch/mabshoff/sage-3.4.1.rc3/spkg'
standard/deps:42: warning: overriding commands for target `installed/'
standard/deps:39: warning: ignoring old commands for target `installed/'
standard/deps:45: warning: overriding commands for target `installed/'
standard/deps:42: warning: ignoring old commands for target `installed/'
standard/deps:177: warning: overriding commands for target `installed/'
standard/deps:45: warning: ignoring old commands for target `installed/'
make[1]: Circular installed/python-2.5.2.p9 <- installed/ dependency dropped.
make[1]: Circular installed/python-2.5.2.p9 <- installed/ dependency dropped.
make[1]: Circular installed/python-2.5.2.p9 <- installed/ dependency dropped.
make[1]: Circular installed/zlib-1.2.3.p4 <- installed/ dependency dropped.
make[1]: Circular installed/zlib-1.2.3.p4 <- installed/ dependency dropped.
make[1]: Circular installed/zlib-1.2.3.p4 <- installed/ dependency dropped.
make[1]: Circular installed/termcap-1.3.1.p0 <- installed/ dependency dropped.
make[1]: Circular installed/termcap-1.3.1.p0 <- installed/ dependency dropped.
make[1]: Circular installed/termcap-1.3.1.p0 <- installed/ dependency dropped.
make[1]: Circular installed/readline-5.2.p6 <- installed/ dependency dropped.
make[1]: Circular installed/readline-5.2.p6 <- installed/ dependency dropped.
make[1]: Circular installed/readline-5.2.p6 <- installed/ dependency dropped.
make[1]: Circular installed/libpng-1.2.35 <- installed/ dependency dropped.
make[1]: Circular installed/libpng-1.2.35 <- installed/ dependency dropped.
make[1]: Circular installed/libpng-1.2.35 <- installed/ dependency dropped.
make[1]: Circular installed/ <- installed/ dependency dropped.
make[1]: Circular installed/ <- installed/ dependency dropped.
make[1]: Circular installed/ <- installed/ dependency dropped.
```


This is due to the directory **$SAGE_ROOT/spkg/base** not being picked up by -bdist.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5774





---

archive/issue_events_013544.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-21T23:37:14Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5774",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5774#event-13544"
}
```



---

archive/issue_comments_045068.json:
```json
{
    "body": "Well, this is only an issue of annoyance, so bumping it to 3.4.2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-21T23:37:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5774#issuecomment-45068",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, this is only an issue of annoyance, so bumping it to 3.4.2.

Cheers,

Michael



---

archive/issue_comments_045069.json:
```json
{
    "body": "As a mere annoyance, it doesn't make sense to keep it as a blocker.",
    "created_at": "2009-06-15T23:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5774#issuecomment-45069",
    "user": "https://github.com/williamstein"
}
```

As a mere annoyance, it doesn't make sense to keep it as a blocker.



---

archive/issue_comments_045070.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5774#issuecomment-45070",
    "user": "https://github.com/williamstein"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_045071.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-17T22:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5774#issuecomment-45071",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_events_013545.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-05-17T22:02:08Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5774",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5774#event-13545"
}
```



---

archive/issue_events_013546.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-05-17T22:02:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5774",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5774#event-13546"
}
```



---

archive/issue_comments_045072.json:
```json
{
    "body": "This doesn't happen anymore.",
    "created_at": "2012-05-17T22:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5774#issuecomment-45072",
    "user": "https://github.com/jdemeyer"
}
```

This doesn't happen anymore.



---

archive/issue_comments_045073.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-17T22:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5774#issuecomment-45073",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_013547.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-05-21T08:05:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5774",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5774#event-13547"
}
```



---

archive/issue_comments_045074.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-05-21T08:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5774#issuecomment-45074",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
