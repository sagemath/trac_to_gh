# Issue 9127: BSD.py doctest failure due to timeout of Heegner index computation.

archive/issues_009127.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  @robertwb @rlmill @williamstein @jhpalmieri\n\nThis failure seems remarkably close to #8749, which is closed as fixed, but this is the same sort of problem on the same doctest. Note, changing SAGE_TIMOUT will not change this, as it appears (to me at least), Sage is switching from one algorithm to another in a time which is independent of the processor speed or settings of any timeout variables. \n\n## Hardware & associated software\n\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler)\n\n == Sage version ==\n* 4.4.3.alpha0 and 4.4.3.alpha1\n \n == The test failure ==\nA full log of all tests can be found at\n\nhttp://boxen.math.washington.edu/home/kirkby/sage-4.4.3.alpha0-Sun-Blade-1000-900MHz-Solaris-10-ptestlong.log.gz\n\n(There are 3 failures, but I believe the other two are common to more than one platform and work is progressing on them)\n\nI would expect to see this fail the same way on 't2' as 't2' is slower on single threaded tasks than the Blade 1000. \n\n\n```\nsage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py\n**********************************************************************\nFile \"/export/home/drkirkby/sage-4.4.3.alpha1/devel/sage-main/sage/schemes/elliptic_curves/BSD.py\", line 377:\n    sage: E.prove_BSD(verbosity=2)               # long time\nExpected:\n    p = 2: True by 2-descent...\n    True for p not in {2, 3} by Kolyvagin.\n    ALERT: p = 3 left in Kolyvagin bound\n        0 <= ord_p(#Sha) <= 2\n        ord_p(#Sha_an) = 2\n    Remaining primes:\n    p = 3: irreducible, surjective, non-split multiplicative\n        (0 <= ord_p <= 2)\n    [3]\nGot:\n    p = 2: True by 2-descent\n    Timeout stopped Heegner index computation...\n    Proceeding to use heegner_index_bound instead.\n    True for p not in {2, 3} by Kolyvagin.\n    p = 3 may divide the Heegner index, for which only a bound was computed.\n    ALERT: p = 3 left in Kolyvagin bound\n        0 <= ord_p(#Sha) <= 2\n        ord_p(#Sha_an) = 2\n    Remaining primes:\n    p = 3: irreducible, surjective, non-split multiplicative\n        (0 <= ord_p <= 2)\n    [3]\n**********************************************************************\n1 items had failures:\n   1 of  35 in __main__.example_6\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /export/home/drkirkby/.sage//tmp/.doctest_BSD.py\n         [132.1 s]\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9127\n\n",
    "created_at": "2010-06-03T12:39:49Z",
    "labels": [
        "elliptic curves",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "BSD.py doctest failure due to timeout of Heegner index computation.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9127",
    "user": "drkirkby"
}
```
Assignee: @JohnCremona

CC:  @robertwb @rlmill @williamstein @jhpalmieri

This failure seems remarkably close to #8749, which is closed as fixed, but this is the same sort of problem on the same doctest. Note, changing SAGE_TIMOUT will not change this, as it appears (to me at least), Sage is switching from one algorithm to another in a time which is independent of the processor speed or settings of any timeout variables. 

## Hardware & associated software

* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM
* Solaris 10 03/2005 (first release of Solaris 10)
* gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
* 4.4.3.alpha0 and 4.4.3.alpha1
 
 == The test failure ==
A full log of all tests can be found at

http://boxen.math.washington.edu/home/kirkby/sage-4.4.3.alpha0-Sun-Blade-1000-900MHz-Solaris-10-ptestlong.log.gz

(There are 3 failures, but I believe the other two are common to more than one platform and work is progressing on them)

I would expect to see this fail the same way on 't2' as 't2' is slower on single threaded tasks than the Blade 1000. 


```
sage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py
**********************************************************************
File "/export/home/drkirkby/sage-4.4.3.alpha1/devel/sage-main/sage/schemes/elliptic_curves/BSD.py", line 377:
    sage: E.prove_BSD(verbosity=2)               # long time
