# Issue 3758: crypto --   sage -t -long devel/sage/sage/crypto/mq/sr.py  fails on many machines

archive/issues_003758.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\n\n=====================================================\n\n[was@localhost ~]$ cat /etc/issue\nRHEL5 -- StartCom Enterprise Linux AS release 5.0.0 (Kishuf)\nKernel \\r on an \\m\n\n        sage -t -long devel/sage/sage/crypto/mq/sr.py\nTotal time for all tests: 4047.3 seconds\n\nBecause of lack of RAM:\n\n[was@localhost ~]$ free\n             total       used       free     shared    buffers     cached\nMem:        255704     223072      32632          0      35608     140592\nSwap:       524280      41776     482504\n\nI still am very unhappy about this doctest failure.  Shouldn't Sage should work and\npass its test suite  with 768MB memory?\n\n=====================================================\n\nOn the Ubuntu LTS 64-bit Sage install with 1GB RAM exactly one failure:\n\n\n        sage -t -long devel/sage/sage/crypto/mq/sr.py\n\nwas@SAGE64VPC:~$ free\n             total       used       free     shared    buffers     cached\nMem:       1028380     576408     451972          0     101512     196976\n\n=====================================================\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3758\n\n",
    "created_at": "2008-08-02T18:59:13Z",
    "labels": [
        "component: algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "crypto --   sage -t -long devel/sage/sage/crypto/mq/sr.py  fails on many machines",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3758",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```

=====================================================

[was@localhost ~]$ cat /etc/issue
RHEL5 -- StartCom Enterprise Linux AS release 5.0.0 (Kishuf)
Kernel \r on an \m

        sage -t -long devel/sage/sage/crypto/mq/sr.py
Total time for all tests: 4047.3 seconds

Because of lack of RAM:

[was@localhost ~]$ free
             total       used       free     shared    buffers     cached
Mem:        255704     223072      32632          0      35608     140592
Swap:       524280      41776     482504

I still am very unhappy about this doctest failure.  Shouldn't Sage should work and
pass its test suite  with 768MB memory?

=====================================================

On the Ubuntu LTS 64-bit Sage install with 1GB RAM exactly one failure:


        sage -t -long devel/sage/sage/crypto/mq/sr.py

was@SAGE64VPC:~$ free
             total       used       free     shared    buffers     cached
Mem:       1028380     576408     451972          0     101512     196976

=====================================================
```


Issue created by migration from https://trac.sagemath.org/ticket/3758





---

archive/issue_comments_026634.json:
```json
{
    "body": "Here's what it looks like:\n\n```\n[was@localhost sage-3.1.alpha0]$ ./sage -t --long devel/sage/sage/crypto/mq/sr.py\nsage -t --long devel/sage/sage/crypto/mq/sr.py              sh: line 1: 28053 Killed                  /home/was/build/sage-3.1.alpha0/local/bin/python /home/was/build/sage-3.1.alpha0/tmp/.doctest_sr.py >/tmp/tmp6Q-Tzr 2>/tmp/tmpNd2IJH\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\t [134.8 s]\nexit code: 768\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t --long devel/sage/sage/crypto/mq/sr.py\nTotal time for all tests: 134.8 seconds\n[was@localhost sage-3.1.alpha0]$ \n```\n",
    "created_at": "2008-08-05T05:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3758#issuecomment-26634",
    "user": "https://github.com/williamstein"
}
```

Here's what it looks like:

```
[was@localhost sage-3.1.alpha0]$ ./sage -t --long devel/sage/sage/crypto/mq/sr.py
sage -t --long devel/sage/sage/crypto/mq/sr.py              sh: line 1: 28053 Killed                  /home/was/build/sage-3.1.alpha0/local/bin/python /home/was/build/sage-3.1.alpha0/tmp/.doctest_sr.py >/tmp/tmp6Q-Tzr 2>/tmp/tmpNd2IJH

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
	 [134.8 s]
exit code: 768
 
----------------------------------------------------------------------
The following tests failed:


	sage -t --long devel/sage/sage/crypto/mq/sr.py
Total time for all tests: 134.8 seconds
[was@localhost sage-3.1.alpha0]$ 
```




---

archive/issue_comments_026635.json:
```json
{
    "body": "This is related to/the same as #1046.",
    "created_at": "2008-08-18T19:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3758#issuecomment-26635",
    "user": "https://github.com/malb"
}
```

This is related to/the same as #1046.



---

archive/issue_events_008610.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2008-08-18T19:38:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3758",
    "milestone": "sage-3.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3758#event-8610"
}
```



---

archive/issue_events_008611.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-18T19:43:24Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3758",
    "milestone": "sage-3.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3758#event-8611"
}
```



