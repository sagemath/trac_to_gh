# Issue 465: LinBox: reenable Strassen-Winograd optimization test on Solaris

archive/issues_000465.json:
```json
{
    "body": "Assignee: mabshoff\n\nHello, \n\nthe lround fix we applied to the LinBox spkg also fixes the Strassen-Winograd optimization test:\n\nchecking best threshold for Strassen-Winograd matrix multiplication...\nfgemm 300x300: 0.45 s, 120 Mffops\n1Wino 300x300: 0.31 s, 174.194 Mffops\n\nfgemm 300x300: 0.45 s, 120 Mffops\n1Wino 300x300: 0.31 s, 174.194 Mffops\n\nfgemm 44x44: 0 s, Inf Mffops\n1Wino 44x44: 0 s, Inf Mffops\n\nfgemm 172x172: 0.09 s, 113.077 Mffops\n1Wino 172x172: 0.05 s, 203.538 Mffops\n\nfgemm 172x172: 0.09 s, 113.077 Mffops\n1Wino 172x172: 0.06 s, 169.615 Mffops\ndone\n\nThis was from the compile test I ran on Neron.\n\nFor the updated spkg have a look at \n\nhttp://sage.math.washington.edu/home/mabshoff/spkg-install-LinBox-enable-SWO\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/465\n\n",
    "created_at": "2007-08-19T22:57:53Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "LinBox: reenable Strassen-Winograd optimization test on Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/465",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Hello, 

the lround fix we applied to the LinBox spkg also fixes the Strassen-Winograd optimization test:

checking best threshold for Strassen-Winograd matrix multiplication...
fgemm 300x300: 0.45 s, 120 Mffops
1Wino 300x300: 0.31 s, 174.194 Mffops

fgemm 300x300: 0.45 s, 120 Mffops
1Wino 300x300: 0.31 s, 174.194 Mffops

fgemm 44x44: 0 s, Inf Mffops
1Wino 44x44: 0 s, Inf Mffops

fgemm 172x172: 0.09 s, 113.077 Mffops
1Wino 172x172: 0.05 s, 203.538 Mffops

fgemm 172x172: 0.09 s, 113.077 Mffops
1Wino 172x172: 0.06 s, 169.615 Mffops
done

This was from the compile test I ran on Neron.

For the updated spkg have a look at 

http://sage.math.washington.edu/home/mabshoff/spkg-install-LinBox-enable-SWO

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/465





---

archive/issue_comments_002299.json:
```json
{
    "body": "At http://sage.math.washington.edu/home/mabshoff/linbox-20070814.p1.spkg is an updated LinBox spkg. Changes:\n\n```\nmabshoff@neron standard$ less linbox-20070814.p1/SPKG.txt\n*20070821:\n\n- reenable tuning test\n- added spkg-check\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-08-21T16:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/465#issuecomment-2299",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

At http://sage.math.washington.edu/home/mabshoff/linbox-20070814.p1.spkg is an updated LinBox spkg. Changes:

```
mabshoff@neron standard$ less linbox-20070814.p1/SPKG.txt
*20070821:

- reenable tuning test
- added spkg-check
```


Cheers,

Michael



---

archive/issue_comments_002300.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-22T19:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/465#issuecomment-2300",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_001164.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-29T03:23:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/465",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/465#event-1164"
}
```



---

archive/issue_events_001165.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-25T01:20:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/465",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/465#event-1165"
}
```



---

archive/issue_comments_002301.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-25T01:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/465#issuecomment-2301",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002302.json:
```json
{
    "body": "This was fixed a while ago. On\n\n```\n-bash-3.00$ uname -a\nSunOS fulvia 5.10 Generic_127128-11 i86pc i386 i86pc\n```\n\nwe now have:\n\n```\nchecking best threshold for Strassen-Winograd matrix multiplication... \nfgemm 300x300: 0.01129 s, 4782.99 Mffops\n1Wino 300x300: 0.012612 s, 4281.64 Mffops\n\nfgemm 812x812: 0.175283 s, 6108.83 Mffops\n1Wino 812x812: 0.180449 s, 5933.95 Mffops\n\nfgemm 1324x1324: 0.707952 s, 6556.77 Mffops\n1Wino 1324x1324: 0.700415 s, 6627.33 Mffops\n\nfgemm 1324x1324: 0.703776 s, 6595.68 Mffops\n1Wino 1324x1324: 0.700589 s, 6625.68 Mffops\n\nfgemm 1068x1068: 0.37835 s, 6439.47 Mffops\n1Wino 1068x1068: 0.381192 s, 6391.46 Mffops\n\nfgemm 1196x1196: 0.525748 s, 6507.98 Mffops\n1Wino 1196x1196: 0.52432 s, 6525.7 Mffops\n\nfgemm 1196x1196: 0.525852 s, 6506.69 Mffops\n1Wino 1196x1196: 0.524372 s, 6525.05 Mffops\ndone\nchecking whether to build documentation... no\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T01:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/465#issuecomment-2302",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This was fixed a while ago. On

```
-bash-3.00$ uname -a
SunOS fulvia 5.10 Generic_127128-11 i86pc i386 i86pc
```

we now have:

```
checking best threshold for Strassen-Winograd matrix multiplication... 
fgemm 300x300: 0.01129 s, 4782.99 Mffops
1Wino 300x300: 0.012612 s, 4281.64 Mffops

fgemm 812x812: 0.175283 s, 6108.83 Mffops
1Wino 812x812: 0.180449 s, 5933.95 Mffops

fgemm 1324x1324: 0.707952 s, 6556.77 Mffops
1Wino 1324x1324: 0.700415 s, 6627.33 Mffops

fgemm 1324x1324: 0.703776 s, 6595.68 Mffops
1Wino 1324x1324: 0.700589 s, 6625.68 Mffops

fgemm 1068x1068: 0.37835 s, 6439.47 Mffops
1Wino 1068x1068: 0.381192 s, 6391.46 Mffops

fgemm 1196x1196: 0.525748 s, 6507.98 Mffops
1Wino 1196x1196: 0.52432 s, 6525.7 Mffops

fgemm 1196x1196: 0.525852 s, 6506.69 Mffops
1Wino 1196x1196: 0.524372 s, 6525.05 Mffops
done
checking whether to build documentation... no
```


Cheers,

Michael
