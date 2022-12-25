# Issue 1247: cremona-20071116.p0.spkg fails to build with gcc 4.2.x

archive/issues_001247.json:
```json
{
    "body": "Assignee: mabshoff\n\n Andrzej Giniewicz reported:\n\n```\n not counting plenty (281) warnings in file curvesort.cc (about\ndeprecated conversion from string constant to 'char*') I also get\nWHOLE lot (about 8000) errors all in one nature:\n\n../g0n/curvesort.cc:106: error: jump to case label\n../g0n/curvesort.cc:105: error:   crosses initialization of 'int\n<anonymous>[3]'\n\nwith different numbers only... problems starts from:\n\ng++ -c -fPIC -g -O2 -DNEW_OP_ORDER -DUSE_PARI_FACTORING -I../include -\nDNTL_ALL -I/opt/sage/local/include -I/opt/sage/local/include  tsat3.cc\n-o tsat3_n.o\nIn file included from tsat3.cc:37:\n../g0n/curvesort.cc ....... etc etc\n\nI think there is no sense to attach such big report... I'm running\ncurrent Arch Linux, that is GCC 4.2.2, gLibc 2.7, kernel 2.6.23.8. Is\nthere some workaround? \n```\n\nSee http://groups.google.com/group/sage-support/t/c2140ece9608358e\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1247\n\n",
    "closed_at": "2007-11-24T15:37:22Z",
    "created_at": "2007-11-23T12:50:51Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.14",
    "title": "cremona-20071116.p0.spkg fails to build with gcc 4.2.x",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1247",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

 Andrzej Giniewicz reported:

```
 not counting plenty (281) warnings in file curvesort.cc (about
deprecated conversion from string constant to 'char*') I also get
WHOLE lot (about 8000) errors all in one nature:

../g0n/curvesort.cc:106: error: jump to case label
../g0n/curvesort.cc:105: error:   crosses initialization of 'int
<anonymous>[3]'

with different numbers only... problems starts from:

g++ -c -fPIC -g -O2 -DNEW_OP_ORDER -DUSE_PARI_FACTORING -I../include -
DNTL_ALL -I/opt/sage/local/include -I/opt/sage/local/include  tsat3.cc
-o tsat3_n.o
In file included from tsat3.cc:37:
../g0n/curvesort.cc ....... etc etc

I think there is no sense to attach such big report... I'm running
current Arch Linux, that is GCC 4.2.2, gLibc 2.7, kernel 2.6.23.8. Is
there some workaround? 
```

See http://groups.google.com/group/sage-support/t/c2140ece9608358e

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1247





---

archive/issue_comments_007790.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-23T12:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1247#issuecomment-7790",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007791.json:
```json
{
    "body": "There is also an issue on OpenSuSE 10.2:\n\n```\nYou mention that there is an issue with cremona.spkg on Linux/Itanium with\nolder gcc and also Solaris. My settings are:\n- openSUSE 10.2 (X86-64),\n- AMD Athlon(tm) 64 Processor 3700+\n- gcc-Version 4.2.1; I think this isn't exactly old, or is it? \n```\n\nSee http://groups.google.com/group/sage-support/t/8e446357a1d15a8a\n\nCheers,\n\nMichael",
    "created_at": "2007-11-23T12:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1247#issuecomment-7791",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There is also an issue on OpenSuSE 10.2:

```
You mention that there is an issue with cremona.spkg on Linux/Itanium with
older gcc and also Solaris. My settings are:
- openSUSE 10.2 (X86-64),
- AMD Athlon(tm) 64 Processor 3700+
- gcc-Version 4.2.1; I think this isn't exactly old, or is it? 
```

See http://groups.google.com/group/sage-support/t/8e446357a1d15a8a

Cheers,

Michael



---

archive/issue_events_003297.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-24T00:38:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1247",
    "milestone": "sage-2.8.14",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1247#event-3297"
}
```



---

archive/issue_comments_007792.json:
```json
{
    "body": "There is a new cremona.spkg that should work with gcc 4.2.x at \n\nhttp://sage.math.washington.edu/home/mabshoff/cremona-20071124.spkg\n\nCheers,\n\nMichael",
    "created_at": "2007-11-24T03:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1247#issuecomment-7792",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There is a new cremona.spkg that should work with gcc 4.2.x at 

http://sage.math.washington.edu/home/mabshoff/cremona-20071124.spkg

Cheers,

Michael



---

archive/issue_comments_007793.json:
```json
{
    "body": "The bundle applied also includes #1238. So close that too when closing this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-24T10:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1247#issuecomment-7793",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The bundle applied also includes #1238. So close that too when closing this ticket.

Cheers,

Michael



---

archive/issue_comments_007794.json:
```json
{
    "body": "Merged in 2.8.14.rc0. Feedback provided by various people indicates that the problem is fixed.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-24T15:37:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1247#issuecomment-7794",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.14.rc0. Feedback provided by various people indicates that the problem is fixed.

Cheers,

Michael



---

archive/issue_events_003298.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-24T15:37:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1247",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1247#event-3298"
}
```



---

archive/issue_comments_007795.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-24T15:37:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1247#issuecomment-7795",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