---

archive/issue_events_008612.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-18T19:43:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3758",
    "milestone": "sage-3.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3758#event-8612"
}
```



---

archive/issue_comments_026636.json:
```json
{
    "body": "Hmm, #4380 seems to make the situation better, but on a 10.4 box with plenty of RAM and a 32 bit build of Sage we still get\n\n```\nvarro:~/sage-3.2.alpha1 mabshoff$ ./sage -t -long devel/sage/sage/crypto/mq/sr.py\nsage -t -long devel/sage/sage/crypto/mq/sr.py                \nhalt 14\n\nerror: no more memory\nSystem 324568k:356856k Appl 319751k/4816k Malloc 3654k/401k Valloc 320512k/4415k Pages 80090/38 Regions 626:685\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\t [812.5 s]\nexit code: 768\n```\n\nBut overall with #4380 applied we see big improvements already.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-29T12:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3758#issuecomment-26636",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, #4380 seems to make the situation better, but on a 10.4 box with plenty of RAM and a 32 bit build of Sage we still get

```
varro:~/sage-3.2.alpha1 mabshoff$ ./sage -t -long devel/sage/sage/crypto/mq/sr.py
sage -t -long devel/sage/sage/crypto/mq/sr.py                
halt 14

error: no more memory
System 324568k:356856k Appl 319751k/4816k Malloc 3654k/401k Valloc 320512k/4415k Pages 80090/38 Regions 626:685

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
	 [812.5 s]
exit code: 768
```

But overall with #4380 applied we see big improvements already.

Cheers,

Michael



---

archive/issue_comments_026637.json:
```json
{
    "body": "Attachment [trac_3758-Fix_Crypto_DocTest.patch](tarball://root/attachments/some-uuid/ticket3758/trac_3758-Fix_Crypto_DocTest.patch) by shumow created at 2009-01-23 22:15:43\n\nThe problem here is that the doctest for sage.crypto.mq.sr.test_consistency uses too much memory.\n\nThere are two options to fix this:\n\n1)  Just take the doc test out.\n<or>\n2)  Change the doctest to call test_consistency w/ max_n=1 instead of max_n=2.  This leads to a more than 5 fold improvement of memory usage / time.\n\nThis patch implements 2, because (1) would make test coverage numbers decrease.",
    "created_at": "2009-01-23T22:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3758#issuecomment-26637",
    "user": "https://trac.sagemath.org/admin/accounts/users/shumow"
}
```

Attachment [trac_3758-Fix_Crypto_DocTest.patch](tarball://root/attachments/some-uuid/ticket3758/trac_3758-Fix_Crypto_DocTest.patch) by shumow created at 2009-01-23 22:15:43

The problem here is that the doctest for sage.crypto.mq.sr.test_consistency uses too much memory.

There are two options to fix this:

1)  Just take the doc test out.
<or>
2)  Change the doctest to call test_consistency w/ max_n=1 instead of max_n=2.  This leads to a more than 5 fold improvement of memory usage / time.

This patch implements 2, because (1) would make test coverage numbers decrease.



---

archive/issue_comments_026638.json:
```json
{
    "body": "looks good.",
    "created_at": "2009-01-24T08:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3758#issuecomment-26638",
    "user": "https://github.com/malb"
}
```

looks good.



---

archive/issue_comments_026639.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T13:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3758#issuecomment-26639",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008613.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T13:15:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3758",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3758#event-8613"
}
```



---

archive/issue_comments_026640.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T13:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3758#issuecomment-26640",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_events_008614.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T13:15:54Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3758",
    "milestone": "sage-3.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3758#event-8614"
}
```



---

archive/issue_events_008615.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T13:15:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3758",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3758#event-8615"
}
```
