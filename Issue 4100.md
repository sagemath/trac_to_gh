# Issue 4100: comparison with None extraordinarily slow

archive/issues_004100.json:
```json
{
    "body": "Assignee: somebody\n\nThis is because the coercion model is invoked, and with types it actually tries to cast one direction or the other, raising errors. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4100\n\n",
    "created_at": "2008-09-11T06:04:35Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "comparison with None extraordinarily slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4100",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody

This is because the coercion model is invoked, and with types it actually tries to cast one direction or the other, raising errors. 

Issue created by migration from https://trac.sagemath.org/ticket/4100





---

archive/issue_comments_029523.json:
```json
{
    "body": "Before\n\n\n```\nsage: timeit(\"1 == None\")\n625 loops, best of 3: 625 \u00b5s per loop\n```\n\n\nAfter\n\n\n```\nsage: timeit(\"1 == None\")\n625 loops, best of 3: 530 ns per loop\n```\n\n\nThis is at least close to \n\n\n```\nsage: timeit(\"1 is None\")\n625 loops, best of 3: 330 ns per loop\n```\n\n\nbut people who don't know about the `is` operator shouldn't be hit that bad...",
    "created_at": "2008-09-11T06:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4100#issuecomment-29523",
    "user": "https://github.com/robertwb"
}
```

Before


```
sage: timeit("1 == None")
625 loops, best of 3: 625 µs per loop
```


After


```
sage: timeit("1 == None")
625 loops, best of 3: 530 ns per loop
```


This is at least close to 


```
sage: timeit("1 is None")
625 loops, best of 3: 330 ns per loop
```


but people who don't know about the `is` operator shouldn't be hit that bad...



---

archive/issue_comments_029524.json:
```json
{
    "body": "Attachment [4100-eq-None.patch](tarball://root/attachments/some-uuid/ticket4100/4100-eq-None.patch) by @robertwb created at 2008-09-11 06:08:54",
    "created_at": "2008-09-11T06:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4100#issuecomment-29524",
    "user": "https://github.com/robertwb"
}
```

Attachment [4100-eq-None.patch](tarball://root/attachments/some-uuid/ticket4100/4100-eq-None.patch) by @robertwb created at 2008-09-11 06:08:54



---

archive/issue_comments_029525.json:
```json
{
    "body": "Review:  patch applies ok to 3.1.2 and all tests in sage/structure pass.  ok!",
    "created_at": "2008-09-18T20:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4100#issuecomment-29525",
    "user": "https://github.com/JohnCremona"
}
```

Review:  patch applies ok to 3.1.2 and all tests in sage/structure pass.  ok!



---

archive/issue_comments_029526.json:
```json
{
    "body": "This patch causes a doctest failure in gen.pyx:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha0$ ./sage -t -long devel/sage/sage/libs/pari/gen.pyx\nsage -t -long devel/sage/sage/libs/pari/gen.pyx             \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha0/tmp/gen.py\", line 689:\n    sage: pari(2.5) > None\nExpected:\n    False\nGot:\n    True\n**********************************************************************\n1 items had failures:\n   1 of  16 in __main__.example_11\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha0/tmp/.doctest_gen.py\n         [56.1 s]\n```\n",
    "created_at": "2008-09-19T02:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4100#issuecomment-29526",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch causes a doctest failure in gen.pyx:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha0$ ./sage -t -long devel/sage/sage/libs/pari/gen.pyx
sage -t -long devel/sage/sage/libs/pari/gen.pyx             
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha0/tmp/gen.py", line 689:
    sage: pari(2.5) > None
Expected:
    False
Got:
    True
**********************************************************************
1 items had failures:
   1 of  16 in __main__.example_11
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha0/tmp/.doctest_gen.py
         [56.1 s]
```




---

archive/issue_comments_029527.json:
```json
{
    "body": "I think the doctest should change, I believe the purpose is to show that things don't go boom when you compare with None, not that an ordering is enforced.",
    "created_at": "2008-09-19T07:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4100#issuecomment-29527",
    "user": "https://github.com/robertwb"
}
```

I think the doctest should change, I believe the purpose is to show that things don't go boom when you compare with None, not that an ordering is enforced.



---

archive/issue_comments_029528.json:
```json
{
    "body": "I agree with Robert.  Let's change that doctest (or even remove it, since I don't think it serves any useful purpose!)",
    "created_at": "2008-09-19T07:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4100#issuecomment-29528",
    "user": "https://github.com/JohnCremona"
}
```

I agree with Robert.  Let's change that doctest (or even remove it, since I don't think it serves any useful purpose!)



---

archive/issue_comments_029529.json:
```json
{
    "body": "I fixed the doctest as indicated. If you want to change something or add a comment please post a patch. \n\nCheers,\n\nMichael",
    "created_at": "2008-09-19T15:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4100#issuecomment-29529",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I fixed the doctest as indicated. If you want to change something or add a comment please post a patch. 

Cheers,

Michael



---

archive/issue_comments_029530.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-19T15:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4100#issuecomment-29530",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009350.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-19T15:57:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4100",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4100#event-9350"
}
```



---

archive/issue_comments_029531.json:
```json
{
    "body": "Merged in SAge 3.1.3.alpha0",
    "created_at": "2008-09-19T15:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4100#issuecomment-29531",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in SAge 3.1.3.alpha0
