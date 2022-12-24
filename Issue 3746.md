# Issue 3746: segfault in dist_factor.py on itanium

archive/issues_003746.json:
```json
{
    "body": "Assignee: yi\n\n\n\n\n```\nwstein@iras:~/iras/build/sage-3.0.6.final>         ./sage -t -long devel/sage/sage/dsage/dist_functions/dist_factor.py\nsage -t -long devel/sage/sage/dsage/dist_functions/dist_factor.pysh: line 1: 17221 Segmentation fault      /home/wstein/iras/build/sage-3.0.6.final/local/bin/python /home/wstein/iras/build/sage-3.0.6.final/tmp/.doctest_dist_factor.py >/tmp/tmpKoKDAX 2>/tmp/tmpz35sr7\n[DSage] Closed connection to localhost\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n         [25.0 s]\nexit code: 768\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long devel/sage/sage/dsage/dist_functions/dist_factor.py\nTotal time for all tests: 25.0 seconds\nwstein@iras:~/iras/build/sage-3.0.6.final> \n```\n\n\n\n```\nwstein@iras:~/iras/build/sage-3.0.6.final> uname -a\nLinux iras 2.6.16.46-0.12-default #1 SMP Thu May 17 14:00:09 UTC 2007 ia64 ia64 ia64 GNU/Linux\n\ncpuinfo:\n...\nprocessor  : 3\nvendor     : GenuineIntel\narch       : IA-64\nfamily     : 32\nmodel      : 0\nrevision   : 7\narchrev    : 0\nfeatures   : branchlong, 16-byte atomic ops\ncpu number : 0\ncpu regs   : 4\ncpu MHz    : 1594.000675\nitc MHz    : 399.167296\nBogoMIPS   : 3186.68\nsiblings   : 2\nphysical id: 3\ncore id    : 1\nthread id  : 0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3746\n\n",
    "created_at": "2008-07-30T13:36:06Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "segfault in dist_factor.py on itanium",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3746",
    "user": "was"
}
```
Assignee: yi




```
wstein@iras:~/iras/build/sage-3.0.6.final>         ./sage -t -long devel/sage/sage/dsage/dist_functions/dist_factor.py
sage -t -long devel/sage/sage/dsage/dist_functions/dist_factor.pysh: line 1: 17221 Segmentation fault      /home/wstein/iras/build/sage-3.0.6.final/local/bin/python /home/wstein/iras/build/sage-3.0.6.final/tmp/.doctest_dist_factor.py >/tmp/tmpKoKDAX 2>/tmp/tmpz35sr7
[DSage] Closed connection to localhost

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [25.0 s]
exit code: 768

----------------------------------------------------------------------
The following tests failed:


        sage -t -long devel/sage/sage/dsage/dist_functions/dist_factor.py
Total time for all tests: 25.0 seconds
wstein@iras:~/iras/build/sage-3.0.6.final> 
```



```
wstein@iras:~/iras/build/sage-3.0.6.final> uname -a
Linux iras 2.6.16.46-0.12-default #1 SMP Thu May 17 14:00:09 UTC 2007 ia64 ia64 ia64 GNU/Linux

cpuinfo:
...
processor  : 3
vendor     : GenuineIntel
arch       : IA-64
family     : 32
model      : 0
revision   : 7
archrev    : 0
features   : branchlong, 16-byte atomic ops
cpu number : 0
cpu regs   : 4
cpu MHz    : 1594.000675
itc MHz    : 399.167296
BogoMIPS   : 3186.68
siblings   : 2
physical id: 3
core id    : 1
thread id  : 0
```


Issue created by migration from https://trac.sagemath.org/ticket/3746





---

archive/issue_comments_026606.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-08-02T18:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3746#issuecomment-26606",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_026607.json:
```json
{
    "body": "This also happens on sage.math (opteron debian):\n\n```\nsage -t -long devel/sage/sage/dsage/dist_functions/dist_factor.pysh: line 1: 19413 Segmentation fault      /home/was/build/sage-3.1.alpha0/local/bin/python /home/was/build/sage-3.1.alpha0/tmp/.doctest_dist_factor.py >/tmp/tmpPwlp8k 2>/tmp/tmpRTHU_D\n[DSage] Closed connection to localhost\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\t [25.5 s]\n```\n",
    "created_at": "2008-08-02T18:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3746#issuecomment-26607",
    "user": "was"
}
```

This also happens on sage.math (opteron debian):

```
sage -t -long devel/sage/sage/dsage/dist_functions/dist_factor.pysh: line 1: 19413 Segmentation fault      /home/was/build/sage-3.1.alpha0/local/bin/python /home/was/build/sage-3.1.alpha0/tmp/.doctest_dist_factor.py >/tmp/tmpPwlp8k 2>/tmp/tmpRTHU_D
[DSage] Closed connection to localhost

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
	 [25.5 s]
```




---

archive/issue_comments_026608.json:
```json
{
    "body": "Changing assignee from yi to gfurnish.",
    "created_at": "2008-12-10T02:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3746#issuecomment-26608",
    "user": "gfurnish"
}
```

Changing assignee from yi to gfurnish.



---

archive/issue_comments_026609.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-10T02:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3746#issuecomment-26609",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026610.json:
```json
{
    "body": "I mentioned in #4745 that the second of the three patches might fix this -- here is what I think happened to cause this.  The race condition in question caused dsage to read in a pickled object from a file before it was done being written to the file.  This caused mysterious failures at best and segfaults at worse.  With #4745 applied I ran these doctests for 10200 iterations (~7 hours) without a single doctest failure.  I think that #4745 kills this heisenbug.",
    "created_at": "2008-12-10T02:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3746#issuecomment-26610",
    "user": "gfurnish"
}
```

I mentioned in #4745 that the second of the three patches might fix this -- here is what I think happened to cause this.  The race condition in question caused dsage to read in a pickled object from a file before it was done being written to the file.  This caused mysterious failures at best and segfaults at worse.  With #4745 applied I ran these doctests for 10200 iterations (~7 hours) without a single doctest failure.  I think that #4745 kills this heisenbug.



---

archive/issue_comments_026611.json:
```json
{
    "body": "Apparently the last time I tested this I forgot to use long mode, so I reran it after night.  After testing for 24722.3 seconds dist_factor failed a test case (looks like a time-out), but it did not segfault.  I will continue to stress test this, but I think my earlier assessment is still correct.",
    "created_at": "2008-12-10T14:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3746#issuecomment-26611",
    "user": "gfurnish"
}
```

Apparently the last time I tested this I forgot to use long mode, so I reran it after night.  After testing for 24722.3 seconds dist_factor failed a test case (looks like a time-out), but it did not segfault.  I will continue to stress test this, but I think my earlier assessment is still correct.



---

archive/issue_comments_026612.json:
```json
{
    "body": "Fixed by merging #4745 in Sage 3.2.2.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-11T15:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3746#issuecomment-26612",
    "user": "mabshoff"
}
```

Fixed by merging #4745 in Sage 3.2.2.alpha2.

Cheers,

Michael



---

archive/issue_comments_026613.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-11T15:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3746#issuecomment-26613",
    "user": "mabshoff"
}
```

Resolution: fixed