Expected:
    p = 2: True by 2-descent...
    True for p not in {2, 3} by Kolyvagin.
    ALERT: p = 3 left in Kolyvagin bound
        0 <= ord_p(#Sha) <= 2
        ord_p(#Sha_an) = 2
    Remaining primes:
    p = 3: irreducible, surjective, non-split multiplicative
        (0 <= ord_p <= 2)
    [3]
Got:
    p = 2: True by 2-descent
    Timeout stopped Heegner index computation...
    Proceeding to use heegner_index_bound instead.
    True for p not in {2, 3} by Kolyvagin.
    p = 3 may divide the Heegner index, for which only a bound was computed.
    ALERT: p = 3 left in Kolyvagin bound
        0 <= ord_p(#Sha) <= 2
        ord_p(#Sha_an) = 2
    Remaining primes:
    p = 3: irreducible, surjective, non-split multiplicative
        (0 <= ord_p <= 2)
    [3]
**********************************************************************
1 items had failures:
   1 of  35 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file /export/home/drkirkby/.sage//tmp/.doctest_BSD.py
         [132.1 s]
```




Issue created by migration from https://trac.sagemath.org/ticket/9127





---

archive/issue_comments_084912.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-03T17:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9127#issuecomment-84912",
    "user": "@rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084913.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-05T14:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9127#issuecomment-84913",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084914.json:
```json
{
    "body": "This one confuses me.  Before I apply the patch, the file passes long tests for me (ubuntu 64-bit, on 4.4.3).  But after the patch it does not:\n\n```\nsage -t -long \"sage/schemes/elliptic_curves/BSD.py\"         \n**********************************************************************\nFile \"/storage/jec/sage-4.4.3/devel/sage-tests/sage/schemes/elliptic_curves/BSD.py\", line 377:\n    sage: E.prove_BSD(verbosity=2)               # long time\nExpected:\n    p = 2: True by 2-descent\n    ...\n    True for p not in {2, 3} by Kolyvagin.\n    ...\n    ALERT: p = 3 left in Kolyvagin bound\n        0 <= ord_p(#Sha) <= 2\n        ord_p(#Sha_an) = 2\n    Remaining primes:\n    p = 3: irreducible, surjective, non-split multiplicative\n        (0 <= ord_p <= 2)\n    [3]\nGot:\n    p = 2: True by 2-descent\n    True for p not in {2, 3} by Kolyvagin.\n    ALERT: p = 3 left in Kolyvagin bound\n        0 <= ord_p(#Sha) <= 2\n        ord_p(#Sha_an) = 2\n    Remaining primes:\n    p = 3: irreducible, surjective, non-split multiplicative\n        (0 <= ord_p <= 2)\n    [3]\n**********************************************************************\n```\n\n\nSo whether or not the patch fixes things on some systems, it breaks others, so cannot be included.",
    "created_at": "2010-06-05T14:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9127#issuecomment-84914",
    "user": "@JohnCremona"
}
```

This one confuses me.  Before I apply the patch, the file passes long tests for me (ubuntu 64-bit, on 4.4.3).  But after the patch it does not:

```
sage -t -long "sage/schemes/elliptic_curves/BSD.py"         
**********************************************************************
File "/storage/jec/sage-4.4.3/devel/sage-tests/sage/schemes/elliptic_curves/BSD.py", line 377:
    sage: E.prove_BSD(verbosity=2)               # long time
Expected:
    p = 2: True by 2-descent
    ...
    True for p not in {2, 3} by Kolyvagin.
    ...
    ALERT: p = 3 left in Kolyvagin bound
        0 <= ord_p(#Sha) <= 2
        ord_p(#Sha_an) = 2
    Remaining primes:
    p = 3: irreducible, surjective, non-split multiplicative
        (0 <= ord_p <= 2)
    [3]
Got:
    p = 2: True by 2-descent
    True for p not in {2, 3} by Kolyvagin.
    ALERT: p = 3 left in Kolyvagin bound
        0 <= ord_p(#Sha) <= 2
        ord_p(#Sha_an) = 2
    Remaining primes:
    p = 3: irreducible, surjective, non-split multiplicative
        (0 <= ord_p <= 2)
    [3]
**********************************************************************
```


So whether or not the patch fixes things on some systems, it breaks others, so cannot be included.



---

archive/issue_comments_084915.json:
```json
{
    "body": "Attachment [trac_9127.patch](tarball://root/attachments/some-uuid/ticket9127/trac_9127.patch) by @rlmill created at 2010-06-05 15:02:35",
    "created_at": "2010-06-05T15:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9127#issuecomment-84915",
    "user": "@rlmill"
}
```

Attachment [trac_9127.patch](tarball://root/attachments/some-uuid/ticket9127/trac_9127.patch) by @rlmill created at 2010-06-05 15:02:35



---

archive/issue_comments_084916.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-05T15:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9127#issuecomment-84916",
    "user": "@rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084917.json:
```json
{
    "body": "The patch results in the test passing on the Sun Blade 1000 where the test originally failed. \n\n\n```\ndrkirkby@redstart:~/sage-4.4.3.alpha3$ ./sage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/BSD.py\"\n         [135.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 135.0 seconds\n```\n\n\nI would be tempted to give it a positive review, though the fact John had a problem, it would be wise to wait and see if he has any further comments. But the changes look OK to me and it solves the problem. \n\nDave",
    "created_at": "2010-06-05T17:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9127#issuecomment-84917",
    "user": "drkirkby"
}
```

The patch results in the test passing on the Sun Blade 1000 where the test originally failed. 


```
drkirkby@redstart:~/sage-4.4.3.alpha3$ ./sage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py
sage -t -long "devel/sage/sage/schemes/elliptic_curves/BSD.py"
         [135.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 135.0 seconds
```


I would be tempted to give it a positive review, though the fact John had a problem, it would be wise to wait and see if he has any further comments. But the changes look OK to me and it solves the problem. 

Dave



---

archive/issue_comments_084918.json:
```json
{
    "body": "Changing assignee from @JohnCremona to drkirkby.",
    "created_at": "2010-06-05T17:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9127#issuecomment-84918",
    "user": "drkirkby"
}
```

Changing assignee from @JohnCremona to drkirkby.



---

archive/issue_comments_084919.json:
```json
{
    "body": "Changing assignee from drkirkby to @JohnCremona.",
    "created_at": "2010-06-05T17:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9127#issuecomment-84919",
    "user": "drkirkby"
}
```

Changing assignee from drkirkby to @JohnCremona.



---

archive/issue_comments_084920.json:
```json
{
    "body": "Once this issue is resolved (and it looks like it will be very soon), #8409 can be closed. \n\nDave",
    "created_at": "2010-06-05T19:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9127#issuecomment-84920",
    "user": "drkirkby"
}
```

Once this issue is resolved (and it looks like it will be very soon), #8409 can be closed. 

Dave



---

archive/issue_comments_084921.json:
```json
{
    "body": "Replying to [comment:6 drkirkby]:\n> I would be tempted to give it a positive review, though the fact John had a problem, it would be wise to wait and see if he has any further comments. But the changes look OK to me and it solves the problem. \n> \n> Dave \n\nI think all of the issues with this ticket have been resolved.",
    "created_at": "2010-06-07T12:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9127#issuecomment-84921",
    "user": "@rlmill"
}
```

Replying to [comment:6 drkirkby]:
> I would be tempted to give it a positive review, though the fact John had a problem, it would be wise to wait and see if he has any further comments. But the changes look OK to me and it solves the problem. 
> 
> Dave 

I think all of the issues with this ticket have been resolved.



---

archive/issue_comments_084922.json:
```json
{
    "body": "In which case, positive review. I'm happy with it.",
    "created_at": "2010-06-07T12:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9127#issuecomment-84922",
    "user": "drkirkby"
}
```

In which case, positive review. I'm happy with it.



---

archive/issue_comments_084923.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-07T12:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9127#issuecomment-84923",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084924.json:
```json
{
    "body": "I am happy.  (I thought I had reviewed the new patch, but maybe I was dreaming!)",
    "created_at": "2010-06-07T13:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9127#issuecomment-84924",
    "user": "@JohnCremona"
}
```

I am happy.  (I thought I had reviewed the new patch, but maybe I was dreaming!)



---

archive/issue_comments_084925.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-09T02:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9127#issuecomment-84925",
    "user": "@mwhansen"
}
```

Resolution: fixed
